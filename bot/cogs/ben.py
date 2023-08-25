import random
import discord
from discord.ext import commands



class Ben(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command(alliases=['8ball'])
    async def ben(self, ctx, *, question):
        yes_responses = ["Yes.", 'I think yes.']
        maybe_responses = ['Try again.', 'Not sure.', 'Why u asking me this?']
        no_responses = ["No","Think again.",'Outlook not good.','I think no.']
    
        all_responses = yes_responses + maybe_responses + no_responses
        response = random.choice(all_responses)
    
        if response in no_responses:
            color = 0xF00606
        elif response in yes_responses:
            color = 0x319d17
        else:
            color = 0xfee700

        em = discord.Embed(title='Ask Ben!', color=color)
        em.add_field(name='Response:', value=f'> {response}')
        await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(Ben(client))