# -*- coding:utf-8 -*-
import discord
import asyncio
import os
chat = 1
access_token=os.environ['BOT_TOKEN']
token = access_token
client = discord.Client()
@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
# made by. D0ANT
# discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    global chat
    
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.
    
    if message.content == "/test": # !명령어 라는 채팅을 친다
        # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
        await message.channel.send("test")
        # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
        await message.author.send("test")
    
    #execute 도움
    
    if message.content == "A~":
        await message.channel.send("AAAAAAAAeyo~")
    if message.content == "/execute":
        await message.channel.send("/execute [align/as/at/rotation/postioned/facing/if/unless/in/run/store]")
    if message.content == "/execute align":
        await message.channel.send("실행 개체의 좌표를 반올림한다. 이과정에서 설정된 좌표값은 0으로 맞춰지기 때문에 블럭에 정 중앙에 위치시킬려면 /execute postioned ~0.5 ~ ~0.5 까지를 추가해야된다.(/execute align xyz)")
    if message.content == "/execute as":
        await message.channel.send("실행 개체를 설정한다. 이과정에서 이 개체의 위치기준으로 명령어가 실행되지는 않으니 이점 알아둬야한다. (/execute as [@a/@p/@r/@s/@e/플레이어닉네임/UUID])")
    if message.content == "/execute at":
        await message.channel.send("이 개체의 위치에서 명령어를 실행한다. 이때 실행개체를 설정하는것은 아니다. (/execute at [@a/@p/@r/@s/@e/플레이어닉네임/UUID])")
    if message.content == "/execute rotation":
        await message.channel.send("실행 개체의 회전을 가정한다. (/execute rotation [시야X] [시야Z])")
    if message.content == "/execute postioned":
        await message.channel.send("실행 개체의 위치를 가정한다 . (/execute postioned [x좌표] [y좌표] [z좌표])")
    if message.content == "/execute facing":
        await message.channel.send("실행 개체의 시야를 가정한다. (/execute facing [시야X] [시야Z])")
    if message.content == "/execute if":
        await message.channel.send("이 뒤에 나오는 데이터값이 참일때 다음 명령어를 실행한다. (/execute if [block,blocks,entity,data,score])")    
    if message.content == "/execute unless":
        await message.channel.send("이 뒤에 나오는 데이터값이 거짓일때 다음 명령어를 실행한다. (/execute unless [block,blocks,entity,data,score])")
    if message.content == "/execute in":
        await message.channel.send("이 지정된 월드안에서 명령어를 실행한다. (/execute in overworld,nether,the_end)")
    if message.content == "/execute run":
        await message.channel.send("이 명령어 앞에 모든것이 통과되었을때 뒤에 나오는 명령어를 실행한다. (/execute run 명령어)")
    if message.content == "/execute store":
        await message.channel.send("execute run뒤에 나오는 결과값 내용을 지정된 형태에 저장한다. (/execute store [result,succes])")

client.run(token)
