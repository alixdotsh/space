import discord
from discord.ext import commands
from datetime import datetime as dt
import humanize
import asyncpg

class accountinformation(commands.Cog):

    #running the command
    @commands.command()
    async def accountinfo(self, ctx, user: discord.Member):
        if user.nick is not None:
            name=f"{user.name}{user.nick}"
        else:
            name=f"{user.name}"

        # Make and send an embed to the channel
        embed=discord.Embed(
            colour=0x8A2BE2,
            title=f"Account Information For {name}"
        )
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Account Created", value=user.created_at)
        embed.add_field(name="Account Age", value=humanize.precisedelta(dt.now()-user.created_at))
        embed.add_field(name="Joined Server", value=user.joined_at)
        embed.add_field(name="Join Server Age", value=humanize.precisedelta(dt.now()-user.joined_at))


def setup(bot):
    bot.add_cog(modlogs())