# -*- coding:utf-8 -*-
# 위에 구문은 # 빼버리시면 문제 생깁니다.
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언합니다.
import discord
import asyncio
import os
access_token=os.environ['BOT_TOKEN']
token = access_token # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client()
@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
# 봇이 "반갑습니다"를 플레이 하게 됩니다.
# 눈치 채셨을지 모르곘지만, discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))
    print("I'm Ready!") # I'm Ready! 문구를 출력합니다.
    print(client.user.name) # 봇의 이름을 출력합니다.
    print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.
    
    if message.content == "/명령어": # !명령어 라는 채팅을 친다면
        # 메시지 전송이 두가지 방법이 있습니다. 상황에 맞는 구문을 사용하시면 됩니다.
        # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
        await message.channel.send("/법")
        await message.channel.send("/명령어")
        await message.channel.send("/임베드 [ /도개미/아노/앰제이/밍찡이]")
        
        # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
        await message.author.send("/법")
        await message.author.send("/명령어")
        await message.author.send("/임베드 [ /도개미/아노/앰제이/밍찡이]")
        
    if message.content == "/법":
        await message.author.send("법")
        await message.author.send("명예 훼손죄: 야생서버 kill")
        await message.author.send("욕설죄: 징역 1분")
        await message.author.send("협박죄: 징역 30초")
        await message.author.send("도배죄: 징역 30초")
        await message.author.send("사기죄: 야생서버 kill")
        await message.author.send("음성도배: 징역 40초")
        await message.author.send("주거침입죄: 다야 1개")
        await message.author.send("법 안듣음: 10초밴")
        await message.author.send("훔치기:")
        await message.author.send("1번째: 마크시간 1일 감옥형")
        await message.author.send("2번째: 야생서버 kill,아이템 소각")
        await message.author.send("3번째: 야생서버 kick")
        await message.author.send("4번째: 마크시간 3일 감옥형")
        await message.author.send("5번째: 집 파괴")


    #채팅봇


    if message.content == "ㅎㅇ":
        await message.channel.send("ㅇㅇ 나도 ㅎㅇ~")  
    if message.content == "ㅎㅇ?":
        await message.channel.send("ㅇㅇ 나도 ㅎㅇ~")

    if message.content == "뭐하냐?":
        await message.channel.send("너랑 채팅중이잖아ㅋㅋ")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅇㅇ 나도 ㅎㅇ~")  
    
    if message.content == "넌 누가 만듬?":
        await message.channel.send("디스코드 API를 이용함과 동시에 파이썬을 이용해 도개미가 코딩으로 만듬 ㅇㅇ")

    if message.content == "재밌냐?":
        await message.channel.send("이렇게 채팅이나 하고있는데 재밌겠냐")

    if message.content == "마크로 뭐하냐":
        await message.channel.send("야생중")

    if message.content == "서버 열어":
        await message.channel.send("싫음 ^^")

    if message.content == "아무나 나랑 채팅할사람?":
        await message.channel.send("ㅇㅇ 나랑")    
    if message.content == "아무나 나랑 얘기할사람?":
        await message.channel.send("ㅇㅇ 나랑")  
    if message.content == "나랑 얘기할사람?":
        await message.channel.send("ㅇㅇ 나랑")  
    if message.content == "나랑 채팅할사람?":
        await message.channel.send("ㅇㅇ 나랑")         

    #채팅/ 맨션

    if message.content == "도개미야":
        await message.channel.send("@도개미")    
    if message.content == "개미야":
        await message.channel.send("@도개미")   
    if message.content == "도개미":
        await message.channel.send("@도개미")     
    if message.content == "도개미씨":
        await message.channel.send("@도개미")
    if message.content == "개미씨":
        await message.channel.send("@도개미")                          
    
    if message.content == "아노야":
        await message.channel.send("@트롤아노")
    if message.content == "아노":
        await message.channel.send("@트롤아노") 
    if message.content == "아노씨":
        await message.channel.send("@트롤아노")    

    if message.content == "엠제이야":
        await message.channel.send("@엠제이")
    if message.content == "엠제이":
        await message.channel.send("@엠제이")  
    if message.content == "앰제이야":
        await message.channel.send("@엠제이")  
    if message.content == "앰제이":
        await message.channel.send("@엠제이")   
    if message.content == "제이야":
        await message.channel.send("@엠제이")
    if message.content == "앰제이씨":
        await message.channel.send("@엠제이")
    if message.content == "엠제이씨":
        await message.channel.send("@엠제이")
    if message.content == "제이씨":
        await message.channel.send("@엠제이")            

    if message.content == "밍찡아":
        await message.channel.send("@밍찡이")
    if message.content == "밍밍찡아":
        await message.channel.send("@밍찡이")
    if message.content == "밍밍찡":
        await message.channel.send("@밍찡이")      
    if message.content == "밍밍찡씨":
        await message.channel.send("@밍찡이")             
    if message.content == "밍찡씨":
        await message.channel.send("@밍찡이")   



    #임베드

    if message.content == "/임베드 도개미":
            embed = discord.Embed(title="도개미", description="도개미", color=0x42c5fa) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="커맨드", value="쫌한다", inline=True)
            embed.set_footer(text="레드스톤 회로도 쫌 함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            embed.set_footer(text="야생도 쫌 함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
            
    if message.content == "/임베드 아노":
            embed = discord.Embed(title="아노", description="아노", color=0x000000) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="트롤", value="개잘한다", inline=True)
            embed.set_footer(text="맞춤법 틀리기도 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 트롤아노":
            embed = discord.Embed(title="아노", description="아노", color=0x000000) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="트롤", value="개잘한다", inline=True)
            embed.set_footer(text="맞춤법 틀리기도 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 아노트롤":
            embed = discord.Embed(title="아노", description="아노", color=0x000000) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="트롤", value="개잘한다", inline=True)
            embed.set_footer(text="맞춤법 틀리기도 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.                
            
    if message.content == "/임베드 앰제이":
            embed = discord.Embed(title="앰제이", description="앰제이", color=0xffa500) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="커맨드도 좀함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 엠제이":
            embed = discord.Embed(title="앰제이", description="앰제이", color=0xffa500) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="커맨드도 좀함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 MJ":
            embed = discord.Embed(title="앰제이", description="앰제이", color=0xffa500) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="커맨드도 좀함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 mj":
            embed = discord.Embed(title="앰제이", description="앰제이", color=0xffa500) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="커맨드도 좀함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
            
    if message.content == "/임베드 밍찡이":
            embed = discord.Embed(title="밍찡이", description="밍찡이", color=0xbada55) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="야생 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    if message.content == "/임베드 밍밍찡":
            embed = discord.Embed(title="밍찡이", description="밍찡이", color=0xbada55) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="야생 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.    
    if message.content == "/임베드 밍밍찡이":
            embed = discord.Embed(title="밍찡이", description="밍찡이", color=0xbada55) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="건축", value="잘한다", inline=True)
            embed.set_footer(text="야생 잘함") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.        
            
    if message.content == "/임베드":
            embed = discord.Embed(title="embed", description="사과", color=0xff0000) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
            embed.add_field(name="code", value="뭐요", inline=True)
            embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다
            await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
            await message.channel.send("", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
            
client.run(token)
