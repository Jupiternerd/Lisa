'''
Author | Shokkunn
'''
from discord.ext.commands.core import Command
from discord.ext.commands.errors import CommandError
from lisa.client import _prefix
import discord
import asyncio

from utilities.dBframeworks.schematics import Servers, Users
from utilities.constant_code import UserBlacklisted
from discord.ext import commands
import random

class Before(commands.Cog):
    '''
    purpose | this cog conatains checks.
    '''
    def __init__(self, bot):
        self.bot = bot

    '''
    This applies to all commands.
    '''


    async def bot_check(self, ctx):
        err = False
        #if in db
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return err;
        
        
        #if not in db
       # err = self.db_check_list(ctx);
        #ctx.check_blacklist();
        err = ctx.check_list();
        print(err)

        return err;
        #if user not in database



    


def setup(bot):
    bot.add_cog(Before(bot))