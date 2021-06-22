'''
Author | Shokkunn
'''


from discord.ext import commands
import asyncio
import random

class Lifelike(commands.Cog):
    '''
    purpose | this cog conatains checks.
    '''
    def __init__(self, bot):
        self.bot = bot

    '''
    This applies to all commands.
    '''

    @commands.Cog.listener()
    async def on_command(self, ctx):                
        
        await ctx.trigger_typing();
        

    
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        
        pass;


def setup(bot):
    bot.add_cog(Lifelike(bot))