import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason=None):
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)

        await member.kick(reason=reason)
        em = discord.Embed(description=f"Kicked {member.mention}. **Reason:** {reason}")
        await audit_channel.send(embed=em)

async def setup(client):
    await client.add_cog(Kick(client))