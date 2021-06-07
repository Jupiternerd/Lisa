'''
Author | Shokkunn
'''
import discord
from discord.ext import commands

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
        else:
            await guild.owner.send("b")
            

 
def setup(bot):
    bot.add_cog(ServerJoin(bot))