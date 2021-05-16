import os
import asyncio
from discord.ext import commands

class Admin(commands.Cog): #NOT TO BE DISPLAYED IN ~help!!!! All the admin commands
    def __init__(self, bot):
        self.bot = bot
        self.password = 'Deppresso' #yes its just one of my alt username

    @commands.command(name='deletesongs')
    @commands.is_owner()
    async def deletesongs(self, ctx, password):
        if password == self.password:
            music = 'music'
            for song in os.listdir(music):
                song_path = os.path.join(music, song)
                try:
                    if os.path.isfile(song_path) or os.path.islink(song_path):
                        os.unlink(song_path)
                        print(f'{song} deleted when cleaning up player.\n')
                except Exception as e:
                    await ctx.send('Failed to delete {}. Reason: {}'.format(song_path, e))
                    print('Failed to delete {}. Reason: {}'.format(song_path, e))
            await ctx.send('songs deleted')
        else:
            await ctx.send('Error')

    @commands.command(name='reboot')
    @commands.is_owner()
    async def reboot(self, ctx, password):
        if password == self.password:
            for i in range(5):
                await asyncio.sleep(1)
                print(f'Rebooting in {5 - i}')
                await ctx.send(f'Rebooting in {5 - i}')
            await ctx.send('Rebooting now!')
            os.system('sudo shutdown -r now')
        else:
            print('wrong password')
            await ctx.send('Error')

    @commands.command(name='shutdown')
    @commands.is_owner()
    async def reboot(self, ctx, password):
        if password == self.password:
            for i in range(5):
                await asyncio.sleep(1)
                print(f'Shutting down in {5 - i}')
                await ctx.send(f'shutting down in {5 - i}')
            await ctx.send('Goodbye!')
            os.system('sudo shutdown -h now')
        else:
            print('wrong password')
            await ctx.send('Error')

def setup(bot):
    bot.add_cog(Admin(bot))