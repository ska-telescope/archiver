
#Imports
from tango import DeviceProxy
import json
import argparse

fqdn_list = argparse.ArgumentParser()
fqdn_list.add_argument("cm_fqdn")
fqdn_list.add_argument("em_fqdn")
args = fqdn_list.parse_args()

#Configuration Manager Proxy
conf_manager_proxy = DeviceProxy(str(args.cm_fqdn))

#Event subscriber Proxy
evt_subscriber_proxy = DeviceProxy(str(args.em_fqdn))

try:
    conf_manager_proxy.Archiveradd(str(args.em_fqdn))

except Exception as except_occured:
    print("Archiver is already added. Process will be continued.")

#conf_manager_proxy.SetArchiver = "tango://alpha:10000/archiving/hdb++/eventsubscriber.01"

with open("/attribute_fqdn.txt") as json_file:
    attribute_list = json.load(json_file)
    for attribute in attribute_list:
        try:
            duplicate_attribute = (attribute)          # Used in Exception to show duplicate attributes
            evt_subscriber_proxy.AttributeAdd([attribute, "ALWAYS", "0"])

        except Exception as except_occured:
            print("Exception: Attribute alredy subscribed:", duplicate_attribute)
            pass