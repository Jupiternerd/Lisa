'''
Author | Shokkunn
'''
import discord
import asyncio

from discord.ext.commands import bot
from utilities.constants import constants
from discord.ext import commands, tasks

class BeforeCommand(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
    

    async def cog_before_invoke(self, ctx):
        print (ctx)
        return
        

    async def msg(self, message):
        await message.channel.send(constants.a)
        print("a")

def setup(bot):
    bot.add_cog(BeforeCommand(bot))