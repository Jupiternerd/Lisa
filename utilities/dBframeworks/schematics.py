'''
purpose | make adding in documents into Mongodb easier, could have used MongoEngine, or something of that name, instead since they have Schemas but hey I already 
did all this.


'''


from asyncio.windows_events import NULL


def Bot(name, _id, prefix, status, activity):
    '''
    purpose | mongodb framework for bots

    options : {

        "name" : //name of bot

        "_id": //Usually 1 since we are only going to have one document for now (There is only one bot.)

        "prefix": //get it from client. (default "-")

        "status": //Thing you want the bot to be on (ready, idle, dnd) (default "idle")

        "activity": //Thing you want the bot to be saying (default "nothing")

    }

    '''
    bot = {
        "name": name,
        "_id": _id,
        "prefix": prefix or "-",
        "status": status or "idle",
        "activity": activity or "nothing"
    }
    return bot
def Server(name, _id, prefix, owner, blacklist):
    '''
    options : {

        name : server name

        _id: id (Str)

        owner: id (Str)

        prefix : prefix

        cogs : ["core", "fun", "misc", "moderation"]



    }
    '''

    server = {
        "name": name,
        "_id": _id,
        "prefix": prefix or "-",
        "owner":  owner or NULL,
        "cogs": ["core", "fun", "misc", "moderation"],
        "blacklist": set()

    }
    return server

def Starter():
    """
    Starter for stats of collection.
    """
    starter = {
                "xp": 0,
                "lvl": 1,
                "nick": None,
                "mental": {
                    "love": 0,
                    "hate": 0,
                    "friend": 0
                }
    }

    return starter
def Characters(name, _id, set, price, description, color, blood, sex, phrase):
    character = {
        "_id": _id,
        "name": name,
        "set": set,
        "price": price,
        "description": description,
        "color": color,
        "blood": blood,
        "sex": sex,
        "links": {
            "default": None,
            "splash": None,
            "happy": None,
            "sad": None,
            "annoyed": None,
            "blushed": None,
            "surprised": None
        },
        "likes": ["Rod"],
        "dislikes": ["fish"],
        "phrase": phrase





    }

    return character

def User(name, _id, prefix, owner, lock=False):
    '''
    options : {

        name : server name

        _id: id (Str)

        owner: id (Str)

        prefix : prefix

        lock : false



    }
    '''

    user = {
        "_id": _id,
        "name": name,
        "prefix": None,
        "owner":  owner or None,
        "currency": [0, 0],
        "collection": {
            "0": Starter()
                
            },
        "lock": lock
        }
        
        
    
    return user



    
