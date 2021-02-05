'''
Author | Shokkunn
'''
from lisa.client import _prefix
import discord
import asyncio

from utilities.dBframeworks.schematics import Server, User
from discord.ext import commands

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
        #if in db
        if isinstance(ctx.channel, discord.channel.DMChannel): 
            return False
        #if not in db
        return self.stored_in_db(ctx)
        #if user not in database


    def stored_in_db(self, ctx):
        #print(ctx.command)
        guild = ctx.guild;
        user = ctx.author;
        db = self.bot.DiscordDb["servers"]
        udb = self.bot.DiscordDb["users"]
        #statisticDb = self.bot.StatsDb["general"]
        userdb = udb.find_one({"_id": user.id})
        serverdb = db.find_one({"_id": guild.id})
        #print(db)
        

        if not serverdb:
            schematic = Server(
               name= guild.name, 
               _id= guild.id,
               owner = guild.owner_id,
               prefix= "-",
            )
            #statisticDb.find_one_and_update()
            db.insert_one(schematic)
            print("nodb serv")
            
            
            return False

        else: 
            if not userdb:
                #if user.bot: return
                uschematic = User(
                    name= user.name, 
                    _id= user.id,
                    owner = False,
                    prefix= "!",
                )
                udb.insert_one(uschematic)
                print("nodb user")
                return False

        return True
    

def setup(bot):
    bot.add_cog(Before(bot))