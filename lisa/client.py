
import os
from logging import warning
from os import listdir
from os.path import isdir, isfile, join
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utilities.dBframeworks.schematics import Bot
from utilities.dbUtils import Mango

load_dotenv()

def _prefix(bot, ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel): 
        print("aa")
        return "-"
    guild = ctx.guild
    #print(dir(bot))
    prefix = bot.DiscordDb["bots"].find_one({"_id": 1})
    guildPrefix = bot.DiscordDb["servers"].find_one({"_id": guild.id})
    if guildPrefix is not None:
        prefix = guildPrefix

    return prefix["prefix"];
    


class CustomClient(commands.Bot):
    '''
    purpose | To package useful stuff that I might need later into a class to make a discord bot

    {Dict} options : {
        name: //name
        token: //token (optional)

    }
    '''


    def __init__(self):
        
        self.token = os.environ.get("TOKEN")
        intent = discord.Intents.default()
        intent.members = True
        super().__init__(command_prefix= _prefix, intents = intent)


    def begin(self):
        '''
        purpose | login to the bot

        {String} token : used to login into the bot. Optional
        '''
        self.remove_command('help')
        Mango.login(self)
        
        
        mangoBots = self.DiscordDb["bots"]
        mangoBot = mangoBots.find_one({"_id": 1})  # find bot

        #name, doc_id, prefix, presence
        Lisa = Bot(
            name="Lisa",
            _id=1,
            prefix="!",
            status="eating",
            activity= ["AAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"]
        ) #If there is no bot then we make bot and add it into our db

        if not mangoBot:

            mangoBots.insert_one(Lisa)
            mangoBot = Lisa
            warning("No bot!")
            
        self.load_cogs("./cogs")
        self.run()
        
    def run(self):
        super().run(self.token)
    
    def load_cogs(self, path = './cogs'):
        '''
        purpose | read path to cogs and add them in

        {String} path : path to search for cogs in. [ default './cogs']
        '''
        for filename in listdir(path):
            file = join(path, filename)
            
            if not filename.startswith("__"):
                if isfile(file): #If the file is actually a file and not a directory
                    if filename.endswith('.py'):
                        cogPath = path[2:].replace("\\", ".")
                        self.load_extension(f'{cogPath}.{filename[:-3]}')
                        print(f"[load_cogs] Loaded Cog [ {filename} ]")
                        
                if isdir(file):
                    #If the path is a directory then rerun this function but with this file directory to search in.
                    self.load_cogs(file)
                    
