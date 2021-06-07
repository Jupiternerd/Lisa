'''
Author | Shokkunn
'''
from discord.ext.commands.core import Command
from discord.ext.commands.errors import CommandError
from lisa.client import _prefix
import discord
import asyncio

from utilities.dBframeworks.schematics import Server, User
from utilities.constant_code import UserBlacklisted
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
        err = False
        #if in db
        if isinstance(ctx.channel, discord.channel.DMChannel):
            return err;
        
        
        #if not in db
        err = self.db_check_list(ctx);
        self.check_blacklist(ctx);

        return err;
        #if user not in database

    def check_blacklist(self, ctx):
        if (self.serverdb):
            blcklst = self.serverdb["blacklist"]
            if str(ctx.author.id) in blcklst:
                raise UserBlacklisted(ctx.author)
        
        else: return;

    def db_check_list(self, ctx):
        #print(ctx.command)
        guild = ctx.guild;
        user = ctx.author;
        db = self.bot.DiscordDb["servers"]
        udb = self.bot.DiscordDb["users"]
        #statisticDb = self.bot.StatsDb["general"]
        userdb = udb.find_one({"_id": user.id})
        self.serverdb = db.find_one({"_id": guild.id})
        #print(db)
        

        if not self.serverdb:
        
            schematic = Server(
               name= guild.name, 
               _id= guild.id,
               owner = guild.owner_id,
               prefix= "-",
               blacklist= {}
            )
            #statisticDb.find_one_and_update()
            db.insert_one(schematic)
            print("nodb serv")
            
            
            return False

        elif not userdb:
                #if user.bot: return
                uschematic = User(
                    name= user.name, 
                    _id= user.id,
                    owner = False,
                    prefix= None,
                    lock= False

                )
                udb.insert_one(uschematic)
                print("nodb user")
                
                return False
        

        return True


def setup(bot):
    bot.add_cog(Before(bot))