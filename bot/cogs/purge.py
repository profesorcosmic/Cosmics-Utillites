import discord
from discord.ext import commands
import asyncio

class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command(alliases=['clear', 'del'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
        if amount <= 0:
            await ctx.send("Please provide a positive non-zero, non-decimal number to purge.")
            return
        if amount > 99:
            await ctx.send("You can only delte 99 messages at a time. If you need to delete more messages, run the command multiple times.")
            return

        # Fetch the messages to delete
        messages = [msg async for msg in ctx.channel.history(limit=amount + 1)]

        # Delete the messages**
        await ctx.channel.delete_messages(messages)

        # Send the "Purged by" message and delete it after 5 seconds => ("Purged by <User Who Purged>")
        purged_by_message = await ctx.send(f"Purged by {ctx.author.mention}")
        await audit_channel.send(f"{amount} messaged deleted in {ctx.channel.mention} by {ctx.author.mention}.")

        await asyncio.sleep(5)
        await purged_by_message.delete()


async def setup(client):
    await client.add_cog(Purge(client))