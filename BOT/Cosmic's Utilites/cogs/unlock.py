import discord
from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unlock(self, ctx):
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
        await ctx.send( ctx.channel.mention + " **is now out of lockdown.**")
        await audit_channel.send(ctx.channel.mention + "was taken out of lockdown mode by " + {ctx.author.mention})

async def setup(client):
    await client.add_cog(Unlock(client))

