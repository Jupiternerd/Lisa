import discord
from utilities.dBframeworks.schematics import Servers, Users
from discord.ext import commands
from utilities.constant_code import UserBlacklisted

class CustomContext(commands.Context):
    
    def check_list(self):
        ctx = self
        db = self.bot.DiscordDb["servers"]
        self.serverdb = db.find_one({"_id": self.guild.id})
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
        
            schematic = Servers(
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
                uschematic = Users(
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

    def check_blacklist(self):
        if (self.serverdb):
            blcklst = self.serverdb["blacklist"]
            if str(self.author.id) in blcklst:
                raise UserBlacklisted(self.author)
        
        else: return;    
