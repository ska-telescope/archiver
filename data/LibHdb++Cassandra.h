/* Copyright (C) : 2014-2017
   European Synchrotron Radiation Facility
   BP 220, Grenoble 38043, FRANCE

   This file is part of libhdb++cassandra.

   libhdb++cassandra is free software: you can redistribute it and/or modify
   it under the terms of the Lesser GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   libhdb++cassandra is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Lesser
   GNU General Public License for more details.

   You should have received a copy of the Lesser GNU General Public License
   along with libhdb++cassandra.  If not, see <http://www.gnu.org/licenses/>. */

#ifndef _HDBPP_CASSANDRA_H
#define _HDBPP_CASSANDRA_H

#include "AttributeName.h"
#include "AttributeCache.h"
#include <LibHdb++.h>

#include <tango.h>
#include <cassandra.h>
#include <map>
#include <string>
#include <vector>

namespace HDBPP
{
// forward declare
class PreparedStatementCache;

/**
 * @class HdbPPCassandra
 * @ingroup HDBPP-Interface
 * @brief HdbPPCassandra implements the AbstractDB interface to store tango event data in a
 * cassandra database cluster.
 *
 * The HdbPPCassandra driver is loaded dynamically from libhdbpp (@see HdbClient)
 * when the class or device configuration requests this archiver library. A valid configuration
 * must be passed as the constructor parameter, @see HdbPPCassandra() for configuration parameter
 * documentation
 */
class HdbPPCassandra : public AbstractDB
{
public:

    /**
     * @brief HdbPPCassandra constructor
     *
     * The configuration parameters must contain the following strings:
     *
     * - Mandatory:
     *     - contact_points: Cassandra cluster contact point hostname, eg cassandra_db,
     *       given as a comma separated list. The contact points are used to initialize
     *       the driver and it will automatically discover the rest of the nodes in your
     *       Cassandra cluster. Tip: include more than one contact point to be robust
     *       against node failures.
     *     - keyspace: Keyspace to use within the cluster, eg, hdb_test
     *     - consistency: Determine the number of replicas on which the read/write must 
     *       respond/succeed before acknowledgement. This must be one of the following values:
     *          - ALL: Equivalent CASS_CONSISTENCY_ALL
     *          - EACH_QUORUM : Equivalent CASS_CONSISTENCY_EACH_QUORUM
     *          - QUORUM : Equivalent CASS_CONSISTENCY_QUORUM
     *          - LOCAL_QUORUM : Equivalent CASS_CONSISTENCY_LOCAL_QUORUM
     *          - ONE : Equivalent CASS_CONSISTENCY_ONE
     *          - TWO : Equivalent CASS_CONSISTENCY_TWO
     *          - THREE : Equivalent CASS_CONSISTENCY_THREE
     *          - LOCAL_ONE : Equivalent CASS_CONSISTENCY_LOCAL_ONE
     *          - ANY : Equivalent CASS_CONSISTENCY_ANY
     *          - SERIAL : Equivalent CASS_CONSISTENCY_SERIAL
     *          - LOCAL_SERIAL : Equivalent CASS_CONSISTENCY_LOCAL_SERIAL
     * - Optional:
     *      - user: Cluster log in user name
     *      - password: Password for above user name
     *      - local_dc: Datacenter name used for queries with LOCAL consistency
     *        level (e.g. LOCAL_QUORUM). In the current version of this library, all the
     *        statements are executed with LOCAL_QUORUM consistency level.
     *      - store_diag_time: Either true to store the times or false to omit them.
     * - Debug:
     *     - logging_level: One of the following:
     *          - DISABLED: No logging
     *          - ERROR: Error level logging
     *          - WARNING: Warning level logging
     *          - INFO: Info level logging
     *          - DEBUG: Debug level logging (maximum logging)
     *     - cassandra_driver_log_level:  Cassandra logging level, see CassLogLevel in Datastax
     *       documentation. This must be one of the following values:
     *          - TRACE: Equivalent CASS_LOG_TRACE
     *          - DEBUG: Equivalent CASS_LOG_DEBUG
     *          - INFO: Equivalent CASS_LOG_INFO
     *          - WARN: Equivalent CASS_LOG_WARN
     *          - ERROR: Equivalent CASS_LOG_ERROR
     *          - CRITICAL: Equivalent CASS_LOG_CRITICAL
     *          - DISABLED: Equivalent CASS_LOG_DISABLED
     *
     * @param configuration A list of configuration parameters to start the driver with.
     */
    HdbPPCassandra(std::vector<std::string> configuration);

    /**
     * @brief HdbPPCassandra destructor
     *
     * The destructor will attempt to disconnect an open Cassandra session
     */
    ~HdbPPCassandra();

    /**
     * @brief Insert an attribute archive event into the database
     *
     * Inserts an attribute archive event for the EventData into the database. If the attribute
     * does not exist in the database, then an exception will be raised. If the attr_value
     * field of the data parameter if empty, then the attribute is in an error state
     * and the error message will be archived.
     *
     * @param data Tango event data about the attribute.
     * @param ev_data_type HDB event data for the attribute.
     * @throw Tango::DevFailed
     */
    virtual void insert_Attr(Tango::EventData *data, HdbEventDataType ev_data_type);

