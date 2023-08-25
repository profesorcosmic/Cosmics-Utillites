import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! `{self.client.latency * 1000:.2f}` ms.')

async def setup(client):
    await client.add_cog(Ping(client))