import discord
from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command()
    async def roll(self, ctx, *, sides=20):
        em = discord.Embed(title="Rolled:", description=f'{random.randint(1, sides)}', color=ctx.author.color)
        await ctx.send(embed=em)

async def setup(client):
    await client.add_cog(Roll(client))

    