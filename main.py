import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import praw
import random
import os

Client = discord.Client()
client = commands.Bot(command_prefix = '.')

print('Logging into reddit')
reddit = praw.Reddit(client_id='4CUXwh1iZMgvNg',
                     client_secret='M1ga5gj9M4LpFgE-CC1wQZkNXFs',
                     username='Snegelen',
                     password='folkeskole99',
                     user_agent='Testing reddit module')
print('Logged in')



@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def wait_until_login():
    await client.change_presence(game=discord.Game(name='something goes here'))

@client.event
async def on_message(message):
    userID = message.author.id
    randNumber = random.randint(1,100)
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        
    #Memes in the new section on reddit
    if message.content.upper().replace(" ", "").startswith("!NEWMEMES"):
        memesSubredditNew = reddit.subreddit('memes').new()
        
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditNew if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    #Memes in the top section on reddit
    if message.content.upper().replace(" ", "").startswith("!TOPMEMES"):
        memesSubredditTop = reddit.subreddit('memes').top()
        
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditTop if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    #Memes in the rising section on reddit
    if message.content.upper().replace(" ", "").startswith("!RISINGMEMES"):
        memesSubredditRising = reddit.subreddit('memes').rising()
        rN = random.randint(1,29)

        for x in range (0, rN):
            output = next(i for i in memesSubredditRising if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, rN) )
        await client.send_message(message.channel, output.url)

    #Memes in the controversial section on reddit
    if message.content.upper().replace(" ", "").startswith("!CONTROVERSIALMEMES"):
        memesSubredditControversial = reddit.subreddit('memes').controversial()
        
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditControversial if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)
        
    #Memes in the hot section on reddit
    if message.content.upper().replace(" ", "").startswith("!HOTMEMES"):
        memesSubredditHot = reddit.subreddit('memes').hot()              
        
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditHot if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)
    await client.process_commands(message)

    #Memes in the hot section on reddit
    if message.content.upper().replace(" ", "").startswith("!OFFENSIVEMEMES"):
        memesSubredditOffensive = reddit.subreddit('OffensiveMemes').hot()              
        
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditOffensive if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    if message.content.upper().replace(" ", "").startswith("!CHRISTIANMEMES"):
        memesSubredditChristian = reddit.subreddit('dankchristianmemes').hot()  
         
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditChristian if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    if message.content.upper().replace(" ", "").startswith("!SPOOK"):
        memesSubredditSpook = reddit.subreddit('spookymemes').hot()  
         
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditSpook if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    if message.content.upper().replace(" ", "").startswith("!SPONGEBOB"):
        memesSubredditSB = reddit.subreddit('BikiniBottomTwitter').hot()  
         
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditSB if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.url)

    if message.content.upper().replace(" ", "").startswith("!DADJOKE"):
        memesSubredditDadJoke = reddit.subreddit('dadjokes').hot()  
         
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditDadJoke if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> jokeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.title)
        await client.send_message(message.channel, output.selftext)

    if message.content.upper().replace(" ", "").startswith("!DARKHUMOR"):
        memesSubredditDarkHumor = reddit.subreddit('darkhumorjokes').hot()  
         
        for x in range (0, randNumber):
            output = next(i for i in memesSubredditDarkHumor if not i.stickied)
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> jokeID: %d " % (userID, randNumber) )
        await client.send_message(message.channel, output.title)
        await client.send_message(message.channel, output.selftext)

    if message.content.upper().replace(" ", "").startswith("!ANIMEMEMES"):
        memesSubredditAnimeMemes = reddit.subreddit('animememes').hot()
        memesSubredditAnimeMemes2 = reddit.subreddit('MemesOfAnime').hot()
        temp = random.randint(0,1)
        userID = message.author.id

        if temp == 1:
            for x in range (0, randNumber):
                output = next(i for i in memesSubredditAnimeMemes if not i.stickied)            
            await client.send_message(message.channel, "<@%s> memeD: %d " % (userID, randNumber) )
            await client.send_message(message.channel, output.title)
            await client.send_message(message.channel, output.url)
        if temp == 0:
            for x in range (0, randNumber):
                output = next(i for i in memesSubredditAnimeMemes2 if not i.stickied)            
            await client.send_message(message.channel, "<@%s> memeID: %d " % (userID, randNumber) )
            await client.send_message(message.channel, output.title)
            await client.send_message(message.channel, output.url)
        
    await client.process_commands(message)

client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!hot memes', value='Returns a meme from r/memes hot section', inline=False)
    embed.add_field(name='!new memes', value='Returns a meme from r/memes new section', inline=False)
    embed.add_field(name='!top memes', value='Returns a meme from r/memes top section', inline=False)
    embed.add_field(name='!rising memes', value='Returns a meme from r/memes rising section', inline=False)
    embed.add_field(name='!controversial memes', value='Returns a meme from r/memes controversial section', inline=False)
    embed.add_field(name='!offensive memes', value='Returns a meme from r/offensivememes hot section', inline=False)
    embed.add_field(name='!christian memes', value='Returns a meme from r/dankchristianmemes hot section', inline=False)
    embed.add_field(name='!spook', value='Returns a meme from r/spookymemes hot section', inline=False)
    embed.add_field(name='!spongebob', value='Returns a meme from r/BikiniBottomTwitter hot section', inline=False)
    embed.add_field(name='!dad joke', value='Returns a meme from r/dadjokes hot section', inline=False)
    embed.add_field(name='!darkhumor', value='Returns a meme from r/darkhumorjokes hot section', inline=False)
    embed.add_field(name='!anime memes', value='Returns a meme from r/animememes hot section', inline=False)
    
    await client.send_message(author, embed=embed)
    
client.run(os.getenv('TOKEN'))
