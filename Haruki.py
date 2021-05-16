import discord
from discord.ext import commands
from pathlib import Path
import asyncio
from random import choice

class client(commands.Bot): #body of the bot
    def __init__(self, token):
        self.token = token
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
        super().run(self.token)

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
                'I do not understand 【⁀⊙﹏☉⁀?】)']
        cooldown = ['Chill out dude...  ', 'Can you wait??!!  ','SERIOUSLY, SLOW DOWN   ','Yamete Kudasai Oni Chan...']
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Sowwwy, please enter the required argument (人◕ω◕), use ~help if you do not understand.')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(choice(text))
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{choice(cooldown)} This command is on cooldown, you can use it in {round(error.retry_after, 2)} seconds.')
        else:
            print('Unknown error occured, please check logs.')
            await ctx.send('An unknown error occured')

    async def change_status(self):
        status = ['with sadness', 'with life', 'with Paw', 'with Fire', 'with codes']
        while not client.is_closed(self):
            await client.change_presence(self,activity=discord.Game(choice(status)))
            await asyncio.sleep(20)
