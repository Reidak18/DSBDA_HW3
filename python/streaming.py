import websocket
import requests
import random
import json

def get_streaming_server_key(token):
    request_url = "https://api.vk.com/method/streaming.getServerUrl?access_token={}&v=5.64".format(token)
    r = requests.get(request_url)
    data = r.json()
    return {"server":data["response"]["endpoint"],"key":data["response"]["key"]}

def listen_stream():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://{}/stream?key={} ".format(stream["server"], stream["key"]),
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def on_message(ws, message):
    print(">>>> receive message:", message)

def on_error(ws, error):
    print(">>>> error thead:",error)

def on_close(ws):
    print(">>>> close thead")

def on_open(ws):
    print(">>>> open thead")
    
def set_rules(value):
    rule_params = {"rule":{"value":value,"tag":'tag_'+str(random.randint(11111, 99999))}}
    headers = {'content-type': 'application/json'}
    r = requests.post("https://{}/rules?key={}".format(stream["server"], stream["key"]), data=json.dumps(rule_params), headers=headers)
    data = r.json()

    return data['code'] == 200


if __name__ == '__main__':
    stream = get_streaming_server_key("602c1096602c1096602c109628605970766602c602c10963fe3c0f8932f9fe24fd0b6cd")
    set_rules('я')
    set_rules('ты')
    set_rules('кот')
    listen_stream()
