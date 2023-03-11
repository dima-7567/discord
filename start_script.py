import logging
import discord

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "MTA4MTU4OTcwMjczOTYyODEwNA.G-PPP1.5ZpVhdf07IiuzwwzQ9p1RGH26o7WtFKHpm5P44"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
