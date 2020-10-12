import discord
from discord.ext import commands


class CommandInfo(commands.Cog):

    # running the command
    @commands.command()
    async def commandinfo(self, ctx):

        # Make and send an embed to the channel listing all the possible commands to run
        embed = discord.Embed(
            colour=0x8A2BE2,
            title="Executable Commands",
        )
        embed.add_field(name="ban", value="bans the user from the server")
        embed.add_field(name="kick", value="kicks the user from the server")
        embed.add_field(name="mute", value="mutes the user for the given amount of time in minutes")
        embed.add_field(name="setchannel_modlogs <channel>", value="selects where modlogs goes")
        embed.add_field(name="accountinfo", value="gives you information of the account chosen")
        embed.add_field(name="setprefix", value="changes the default prefix")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandInfo())
