import sys
import pymongo
import re
from pymongo import MongoClient
import tshark

# The number of BSON documents written
total = 0

#URI (Uniform Resource Identifier) to connect to MongoDB database 
client_URI = "mongodb+srv://coline:clondonc@cluster0.4olg7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" 
client = MongoClient(client_URI)
db = client.Tshark # use or create a database named Twitter
test_collection = db.test #use or create a collection named 
test_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique
post= {"name":"cidhf","age":22}
test_collection.insert_one(post)

# Read the file from stdin, line by line
for line in sys.stdin:
        line = line.rstrip('\n')
        parsed = line.split("\t")
        total = total + 1

        # Construct the "record to be inserted
        netpacket = {
                'framenumber': parsed[0],
                'sourceIP': parsed[1],
                'destIP': parsed[2],
                'framelength': parsed[3],
                'IPlength': parsed[4]
                }

        # Store it!
        net_id = traffic.insert(netpacket)

client.close()

# Present the total number of BSON documents written
print("Total number of documents stored: "), total
