#!/usr/bin/env python3
from discord.ext import commands


def setup(bot):
    bot.add_cog(Default(bot))


class Default(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello!')

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'{latency} ms')
