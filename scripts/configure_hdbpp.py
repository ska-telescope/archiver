
#Imports
from tango import DeviceProxy
import time
import json

# Creating Device proxies
try:
    conf_manager_proxy = DeviceProxy('tango://databaseds:10000/archiving/hdbpp/confmanager01')
    print("conf_manager_proxy done")
    evt_subscriber_proxy = DeviceProxy("tango://databaseds:10000/archiving/hdbpp/eventsubscriber01")
    property = evt_subscriber_proxy.delete_property("AttributeList")
    property = evt_subscriber_proxy.get_property("AttributeList")
    print("get_property Name after delete_property------------------------------------------AttributeList: ", property)
    print("evt_subscriber_proxy done")
except Exception as except_occured:
     print("except_occured: ", except_occured)
     pass

# Add archiver
#conf_manager_proxy.command_inout("ArchiverAdd", "tango://databaseds:10000/archiving/hdb++/eventsubscriber.06")
#time.sleep(2)
#print("ArchiverAdd done success")

# SetAttributeName
conf_manager_proxy.write_attribute("SetAttributeName","sys/tg_test/1/ampli")

# SetArchiver
conf_manager_proxy.write_attribute("SetArchiver", "tango://databaseds:10000/archiving/hdbpp/eventsubscriber01")

# SetStrategy
conf_manager_proxy.write_attribute("SetStrategy","ALWAYS")

# SetPollingPeriod
conf_manager_proxy.write_attribute("SetPollingPeriod",1000)

# SetEventPeriod
conf_manager_proxy.write_attribute("SetPeriodEvent",3000)

# Add Attribute
conf_manager_proxy.command_inout("AttributeAdd")

print("AttributeAdd done success")

archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
print("archiver_list before : ", archiver_list)

# Attribute Remove
# conf_manager_proxy.command_inout("AttributeRemove", "tango://databaseds:10000/sys/tg_test/1/ampli")
# print("get_property Name after AttributeRemove------------------------------------------AttributeList: ", property)

# Archiver Remove
#conf_manager_proxy.command_inout("ArchiverRemove", "tango://databaseds:10000/archiving/hdbpp/eventsubscriber01")

# archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
# print("archiver_list after: ", archiver_list)








# 'tango://databaseds.tangonet:10000/archiving/hdbpp/confmanager01'
# try:
#     print("Creating Device proxies -------------------------------------------------------------------")
#     conf_manager_proxy = DeviceProxy('tango://databaseds.tangonet:10000/archiving/hdbpp/confmanager01')
#     print("conf_manager_proxy: ", conf_manager_proxy)
#     evt_subscriber_proxy = DeviceProxy("tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
#     print("evt_subscriber_proxy: ", evt_subscriber_proxy)
# except Exception as except_occured:
#     print("except_occured: ", except_occured)
#
# property= conf_manager_proxy.get_property("ArchiverList")
# print("get_property Name before ArchiverRemove ------------------------------------------ArchiverList: ", property)
#
# property= evt_subscriber_proxy.get_property("AttributeList")
# print("get_property Name before AttributeRemove------------------------------------------AttributeList: ", property)
# conf_manager_proxy.delete_property("ArchiverList")
# time.sleep(5)
# property= evt_subscriber_proxy.delete_property("ArchiverList")
# time.sleep(5)
#
# property= evt_subscriber_proxy.get_property("AttributeList")
# print("get_property Name after delete_property------------------------------------------AttributeList: ", property)
#
# #conf_manager_proxy.command_inout("ArchiverRemove","tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
# # evt_subscriber_proxy.command_inout("AttributeRemove", "sys/tg_test/1/ampli")
# time.sleep(5)
#
# property= conf_manager_proxy.get_property("ArchiverList")
# print("get_property Name after ArchiverRemove ------------------------------------------ArchiverList: ", property)
#
# #conf_manager_proxy.command_inout("ArchiverAdd","tango://databaseds.tangonet:10000/archiving/hdbpp/eventsubscriber01")
# time.sleep(5)
# property= conf_manager_proxy.get_property("ArchiverList")
# print("get_property Name after ArchiverAdd ------------------------------------------ArchiverList: ", property)
#
# # property= evt_subscriber_proxy.get_property("AttributeList")
# # print("get_property Name after AttributeRemove------------------------------------------AttributeList: ", property)
# time.sleep(5)
#
# # AttributeAdd method
# # conf_manager_proxy.write_attribute("SetAttributeName","sys/tg_test/1/ampli")
# # print("Setattribute Name Success------------------------------------------")
# # conf_manager_proxy.write_attribute("SetArchiver", "archiving/hdbpp/eventsubscriber01")
# # print("SetArchiver Success------------------------------------------")
# # conf_manager_proxy.write_attribute("SetStrategy", "ALWAYS")
# # print("SetStrategy Success------------------------------------------")
# # conf_manager_proxy.write_attribute("SetCodePushedEvent",True)
# # print("SetCodePushedEvent Success------------------------------------------")
# # conf_manager_proxy.write_attribute("SetTTL", 0)
# # print("SetTTL Success------------------------------------------")
#
# # conf_manager_proxy.command_inout("AttributeAdd")
# print("AttributeAdd command Success------------------------------------------")
#
# time.sleep(5)
#
# property= conf_manager_proxy.get_property("ArchiverList")
# print("get_property Name Success after SetArchiver ------------------------------------------ArchiverList: ", property)
# property= evt_subscriber_proxy.get_property("AttributeList")
# print("get_property Name Success after SetAttributeName ------------------------------------------AttributeList: ", property)



