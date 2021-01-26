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
def Server(name, _id, prefix, owner):
    '''
    options : {

        name : server name

        _id: id (Str)

        owner: id (Str)

        prefix : prefix


    }
    '''

    server = {
        "name": name,
        "_id": _id,
        "prefix": prefix or "-",
        "owner":  owner or NULL,
        
    }
    return server
