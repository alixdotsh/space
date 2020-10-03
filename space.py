import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

import json
with open("config.json") as a:
  config = json.load(a)
# config is now a dictionary object
# and as such:
token = config['token']

client.run(token)
