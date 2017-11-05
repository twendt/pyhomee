#        {
#            "added": 1509750782, 
#            "attributes": [], 
#            "cube_type": 1, 
#            "denied_user_ids": [], 
#            "favorite": 0, 
#            "history": 1, 
#            "id": 24, 
#            "image": "default", 
#            "name": "Popp / Duwi ZW FB Wireless remote control 10-channel", 
#            "note": "", 
#            "order": 12, 
#            "owner": 1, 
#            "phonetic_name": "", 
#            "profile": 0, 
#            "protocol": 1, 
#            "routing": 0, 
#            "services": 255, 
#            "state": 1, 
#            "state_changed": 1509751110
#        }
import urllib
from pyhomee.attribute import Attribute

class Node():
    def __init__(self, node_dict):
        self.id = node_dict["id"]
        self.name = urllib.parse.unquote(node_dict["name"]).replace(" ", "_")
        self.profile = node_dict["profile"]
        self.state_changed = node_dict["state_changed"]
        self.added = node_dict["added"]
        self.attributes = []
        self.add_attributes(node_dict['attributes'])

    def add_attributes(self, attributes):
        for attribute in attributes:
            self.attributes.append(Attribute(attribute))
