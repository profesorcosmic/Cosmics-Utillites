import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def commandban(self, ctx, member: discord.Member, *, reason=None):
        id_to_save = member.id
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
    
        try:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member.name}. Reason: {reason}")
            await audit_channel.send(f"<@{id_to_save}> was banned!\n> Id:`{id_to_save}`\n> Reason:`{reason}`")
            return
        except discord.Forbidden:
            await ctx.send(f"The bot doesn't have permission to ban this member.")
            return
        except Exception as e:
            await ctx.send(f"An unknown error occurred while trying to ban this member:\n{e}")
            return

async def setup(client):
    await client.add_cog(Ban(client))