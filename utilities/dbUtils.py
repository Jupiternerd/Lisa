import os, pymongo
from dotenv import load_dotenv
load_dotenv()
uri = os.environ.get("URI")


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
            client.MongoClient = pymongo.MongoClient(uri)
            print("[Mango] Connecting to the Big Mango Cloud..")
            # print(client.MongoClient.test)
        except Exception as e:
            print(e)
            Mango.login()
        else:   

            client.DiscordDb = client.MongoClient["discord"]
            client.StatsDb = client.MongoClient["stats"]
        finally:
            print("[Mango] Done")

            
    

    
    
        


         
    
    
       