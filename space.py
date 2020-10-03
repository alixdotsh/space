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

client.run('NzE1Mzc3NjA2MDkwMDMxMTM0.Xs8VUA.VAFyZ_X9y7Mr6kYAvdJJK5mhX0c')