import discord
from discord.ext import commands
from discord.ext.commands import guild_only

class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @guild_only()  # Might not need ()
    async def commandunban(self, ctx, id: int):
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
        try:
            user = await self.client.fetch_user(id)
            await ctx.guild.unban(user)
            await audit_channel.send(f"Unbanned <@{user}")
        except Exception as e:
            await ctx.send(f"An unknown error occurred while trying to unban this member:\n{e}")
            return
        
async def setup(client):
    await client.add_cog(Unban(client))