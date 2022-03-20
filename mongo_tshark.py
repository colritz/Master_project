import pyshark
import time
import re
import pymongo
from pymongo import MongoClient

# The number of BSON documents written
total = 0


#URI (Uniform Resource Identifier) to connect to MongoDB database 
client_URI = "mongodb+srv://coline:clondonc@cluster0.4olg7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" 
client = MongoClient(client_URI)
db = client.Tshark # use or create a database named Twitter
test_collection = db.test #use or create a collection named 
test_collection.create_index([("id", pymongo.ASCENDING)],unique = True) # make sure the collected tweets are unique


# define interface
networkInterface = "eth0"

# define capture object
capture = pyshark.LiveCapture(interface=networkInterface)

print("listening on %s" % networkInterface)

while True:
    for packet in capture.sniff_continuously(packet_count=1):
    # adjusted output
        try:
        # get timestamp
        #localtime = time.asctime(time.localtime(time.time()))
     
        # get packet content
        #protocol = packet.transport_layer   # protocol type
        #src_addr = packet.ip.src            # source address
        #src_port = packet[protocol].srcport   # source port
        #dst_addr = packet.ip.dst            # destination address
        #dst_port = packet[protocol].dstport   # destination port
        #length = packet.length
        
            netpacket = {
                    'localtime':time.asctime(time.localtime(time.time())),
                    'protocol': packet.transport_layer,
                    'sourceIP': packet.ip.src,
                    'destIP': packet.ip.dst,
                    'packetlength':packet.length ,
                    }
        
        #netpacket="%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, length)

        # output packet info
            print (netpacket)
            test_collection.insert_one(netpacket)
            
        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
        
    print ("done")
    
