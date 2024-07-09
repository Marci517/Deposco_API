import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

# Define your credentials
username = 'hbird'
password = 'Hbird@APi9'


# Function to get all inventories
def get_all_inventories(root):
    inventories = []
    for item_inventory in root.findall('.//itemInventory'):
        item_number = item_inventory.find('itemNumber').text
        for facility_inventory in item_inventory.findall('facilityInventory'):
            facility = facility_inventory.find('facility').text
            inventory = facility_inventory.find('inventory')
            total = inventory.find('total').text
            available_to_promise = inventory.find('availableToPromise').text
            unallocated = inventory.find('unallocated').text
            allocated = inventory.find('allocated').text

            inventories.append({
                'itemNumber': item_number,
                'facility': facility,
                'total': total,
                'availableToPromise': available_to_promise,
                'unallocated': unallocated,
                'allocated': allocated
            })
    return inventories


# Function to get one item/product
def get_one_product(inventoryNumber):
    url = f'https://nfie-uat.deposco.com/integration/NFIE/items/{inventoryNumber}'
    # Make the API call with Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password))


# Define the URL of the API endpoint
url = 'https://nfie-uat.deposco.com/integration/NFIE/inventory/full'

# Make the API call with Basic Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data
    root = ET.fromstring(response.content)
    # Get all inventories
    inventories = get_all_inventories(root)
    for i in inventories:
        get_one_product(inventories['inventoryNumber'])

    # Print the inventories
    for inventory in inventories:
        print(inventory)
else:
    print(f"Failed to retrieve data: {response.status_code}")
