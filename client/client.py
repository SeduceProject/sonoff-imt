import argparse, json, requests
from argparse import RawTextHelpFormatter

server_ip = "192.168.0.36"
server_port = "5000"


parser = argparse.ArgumentParser(description="Control the devices connected to the Sonoff server", formatter_class=RawTextHelpFormatter)
parser.add_argument("operation", help="""    devices: print information about connected devices
    fulldevices: update the information before printing it
    on: switch on the device (--id is required)
    off: switch off the device (--id is required)
        """)
parser.add_argument("--id", help="select the device from its id")
args = parser.parse_args()

if args.operation == "devices" or args.operation == "fulldevices":
    url = "http://%s:%s/%s" % (server_ip, server_port, args.operation)
    ret = requests.get(url)
    data = json.loads(ret.content.decode('UTF-8'))
    for dev in data:
        print('+ %s - %s' % (dev['id'], dev['desc']))
        print('  network: %s:%s' % (dev['ip'], dev['port']))
        print('  power status: %s' % dev['power'])
        print('  startup conf: %s' % dev['startup'])
if args.operation == "on" or args.operation == "off":
    if args.id is not None:
        url = "http://%s:%s/%s/%s" % (server_ip, server_port, args.operation, args.id)
        ret = requests.get(url)
        print(ret.content.decode('UTF-8'))
    else:
        print("--id is required for 'on' and 'off' operations")
