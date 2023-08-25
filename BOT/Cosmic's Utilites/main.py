import discord
from discord.ext import commands
import os
import asyncio


TOKEN=''


intents = discord.Intents.all()
client = commands.Bot(command_prefix='>', intents=intents)
client.remove_command("help")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='paint dry👀'))
    print(f"Your bot is logged in as {client.user.name}#{client.user.discriminator}")
    print("_________________________")

# Load cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print("File loaded: ", filename)
    print("_________________________")

# Main function
async def main():
    async with client:
        try:
            await load()
            await client.start(TOKEN)
        except Exception as e:
            print("Error: ", e)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())