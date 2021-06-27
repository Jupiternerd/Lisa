from discord.ext import commands
import re, discord;
from discord.ext.commands.errors import BadArgument
class UserBlacklisted(commands.CommandError):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        
class NotInDb(commands.CommandError):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

class addOrSubtract_converter(commands.Converter):
    async def convert(self, ctx, arguments):
        if arguments in {"+", "add"}:
            return "add"
        if arguments in {"-", "minus", "remove", "subtract"}:
            return "subtract"

        raise BadArgument(ctx.message)

class quoted_converter(commands.Converter):
    async def convert(self, ctx, arguments):
        if arguments.startswith("\"") and arguments.endswith("\""):
            print (arguments)
            return arguments[1:len(arguments)]

        raise BadArgument(ctx.message)

class reasoning_converter(commands.Converter):
    async def convert(self, ctx, arguments):
        reg = re.compile("(for)")
        
        content = ctx.message.content
        before = re.search(reg, str(content))
        if before:
            print(content[content.index(before[1]) + len(before[1]) + 1:len(content)])

            
            
           
            return content[content.index(before[1]) + len(before[1]) + 1:len(content)]




        raise BadArgument(ctx.message)
