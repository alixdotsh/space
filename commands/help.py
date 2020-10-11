import discord
from discord.ext import commands
class chelp(Commands.cog):

    #running the command
    @commands.command()
    async def chelp(self, ctx, user: discord.Member):

         # Make and send an embed to the channel listing all the possible commands to run
        embed=discord.Embed(
            colour=0x8A2BE2,
            title=f"Executable Commands"
        )
        embed.add_field(name="Ban", value="-ban: bans a user")
        embed.add_field(name="Kick", value="-kick: kicks a user")
        embed.add_field(name="Mute", value="-mute: mutes a user for _ amount of time given")
        embed.add_field(name="Setchannel_modlogs", value="-setchannel_modlogs <channel>: Chooses and saves where modlogs will go")
        embed.add_field(name="AccountInformation", value="-accountinfo: basic account information")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(chelp())