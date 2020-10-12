from flask import Flask, request
from mdns import get_device_info
from os import path
import json, requests

app = Flask(__name__)
device_info = {}


@app.route('/devices', methods=['GET'])
def list_devices():
    return json.dumps(list(device_info.values()), indent=4)


@app.route('/fulldevices', methods=['GET'])
def update_list_devices():
    update_device_info()
    return json.dumps(list(device_info.values()), indent=4)


@app.route('/on/<device_id>', methods=['GET'])
def on_device(device_id):
    if device_id in device_info:
        info = device_info[device_id]
        body_post = { 
                "deviceid": device_id,
                "data": { "switch": "on" }
                }
        url_post = 'http://%s:%s/zeroconf/switch' % (info['ip'], info['port'])
        requests.post(url_post, json.dumps(body_post))
        return { 'result': 'ok' }
    else:
        return { 'result': 'error: id %s is unknown' % device_id }


@app.route('/startup/<device_id>/<startup>', methods=['GET'])
def update_startup(device_id, startup):
    # State of switch when power supply is recovered
    valid_startup = ['off', 'on', 'stay']
    if device_id in device_info:
        info = device_info[device_id]
        if startup in valid_startup:
            body_post = { 
                    "deviceid": device_id,
                    "data": { "startup": startup }
                    }
            url_post = 'http://%s:%s/zeroconf/startup' % (info['ip'], info['port'])
            ret = requests.post(url_post, json.dumps(body_post))
            print(ret.text)
            return { 'result': 'ok' }
        else:
            return { 'result': 'error: startup value %s is unknown' % status }
    else:
        return { 'result': 'error: id %s is unknown' % device_id }


@app.route('/desc/<device_id>', methods=['POST'])
def off_device(device_id):
    if device_id in device_info:
        if 'desc' in request.json:
            device_info[device_id]['desc'] = request.json['desc']
            desc = {}
            for d in device_info.values():
                if 'desc' in d:
                    desc[device_id] = d['desc']
            if len(desc) > 0:
                with open('desc.json', 'w') as outfile:
                    json.dump(desc, outfile)
        return { 'result': 'ok' }
    else:
        return { 'result': 'error: id %s is unknown' % device_id }


def update_device_info():
    global device_info
    device_info = get_device_info()
    if path.exists('desc.json'):
        with open('desc.json') as json_file:
            data = json.load(json_file)
            for d in data:
                device_info[d]['desc'] = data[d]


if __name__ == "__main__":
    print("+ Scanning for devices:")
    update_device_info()
    if len(device_info) > 0:
        print("+ Start the server")
        app.run(host= '0.0.0.0')
    else:
        print("+ No detected device!")
