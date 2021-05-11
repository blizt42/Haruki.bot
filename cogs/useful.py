import discord
import googlesearch
import random
import asyncio
from googlesearch import search
from discord.ext import commands
from random import choice

class Useful(commands.Cog): #All the useful commands
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='clear')
    async def clear(self,ctx, amount=4):
        if amount > 30:
            await ctx.send('Too much to clear, clearing 30 messages instead')
            await asyncio.sleep(3)
            amount = 30
        await ctx.channel.purge(limit=amount + 1)
        print(f'Purged {amount} msg.')

    @commands.command(name='flip')
    async def flip(self,ctx):
        coin = ['Heads', 'Tails']
        await ctx.send(choice(coin))

    @commands.command(name='search')
    async def find(self,ctx, *, look):
        author = ctx.author.mention
        await ctx.channel.send(f"I have found links related, {author} !")
        for find in search(look, tld="co.in", num=5, stop=5, pause=2):
            print(f'Sending URL: {find}')
            await ctx.send(f"\n»» {find}")

def setup(bot):
    bot.add_cog(Useful(bot))
