import os
import discord
from discord.ext import commands

class Admin(commands.Cog): #NOT DISPLAYED IN ~help!!!! All the admin commands
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='deletesongs')
    async def deletesongs(self, ctx, password):
        if password == 'Deppresso': #yes its just one of my alt username
            music = 'music'
            for song in os.listdir(music):
                song_path = os.path.join(music, song)
                try:
                    if os.path.isfile(song_path) or os.path.islink(song_path):
                        os.unlink(song_path)
                except Exception as e:
                    await ctx.send('Failed to delete {}. Reason: {}'.format(song_path, e))
                    print('Failed to delete {}. Reason: {}'.format(song_path, e))
            await ctx.send('songs deleted')
        else:
            await ctx.send('Error')

def setup(bot):
    bot.add_cog(Admin(bot))