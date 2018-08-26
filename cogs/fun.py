import discord
from discord.ext import commands
import os
import random

class Fun:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if self.bot.user in message.mentions:
            this_dir = os.path.dirname(__file__)
            images_filepath = os.path.realpath("{0}/images".format(this_dir))
            random_image_name = getRandomFile(images_filepath)
            random_image_string = random_image_name.replace('.jpg', '')
            await message.channel.send(content = random_image_string, file=discord.File(f'{images_filepath}/{random_image_name}'))

def getRandomFile(path):
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]

def setup(bot):
    bot.add_cog(Fun(bot))