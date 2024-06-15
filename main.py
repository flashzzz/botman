
from discord import (
    Intents, Client, app_commands, Message as DiscordMessage, Thread)
import logging
from src.utils.logging_utils import logger
from src.utils.common_utils import should_block
from src.config.env import DISCORD_TOKEN


logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)

intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready()-> None:
    logger.info(f"{client.user} has been summoned!")


# calls for each message
@client.event
async def on_message(message: DiscordMessage):
    try:
        # ignore messages from the bot
        if message.author == client.user:
            return
        
        # block servers not in allow list
        if should_block(guild=message.guild):
            return

        channel = message.channel
        
        # skip moderation and threads
        
        if message.content == "ping":
            await message.channel.send("pong")
        if message.content == "pong":
            await message.channel.send("ping")
    except Exception as e:
        logger.error(e, exc_info=True)
    
    
client.run(DISCORD_TOKEN)