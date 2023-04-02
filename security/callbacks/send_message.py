from hawk import QueueCallback
from rocketchat.main import RocketChatBot

from security.settings import ROCKET_CHAT_CHANNEL_BLOCK_IP


class SendMessageRocketChatCallback(QueueCallback):
    async def handle(self, message: dict):
        message = message.get('message')
        if message:
            with RocketChatBot() as rocket_chat:
                rocket_chat.chat_post_message(text=message, channel=ROCKET_CHAT_CHANNEL_BLOCK_IP)
