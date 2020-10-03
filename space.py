import discord
from discord.ext import commands
import glob
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)
import json
with open("config.json") as a:
  config = json.load(a)
# config is now a dictionary object
# and as such:
token = config['token']
for file in glob.glob("commands/*.py"):
    client.load_extension(file.replace(os.sep, ".")[:-3])
client.load_extension("jishaku")
client.run(token)
