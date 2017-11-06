import hashlib
import websocket
import time
import json
import requests
import urllib
import logging
from pyhomee.util import get_token
from pyhomee.node import Node
from pyhomee.subscribe import SubscriptionRegistry

_LOGGER = logging.getLogger(__name__)

class HomeeCube():

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.token = self._get_token()
        #websocket.enableTrace(True)
        self.nodes = []
        self._get_nodes()
        self.registry = SubscriptionRegistry(self)
        self.registry.start()

    def _get_token(self):
        url = "http://{}:7681/access_token".format(self.hostname)
        headers = { "Content-Type": "application/x-www-form-urlencoded"}

        form = {
            "device_name": "Home Assistant",
            "device_hardware_id": "homeassistant",
            "device_os": 5,
            "device_type": 3,
            "device_app": 1
        }
        auth = ( self.username, hashlib.sha512(self.password.encode('utf-8')).hexdigest())
        r = requests.post(url, auth=auth, data=form)
        try:
            token = r.text.split("&")[0].split("=")[1]
        except:
            raise Exception("Authenticationfailed")
        return token

    def get_token(self):
        return self.token

    def _get_nodes(self):
        ws = websocket.create_connection("ws://{}:7681/connection?access_token={}".format(self.hostname, self.token),
                                       subprotocols = ["v2"])
        _LOGGER.info("Sending request")
        ws.send("GET:nodes")
        nodes = ws.recv()
        _LOGGER.info(nodes)
        ws.close()
        try:
            parsed = json.loads(nodes)
            #print json.dumps(parsed, indent=4, sort_keys=True)
        except:
            return
        if "nodes" in parsed:
            for node in parsed["nodes"]:
                self.nodes.append(Node(node))
        return

    def get_nodes(self):
        return self.nodes

    def register(self, node, callback):
        self.registry.register(node, callback)

    def send_node_command(self, node, attribute, target_value):
        self.registry.send_node_command(node, attribute, target_value)

    def play_homeegram(self, id):
        self.registry.play_homeegram(id)

    def stop(self):
        self.registry.stop()
