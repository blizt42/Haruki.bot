#from discord.voice_client import VoiceClient
import discord
from discord.ext import commands, tasks
from pathlib import Path
import youtube_dl
import asyncio
import random
import time
from googlesearch import search
import praw
import shutil
import os
from random import choice

class client(commands.Bot): #body of the bot
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./cogs/*.py")]
        super().__init__(command_prefix=self.prefix)

    def setup(self):
        print('setting up cogs')
        for cog in self._cogs:
            try:
                self.load_extension(f'cogs.{cog}')
                print(f'Loaded: {cog}.')
            except Exception as e:
                print(f'Error loading {cog} cog. Reason: {e}')
        print('Setup complete.')


    def run(self):
        client.remove_command(self, name='help')

        self.setup()
        super().run('TOKEN') #insert token here

    async def shutdown(self):
        print('Turning off, goodbye.')
        try:
            await super().close()
        except:
            print('Error')

    async def close(self):
        print('Closing on keyboard interrupt...')
        await self.shutdown()

    async def on_ready(self):
        print('Ready!!')
        await self.change_status()

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or('~')(bot, msg)

    async def on_command_error(self,ctx,  error):
        text = ['Im Sowwyyy, unknown command, please try again ♥♥♥', 'Hmm, wrong command?',
                'I dont understand 【⁀⊙﹏☉⁀?】)']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Sowwwy, please enter the required argument (人◕ω◕)')
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(choice(text))

    async def change_status(self):
        status = ['with sadness', 'with life', 'with Paw', 'with Fire', 'with codes']
        while not client.is_closed(self):
            await client.change_presence(self,activity=discord.Game(choice(status)))
            await asyncio.sleep(20)
