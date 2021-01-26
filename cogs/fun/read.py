'''
Author | Shokkunn
'''
import discord
import asyncio
from utilities.novel import Novel
from discord.ext.commands import bot
from utilities.constants import constants
from discord.ext import commands, tasks

class Read(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["novel"])
    async def read(self, ctx):
        novelJSON = self.bot.OrioDb["stories"].find_one({"_id": 0})
        x = Novel(novelJSON, self.bot, ctx)
        #print(novelJSON + "NOVEL")
        

def setup(bot):
    bot.add_cog(Read(bot))