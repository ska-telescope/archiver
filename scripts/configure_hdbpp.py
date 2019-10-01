
#Imports
from tango import DeviceProxy
import time
import json

# Creating Device proxies
try:
    conf_manager_proxy = DeviceProxy('tango://archiver-1234-databaseds:10000/archiving/hdbpp/confmanager01')
    print("conf_manager_proxy done")
    evt_subscriber_proxy = DeviceProxy("tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
    property = evt_subscriber_proxy.delete_property("AttributeList")
    property = evt_subscriber_proxy.get_property("AttributeList")
    print("get_property Name after delete_property------------------------------------------AttributeList: ", property)
    archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
    print("archiver_list before : ", archiver_list)

    # Archiver Remove
    # conf_manager_proxy.command_inout("ArchiverRemove", "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")

    archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
    print("archiver_list after: ", archiver_list)

    print("evt_subscriber_proxy done")
except Exception as except_occured:
     print("except_occured: ", except_occured)
     pass

# Add archiver
#conf_manager_proxy.command_inout("ArchiverAdd", "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
# time.sleep(2)
# print("ArchiverAdd done success")

# SetAttributeName
conf_manager_proxy.write_attribute("SetAttributeName","tango://archiver-1234-databaseds:10000/sys/tg_test/1/ampli")
print("SetAttributeName: ", conf_manager_proxy.SetAttributeName)
# SetArchiver
conf_manager_proxy.write_attribute("SetArchiver", "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
print("SetArchiver: ", conf_manager_proxy.SetArchiver)

# SetStrategy
conf_manager_proxy.write_attribute("SetStrategy","ALWAYS")
print("SetStrategy: ", conf_manager_proxy.SetStrategy)

# SetPollingPeriod
conf_manager_proxy.write_attribute("SetPollingPeriod",1000)
print("SetPollingPeriod: ", conf_manager_proxy.SetPollingPeriod)

# SetEventPeriod
conf_manager_proxy.write_attribute("SetPeriodEvent",3000)
print("SetPeriodEvent: ", conf_manager_proxy.SetPeriodEvent)

# Add Attribute
conf_manager_proxy.command_inout("AttributeAdd")

print("AttributeAdd done success")
property = evt_subscriber_proxy.get_property("AttributeList")
print("get_property Name after-----------------------------------------AttributeList: ", property)
#
archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
print("archiver_list after : ", archiver_list)

# Attribute Remove
# try:
#     conf_manager_proxy.command_inout("AttributeRemove", "sys/tg_test/1/ampli")
#     print("get_property Name after AttributeRemove------------------------------------------AttributeList: ", property)
# except Exception as except_occured:
#      print("except_occured: ", except_occured)
#      pass

# Archiver Remove
#conf_manager_proxy.command_inout("ArchiverRemove", "archiving/hdbpp/eventsubscriber01")

# archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
# print("archiver_list after: ", archiver_list)