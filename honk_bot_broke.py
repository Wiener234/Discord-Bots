import discord
import random
from time import sleep
from discord.ext import commands
from datetime import datetime
import youtube_dl
import os
from colorama import Fore, Back

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)

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

file = open("honk_bot_token.txt")
token = file.readline()
file.close()


time_10_00 = "10:00:00"
time_12_00 = "12:00:00"
time_15_30 = "15:30:00"
time_18_30 = "18:30:00"


def conBot(message):
    print(colors.fg.red,"Bot: ",colors.reset, message)

@client.event
async def on_ready():
    conBot("Running...")

@client.command()
async def gif(ctx):
    await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/GooseDance.gif'))
    print("Gif send to " + ctx.author.name)
    sleep(1)

@client.command()
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
        for guild in client.guilds:
            for member in guild.members:
                memberName.append(member.name)
       # print(memberName)

        numberOfVotes = len(dictKick[member.name])
        #print (numberOfVotes)

        await ctx.channel.send("vote kick: " + member.name + " (" + str(numberOfVotes) + "/" + str(int(memberCountDisp/2)) + ")")

        if numberOfVotes > memberCount/2:
            await member.kick()


@client.command()
async def meme(ctx):

    rand = random.randint(1, 8)
    if rand == 1:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme1.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 2:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme2.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 3:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme3.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 4:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme4.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 5:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme5.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 6:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme6.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 7:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme7.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)
    if rand == 8:
        await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme8.png'))
        print("Meme send to " + ctx.author.name)
        sleep(1)



@client.command()
async def honk(ctx):
    user = ctx.author
    if user.voice != None:
        voice_channel = user.voice.channel
        vc = await voice_channel.connect()
        print("is Playing Honk")
        vc.play(discord.FFmpegPCMAudio('/home/nils/Scripts/test.mp3'))
        while vc.is_playing():
            sleep(3)
        print('disconected')
        await vc.disconnect()
    else:
       await ctx.message.channel.send('User is not in a channel')



@client.command()
async def test(ctx):
    if ctx.author.id == 292301348504862721:
        channel = client.get_channel(806616662337912883)
        await ctx.author.move_to(channel)


# @client.command()
# async def play(ctx, url: str):
#     song_there = os.path.isfile("song.m4a")
#     try:
#         if song_there:
#             os.remove("song.m4a")
#     except PermissionError:
#         await ctx.send("Wait for song to end playing.")
#
#     voice_channel = ctx.author.voice.channel
#     vc = await voice_channel.connect()
#
#     FFMPEG_OPTIONS = {
#         'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
#         'options': '-vn -report -fifo_format m4a -attempt_recovery 1 -recovery_wait_time 1',
#
#     }
#
#     ydl_opts = {
#         #'format': 'bestaudio',
#         #'postprocessors': [{
#          #   'key': 'FFmpegExtractAudio',
#          #   'preferredcodec': 'mp3',
#           #  'preferredquality': '192',
#         #}],
#
#
#         'format': 'bestaudio/best',
#
#     }
#
#
#
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#         sleep(3)
#     for file in os.listdir("/home/nils/Scripts"):
#         if file.endswith(".m4a"):
#             os.rename(file, "song.m4a")
#     print('playing')
#     vc.play(discord.FFmpegPCMAudio('/home/nils/Scripts/song.m4a', **FFMPEG_OPTIONS))
#
#     while vc.is_playing():
#
#         print("while")
#         sleep(3)
#
#     if not vc.is_playing():
#         print(stoped)
#     print("disconect")
#     await vc.disconnect()








#@client.command()
#async def daily_meme(ctx):
#    await ctx.channel.send("memes will be send")
#    print("memes will be send on the given dates")
#    while True:
#        real_time = datetime.now().strftime('%H:%M:%S')
#
#        if real_time == time_10_00:
#            rand = random.randint(1, 7)
#            if rand == 1:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme1.png'))
#                print("10:00:00")
#                sleep(1)
#            if rand == 2:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme2.png'))
#                print("10:00:00")
#                sleep(1)
#            if rand == 3:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme3.png'))
#                print("10:00:00")
#                sleep(1)
#            if rand == 4:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme4.png'))
#                print("10:00:00")
#                sleep(1)
#            if rand == 5:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme5.png'))
#                print("10:00:00")
#                sleep(1)
#            if rand == 6:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme6.png'))
#                print("10:00:00")
#                sleep(1)
#
#        if real_time == time_12_00:
#            rand = random.randint(1, 7)
#            if rand == 1:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme1.png'))
#                print("12:00:00")
#                sleep(1)
#            if rand == 2:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme2.png'))
#                print("12:00:00")
#                sleep(1)
#            if rand == 3:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme3.png'))
#                print("12:00:00")
#                sleep(1)
#            if rand == 4:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme4.png'))
#                print("12:00:00")
#                sleep(1)
#            if rand == 5:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme5.png'))
#                sleep(1)
#            if rand == 6:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme6.png'))
#                print("12:00:00")
#                sleep(1)
#
#        if real_time == time_15_30:
#            rand = random.randint(1, 7)
#            if rand == 1:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme1.png'))
#                print("15:30:00")
#                sleep(1)
#            if rand == 2:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme2.png'))
#                print("15:30:00")
#                sleep(1)
#            if rand == 3:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme3.png'))
#                print("15:30:00")
#                sleep(1)
#            if rand == 4:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme4.png'))
#                print("15:30:00")
#                sleep(1)
#            if rand == 5:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme5.png'))
#                print("15:30:00")
#                sleep(1)
#            if rand == 6:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme6.png'))
#                print("15:30:00")
#                sleep(1)
#
#        if real_time == time_18_30:
#            rand = random.randint(1, 7)
#            if rand == 1:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme1.png'))
#                print("18:30:00")
#                sleep(1)
#            if rand == 2:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme2.png'))
#                print("18:30:00")
#                sleep(1)
#            if rand == 3:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme3.png'))
#                print("18:30:00")
#                sleep(1)
#            if rand == 4:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme4.png'))
#                print("18:30:00")
#                sleep(1)
#            if rand == 5:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme5.png'))
#                print("18:30:00")
#                sleep(1)
#            if rand == 6:
#                await ctx.author.send(file=discord.File('/home/nils/Scripts/Meme/Meme6.png'))
#                print("18:30:00")
#                sleep(1)

client.run(token)
