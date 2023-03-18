from discord.ext import commands
from start_script import intents
from apps import get_cat
from Commands import Commands


bot = commands.Bot(command_prefix='$', intents=intents)


# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print('------')
#
#
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if "кот" in message.content.lower():
#         await message.channel.send(get_cat())
#     else:
#         await message.channel.send("Хочешь кота")
