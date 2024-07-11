import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth
import xml.dom.minidom

# Define credentials
username = 'hbird'
password = 'Hbird@APi9'


# Function to get all inventories
def get_all_inventories(root):
    inventories = []

    for item_inventory in root.findall('.//itemInventory'):
        item_number = item_inventory.find('itemNumber').text
        facility_inventory = item_inventory.find('facilityInventory')
        facility = facility_inventory.find('facility').text
        inventory = facility_inventory.find('inventory')
        total = inventory.find('total').text
        available = inventory.find('availableToPromise').text
        unallocated = inventory.find('unallocated').text
        allocated = inventory.find('allocated').text

        inventories.append({
            'itemNumber': item_number,
            'facility': facility,
            'total': total,
            'availableToPromise': available,
            'unallocated': unallocated,
            'allocated': allocated
        })

    return inventories


# Define the URL of the API endpoint
url = 'https://nfie-uat.deposco.com/integration/NFIE/inventory/full'

# Make the API call with Basic Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data
    root = ET.fromstring(response.content)
    # Get all inventories
    itemInventories = get_all_inventories(root)

    # Get and print product details for each item number
    for i in itemInventories:
        print(i)

else:
    print(f"Failed to retrieve data: {response.status_code}")
