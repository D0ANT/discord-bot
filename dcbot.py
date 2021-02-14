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



    #커맨드

    if message.content == "/advancements":
        await message.channel.send("발전과제에 달성, 철회등을 조절한다. (/cmd)")
    if message.content == "/ban":
        await message.channel.send("어떤 플레이어의 접속을 불가하게 만든다. (/cmd)")
    if message.content == "/op":
        await message.channel.send("지정된 플레이어의 명령어권한을 부여한다. (/cmd)")
    if message.content == "/deop":
        await message.channel.send("deop - 지정된 플레이어의 명령어권한을 취소한다. (/cmd)")
    if message.content == "/pardon":
        await message.channel.send("접속불가된 권한을 취소시킨다. (/cmd)")
    if message.content == "/ben-ip":
        await message.channel.send("지정된 ip를 가진 플레이어의 접속권한을 없앤다. (/cmd)")
    if message.content == "/clear":
        await message.channel.send("지정된 플레이어의 아이템을 없앤다. (/cmd)")
    if message.content == "/clone":
        await message.channel.send("2개의 지정된 좌표안에 있는 건축물을 3번째 좌표에 붙여넣는다. (/cmd)")
    if message.content == "/defficulty":
        await message.channel.send("이 월드의 난이도를 조절한다. (/cmd)")
    if message.content == "/effect":
        await message.channel.send("지정된 엔티티에 효과를 부여한다. (/cmd)")
    if message.content == "/enchant":
        await message.channel.send("지정된 엔티티가 들고 있는 아이템에 마법을 부여한다. (/cmd)")
    if message.content == "/give":
        await message.channel.send("지정된 엔티티에게 아이템을 지급한다. (/cmd)")
    if message.content == "/replaceitem":
        await message.channel.send("지정된 엔티티에 슬롯에 아이템을 바꾼다. (/cmd)")
    if message.content == "/fill":
        await message.channel.send("좌표2개의 안에 있는 블럭을 설정된 블럭으로 바꾼다. (/cmd)")
    if message.content == "/gamemode":
        await message.channel.send("플레이어의 게임모드를 설정한다. (/cmd)")
    if message.content == "/kick":
        await message.channel.send("지정 플레이어를 접속을 종료시킨다. (/cmd)")
    if message.content == "/tell":
        await message.channel.send("지정 플레이어에게 메시지를 보낸다. (/cmd)")
    if message.content == "/tellraw":
        await message.channel.send("지정플레이어에게 nbt가 설정되어있는 메시지를 보낸다. (/cmd)")
    if message.content == "/playsound":
        await message.channel.send("지정 플레이어에게 마인크래프트 소리를 플레이시킨다. (/cmd)")
    if message.content == "/stopsound":
        await message.channel.send("지정 플레이어에게 재생되고 있는 소리를 정지시킨다. (/cmd)")
    if message.content == "/say":
        await message.channel.send("모든 플레이어에게 메시지를 보낸다. (/cmd)")
    if message.content == "/setblock":
        await message.channel.send("지정된 좌표에 블럭을 설정한다. (/cmd)")
    if message.content == "/setworldspawn":
        await message.channel.send("월드의 시작지점을 설정한다. (/cmd)")
    if message.content == "/stop":
        await message.channel.send("서버를 끈다. (/cmd)")
    if message.content == "/summon":
        await message.channel.send("지정된 엔티티를 생성시킨다. (/cmd)")
    if message.content == "/time":
        await message.channel.send("시간을 설정한다. (/cmd)")
    if message.content == "/title":
        await message.channel.send("지정된 플레이어의 화면에 큰 글씨를 띄운다. (/cmd)")
    if message.content == "/trigger":
        await message.channel.send("지정된 트리거스코어보드에 점수를 부여한다. (/cmd)")
    if message.content == "/whitelist":
        await message.channel.send("화이트리스트가 켜져있을때는 화이트리스트 안에 있는사람만 접속이 가능하다. (/cmd)")
    if message.content == "/worldborder":
        await message.channel.send("월드보더를 설정한다. (/cmd)")
    if message.content == "/pardon-ip":
        await message.channel.send("지정된 접속거부된 ip의 밴을 푼다. (/cmd)")
    if message.content == "/tp":
        await message.channel.send("지정된 엔티티를 어떤 위치로 순간이동시킨다. (/cmd)")
    if message.content == "/spreadplayers":
        await message.channel.send("지정엔티티를 지정된 중앙좌표를 기준으로 산개시킨다. (/cmd)")
    if message.content == "/scoreboard":
        await message.channel.send("점수판을 다루는 명령어이다. (/cmd)")
    if message.content == "/particle":
        await message.channel.send("입자를 생성시킨다. (/cmd)")
    if message.content == "/spawnpoint":
        await message.channel.send("지정된 플레이어의 생성지점을 설정한다. (/cmd)")
    if message.content == "/kill":
        await message.channel.send("지정엔티티를 없앤다. (/cmd)")
    if message.content == "/carrot":
        await message.channel.send("도개미는 코딩중이여서 당근을 흔들고있다. (?)")
    if message.content == "/source_code":
        await message.channel.send("소스코드 링크: https://github.com/D0ANT/discord-bot/blob/master/dcbot.py")
    if message.content == "/추가요청":
        await message.channel.send("추가요청 링크: https://github.com/D0ANT/discord-bot/issues/1")


client.run(token)
