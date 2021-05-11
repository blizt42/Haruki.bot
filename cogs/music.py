import discord
import async_timeout
import youtube_dl
import asyncio
import shutil
import os
from discord.ext import commands

####youtube####
youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {'options': '-vn'}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer): #songfile creator
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        shutil.move(filename, f'music/{filename}')
        return cls(discord.FFmpegPCMAudio(f'music/{filename}', **ffmpeg_options), data=data)

    @classmethod
    async def check_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
        if 'entries' in data:
            data = data['entries'][0]
        searched = data['title']
        return searched

class MusicPlayer: #The player that will play music
    def __init__(self, ctx):
        self.bot = ctx.bot
        self.guild = ctx.guild
        self.channel = ctx.channel
        self.cog = ctx.cog

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()
        self.current = None
        self.nowplaying =None

        self.stop = False
        self.loop = False
        self.loopsong = None

        ctx.bot.loop.create_task(self.Player())
    async def Player(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            if self.stop:
                print(f'Stopping player for {self.bot}')
                return
            self.next.clear()
            try:
                async with async_timeout.timeout(300):
                    if not self.loop:
                        player = await self.queue.get()
                        print(f'url get : {player}')
                    else:
                        print('debug')
                        player = self.loopsong
            except asyncio.TimeoutError:
                return self.destroy(self.guild)
            try:
                print(player)
                player = await YTDLSource.from_url(player , loop=self.bot.loop)
                print(f'Prepared {player.title}')
            except Exception as e:
                await self.channel.send(f'An error occured. Reason: {e}')
                print(f'Error in processing song: {e}')
                continue
            self.current = player
            self.guild.voice_client.play(player, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.nowplaying = await self.channel.send(f'**Now Playing:** `{player.title}`')
            self.loopsong = player.title
            try:
                await self.next.wait()
            except Exception as e:
                print(f'error: {e}')
            player.cleanup()
            self.current = None

            try:
                await self.nowplaying.delete()
            except discord.HTTPException:
                pass

    def destroy(self, guild):
        return self.bot.loop.create_task(self.cog.cleanup(guild))

    def killplayer(self):
        self.stop = True

    def set_loop(self):
        if self.loop:
            self.loop = False
        else:
            self.loop = True

    def get_loop(self):
        return self.loop
    def get_song(self):
        return self.loopsong

class MusicCommands(commands.Cog): #ALl commands for music
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild): #Not by me
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass
        music = 'music'
        await asyncio.sleep(5)
        for song in os.listdir(music):
            song_path = os.path.join(music, song)
            try:
                if os.path.isfile(song_path) or os.path.islink(song_path):
                    os.unlink(song_path)
                print(f'{song} deleted when cleaning up player.\n')
            except Exception as e:
                print('Failed to delete {}. Reason: {} \n'.format(song_path, e))

    def get_MusicPlayer(self, ctx):
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='join')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("HEY!! You are not connected to a voice channel :(")
        else:
            try:
                channel = ctx.message.author.voice.channel
                await channel.connect()
                await ctx.send('Connected and listening to your sexy voice.')
            except Exception as e:
                print(f'~join error. Reason: {e}')
                await ctx.send(f'HEY!!!! Connecting error: {e}')

    @commands.command(name='play', aliases=['p'])
    async def play(self, ctx, *, url):
        await ctx.trigger_typing()
        voice = ctx.voice_client

        if not voice:
            await ctx.invoke(self.join)

        player = self.get_MusicPlayer(ctx)
        source = await YTDLSource.from_url(url, loop=self.bot.loop)
        await player.queue.put(url)
        await ctx.send(f'{source.title} has been added to the queue.')

    @commands.command(name='loop')
    async def loop(self, ctx):
        voice = ctx.voice_client
        player = self.get_MusicPlayer(ctx)
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!', delete_after=20)
        if player.get_song() == None:
            return await ctx.send('No song is currently playing!!')
        player.set_loop()
        if player.get_loop():
            await ctx.send(f'Player is now looping: {voice.source.title}')
        else:
            await ctx.send(f'Player has stop looping, use ~view to view upcoming songs')
        if voice.is_paused():
            await ctx.send(f'Note: Bot is paused, use ~resume.')

    @commands.command(name='skip')
    async def skip(self, ctx):
        voice = ctx.voice_client
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!')

        if voice.is_paused():
            pass
        elif not voice.is_playing():
            return

        voice.stop()
        await ctx.send('Skipping...')

    @commands.command(name='pause')
    async def pause(self, ctx):
        voice = ctx.voice_client
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!')
        if voice.is_paused():
            return await ctx.send('The player is currently paused')

        voice.pause()
        await ctx.send('Player is now paused...')

    @commands.command(name='resume')
    async def resume(self, ctx):
        voice = ctx.voice_client
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!')
        if voice.is_paused():
            pass
        else:
            return await ctx.send('Player is currently playing!')

        voice.resume()
        await ctx.send('Now resuming player...')

    @commands.command(name='view')
    async def view(self, ctx):
        await ctx.trigger_typing()
        player = self.get_MusicPlayer(ctx)
        list = player.queue._queue

        voice = ctx.voice_client
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!')

        title = 'Now playing:'
        em = discord.Embed(title=title + ' (Looping)' if player.get_loop() else title, description=f'{voice.source.title}')

        view = ''
        search = ''
        count = 0
        if len(list) != 0:
            for song in list:
                count += 1
                if count <= 5:
                    searched = await YTDLSource.check_url(song, loop=self.bot.loop)
                    search += '{:>2}:{:^20} -> {}'.format(count, song, searched) + '\n'
                else:
                    view += '{:>2}:{:^20}'.format(count, song) + '\n'
            em.add_field(name='Up next:', value=search)
            if count > 5:
                em.add_field(name='Rest of queue', value=view, inline=False)
            em.set_footer(text="Haruki's music playlist",icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = em)

    @commands.command(name='stop', aliases=['leave'])
    async def stop(self, ctx):
        voice = ctx.voice_client
        if not voice or not voice.is_connected():
            return await ctx.send('Heyy!! I am not currently playing anything!')

        await ctx.send('Goodbye!')
        player = self.get_MusicPlayer(ctx)
        player.killplayer()
        await self.cleanup(ctx.guild)

def setup(bot):
    bot.add_cog(MusicCommands(bot))
