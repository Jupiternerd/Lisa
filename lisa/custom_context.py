import discord

from utilities.dBframeworks.schematics import Servers, Users
from discord.ext import commands
from utilities.constant_code import NotInDb, UserBlacklisted

class CustomContext(commands.Context):

    def add_on_cmd(self):
        print (self.universe)
        userDb = self.bot.DiscordDb["users"]# Get user DB
        serverDb = self.bot.DiscordDb["servers"] # Get Server Db


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

        if not guild_server: # If the guild server is not found in the DB.
            serverDb.insert(schematic(Servers, self.guild.name, self.guild.id, self.guild.owner_id))
            print("Logged new Server")

            raise NotInDb(self.author)

        elif not userDb.find_one({"_id": self.author.id}): #If a user is not found in the DB.
            if self.author.bot: return
            userDb.insert(schematic(Users, self.author.name, self.author.id, False))
            print("Logged new User")
            users = guild_server.get("users")

            if self.author.id in users: # Check if the user is in the guild in the Mongodb
                
                users.append(self.author.id)

                update = { "$set": { 'users': users } } 
                serverDb.update_one({"_id": self.guild.id}, update)
                print("Logged new User Into ServerDB")

            raise NotInDb(self.author)
        
        blacklist()
        #print(guild_server)
        
        #print(users)

        return True



    async def format_user_name(self): #Some cringe stuff, I am dissapointed but its for the greater good.
        user = self.universe.get("customization")
        prefix = user.get("c_prefix")
        suffix = user.get("c_suffix") 

 
        replacement = (f"{prefix} " if prefix is not None else "") + (self.author.name.capitalize()) + (f"-{suffix}" if suffix is not None else "");
  
        
        return replacement.capitalize()
            

