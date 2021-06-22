import os, pymongo
from dotenv import load_dotenv
load_dotenv()
uri = os.environ.get("URI")
ouri = os.environ.get("OURI")

class Mango:
    
    '''
    purpose | Mongodb management class, uses pymongo

    '''

    @staticmethod
    def login(client): 
        '''
        purpose | Logins into the mongoDb using pymongo. The URI is in a env variable. Password authenticated uri
        ''' 
        try:
            client.selfMongoClient = pymongo.MongoClient(uri)
            #client.orioMongoClient = pymongo.MongoClient(ouri)
            print("[Mango] Connecting to the Big Mango Cloud..")
            # print(client.MongoClient.test)
        except Exception as e:
            print(e)
            Mango.login()
        else:   

            client.UniverseDb = client.selfMongoClient["universe"]
            #client.OrioStatsDb = client.orioMongoClient["stats"]
            client.DiscordDb = client.selfMongoClient["discord"]
            
            client.StatsDb = client.selfMongoClient["stats"]
        finally:
            print("[Mango] Done")
    

            
    

    
    
        


         
    
    
       