#"based_on": 1, 
#"changed_by": 1, 
#"changed_by_id": 0, 
#"current_value": 0.0, 
#"data": "", 
#"editable": 0, 
#"id": 132, 
#"instance": 0, 
#"last_changed": 1509886755, 
#"last_value": 0.0, 
#"maximum": 1, 
#"minimum": 0, 
#"node_id": 23, 
#"options": [], 
#"state": 1, 
#"step_value": 0.5, 
#"target_value": 0.0, 
#"type": 30, 
#"unit": ""

class Attribute():
    def __init__(self, attribute_dict):
        self.id = attribute_dict['id']
        self.node_id = attribute_dict['node_id']
        self.editable = attribute_dict['editable']
        self.value = attribute_dict['current_value']
        self.unit = attribute_dict['unit']
        self.type = attribute_dict['type']
