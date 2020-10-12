import discord
from discord.ext import commands
import glob
import os
import asyncpg

async def ger_prefix(bot, message):
    conn = await asyncpg.connect(user='space', password='hellowo', database='space', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM prefix WHERE guild_id = $1''', message.guild.id)
    await conn.close()
    if len(value) == 0:
        return '-'
    return values[0]['prefix']


client = commands.Bot(command_prefix=get_prefix)

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
