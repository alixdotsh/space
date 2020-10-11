import discord
from discord.ext import commands
import asyncpg
class setprefix(commands.Cog):

    #running the command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix:str):

        #connecting to the database
        conn = await asyncpg.connect(user='space', password='hellowo', database='space', host='127.0.0.1')
        await conn.fetch('''INSERT INTO prefix (guild_id, prefix) VALUES ($1, $2)on conflict(guild_id)do update set prefix = $2''', ctx.guild.id,
                         prefix)
        await conn.close()

        await ctx.send(f"I have successfully changed the prefix to `{prefix}`")

def setup(bot):
    bot.add_cog(selectchannel())