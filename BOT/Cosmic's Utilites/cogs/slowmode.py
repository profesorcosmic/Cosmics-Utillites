import discord
from discord.ext import commands

# Setup the class
class Slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    # The slowmode command
    @commands.command(aliases=['sm', 'ratelimit'])
    async def slowmode(self, ctx, time=0):
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
        if time > 21600:
            await ctx.send("You are limited to 21600 seconds.")

        await ctx.channel.edit(slowmode_delay=time)
        await ctx.send(f"Slowmode set to `{time}` seconds.")
        await audit_channel.send(f"Slowmode in {ctx.channel.mention} set to {time} seconds by {ctx.author}.")

async def setup(client):
    await client.add_cog(Slowmode(client))