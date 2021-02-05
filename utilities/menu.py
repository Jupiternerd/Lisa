'''
author : Shokk

'''
import discord
from discord.ext.commands import bot
from utilities.constants import constants
from discord.ext import commands, tasks

class Pages:
    '''
    purpose | serve as page containers
    '''
    def __init__(self, singles, index):
        self.index = singles["index"] or index
        self.type = singles["type"] or 0
        content = singles["content"]
        self.title = content["msg_title"] or None
        self.content = content["msg_content"] or None
        self.color = content["color"] or None
        self.bg = content["bg"] or None

class Novel:
    '''
    purpose | this cog conatains novel playing parts.

    pages : [one: {}]
    '''
    def __init__(self, json, bot, ctx):
        self.pageCount = 0
        self.index = 0
        self.pages = []
        for singles in json["multiples"]:
            #print (singles)
            self.pageCount + 1
            newSingles = Pages(singles, self.pageCount)
            newSingles.bg = bot.OrioDb["backgrounds"].find_one({"name": newSingles.bg}) or None
            self.pages.append(newSingles)
        print(self.pages[1].bg)

    def display(self, a):
        pass

    async def start():
        pass