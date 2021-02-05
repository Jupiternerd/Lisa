
import io, discord
from PIL import Image, ImageDraw

class Gif:
    '''
    purpose | this cog conatains novel playing parts.

    params
    
    :json : json of the novel you want to play
    
    :bot : client
    
    :channel : channel to send msg in

    :user : user you only want to react to

    '''
    def __init__(self, channel):
        self.channel = channel


        pass

    async def start(self):
       

       images = []
       width = 200
       center = width // 2
       color_1 = (0, 0, 0)
       color_2 = (255, 255, 255)
       max_radius = int(center * 1.5)
       step = 8

       for i in range(0, max_radius, step):
          im = Image.new('RGB', (width, width), color_1)
          draw = ImageDraw.Draw(im)
          draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
          images.append(im)

       for i in range(0, max_radius, step):
          im = Image.new('RGB', (width, width), color_2)
          draw = ImageDraw.Draw(im)
          draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
          images.append(im)

       buf = io.BytesIO()
       #print(images[0])
       images[0].save(buf, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=1, format="GIF")
       
       buf.seek(0)
       #print(byte_im)
       

       

       await self.channel.send(file=discord.File(fp=buf, filename="why.gif"))

        
 