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
class Read(commands.Cog, name="Read mf"):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["novel"])
    async def read(self, ctx):
        novelJSON = self.bot.UniverseDb["stories"].find_one({"_id": 2})
        x = Novel(novelJSON, self.bot, ctx.channel, ctx.message.author)

        def te(args):
            print(args.content)

        x.events.message_collected += te
        await x.start() 
        #print(novelJSON + "NOVEL")   
    @commands.group(name= "tomo", invoke_without_command = True)
    async def tomo(self, ctx):

        self.UserDb = self.bot.DiscordDb["users"].find_one({"_id": ctx.author.id})



        pass;

    @tomo.command(name= "feed")
    async def dachi(self, ctx):
        print("feed")



    @commands.command(aliases=["gif"])
    async def g(self, ctx):
        x = Gif(ctx.channel)
        await x.start() 
        print("aaa", ctx.author.id)
        del x
    @is_owner()
    @commands.command(name="makeChar", aliases=["makeCharacter", "make"])
    async def makeChar(self, ctx):
        udb = self.bot.UniverseDb["characters"]
        uschematic = Characters(
            name= "test",
            _id= 0,
            set = 0,
            price = 0,
            description= "yes",
            color= "ff0000",
            blood= 0,
            sex= 0,
            phrase= 0
        )
        udb.insert_one(uschematic)
    @is_owner()
    @commands.command(name="s", aliases=["ms", "ma"])
    async def s(self, ctx):
        ctx.tick(0);
        
    
"""     @commands.command(aliases=["me"])
    async def menu(self, ctx):

        embed = Embed(title = "hahahahha end");
        menuJSONf = open("assets/menu.json", 'rb')
        menuJSON = json.load(menuJSONf)
       
        x = Menu(menuJSONA, self.bot, ctx.channel, ctx.message.author)
        await x.start() 
        menuJSONf.close() """
        

def setup(bot):
    bot.add_cog(Read(bot))