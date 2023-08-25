import discord
from discord.ext import commands

class MemberCount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command()
    async def membercount(self, ctx):
        # Getting the total amount of members, robots, and combined.
        total_members = ctx.guild.member_count
        total_humans = len([member for member in ctx.guild.members if not member.bot])
        total_bots = total_members - total_humans
    
        em = discord.Embed(title="Server Member Count", color=0xf0ffff)
        em.add_field(name="Total Members", value=f"{total_members} members", inline=False)
        em.add_field(name="Humans", value=f"{total_humans}", inline=False)
        em.add_field(name="Bots", value=f"{total_bots}", inline=False)
        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(MemberCount(client))