'''
Author | Shokkunn
'''
import asyncio
import discord, typing
from discord import user
from datetime import date
from discord.ext.commands import bot, cog, has_guild_permissions, MissingPermissions
from discord.ext import commands, tasks
from discord.ext.commands.errors import BadArgument, MemberNotFound
from utilities.constant_code import addOrSubtract_converter, quoted_converter, reasoning_converter

class Moderation(commands.Cog):
    '''
    purpose | this cog conatains before invocation tasks.

    @todo | implement the permission check only for this cog
    '''
    def __init__(self, bot):
        self.bot = bot
        self.Db = self.bot.DiscordDb
    
    

    """
    name | kick, 
    purpose | kick players out of servers.
    permissions | kick_members.
    args | (g) member, (o) reason;
    """


    #async def cog_command_error(self, ctx, error):
    #    print(isinstance(error, MissingPermissions))
     #   pass
    @commands.bot_has_permissions(kick_members=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command(name= "kick", help= "-kick people lol")
    @has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.Greedy[discord.Member], reason: reasoning_converter = "None_Given"):
        
        if (not member):
            raise BadArgument
        #print(member)

        pastUserID = [];

        guild = ctx.guild
        sendStr = ""
        for users in member:

    
            if users.id not in pastUserID:
                try:
                    await guild.kick(users, reason=reason)
            
                finally:
                    sendStr += " " + str(users) + ", " 
                    pastUserID.append(users.id)

            

        toSend = f"Kicked {sendStr} for • *{reason}*\n" if len(pastUserID) < 5 else f"Kicked **{len(member)}** users for • *{reason}*."
        return await ctx.reply(toSend)

    """
    name | ban, 
    purpose | ban players out of servers.
    permissions | ban_members.
    args | (g) member, (o) reason;
    """
    @commands.command(name= "ban")
    @has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.Greedy[discord.Member], reason: reasoning_converter = "None_Given"):
        
        if (not member):
            raise BadArgument
        #print(member)

        pastUserID = [];

        guild = ctx.guild
        sendStr = ""
        for users in member:
            print(users)

    
            if users.id not in pastUserID:

                try:
                    await guild.ban(users, reason=reason)
            
                finally:
                    sendStr += " " + str(users) + ", " 
                    pastUserID.append(users.id)


        
        toSend = f"Banned {sendStr} for • *{reason}*\n" if len(pastUserID) < 5 else f"Banned **{len(member)}** users for • *{reason}*."
        return await ctx.reply(toSend)

    """
    name | blacklist, 
    purpose | blacklist players to keep them from not using the bot.
    permissions | blacklist_members.
    args | addOrSubtract [-, +], member, reason.
    """
    @has_guild_permissions(kick_members=True)
    @commands.command(name= "blacklist")
    async def blacklist(self, ctx, addOrRemove: addOrSubtract_converter, member: commands.Greedy[discord.Member], reason: reasoning_converter = "None_Given"):
        
        if (not member):
            raise BadArgument

        guild = ctx.guild
        pastUserID = None
        filter = {"_id": guild.id}

        db = self.bot.DiscordDb["servers"]
        
        blacklist = db.find_one(filter)["blacklist"]



        for users in member:
           # print (users.id != pastUserID)

            if users.id != pastUserID:
                print(str(users.id) not in blacklist)
                
                if addOrRemove is "add":

                    try:
                        if (users.id == ctx.author.id): raise Exception("notAllowed");
                        blacklist[str(users.id)] = { "on": str(date.today()) }
                        
                    except(Exception):
                        print(Exception)
                        #TODO: remove this and add it to the error function
                        return await ctx.reply(f"Could not add **{users.display_name}** to the list! Maybe they are already in it?")

                elif addOrRemove is "subtract":
                    #print("dideAAAAAAAAAAA")
                    try:
                        
                        del blacklist[str(users.id)]
                        print(blacklist)
                    except(Exception):
                        print(Exception)
                        return await ctx.reply(f"Could not remove **{users.display_name}** from the list! Maybe they are already out of there?")
                        
                    

                
            pastUserID = users.id;
        
       

        newvalues = { "$set": { 'blacklist': blacklist } } 

        db.update_one(filter, newvalues)

        await ctx.reply("Done!")



        


def setup(bot):
    bot.add_cog(Moderation(bot))