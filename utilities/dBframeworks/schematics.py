'''
purpose | make adding in documents into Mongodb easier, could have used MongoEngine, or something of that name, instead since they have Schemas but hey I already 
did all this.


'''


from asyncio.windows_events import NULL


def Bots(name, _id, prefix, status, activity):
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
def Servers(name, _id, owner):
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
        "prefix": None,
        "owner":  owner or NULL,
        "cogs": ["core", "fun", "misc", "moderation"],
        "blacklist": {}

    }
    return server

def Starter():
    """
    Starter for stats of collection.
    """
    starter = {
                "_id": 0,
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
def Menus(name, _id, multiples):
    '''
    name : menu name
    
    _id : id of the menu

    multiples : [
 {
             "index": int,
             "embed": {
                 "title": str,
                 "body": str,
                 "color": color,
                 "footer": str
                 
             },
             "reactions": {
                 str: str
             },
             "wait": int
        },
    ]
    '''
    menu = {
        "name": name or None,
        "_id": _id or None,
        "multiples": multiples

        
    }

    return menu



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


def Universe(name="City", _id=0):
    universe = {
        str(_id) : {
             "name": name,
             "level": 1,
             "completion": 0
        }

    }
    return universe;

def Users(name, _id, owner):
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
        "universe": {
            "customization": {
                "c_prefix": None,
                "c_suffix": "san",
                "main_world": 0,
                "main_char": 0
            },
            "currency": [0, 0],
            "worlds": Universe(),

            "char_collection": {
               "0": Starter()
                
            },

        },
        "lock": False

        }
        
        
    
    return user



    
