import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render


class AnimationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 如果是传参的路由在连接中获取关键字参数方法：
        # client_id = self.scope['url_route']['kwargs']['client_id']
        # print(f"客户端ID为：{client_id}")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        print(f"发送了信息")
        await self.send(text_data=json.dumps(
                {'message': message}
            )
        )


def websocket_test(request):
    return render(request, "websocketTest.html")