    /**
     * @brief Inserts the attribute configuration data.
     *
     * Inserts the attribute configuration data (Tango Attribute Configuration event data)
     * into the database. The attribute must be configured to be stored in HDB++,
     * otherwise an exception will be thrown.
     *
     * @param data Tango event data about the attribute.
     * @param ev_data_type HDB event data for the attribute.
     * @throw Tango::DevFailed
     */
    virtual void insert_param_Attr(Tango::AttrConfEventData *data, HdbEventDataType ev_data_type);

    /**
     * @brief Add and configure an attribute in the database.
     *
     * Trying to reconfigure an existing attribute will result in an exception, and if an
     * attribute already exists with the same configuration then the ttl will be updated if
     * different.
     *
     * @param fqdn_attr_name Fully qualified attribute name
     * @param type The type of the attribute.
     * @param format The format of the attribute.
     * @param write_type The read/write access of the type.
     * @param  ttl The time to live in hour, 0 for infinity
     * @throw Tango::DevFailed
     */
    virtual void configure_Attr(std::string fqdn_attr_name, int type, int format, int write_type, unsigned int ttl);

    /**
     * @brief Update the ttl value for an attribute.
     *
     * The attribute must have been configured to be stored in HDB++, otherwise an exception
     * is raised
     *
     * @param fqdn_attr_name Fully qualified attribute nam
     * @param ttl The time to live in hour, 0 for infinity
     * @throw Tango::DevFailed
     */
    virtual void updateTTL_Attr(std::string fqdn_attr_name, unsigned int ttl);

    /**
    * @brief Record a start, Stop, Pause or Remove history event for an attribute.
    *
    * Inserts a history event for the attribute name passed to the function. The attribute
    * must have been configured to be stored in HDB++, otherwise an exception is raised.
    * This function will also insert an additional CRASH history event before the START
    * history event if the given event parameter is DB_START and if the last history event
    * stored was also a START event.
    *
    * @param fqdn_attr_name Fully qualified attribute name
    * @param event
    * @throw Tango::DevFailed
    */
    virtual void event_Attr(std::string fqdn_attr_name, unsigned char event);

private:

    void connect_session();

    bool load_and_cache_attr(AttributeName &attr_name);

    unsigned int get_attr_ttl(AttributeName &attr_name);
    CassUuid get_attr_uuid(AttributeName &attr_name);
    std::pair<CassUuid, unsigned int> get_both_attr_id_and_ttl(AttributeName &attr_name);

    bool attr_type_exists(AttributeName &attr_name, const std::string &attr_type);

    bool find_last_event(const CassUuid &ID, std::string &last_event, AttributeName &attr_name);

    void insert_history_event(const std::string &history_event_name, CassUuid att_conf_id);

    void insert_attr_conf(AttributeName &attr_name, const std::string &data_type, const CassUuid &uuid, unsigned int ttl = 0);

    void insert_domain(AttributeName &attr_name);
    void insert_family(AttributeName &attr_name);
    void insert_member(AttributeName &attr_name);
    void insert_attr_name(AttributeName &attr_name);

    void update_ttl(AttributeName &attr_name, unsigned int ttl);

    std::string get_config_param(const std::map<std::string, std::string> &conf, std::string param, bool mandatory);
    void set_cassandra_consistency_level(std::string consistency_level);
    void set_cassandra_logging_level(std::string level);
    void set_library_logging_level(std::string level);
    std::map<std::string, std::string> extract_config(std::vector<std::string> str, std::string separator);

    CassError execute_statement(CassStatement *statement);
    void throw_execute_exception(std::string message, std::string query, CassError error, const char *origin);

    // Datastax cpp driver 
    CassCluster *_cass_cluster;
    CassSession *_cass_session;
    CassUuidGen *_uuid_generator;
    CassLogLevel _cassandra_logging_level;
    CassConsistency _consistency;

    std::string _keyspace_name;

    // used to flag up whether the library will store the diagnostic timestamps,
    // setting to false via the configuration will save database space
    bool _store_diag_times = false;

    // manage prepared statement objects
    PreparedStatementCache *_prepared_statements;

    // cache some details about attributes, to save db lookup
    AttributeCache _attr_cache;
};

/**
 * @class HdbPPCassandraFactory
 * @ingroup HDB++
 * @brief Factory object to create the database object, in this case an instance of HdbPPCassandra
 */
class HdbPPCassandraFactory : public DBFactory
{
public:
    /**
     * @brief Create a HdbPPCassandra database object
     * @param configuration A list of configuration parameters to start the driver with, see
     * HdbPPCassandra.
     * @throw Tango::DevFailed
     */
    virtual AbstractDB *create_db(std::vector<std::string> configuration);

    virtual ~HdbPPCassandraFactory() {}
};

}; // namespace HDBPP

#endif
