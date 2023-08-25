import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command()
    async def help(self, ctx, *, type=None):
        if type==None:
            em = discord.Embed(title="Help Categories", color=0xf0ffff)
            em.set_author(name="Cosmic's Utilities", icon_url="https://cdn.discordapp.com/attachments/1132654226787541072/1142611651783307324/cu_pfp.png")
            em.add_field(name='Fun', value=">help `fun`", inline=True)
            em.add_field(name='Moderator', value=">help `moderation`", inline=True)
            em.add_field(name='Utility', value=">help `utility`", inline=True)
        elif type.lower() == "fun":
            em = discord.Embed(title="Fun Commands", description='Here are some fun commands (might add more soon)!', color=0xf0ffff)
            em.set_author(name="Cosmic's Utilities", icon_url="https://cdn.discordapp.com/attachments/1132654226787541072/1142611651783307324/cu_pfp.png")
            em.add_field(name=">ben `[question]`", value='Ask ben any question you would like!', inline=False)
        elif type.lower() == "moderation" or type.lower() == "moderator":
            em = discord.Embed(title="Moderation Commands", description='Some Commands for moderation!', color=0xf0ffff)
            em.set_author(name="Cosmic's Utilities", icon_url="https://cdn.discordapp.com/attachments/1132654226787541072/1142611651783307324/cu_pfp.png")
            em.add_field(name=">ban `[member]` `[reason]`", value='Bans a member from the server', inline=False)
            em.add_field(name=">unban `[userId]`", value='Unbans a member from the server', inline=False)
            em.add_field(name=">kick `[member]` `[reason]`", value='Kicks a member from the server', inline=False)
            # em.add_field(name=">warn `[member]` `[intensity; low, med, high]` `[reason]`", value='Warns a member', inline=False)
            # em.add_field(name=">warns `[member]`", value='Show a members warns.', inline=False)
            em.add_field(name=">purge `[amount]`", value='Deletes amount of messages in a channel.', inline=False)
            em.add_field(name=">lockdown", value='Locks a channel so members cant talk.', inline=False)
            em.add_field(name=">unlock", value='Unlocks a channel so members can talk.', inline=False)
            em.add_field(name=">slowmode `[seconds]`", value='Sets the slowmode of a channel', inline=False)
            # em.add_field(name=">timeout `[member]` `[time]` `[reason: optional]`", value='Times out a member for certain amount of time.', inline=False)
        elif type.lower() == 'utility':
            em = discord.Embed(title="Utility Commands", description='Some usefull tools!', color=0xf0ffff)
            em.set_author(name="Cosmic's Utilities", icon_url="https://cdn.discordapp.com/attachments/1132654226787541072/1142611651783307324/cu_pfp.png")
            em.add_field(name='>roll `[amount]`', value='Rolls a dice with the given amount of sides', inline=False)
            em.add_field(name='>membercount', value='Says the current number of members', inline=False)
            em.add_field(name='>translate `[language tag] [phrase]`', value='Translate one thing into another.', inline=False)
        await ctx.send(embed=em)



async def setup(client):
    await client.add_cog(Help(client))

