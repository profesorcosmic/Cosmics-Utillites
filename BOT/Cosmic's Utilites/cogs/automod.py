import discord
from discord.ext import commands, tasks
from datetime import timedelta

class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.anti_spam = commands.CooldownMapping.from_cooldown(5, 15, commands.BucketType.member)
        self.too_many_violations = commands.CooldownMapping.from_cooldown(4, 60, commands.BucketType.member)

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.Cog.listener()
    async def on_message(self, msg):
        permission_to_check = discord.Permissions.kick_members

        user = msg.author
        if user.guild_permissions.kick_members:
            return
        
        # Swearing detection
        auditid = 1142960264849916054
        audit_channel = self.client.get_channel(auditid)
        fitered_words = ["pussy","tranny","faggot","fuck", "f u c k", "shit", "s h i t", "f.u.c.k", "s.h.i.t" "f. u. c. k" "f .u .c .k", "s. h. i. t", "s .h .i .t", "nigga" "n.i.g.g.a" "NIGGA", "N I G G A", "N.I.G.G.A", "n i g g a", "bitch", "BITCH", "B.I.T.C.H", "b.i.t.c.h", "b i c h", "B I C H", "cock", "COCK", "C.O.C.K", "C.0.C.K", "c.o.c.k", "c.0.c.k", "c o c k", "c 0 c k", "C O C K", "C 0 C K"]
        if msg.author == self.client.user:
            return
        try:
            for word in fitered_words:
                if word in msg.content.lower():
                    await msg.delete()
                    await msg.send(f"Please do not swear {msg.author.mention}!")
                    await audit_channel.send(f"Automod detected and deleted a forbidden word:\n> User: {msg.author}\n> Word: {word}")
                    return
        except discord.Forbidden:
            return
        
        # Anti Spam
        if type(msg.channel) is not discord.TextChannel or msg.author.bot:
            return
        bucket = self.anti_spam.get_bucket(msg)
        retry_after = bucket.update_rate_limit()
        if retry_after:
            await msg.delete()
            await msg.channel.send(f"Please don't spam {msg.author.mention}!", delete_after=10)


            await audit_channel.send(f"Automod detected and deleted spam:\n> User: {msg.author.mention}")
            violations = self.too_many_violations.get_bucket(msg)
            check = violations.update_rate_limit()
            if check:
                await msg.author.timeout(timedelta(minutes = 10), reason = 'Spam')
                try: await msg.author.send("You have been muted for spamming.")
                except:
                    pass

    

async def setup(client):
    await client.add_cog(Automod(client))