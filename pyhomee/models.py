import urllib

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

class Attribute():
    def __init__(self, attribute_dict):
        self.id = attribute_dict['id']
        self.node_id = attribute_dict['node_id']
        self.editable = attribute_dict['editable']
        self.value = attribute_dict['current_value']
        self.unit = attribute_dict['unit']
        self.type = attribute_dict['type']

class Group():
    def __init__(self, group_dict):
        self.id = group_dict['id']
        self.category = group_dict['category']
        self.name = group_dict['name']
        self.image = group_dict['image']
        self.note = group_dict['note']
        self.owner = group_dict['owner']
        self.state = group_dict['state']
        self.phonetic_name = group_dict['phonetic_name']
        self.services = group_dict['services']
        self.order = group_dict['order']
        self.added = group_dict['added']

class Relationship():
    def __init__(self, relationship_dict):
        self.id = relationship_dict['id']
        self.homeegram_id = relationship_dict['homeegram_id']
        self.group_id = relationship_dict['group_id']
        self.node_id = relationship_dict['node_id']
        self.order = relationship_dict['order']

class Homeegram():
    def __init__(self, homeegram_dict):
        self.id = homeegram_dict['id']
        self.play = homeegram_dict['play']
        self.name = homeegram_dict['name']
        self.state = homeegram_dict['state']
        self.visible = homeegram_dict['visible']
        self.active = homeegram_dict['active']

