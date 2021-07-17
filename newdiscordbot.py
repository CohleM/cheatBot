import discord
from discord.ext import commands
from scrapeResults import GoogleSearch, getfullscreenshot
from searchPdf import searchPdf
client = discord.Client()

client  = commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def gs(ctx, *, arg):
    "send screenshot of first page of google search"
    GoogleSearch(arg)
    await ctx.send('Search results for ' + arg + ' ' )
    await ctx.send(file = discord.File('screenshot.png'))


@client.command()
async def fs(ctx, *, arg):
    "send full page screenshot of first link of first page"
    getfullscreenshot(arg,1)
    await ctx.send('Search results for ' + arg + ' ' )
    await ctx.send(file = discord.File('full_screenshot.png'))

@client.command()
async def search(ctx, *, arg):
    "search all pdfs"
    await ctx.send(searchPdf(arg)) 

client.run('NzY0NTExNzE3ODM2MTkzNzkz.X4HVBQ.VPqZj4D6BjzSePMN4ZTU4jYrRYA')
