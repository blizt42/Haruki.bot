import discord
from discord.ext import commands
import asyncio
import time

class Communicate(commands.Cog): #ALl commands for communicate
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='at')
    async def at(self,ctx, member: discord.Member, times=5, *, message):
        print(member)
        if str(member) == 'bamb00#4632':
            await ctx.send('Sowwy, please ping him yourself ♦')
            return
        if times > 5:
            await ctx.send('Too many pings, maximum 5, now pinging 5 times')
            times = 5
        for i in range(times):
            time.sleep(1)
            await ctx.send(f'{message} ,{member.mention}')

    @commands.command(name='dma')
    async def dma(self,ctx, member: discord.Member, times=3, *, text):
        if str(member) == 'bamb00#4632':
            await ctx.send('lol just dm XD Scrub')
            return
        if times > 3:
            times = 3
            await ctx.send('Too many messages, maximum 3, now sending 3 times')
        channel = await member.create_dm()
        for i in range(times):
            await asyncio.sleep(1)
            await channel.send(text)
        await ctx.channel.purge(limit=2)

    @commands.command(name='dm')
    async def dm(self,ctx, member: discord.Member, times=10, *, text):
        if str(member) == 'bamb00#4632':
            await ctx.send(f'Please message him yourself (•ˋ _ ˊ•) {ctx.message.author.mention}.')
            return
        if times > 3:
            await ctx.send('Too many messages, maximum 3, now sending 3 times')
            times = 3
        channel = await member.create_dm()
        await channel.send(f'{ctx.message.author} says....')
        for i in range(times):
            time.sleep(1)
            await channel.send(text)

def setup(bot):
    bot.add_cog(Communicate(bot))