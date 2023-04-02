import asyncio
from hawk import Consumer

from security.callbacks import SendMessageRocketChatCallback

loop = asyncio.get_event_loop()


async def main():
    consumer = Consumer()
    consumer.add_consumer_callback('send_message_alert', callback=SendMessageRocketChatCallback())
    await consumer.consume()


if __name__ == "__main__":
    loop.run_until_complete(main())
    loop.close()
