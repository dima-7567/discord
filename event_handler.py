from discord.ext import commands
from start_script import intents
from apps import get_cat
from Commands import Commands


bot = commands.Bot(command_prefix='$', intents=intents)

