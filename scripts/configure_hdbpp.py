
#Imports
import sys
from tango import DeviceProxy, DevFailed

def create_proxy():
    # Creating Device proxies
    ret_value = False
    try:
        conf_manager_proxy = DeviceProxy('tango://archiver-1234-databaseds:10000/archiving/hdbpp/confmanager01')
        print("conf_manager_proxy done")
        evt_subscriber_proxy = DeviceProxy("tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
        print("evt_subscriber_proxy done")
        # property = evt_subscriber_proxy.delete_property("AttributeList")
        property = evt_subscriber_proxy.get_property("AttributeList")
        print("get_property Name ------------------------------------------AttributeList: ",
              property)
        archiver_list = conf_manager_proxy.read_attribute("ArchiverList")
        print("archiver_list : ", archiver_list)
        ret_value = True
        # Archiver Remove
        # conf_manager_proxy.command_inout("ArchiverRemove", "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
    except Exception as except_occured:
        print("except_occured: ", except_occured)
        ret_value = False
    return ret_value

def cm_configure_attributes():
    ret_value = False
    try:
        # SetAttributeName
        conf_manager_proxy.write_attribute("SetAttributeName",
                                           "tango://archiver-1234-databaseds:10000/sys/tg_test/1/ampli")
        print("SetAttributeName: ", conf_manager_proxy.SetAttributeName)

        # SetArchiver
        conf_manager_proxy.write_attribute("SetArchiver",
                                           "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
        print("SetArchiver: ", conf_manager_proxy.SetArchiver)

        # SetStrategy
        conf_manager_proxy.write_attribute("SetStrategy", "ALWAYS")
        print("SetStrategy: ", conf_manager_proxy.SetStrategy)

        # SetPollingPeriod
        conf_manager_proxy.write_attribute("SetPollingPeriod", 1000)
        print("SetPollingPeriod: ", conf_manager_proxy.SetPollingPeriod)

        # SetEventPeriod
        conf_manager_proxy.write_attribute("SetPeriodEvent", 3000)
        print("SetPeriodEvent: ", conf_manager_proxy.SetPeriodEvent)
        ret_value = True

    except Exception as except_occured:
        print("except_occured: ", except_occured)
        ret_value = False
    return ret_value

def cm_add_attribute():
    ret_value = False
    try:
        # Add Attribute
        conf_manager_proxy.command_inout("AttributeAdd")
        ret_value = True
    except DevFailed as df:
        # print("cm_add_attribute except_occured: ", df)
        str_df = str(df)
        print("cm_add_attribute except_occured reason: ", str_df)

        if "reason = Already archived" in str_df:
            start_archiving()
            ret_value = True
        else:
            ret_value = False
    return ret_value

def start_archiving():
    try:
        conf_manager_proxy.command_inout("AttributeStart", "sys/tg_test/1/ampli")
    except Exception as except_occured:
        print("start_archiving except_occured: ", except_occured)



# conf_manager_proxy = None
# evt_subscriber_proxy = None
#
# result = create_proxy()
conf_manager_proxy = DeviceProxy('tango://archiver-1234-databaseds:10000/archiving/hdbpp/confmanager01')
evt_subscriber_proxy = DeviceProxy("tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")

print ("conf_manager_proxy: ", conf_manager_proxy)
print("evt_subscriber_proxy: ", evt_subscriber_proxy)

result = cm_configure_attributes()
if result == True:
    result = cm_add_attribute()
else:
    print ("No add_attribute")





# Add archiver
#conf_manager_proxy.command_inout("ArchiverAdd", "tango://archiver-1234-databaseds:10000/archiving/hdbpp/eventsubscriber01")
# time.sleep(2)
# print("ArchiverAdd done success")

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