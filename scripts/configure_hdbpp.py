
#Imports
from tango import DeviceProxy
import time
import json
#import argparse

# fqdn_list = argparse.ArgumentParser()
# fqdn_list.add_argument("cm_fqdn")
# fqdn_list.add_argument("em_fqdn")
# args = fqdn_list.parse_args()

#Configuration Manager Proxy
try:
#conf_manager_proxy = DeviceProxy(str(args.cm_fqdn))
    print("Creating Device proxies -------------------------------------------------------------------")
    conf_manager_proxy = DeviceProxy('tango://databaseds.tangonet:10000/archiving/hdbpp/confmanager01')
    print("conf_manager_proxy: ", conf_manager_proxy)

#Event subscriber Proxy
#evt_subscriber_proxy = DeviceProxy(str(args.em_fqdn))
    evt_subscriber_proxy = DeviceProxy("tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
    print("evt_subscriber_proxy: ", evt_subscriber_proxy)
except Exception as except_occured:
    print("except_occured: ", except_occured)

try:
    print("ArchiverRemove ------------------------------------------------------------------------------")
    conf_manager_proxy.command_inout("ArchiverRemove","tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
except Exception as except_occured:
    print("except_occured: ", except_occured)

print("sleeping -----------------------------------------------------------------------------")
time.sleep(30);

try:
    print("ArchiverAdd on conf manager ----------------------------------------------------------------")
    conf_manager_proxy.command_inout("ArchiverAdd","tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
    # conf_manager_proxy.Archiveradd("archiving/hdbpp/eventsubscriber01")

except Exception as except_occured:
    print("except_occured: ", except_occured)


#conf_manager_proxy.SetArchiver = "tango://alpha:10000/archiving/hdb++/eventsubscriber.01"

try:
    print("AttributeRemove on evt subscriber--------------------------------------------------------")
    evt_subscriber_proxy.command_inout("AttributeRemove", "tango://databaseds.tangonet:10000/sys/tg_test/1/ampli")
except Exception as except_occured:
    print("except_occured: ", except_occured)

print("sleeping -----------------------------------------------------------------------------")
time.sleep(30);
time.sleep(30);

try:
    print("AttributeAdd on evt subscriber--------------------------------------------------------")
    evt_subscriber_proxy.command_inout("AttributeAdd", ["tango://databaseds.tangonet:10000/sys/tg_test/1/ampli", "ALWAYS", "0"])
except Exception as except_occured:
    print("except_occured: ", except_occured)


# with open("/attribute_fqdn.txt") as json_file:
#     attribute_list = json.load(json_file)
#     for attribute in attribute_list:
#         print("attribute: ", attribute)
#         print("type",type(attribute))
#         try:
#             print("AttributeAdd on evt subscriber--------------------------------------------------------")
#             evt_subscriber_proxy.command_inout("AttributeAdd",[attribute, "ALWAYS", "0"])
#             #evt_subscriber_proxy.AttributeAdd([attribute, "ALWAYS", "0"])
#         except Exception as except_occured:
#             print("except_occured: ", except_occured)
#
#             pass