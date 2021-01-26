'''
Author | Shokkunn
'''
import discord
import asyncio
from discord.ext import commands, tasks

class ServerJoin(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = discord.utils.find(lambda chan: chan.name == "general", guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send("a")

    @commands.command(aliases=["b", "c"])
    async def a(self, ctx):
        await ctx.send("Bruh")\

    def bot_check_once(self, ctx):
        if ctx.author.id == 763039325813604402:
            return True
        else:
            return False


 
def setup(bot):
    bot.add_cog(ServerJoin(bot))