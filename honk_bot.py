import discord
from discord.ext import commands
from colorama import Fore, Back
from time import sleep
import random

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

dictKick = {}

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

file = open("/home/pi/Code/Python/honk_bot_token.txt")
token = file.readline()
file.close()

def conBot(message):
    print(colors.fg.red,"Bot: ",colors.reset, message)

@bot.event
async def on_ready():
    conBot("Running...")


@bot.command()
async def voteKick(ctx, member: discord.Member):

    await ctx.message.delete()


    if not member.name in dictKick:
        dictKick[member.name] = []


    if ctx.message.author.name in dictKick[member.name]:
        pass
    else:  

        #all member on server
        memberCount = ctx.guild.member_count

        memberName = []

        # create List with UserKick as name and add User how sends command 
       # if member.name in dictKick:
        dictKick[member.name].append(ctx.message.author.name)
       # else: 
        #    dictKick[member.name] = []
         #   dictKick[member.name].append(ctx.message.author.name)

        print(dictKick)

       #memberCount for display
        
        if not memberCount % 2 == 0:
            memberCountDisp = memberCount + 1
            print(memberCountDisp)

        #create List with all user
        for guild in bot.guilds:
            for member in guild.members:
                memberName.append(member.name)
       # print(memberName)

        numberOfVotes = len(dictKick[member.name])
        print (numberOfVotes)

        await ctx.channel.send("vote kick: " + member.name + " (" + str(numberOfVotes) + "/" + str(int(memberCountDisp/2)) + ")")
        
        if numberOfVotes > memberCount/2:
            await member.kick()

#    await ctx.message.delete()
    #    await member.kick()



@bot.command()
async def honk(ctx):
    user = ctx.author
    if user.voice != None:
        voice_channel = user.voice.channel
        vc = await voice_channel.connect()
        conBot("is Playing Honk")
        vc.play(discord.FFmpegPCMAudio('/home/pi/Code/Python/honk.mp3'))
        while vc.is_playing():
            sleep(3)
        conBot('disconected')
        await vc.disconnect(force=True)
    else:
       await ctx.message.channel.send('User is not in a channel')



@bot.command()
async def gif(ctx):
    await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/GooseDance.gif'))
    #print("Gif send to " + ctx.author.name)
    sleep(1)

@bot.command()
async def meme(ctx):

    rand = random.randint(1, 8)
    if rand == 1:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme1.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 2:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme2.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 3:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme3.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 4:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme4.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 5:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme5.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 6:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme6.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 7:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme7.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 8:
        await ctx.channel.send(file=discord.File('/home/pi/Code/Python/Meme/Meme8.png'))
        #print("Meme send to " + ctx.author.name)
        sleep(1)



bot.run(token)
