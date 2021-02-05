'''
Author | Shokkunn
'''
import discord
import asyncio

from utilities.dBframeworks.schematics import Server
from discord.ext import commands

class Command(commands.Cog):
    '''
    purpose | this cog conatains bot things.
    '''
    def __init__(self, bot):
        self.bot = bot
    @commands.Bot.before_invoke
    async def bot_before_invoke(self, ctx):
        await ctx.trigger_typing()


    

def setup(bot):
    
    bot.add_cog(Command(bot))