# -*- coding:utf-8 -*-
import discord
import asyncio
import os
chat = 1
access_token=os.environ['BOT_TOKEN']
MJid=os.environ['MJid']
MINGid=os.environ['MINGid']
ANOid=os.environ['ANOid']
DOANTid=os.environ['DOANTid']
token = access_token
client = discord.Client()
@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
# made by. D0ANT,도개미
# discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)
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
    
    if message.content == "/명령어": # !명령어 라는 채팅을 친다
        # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.  await message.channel.send("")
        # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
        await message.author.send("")
        
    if message.content == "/채팅응답 off" or message.content == "/채팅 응답 off" or message.content == "/채팅응답 OFF" or message.content == "/채팅 응답 OFF":
        if chat == 0:
            await message.channel.send("이미 꺼져있습니다.")
        else:
            await message.channel.send("채팅 응답이 꺼졌습니다.")
            chat = 0
        #맨션
     
      
 '''
        if message.content == "도개미야":
            await message.channel.send(DOANTid)    
        if message.content == "개미야":
            await message.channel.send(DOANTid)   
        if message.content == "도개미":
            await message.channel.send(DOANTid)     
        if message.content == "도개미씨":
            await message.channel.send(DOANTid)
        if message.content == "개미씨":
            await message.channel.send(DOANTid)                          

        if message.content == "아노야":
            await message.channel.send(ANOid)
        if message.content == "아노":
            await message.channel.send(ANOid)
        if message.content == "아노씨":
                await message.channel.send(ANOid)    

        if message.content == "엠제이야":
            await message.channel.send(MJid)
        if message.content == "엠제이":
            await message.channel.send(MJid)  
        if message.content == "앰제이야":
            await message.channel.send(MJid)  
        if message.content == "앰제이":
            await message.channel.send(MJid)   
        if message.content == "제이야":
            await message.channel.send(MJid)
        if message.content == "앰제이씨":
            await message.channel.send(MJid)
        if message.content == "엠제이씨":
            await message.channel.send(MJid)
        if message.content == "제이씨":
            await message.channel.send(MJid)            

        if message.content == "밍찡아":
            await message.channel.send(MINGid)
        if message.content == "밍밍찡아":
            await message.channel.send(MINGid)
        if message.content == "밍밍찡":
            await message.channel.send(MINGid)      
        if message.content == "밍밍찡씨":
            await message.channel.send(MINGid)             
        if message.content == "밍찡씨":
            await message.channel.send(MINGid)'''

client.run(token)
