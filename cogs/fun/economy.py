'''
Author | Shokkunn
'''
import discord
import asyncio

from discord.ext.commands import bot
from utilities.constants import constants
from discord.ext import commands, tasks

class Economy(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
    


def setup(bot):
    bot.add_cog(Economy(bot))