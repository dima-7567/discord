import logging
import discord

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.StreamHandler()
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
