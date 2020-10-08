import discord
from discord.ext import commands
import asyncpg
class modlogs(commands.Cog):

    @commands.Cog.listener()
    async def on_modlog(self, user, moderator, command, reason):
        conn = await asyncpg.connect(user='Space', password='hellowo',
                                     database='Space', host='127.0.0.1')
        values = await conn.fetch('''SELECT * FROM modlogs WHERE guild_id = $1''', moderator.guild.id)
        await conn.close()
        if len (values) == 0:
            return
        modlogs = moderator.guild.get_channel (values[0]["modlogs_channel"])
        if modlogs is None:
            modlogs = await moderator.guild.create_text_channel(name="mod-logs")
            await modlogs.set_permissions(modlogs.guild.default_role, send_messages=False)
            await modlogs.set_permissions(modlogs.guild.me, send_messages=True)
            conn = await asyncpg.connect(user='Space', password='hellowo',
                                         database='Space', host='127.0.0.1')
            values = await conn.fetch('''INSERT INTO modlogs (guild_id, modlogs_channel) VALUES ($1, $2)''', moderator.guild.id, modlogs.id)
            await conn.close()
        embed=discord.Embed(
            colour=0x8A2BE2,
            title=f"New Audit Log",
            description=f"{moderator.mention} to {user.mention}\n Command: {command}\n Reason: {reason}"
        )
        embed.set_author(name=moderator.name, icon_url=moderator.avatar_url)
        await modlogs.send(embed=embed)


def setup(bot):
    bot.add_cog(modlogs())