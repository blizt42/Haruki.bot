import discord
import random
import praw
from discord.ext import commands
from random import choice

class Fun(commands.Cog): #All the fun commands
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Good day {member.mention}! Paw\'s cousin wishes that you are dead! ~help for commands')

    @commands.command(name='about')
    async def info(self, ctx):
        file = discord.File("misc/Haruki.jpg", filename="Haruki.jpg")
        em = discord.Embed(title='About', description='Hi, my name is Haruki and I am [REDACTED] years old')
        em.add_field(name='Info',
                     value="Paw's cousin that will be forever online. Totally not named after a certain person 0wO")
        em.set_image(url='attachment://Haruki.jpg')
        await ctx.send(embed=em, file = file)

    @commands.command(name='hi')
    async def hi(self,ctx):
        await ctx.send(f'Hello, {ctx.message.author.mention}')

    @commands.command(name='ping')
    async def ping(self,ctx):
        await ctx.send(f'Pingu! Latency: {round(self.bot.latency * 1000)}ms')

    @commands.command(name='praise', aliases=['gd'])
    async def gd(self,ctx):
        reply = ['Thank you!', 'SANKYOU (ᗒᗜᗕ)՛̵̖', "Arigatoo", 'I love you oni-chan ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)',
                 'Thanks! Now donate me your life saving Haha', 'No. staph it (〃 ω 〃)',
                 'YAY, HUGS AND KISSES', 'Love you too (っ´▽｀)っ', 'Thank you my simp ಠoಠ', 'Lol simp', 'kcan ヽ(ﾟДﾟ)ﾉ']
        await ctx.send(choice(reply))

    @commands.command(name='reddit', aliases=['r'])
    async def reddit(self, ctx, subr):
        text = ['Here you go :))', 'Here is one!', 'Hai!', ':)']
        reddit = praw.Reddit(client_id='6x0ub8KbzhNYjA',
                             client_secret='faAZzPicEppifLF61rVhDA0akaXiBw',
                             user_agent='Haruki')
        print(f'~r Reddit connection: {reddit.read_only}')
        await ctx.trigger_typing()
        try:
            redditpost = reddit.subreddit(f'{subr}').new()
            post_to_pick = random.randint(1,10)
            for i in range(0, post_to_pick):
                submission = next(x for x in redditpost if not x.stickied)
            await ctx.send(f'{choice(text)}\n{submission.url}')
        except Exception as e:
            print(f'~reddit Error; {e}')

    @commands.command(name='rp')
    async def randompicture(self,ctx):
        num = random.randint(0, 9)
        text = ['Here you go :))', 'Here is one!', 'Hai!', ':)']
        await ctx.send(text[random.randint(0, 3)])
        await ctx.send(file=discord.File(f'pictures/{num}.jpeg'))

    @commands.command(name='yeetball', aliases=['yb'])
    async def yeetball(self,ctx):
        file = open('misc/yeetball.txt', 'r')
        response = []
        for line in file:
            response.append(line[:-1])
        await ctx.send(choice(response))
        file.close()

def setup(bot):
    bot.add_cog(Fun(bot))