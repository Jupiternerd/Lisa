'''
Author | Shokkunn
'''
import discord
import asyncio

from discord.ext.commands import bot
from discord.ext import commands, tasks

class Core(commands.Cog):
    '''
    purpose | Help command.
    '''
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def help(self, ctx):
        await ctx.send("ok")
        


def setup(bot):
    bot.add_cog(Core(bot))