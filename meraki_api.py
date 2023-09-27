import meraki
from pprint import pprint

#Define API Key, Organization ID, and Network ID for the Cisco Meraki Always on Sandbox
MERAKI_DASHBOARD_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
ORG_ID = '549236'
NET_ID = 'L_646829496481105433'

#Create the Meraki Dashboard API with the API Key
DASHBOARD = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY)

#API calls to get the Organizations, Networks, and Devices in the specified IDs.
ORGS = DASHBOARD.organizations.getOrganizations()
NETS = DASHBOARD.organizations.getOrganizationNetworks(ORG_ID)
DEVICES = DASHBOARD.networks.getNetworkDevices(NET_ID)

#Loop through all organizations in the dashboard and print the IDs and Names.
for ORG in ORGS:
    print(f"Org ID:  {ORG['id']} and Org Name: {ORG['name']}")

#Loop through all the networks in an organization and print the ID, Name, and Tags.
for NET in NETS:
    print(f"Network ID: {NET['id']}, Name: {NET['name']}, Tags: {NET['tags']}")

#Loop through all devices in a network and print the model, serial, mac, and firmware version.
for DEVICE in DEVICES:
    print(f"Device Model: {DEVICE['model']}, Serial: {DEVICE['serial']}, MAC: {DEVICE['mac']}, Firmare: {DEVICE['firmware']}")
