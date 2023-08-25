import discord
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"🆕 New channel created: {channel.mention} (Type: {channel.type})")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"🗑️ Channel deleted: {channel.name} (Type: {channel.type})")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        audit_channel = self.client.get_channel(1142960264849916054)
        if before.name != after.name:
            await audit_channel.send(f"📝 Channel name changed: {before.name} -> {after.name} (Type: {after.type})")
        if before.topic != after.topic:
            await audit_channel.send(f"📝 Channel topic updated in {after.name}: {before.topic} -> {after.topic}")

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"👑 New role created: {role.mention}")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"👑 Role deleted: {role.name}")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        audit_channel = self.client.get_channel(1142960264849916054)
        if before.name != after.name:
            await audit_channel.send(f"📝 Role name changed: {before.name} -> {after.name}")
        if before.permissions != after.permissions:
            await audit_channel.send(f"📝 Role permissions updated in {after.name}:\nBefore: {before.permissions}\nAfter: {after.permissions}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"👋 Member joined: {member.mention}")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        audit_channel = self.client.get_channel(1142960264849916054)
        await audit_channel.send(f"👋 Member left: {member.mention}")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.roles != after.roles:
            added_roles = [role for role in after.roles if role not in before.roles]
            removed_roles = [role for role in before.roles if role not in after.roles]
            audit_channel = self.client.get_channel(1142960264849916054)
            if added_roles:
                await audit_channel.send(f"👤 Roles added to {after.mention}: {', '.join(role.mention for role in added_roles)}")
            if removed_roles:
                await audit_channel.send(f"👤 Roles removed from {after.mention}: {', '.join(role.mention for role in removed_roles)}")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content != after.content and not after.author.bot:
            audit_channel = self.client.get_channel(1142960264849916054)
            await audit_channel.send(f"✏️ Message edited by {after.author.mention} in {before.channel.mention}:\nBefore: {before.content}\nAfter: {after.content}")

async def setup(client):
    await client.add_cog(Logs(client))
