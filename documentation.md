# Deposco API Documentation
## Get All Products

### XML Tree

- ns2:items
  - item
    - businessUnit
    - number
    - name
    - itemType
    - classType
    - shortDescription
    - longDescription
    - dimension
      - length
      - width
      - height
      - volume
    - itemWeight
      - weight
    - abcCategory
    - productCode
    - originCountry
    - cycleCount
    - tradingPartner
    - purchaseCost
    - unitPrice
    - bornOnDateRequired
    - expirationDateRequired
    - receiveDateRequired
    - quarantineRequired
    - inspectionRequired
    - catchWeightRequired
    - hazmat
    - hazmatCode
    - intangibleItemFlag
    - inventoryTrackingEnabled
    - lotTrackingEnabled
    - serialTrackingEnabled
    - shippable
    - purchased
    - receiveOverTolerance
    - receiveUnderTolerance
    - cycleCountFrequency
    - reorderQuantity
    - customFields
    - carrierSpecialServices
    - packs
      - pack
        - type
        - quantity
        - weight
        - weightUOM
        - dimension
          - length
          - width
          - height
          - volume
        - units
        - upcs
        - customMappings
    - upcs
    - nmfcNumber
    - harmonizedCode
    - mixLots
    - customMappings
    - components
    - itemVendors
    - ule
    - kitOrderOnly
    - kitStockOnly
    - createdDate
    - updatedDate
    - assemblyCost
    - handlingCost
    - storageCost
    - assembleToOrderFlag
    - salesEnabledFlag
    - reorderPoint
    - pickStrategy
    - planItems


  
### Fields Description (of item)

**businessUnit**

Description: The business unit code.

Example: "ZESTT"

---
**number**

Description: The item number or SKU.

Example: "Z-PK104"

---
**name**

Description: The name of the item.

Example: "Z- Large Box"

---
**itemType**

Description: The type of the item.

Nullable: Yes

---
**classType**

Description: The class of the item.

Nullable: Yes

---
**shortDescription**

Description: A short description of the item.

Example: "Z- Large Box"

---
**longDescription**

Description: A detailed description of the item.

Example: "Z- Large Box"

---
**dimension**

Description: The dimensions of the item.

length: Length of the item.
Example: 0.0

width: Width of the item.
Example: 0.0

height: Height of the item.
Example: 0.0

volume: Volume of the item.
Example: 0.0

---
**itemWeight**

Description: The weight details of the item.

weight: Weight of the item.

Example: 0.0

---
**abcCategory**

Description: ABC category.

Nullable: Yes

---
**productCode**

Description: Product code.

Nullable: Yes

---
**originCountry**

Description: Country of origin.

Example: "IN"

---
**cycleCount**

Description: Indicates if the item requires cycle counting.

Example: false

---
**tradingPartner**

Description: Trading partner information.

Nullable: Yes

---
**purchaseCost**

Description: Purchase cost of the item.

Example: 0.0

---
**unitPrice**

Description: Unit price of the item.

Example: 0.0

---
**bornOnDateRequired**

Description: Indicates if a born-on date is required.

Example: false

---
**expirationDateRequired**

Description: Indicates if an expiration date is required.

Example: false

---
**receiveDateRequired**

Description: Indicates if a recieve date is required.

Example: false

---
**quarantineRequired**

Description: Indicates if quarantine is required.

Example: false

---
**inspectionRequired**

Description: Indicates if inspection is required.

Example: false

---
**catchWeightRequired**

Description: Indicates if catch weight is required.

Nullable: Yes

---
**hazmat**

Description: Indicates if the item is hazardous material.

Example: false

---
**hazmatCode**

Description: Hazardous material code.

Nullable: Yes

---
**intangibleItemFlag**

Description: Indicates if the item is intangible.

Example: false

---
**inventoryTrackingEnabled**

Description: Indicates if inventory tracking is enabled.

Example: false

---
**lotTrackingEnabled**

Description: Indicates if lot tracking is enabled.

Example: false

---
**serialTrackingEnabled**

Description: Indicates if serial tracking is enabled.

Example: false

---
**shippable**

Description: Indicates if the item is shippable.

Example: false

---
**purchased**

Description: Indicates if the item is purchased.

Example: false

---
**receiveOverTolerance**

Description: Receive over tolerance percentage.

Example: 1.0

---
**receiveUnderTolerance**

Description: Receive under tolerance percentage.

Nullable: Yes

---
**cycleCountFrequency**

Description: Frequency of cycle count.

Example: 0

---
**reorderQuantity**

Description: Quantity to reorder.

Example: 0

---
**customFields**

Description: Custom fields for additional data.

---
**carrierSpecialServices**

Description: Carrier special services (if any).

---
**packs**

Description: Packing details.

pack: Information about a pack.

type: Type of pack.
Example: "Pallet"

quantity: Quantity in the pack.
Example: 1

weight: Weight of the pack.
Example: 0.9

weightUOM: Unit of measure for weight.
Example: "LB"

dimension: Dimensions of the pack.

length: Length of the pack.
Example: 6.0

width: Width of the pack.
Example: 10.0

height: Height of the pack.
Example: 1.75

volume: Volume of the pack.
Example: 105.0

units: Unit of measure for dimensions.
Example: "IN"

upcs: Universal Product Codes for the pack (if any).

customMappings: Custom mappings for the pack.
Nullable: Yes

---
**nmfcNumber**

Description: NMFC Number.

Nullable: Yes

---
**harmonizedCode**

Description: Harmonized code.

Nullable: Yes

---
**mixLots**

Description: Indicates if the item can mix lots.

Example: false

---
**customMappings**

Description: Custom mappings.

Nullable: Yes

---
**components**

Description: Item components.

Nullable: Yes

---
**itemVendors**

Description: Item vendors.

Nullable: Yes

---
**ule**

Description: Unit load equipment.

Example: 0.0

---
**kitOrderOnly**

Description: Indicates if the item is order only for kits.

Example: false

---
**kitStockOnly**

Description: Indicates if the item is stock only for kits.

Example: false

---
**createdDate**

Description: Creation date of the item.

Example: "2023-07-27T10:23:29"

---
**updatedDate**

Description: Last update date of the item.

Example: "2024-02-20T10:52:41"

---
**assemblyCost**

Description: Assembly cost of the item.

Example: 0.0

---
**handlingCost**

Description: Handling cost of the item.

Example: 0.0

---
**storageCost**

Description: Storage cost of the item.

Example: 0.0

---
**assembleToOrderFlag**

Description: Indicates if the item is assembled to order.

Example: false

---
**salesEnabledFlag**

Description: Indicates if the item is enabled for sales.

Example: false

---
**reorderPoint**

Description: Reorder point quantity.

Example: 0

---
**pickStrategy**

Description: Picking strategy.

Nullable: Yes

---
**planItems**

Description: Plan items.