import discord

from utilities.dBframeworks.schematics import Servers, Users
from discord.ext import commands
from utilities.constant_code import NotInDb, UserBlacklisted

class CustomContext(commands.Context):
    #holy shaait redo pelase
    def check_list(self):
        userDb = self.bot.DiscordDb["users"]# Get user DB
        serverDb = self.bot.DiscordDb["servers"] # Get Server Db

        guild_server = serverDb.find_one({"_id": self.guild.id})

        def schematic(Stype, name, id, owner):
            return Stype(name= name, _id= id, owner= owner)

        def blacklist():
            if (guild_server):
                blcklst = guild_server.get("blacklist")
                if str(self.author.id) in blcklst:
                    raise UserBlacklisted(self.author)
                else: return

        if not guild_server:
            serverDb.insert(schematic(Servers, self.guild.name, self.guild.id, self.guild.owner_id))
            print("Logged new Server")

            raise NotInDb(self.author)

        elif not userDb.find_one({"_id": self.author.id}):
            userDb.insert(schematic(Users, self.author.name, self.author.id, False))
            print("Logged new User")

            raise NotInDb(self.author)
        
        blacklist()

        return True
        

        

        




    async def format_user_name(self):
        user = self.universe.get("customization")
        prefix = user.get("c_prefix")
        suffix = user.get("c_suffix") 

 
        replacement = (f"{prefix} " if prefix is not None else "") + (self.author.name.capitalize()) + (f"-{suffix}" if suffix is not None else "");
  
        
        return replacement.capitalize()
            

