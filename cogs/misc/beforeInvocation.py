'''
Author | Shokkunn
'''
import discord
import asyncio
from discord.ext import commands, tasks

class beforeCommand(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print("a")

    @commands.command(aliases=["b", "c"])
    async def a(self, ctx):
        await ctx.send("Bruh")



    

 
def setup(bot):
    bot.add_cog(beforeCommand(bot))