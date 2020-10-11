import discord
from discord.ext import commands
class commandinfo(commands.Cog):

    #running the command
    @commands.command()
    async def commandinfo(self, ctx, user):

         # Make and send a message to the channel listing all the possible commands to run
            await ctx.send(f"`-ban`: bans a user\n `-kick`: kicks a user\n `-mute`: mutes a user for x amount of time\n `setchannel_modlogs <channel>`: sets a channel for modlogs to send\n `-accountinfo`: basic account information")

def setup(bot):
    bot.add_cog(commandinfo())
