import discord
from discord.ext import commands
class commandinfo(commands.Cog):

    #running the command
    @commands.command()
    async def commandinfo(self, ctx, user: discord.Member):

         # Make and send an embed to the channel listing all the possible commands to run
        embed=discord.Embed(
            colour=0x8A2BE2,
            title=f"Executable Commands",
            description=f"-ban: bans the user\n -kick: kicks the user\n -mute: mutes a user for x amount of time\n -selectchannel_modlogs <channel>: chooses where modlogs go\n -accountinfo: basic account stuff"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(commandinfo())