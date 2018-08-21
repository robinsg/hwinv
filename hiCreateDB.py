from cloudant.client import Cloudant
from cloudant.error import CloudantException

# Connect to cloudant service instance
# Following is found on IBM Cloud Dashboard
# Click - Services MapleDBs
# Click - View Credentials for MapleAdmin
client = Cloudant("70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix",
                  "415faa16400b70485fbacecbd6eebe950f5e022676dd89de2cbc10999cfc3a61",
                  url = "https://70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix:415faa16400b70485fbacecbd6eebe950f5e022676dd89de2cbc10999cfc3a61@70c9f5bf-dd62-4fbe-a3d1-4cc83eeed72b-bluemix.cloudant.com")
                  
# Connect to Cloudant using the credintials above
client.connect()

# Set the database we want to work with
# databse name cannot contain upper case letters
databaseName = "maplehwinv"

# Create the database
hiDatabase = client.create_database(databaseName)
if hiDatabase.exists():
    print("'{0}' succesfully created.\n".format(databaseName))

    
    
client.disconnect()
print("Disconnected from database")


