import discord
import random
import praw
import requests
import json
from discord.ext import commands
from random import choice

class guesstn:
    def __init__(self, ctx):
        self.bot = ctx.bot
        self.status = False
        self.number = None
        self.diff = None
        self.tries = 1

    def generateNumber(self, diff):
        self.diff = diff
        if self.diff == 'easy':
            self.number = random.randint(1,10)
        elif self.diff == 'medium':
            self.number = random.randint(1,1000)
        else:
            self.number = random.randint(1,10000)

    def get_tries(self):
        return self.tries
    def up_tries(self):
        self.tries += 1
    def get_number(self):
        return self.number
    def set_status(self):
        if self.status:
            self.status = False
        else:
            self.status = True
    def get_status(self):
        return self.status

class Fun(commands.Cog): #All the fun commands
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.guessplayers = {}
        self.tenorkey = '' #insert tenor api token here
        self.limit = 10
        self.redditkey = ['','', 'Haruki'] #[client_id, client_secret, user_agent]

    def get_guesstn(self, ctx):
        try:
            guessing = self.guessplayers[ctx.author.id]
        except KeyError:
            guessing = guesstn(ctx)
            self.guessplayers[ctx.author.id] = guessing
        return guessing

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Good day {member.mention}! Paw\'s cousin wishes that you are dead! ~help for commands')

    @commands.command(name='gtn', aliases=['g'])
    async def guesstn(self, ctx, msg):
        difficulty = ['easy','medium','hard']
        guessingplayer  = self.get_guesstn(ctx)
        try:
            if msg in difficulty:
                if guessingplayer.get_status():
                    return await ctx.send('You are currently guessing!')
                if msg == 'easy':
                    em = discord.Embed(title='Guess the number', description=f'Difficuly: {msg}, Number is from 1-10, start guessing!')
                elif msg == 'medium':
                    em = discord.Embed(title='Guess the number', description=f'Difficuly: {msg}, Number is from 1-1000, start guessing!')
                else:
                    em = discord.Embed(title='Guess the number', description=f'Difficuly: {msg}, Number is from 1-10000, start guessing!')
                em.set_footer(text='Luck is totally not a factor. use ~g {number} to guess!',
                              icon_url=self.bot.user.avatar_url)
                guessingplayer.set_status()
                guessingplayer.generateNumber(msg)
                await ctx.send(embed=em)
            if not guessingplayer.get_status():
                return await ctx.send('You are not currently guessing! use ~gtn {easy/medium/hard} to start.')
            if msg == 'stop':
                await ctx.send('Giving up already? Haizz :(   Cleaning up...')
                del self.guessplayers[ctx.author.id]
                return
            try:
                number = int(msg)
                if number == guessingplayer.get_number():
                    guess = discord.Embed(title='Congrats',
                                          description=f'You have correctly guessed the number in {guessingplayer.get_tries()} tries! [{guessingplayer.get_number()}]')
                    guess.set_footer(text='Sugoi suGoi!!', icon_url=self.bot.user.avatar_url)
                    del self.guessplayers[ctx.author.id]
                elif number < guessingplayer.get_number():
                    guess = discord.Embed(title='Too Low!',
                                          description='Try going higher.')
                    guess.set_footer(text='Never give up!', icon_url=self.bot.user.avatar_url)
                    guessingplayer.up_tries()
                else:
                    guess = discord.Embed(title='Too High!',
                                          description='Try going lower.')
                    guess.set_footer(text='Never give up!', icon_url=self.bot.user.avatar_url)
                    guessingplayer.up_tries()
                return await ctx.send(embed=guess)

            except Exception as e:
                if msg in difficulty:
                    return
                print('error', e)
                await ctx.send('This is not a number, try again')

        except Exception as e:
            print(e)

    @commands.command(name='about')
    @commands.cooldown(1, 10, commands.BucketType.user)
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
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def reddit(self, ctx, subr):
        text = ['Here you go :))', 'Here is one!', 'Hai!', ':)']
        reddit = praw.Reddit(client_id=self.redditkey[0],
                             client_secret=self.redditkey[1],
                             user_agent=self.redditkey[2])
        print(f'~r Reddit connection: {reddit.read_only}')
        await ctx.trigger_typing()
        try:
            redditpost = reddit.subreddit(f'{subr}').new()
            post_to_pick = random.randint(1,10)
            for i in range(0, post_to_pick):
                submission = next(x for x in redditpost if not x.stickied)
            em = discord.Embed(title=f'r/{subr}', description=choice(text))
            em.set_image(url=submission.url)
            await ctx.send(embed=em)
            print(f'Reddit post link for r/{subr} : {submission.url}')
        except Exception as e:
            await ctx.send('Unkown subreddit, try again.')
            print(f'~reddit Error; {e}')

    @commands.command(name='rp')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def randompicture(self,ctx):
        num = random.randint(0, 9)
        text = ['Here you go :))', 'Here is one!', 'Hai!', ':)']
        await ctx.send(text[random.randint(0, 3)])
        await ctx.send(file=discord.File(f'pictures/{num}.jpeg'))

    @commands.command(name='yeetball', aliases=['yb'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yeetball(self,ctx):
        file = open('misc/yeetball.txt', 'r')
        response = []
        for line in file:
            response.append(line[:-1])
        await ctx.send(choice(response))
        file.close()

    @commands.command(name='action', aliases=['act'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def act(self, ctx, action, member:discord.Member):
        search_terms = {'hug':'hugs', 'kiss':'kisses', 'slap':'slaps', 'lick':'licks', 'cuddle':'cuddles','punch':'punches',
                        'pat':'pats','poke':'pokes','boop':'boops', 'kill':'kills','bully':'bullies'}
        if action not in search_terms:
            return await ctx.send('You wanna what now?? Try again :/')
        if ctx.author == member:
            return await ctx.send('That is gay')
        response = []
        r = requests.get(
            "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % ('anime '+ action, self.tenorkey, self.limit))
        if r.status_code== 200:
            top_10gifs = json.loads(r.content)
            try:
                for result in top_10gifs['results']:
                    for media in result['media']:
                        response.append(media['mediumgif']['url'])
            except Exception as e:
                print('action error:', e)
            em = discord.Embed()
            em.set_author(name=f'{ctx.author} {search_terms[action]} {member}', icon_url=ctx.author.avatar_url)
            em.set_image(url=choice(response))
            await ctx.send(embed=em)

    @commands.command(name='emote', aliases=['emt'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def emote(self, ctx, emote):
        search_terms = {'blush':'blushes', 'cry':'cries', 'dance':'dances', 'lewd':'becomes lewd',
                        'pout':'pouts', 'shrug':'shrugs','smile':'smiles','smug':'is smugging',
                        'wag':'wags','laugh':'laughs', 'grin':'grins'}
        if emote not in search_terms:
            return await ctx.send('You wanna what now?? Try again :/')
        response = []
        r = requests.get(
            "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % ('anime ' + emote, self.tenorkey, self.limit))
        if r.status_code== 200:
            top_10gifs = json.loads(r.content)
            try:
                for result in top_10gifs['results']:
                    for media in result['media']:
                        response.append(media['mediumgif']['url'])
            except Exception as e:
                print('emote error:',e)
            em = discord.Embed()
            em.set_author(name=f'{ctx.author} {search_terms[emote]}...', icon_url=ctx.author.avatar_url)
            em.set_image(url=choice(response))
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Fun(bot))