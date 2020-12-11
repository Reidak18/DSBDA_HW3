# -*- coding: utf-8 -*-
from vkstreaming import Streaming
#import requests

#def get_streaming_server_key(token):
#    request_url = "https://api.vk.com/method/streaming.getServerUrl?access_token={}&v=5.64".format(token)
#    r = requests.get(request_url)
#    data = r.json()
#    print({"server":data["response"]["endpoint"],"key":data["response"]["key"]})
#    return {"server":data["response"]["endpoint"],"key":data["response"]["key"]}

if __name__ == '__main__':
#    get_streaming_server_key("602c1096602c1096602c109628605970766602c602c10963fe3c0f8932f9fe24fd0b6cd")
    api = Streaming("streaming.vk.com", "6b97d841777df36a36357ddf7a5ba1581548e236")

    api.del_all_rules()
#    api.add_rules("Котики", "кот")

    rules = api.get_rules()
#    for rule in rules:
#        print(("{tag:15}:{value}").format(**rule))

    @api.stream
    def my_func(event):
        print("[{}]: {}".format(event['author']['id'], event['text']))

    api.start()
