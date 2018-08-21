from cloudant.client import Cloudant
from cloudant.error import CloudantException

# Connect to cloudant service instance
# Following is found on IBM Cloud Dashboard
# Click - Services MapleTest
# Click - View Credentials for MapleAdmin
client = Cloudant("70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix",
                  "415faa16400b70485fbacecbd6eebe950f5e022676dd89de2cbc10999cfc3a61",
                  url = "https://70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix:415faa16400b70485fbacecbd6eebe950f5e022676dd89de2cbc10999cfc3a61@70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix.cloudant.com")
                  
# Connect to Cloudant using the credintials abive
client.connect()

# Set the database we want to work with
databaseName = "maplehwinv"

# If DB already created, just open it ####
hiDatabase = client[databaseName]

    
invItem = [
   ["Cable", "5M", "Blue", "IBM", "", "", "5M OM3 fibre channel cable"]
]

# Create documents by using the inventory item(s).
# Go through each row in the array
for document in invItem:
    # Retrieve the fields in each row.
    Type = document[0]
    Size = document[1]
    Colour = document[2]
    Manufacturer = document[3]
    PartNumber = document[4]
    FeatureCode = document[5]
    Description = document[6]

    # Create a JSON document that represents
    # all the data in the row.
    jsonDocument = {
        "typeField": Type,
        "sizeField": Size,
        "colourField": Colour,
        "manufacturerField": Manufacturer,
        "partNumField": PartNumber,
        "featureCodeField": FeatureCode,
        "descriptionField": Description,
        }

    # Create a document by using the database API.
    newDocument = hiDatabase.create_document(jsonDocument)

    # Check that the document exists in the database.
    if newDocument.exists():
        print("Document '{0}' successfully created:".format(Description))
     
client.disconnect()
