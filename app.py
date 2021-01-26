# Author : Wai 
# To learn pyMongo
from lisa.client import CustomClient
import logging

Lisa = CustomClient()
Lisa.begin()



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)




