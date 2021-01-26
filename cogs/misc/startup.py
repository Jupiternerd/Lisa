'''
Author | Shokkunn
'''
import discord
import random
from discord.enums import ActivityType
from discord.ext import commands, tasks

class Startup(commands.Cog):
    '''
    purpose | this cog conatains startup tasks.
    '''
    def __init__(self, bot):
        self.bot = bot
        self.get_presString.start()
        #self.presences = 0
        #print(dir(bot))
        #print("=====================================================")


    @commands.Cog.listener()
    async def on_ready(self):
        print("[L!sa] Bot online")
        
        #await self.bot.change_presence(status= discord.Status.do_not_disturb, activity=discord.Game(name="a"))
        

    @tasks.loop(seconds=random.randint(120, 300))
    async def get_presString(self):
        bot = self.bot.DiscordDb["bots"].find_one({"_id": 1})
        activityArr = bot["activity"]
        activity = activityArr[random.randint(0, len(activityArr) - 1)]
        print(activity)
        status = bot["status"] 

        # Special types
        special_types = ["online", "idle", "dnd"]
        
        

        for types in special_types: #loop through these three
            if types in activity.lower(): #see if the activity includes the three, then we set the status to that one.
                print("[Startup.Cog] Found a match for speical types!")
                status = types;

        randString = f"• @{bot['name']} | " + str(activity)
        
        await self.changePresence(statusStr= status, presStr= randString)
        # TODO: 
        '''
        @todo : Make it so that we can identify what the status are and can have custom profiles to change. We have to
        drastically slow down the randInt in the loop but would be a good sacrifice.
        '''
        
    async def changePresence(self, statusStr, presStr):
        '''
        purpose | Change presence of the bot.
        '''
        #print(f'discord.Status.{statusStr}')
        
        await self.bot.change_presence(status= f'discord.Status.{statusStr}', activity=discord.Activity(type=discord.ActivityType.listening, name=presStr))
    
    @get_presString.before_loop
    async def before_ready(self):
        print("[Startup.Cog] Waiting for ready.")
        await self.bot.wait_until_ready()




    
def setup(bot):
    bot.add_cog(Startup(bot))

