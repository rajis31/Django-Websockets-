import json

from channels.generic.websocket import WebsocketConsumer


class  MainConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        for i in range(0,100):
            self.send(text_data=json.dumps({"number": i, "message": message}))

