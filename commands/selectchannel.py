import discord
from discord.ext import commands
import asyncpg

class selectchannel(commands.Cog):

    #running the command
    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def setchannel_modlogs(self, ctx, channel: discord.TextChannel):

        #Connecting to the database uwu
        conn = await asyncpg.connect(user='space', password='hellowo', database='space', host='127.0.0.1')
        await conn.fetch('''INSERT INTO modlogs (guild_id, modlog_channel) VALUES ($1, $2)on conflict(guild_id)do update set modlog_channel = $2''', channel.guild.id,
                         channel.id)
        await conn.close()

        await ctx.send(f" I have landed on the channel {channel.mention} for sending modlogs")

def setup(bot):
    bot.add_cog(selectchannel())