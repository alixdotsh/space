import discord
from discord.ext import commands
class modlogs(commands.Cog):

    @commands.Cog.listener()
    async def on_modlog(self, user, moderator, command, reason):
        modlogs = discord.utils.get(moderator.guild.channels, name="mod-logs")
        if modlogs is None:
            modlogs = await moderator.guild.create_text_channel(name="mod-logs")
            await modlogs.set_permissions(modlogs.guild.default_role, send_messages=False)
            await modlogs.set_permissions(modlogs.guild.me, send_messages=True)
        embed=discord.Embed(
            colour=0x8A2BE2,
            title=f"New Log",
            description=f"{moderator.mention} to {user.mention}\n Command: {command}\n Reason: {reason}"

        )
        await modlogs.send(embed=embed)

def setup(bot):
    bot.add_cog(modlogs())