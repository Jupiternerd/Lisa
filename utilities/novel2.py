'''
author : Shokk

'''
import asyncio
from asyncio.tasks import wait_for
import discord
from utilities.constants import consts as constants
emoji_numbers = constants["emoji_numbers"] 

class Pages:
    '''
    purpose | serve as page containers
    '''
    def __init__(self, singles, index):
        self.index = singles["index"] or index
        #self.reactions = singles[""]
        self.type = singles["type"] or 0
        self.destination = singles["destination"] or None
        content = singles["content"]
        self.title = content["msg_title"] or None
        self.content = content["msg_content"] or None
        self.bottom = content["msg_control"] or None
        self.color = content["color"] or None
        self.bg = content["bg"] or None


class Novel:
    '''
    purpose | this cog conatains novel playing parts.

    params
    
    :json : json of the novel you want to play
    
    :bot : client
    
    :channel : channel to send msg in

    :user : user you only want to react to

    '''
    def __init__(self, json, bot, channel, user):
        self.bot = bot
        self.pageCount = 0
        self.index = 0
        self.pages = []
        self.current_emoji = []
        self.channel = channel
        self.user = user


        self.reactDict = {
            0 : {'⏮️' : {
                "name": self.set_page,
                "args": 'backward'
                }, '⏹️': {
                "name": self.stop,
                "args": ""
                }, '⏭️': {
                "name": self.set_page,
                "args": 'forward'
                }
                },
            1 : {'⏭️': {
                "name": self.set_page,
                "args": 'forward'
                }},
            #DONT USE THESE BELOW
            #2 : {'✏️': self.wait_for_message()},
            #3 : {emoji_numbers[1]: self.set_page(self.page.destination[1])},
            #THEY ARE NOT IMPLEMENTED
            "g_end" : {"❤️": {
                "name": self.stop,
                "args": ""
                }},
            "b_end" : {"🔻": {
                "name": self.stop,
                "args": ""
                }}

        }
        
        for singles in json["multiples"]:
            self.pageCount + 1
            newSingles = Pages(singles, self.pageCount)
            newSingles.bg = bot.OrioDb["backgrounds"].find_one({"name": newSingles.bg})
            self.pages.append(newSingles)
        print(self.pages[0].bg["link"])
    
    async def add_reaction(self):
        if not self.page: raise Exception("There is not self.page!")
        
        print(self.emoji_bank)
        if self.emoji_bank is not self.current_emoji:
            print(self.current_emoji)

            
            self.current_emoji = []

            for emoji in self.emoji_bank:
                self.current_emoji.append(emoji)
                await self.window.add_reaction(emoji)
        else: return

    

    def check(self, reaction, user):
        return reaction.emoji in self.reactDict[self.page.type] and user.id == self.user.id


    async def wait_for_reaction(self):
        while True:
            try:
               reaction, user = await self.bot.wait_for('reaction_add', check= self.check, timeout= constants["timeout"])
               cmd = self.reactDict[self.page.type][reaction.emoji]
               print(cmd["args"])
               await cmd["name"](cmd["args"])
            except asyncio.TimeoutError:
               await self.stop()
               break
            else:
               print(reaction.emoji)
               await self.add_reaction()
               await self.window.remove_reaction(reaction, user)
            #print(self.reactDict[self.page.type][reaction.emoji])
            
            #await reaction.remove(user)
    
    async def wait_for_message(self):
        '''
        @TODO : Finish this, figure out how to properly store stuff.
        '''
        pass


    async def set_page(self, index):

        
        if type(index) is str:
            if index is "forward": self.index += 1;
            elif index is "backward": self.index -= 1;
            
        elif type(index) is int: self.index = index

        self.page = self.pages[self.index]
        print(self.index)
        print(len(self.pages))
        color = discord.Color(int(self.page.color, 16))
        embed = discord.Embed(description= f"idk", color= color, footer=f"Page {self.page.index + 1}").set_image(url=self.page.bg["link"])

        await self.window.edit(embed = embed)



    async def stop(self):
        pass


    async def start(self):
        #self.index = 0
        
        self.page = self.pages[self.index]
        self.emoji_bank = self.reactDict[self.page.type].keys()
        print(hex(int(self.page.color, 16)))
        color = discord.Color(int(self.page.color, 16))
        embed = discord.Embed(description= f"idk", color= color, footer=f"Page {self.page.index + 1}").set_image(url=self.page.bg["link"])
        self.window = await self.channel.send(embed=embed)

        await self.add_reaction()
        await self.wait_for_reaction()