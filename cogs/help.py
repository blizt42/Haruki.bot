import discord
from discord.ext import commands

class Help(commands.Cog): #All the help commands in this bot
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command= True)
    async def help(self,ctx):
        em = discord.Embed(title='Help', description='Use ~help <command> for extended info about the command.',
                           color=ctx.author.color)
        em.add_field(name='INFO', value='about\n', inline=False)
        em.add_field(name='FUN', value='hi, gtn, emote, action, ping, praise, rp, r, yeetball', inline=False)
        em.add_field(name='COMMUNICATE', value='at, dm, dma', inline=False)
        em.add_field(name='USEFUL', value='clear, flip, search', inline=False)
        em.add_field(name='MUSIC', value='join, leave, loop, play, pause, skip, view', inline=False)
        em.set_footer(text='Haruki is here!!!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def about(self,ctx):
        em = discord.Embed(title='About', description='What! you want info about me (๑•́ ₃ •̀๑)')
        em.add_field(name='Usage', value='~about')
        em.set_footer(text='**blushes**', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    # FUN
    @help.command()
    async def gtn(self, ctx):
        em = discord.Embed(title='Guess the number', description='plays a minigame where you literally guess the number!')
        em.add_field(name='Usage', value='~gtn <difficulty> or ~g <difficulty>', inline=False)
        em.add_field(name='Difficulties', value='easy, medium, hard', inline=False)
        em.set_footer(text="pfftt it's not that hard.", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def emote(self,ctx):
        em = discord.Embed(title='Emotes',
                           description='Sends a gif according to your emote!')
        em.add_field(name='Usage', value='~emote <emote> or ~emt <emote>', inline=False)
        em.add_field(name='Type', value='''blush, cry, dance, lewd, pout, shrug, smile, smug, wag, laugh, grin''',
                     inline=False)
        em.set_footer(text="Ones way to express oneself.", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def action(self, ctx):
        em = discord.Embed(title='Actions',
                           description='Sends a gif according to your action to someone!')
        em.add_field(name='Usage', value='~action <action> <Member> or ~act <action> <Member>', inline=False)
        em.add_field(name='Type', value='''hug, kiss, slap, lick, cuddle, punch, pat, poke, boop, kill, bully''',
                     inline=False)
        em.set_footer(text="Ever wanted to do something to someone? Now you can!", icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def hi(self,ctx):
        em = discord.Embed(title='Hi!', description='Greets user')
        em.add_field(name='Usage', value='~hi')
        em.set_footer(text='Hello!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def ping(self,ctx):
        em = discord.Embed(title='Ping', description='Ping me ☺')
        em.add_field(name='Usage', value='~ping')
        em.set_footer(text='Checking my latency!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def praise(self,ctx):
        em = discord.Embed(title='Praise', description='Praise me (◕‿◕✿)')
        em.add_field(name='Usage', value='~praise or ~gd')
        em.set_footer(text='Luv you <3', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def rp(self,ctx):
        em = discord.Embed(title='Random picture', description='Sends random picture')
        em.add_field(name='Usage', value='~rp')
        em.set_footer(text='Pawperty of Jams', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def yeetball(self,ctx):
        em = discord.Embed(title='8ball but YEEET',
                           description='Ask a random question, Haruki and the gang will answer! Owo')
        em.add_field(name='Usage', value='''~yeetball <sentence> or ~AMA <sentence>
                                            eg: ~yeetball Am I smart?''')
        em.set_footer(text='We shall give you the truth!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def r(self,ctx):
        em = discord.Embed(title='Reddit', description='Sends post of the targeted subreddit')
        em.add_field(name='Usage', value='''~r <subreddit>
                                            eg: ~r memes''')
        em.set_footer(text='Read it already... Next!!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    # COMMUNICATE
    @help.command()
    async def at(self,ctx):
        em = discord.Embed(title='@user', description='Haruki will help you ping the user.')
        em.add_field(name='Usage', value='''~at <Member> <Number of repeated message> <Message>
                                                (Note: Only a maximum of 5 pings at one time)''')
        em.set_footer(text='P.S You cannot ping my creator :)', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def dma(self,ctx):
        em = discord.Embed(title='Direct message (Anonymously)', description='DMs user anonymously.')
        em.add_field(name='Usage', value='''~dma <Member> <Number of repeated message> <Message>
                                                (Note: Only a maximum of 3 messages at one time)''')
        em.set_footer(text='Sneaky...', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def dm(self,ctx):
        em = discord.Embed(title='Direct message (With Username)', description='DMs user but with your username.')
        em.add_field(name='Usage', value='''~dm <Member> <Number of repeated message> <Message>
                                                (Note: Only a maximum of 3 messages at one time)''')
        em.set_footer(text='Time to wake up your friends!!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    # USEFUL
    @help.command()
    async def clear(self,ctx):
        em = discord.Embed(title='Clear', description='Clears any amount of messages.')
        em.add_field(name='Usage', value='~clear <Number of messages>')
        em.set_footer(text='Begone messages!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command()
    async def flip(self,ctx):
        em = discord.Embed(title='Heads or Tails', description='Flips a coin')
        em.add_field(name='Usage', value='~flip')
        em.set_footer(text='P(Heads) = P(Tails), if the coin is fair though...', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='search')
    async def find(self,ctx):
        em = discord.Embed(title='Google search tool', description='Uses google search engine, provides 5 results')
        em.add_field(name='Usage', value='~search <query>')
        em.set_footer(text='Search engine go brrrrr', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    # MUSIC
    @help.command(name='join')
    async def joinmusic(self,ctx):
        em = discord.Embed(title='Enter channel', description='Haruki joins the channel')
        em.add_field(name='Usage', value='~join')
        em.set_footer(text='Listening to your sexy voice', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='leave')
    async def leavemusic(self,ctx):
        em = discord.Embed(title='Leave channel', description='Haruki leaves the channel')
        em.add_field(name='Usage', value='~leave or ~stop')
        em.set_footer(text='Bye bye have a good day!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='play')
    async def playmusic(self,ctx):
        em = discord.Embed(title='Music Player', description='Adds a song to the queue list and starts the playlist.')
        em.add_field(name='Usage', value='''~play <Song name> or ~play (if playlist already exist or if player is paused)
                                            aliases: ~p
                                            eg: ~play ussr national anthem''')
        em.set_footer(text='Music time!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='view')
    async def viewmusic(self,ctx):
        em = discord.Embed(title='View playlist',
                           description='Displays all the songs in the playlist (including the song playing)')
        em.add_field(name='Usage', value='~view')
        em.set_footer(text='I like music!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='pause')
    async def pausemusic(self,ctx):
        em = discord.Embed(title='Pause', description='Pauses the song playing.')
        em.add_field(name='Usage', value='~pause')
        em.set_footer(text='BRB toilet break...', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='resume')
    async def pausemusic(self, ctx):
        em = discord.Embed(title='Resume', description='Resumes the song playing.')
        em.add_field(name='Usage', value='~resume')
        em.set_footer(text='Back from the toilet!', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='loop')
    async def loopmusic(self,ctx):
        em = discord.Embed(title='Loop', description='Loops or unloop the current song playing.')
        em.add_field(name='Usage', value='~loop')
        em.set_footer(text='It is just too good...', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

    @help.command(name='skip')
    async def skipmusic(self,ctx):
        em = discord.Embed(title='Skip', description='Skips music.')
        em.add_field(name='Usage', value='~skip')
        em.set_footer(text='Boring...', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help(bot))