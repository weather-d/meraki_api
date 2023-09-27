import meraki
from pprint import pprint
MERAKI_DASHBOARD_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
DASHBOARD = meraki.DashboardAPI(MERAKI_DASHBOARD_API_KEY)
ORGS = DASHBOARD.organizations.getOrganizations()
ORG_ID = '549236'
NETS = DASHBOARD.organizations.getOrganizationNetworks(ORG_ID)
DEVICES = DASHBOARD.networks.getNetworkDevices('L_646829496481105433')

for ORG in ORGS:
    print(f"Org ID:  {ORG['id']} and Org Name: {ORG['name']}")


for NET in NETS:
    print(f"Network ID: {NET['id']}, Name: {NET['name']}, Tags: {NET['tags']}")


for DEVICE in DEVICES:
    print(f"Device Model: {DEVICE['model']}, Serial: {DEVICE['serial']}, MAC: {DEVICE['mac']}, Firmare: {DEVICE['firmware']}")
