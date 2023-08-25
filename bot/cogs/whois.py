import discord
from discord.ext import commands

class Whois(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(colour=0x0091ff, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    
        embed.add_field(name="Roles:", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Whois(client))