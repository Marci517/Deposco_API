import requests
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth
import xml.dom.minidom

# Define credentials
username = 'hbird'
password = 'Hbird@APi9'


# Function to get product details as XML
def get_product_details(itemNumber):
    url = f'https://nfie-uat.deposco.com/integration/NFIE/items/{itemNumber}'
    # Make the API call with Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        # Parse the XML data
        root = ET.fromstring(response.content)
        return root
    else:
        print(f"Failed to retrieve data for item {itemNumber}: {response.status_code}")
        return None


# Function to get all inventories
def get_all_inventories(root):
    itemNumbers = []
    for item_inventory in root.findall('.//itemInventory'):
        item_number = item_inventory.find('itemNumber').text
        itemNumbers.append(item_number)
    return itemNumbers


# Function to prettify XML
def prettify_xml(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


# Define the URL of the API endpoint
url = 'https://nfie-uat.deposco.com/integration/NFIE/inventory/full'

# Make the API call with Basic Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data
    root = ET.fromstring(response.content)
    # Get all inventories
    itemNumbers = get_all_inventories(root)

    # Get and print product details for each item number
    for i in itemNumbers:
        product_details = get_product_details(i)
        if product_details is not None:
            pretty_xml = prettify_xml(product_details)
            print(pretty_xml)
else:
    print(f"Failed to retrieve data: {response.status_code}")
