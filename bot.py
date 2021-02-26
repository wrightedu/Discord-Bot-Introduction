#!/usr/bin/env python3
import os
from os import listdir

import discord
from discord.ext import commands
from dotenv import load_dotenv
from Cogs import *


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


if __name__ == '__main__':
    print('Starting bot')
    for file in listdir('Cogs'):
        if not file.startswith('__') and file.endswith('.py'):
            bot.add_cog(globals()[file[:-3]](bot))
    bot.run(TOKEN)
