'''
Author | Shokkunn
'''
from discord.ext.commands.core import is_owner
from utilities.dBframeworks.schematics import Characters
from utilities.novel import Novel
from utilities.makeGif import Gif
from discord.ext import commands, tasks
from utilities.menu import Menu
from discord import Embed
import json
class Read(commands.Cog, name="wai"):

    def __init__(self, bot):
        self.bot = bot
        
        #print(novelJSON + "NOVEL")   
    @commands.group(name= "panel", invoke_without_command = True)
    async def panel(self, ctx):
        pass;

    @panel.command(name= "ban")
    async def ban(self, ctx):
        print("feed")



   
        

def setup(bot):
    bot.add_cog(Read(bot))