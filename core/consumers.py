from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
import json
from models.implementation import Notifications

@database_sync_to_async
def get_user(user_id):
    try:
        return Users.objects.get(id=user_id)
    except:
        return AnonymousUser()


@database_sync_to_async
def create_notification(receiver, typeof="task_created", status="unread"):
    
    notification_to_create=Notifications.objects.create(user_revoker=receiver, type_of_notification=typeof)
    print('I am here to help')
    return (notification_to_create.user_revoker.username, notification_to_create.type_of_notification)
 

class NotificationConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
            print('connected', event)
            print('Am i finally here')
            print(self.scope['user'].id)
            await self.accept()
            
            await self.send(json.dump({
                "type":"websocket.send",
                "text":"hello",
            }))