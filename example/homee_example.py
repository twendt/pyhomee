from pyhomee import HomeeCube
from pyhomee.attribute import Attribute
import signal
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--cube", dest="cube",
                  help="hostname of Homee Cube")
parser.add_option("-u", "--username",
                  dest="username",
                  help="Username to connect to Cube")
parser.add_option("-p", "--password",
                  dest="password",
                  help="Password to connect to Cube")

(options, args) = parser.parse_args()

cube = HomeeCube(options.cube, options.username, options.password)

def signal_handler(signal, frame):
        cube.stop()
signal.signal(signal.SIGINT, signal_handler)


def print_attribute(attribute):
    print(attribute.value)

nodes = cube.get_nodes()
for node in nodes:
    cube.register(node, print_attribute)

