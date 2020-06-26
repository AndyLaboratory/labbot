import discord
import asyncio
import os

app = discord.Client()



token = os.environ["BOT_TOKEN"]



@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    #messages = ['호스팅에 심각한 오류가 발견되어서 봇이 온라인이여도 명령어는 이용하실 수 없습니다', '명령어 이용 불가', '점검 중']
    messages = [f'{len(app.guilds)}개의 서버에 참여중', '도움말 : 랩 도움말', f'{len(app.users)}명의 유저가 사용함', '봇의 접두사는 랩 입니다', f'{len(app.guilds)}개의 서버와 {len(app.users)}명의 유저와 함께합니다!']
    while True:
        await app.change_presence(status=discord.Status.online,activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(3)

    
@app.event
async def on_message(message):
    msg = message.author
    if message.author.bot:
        return None
#1 도움말
    if message.content == "랩 개발자":
        await message.channel.send("랩ㅣAndyLab#7498")
    if message.content == "랩 도움말":
        helpembed=discord.Embed(color=0x00f1ff, title='도움말', description="도움말입니다.", timestamp=message.created_at)
        helpembed.add_field(name="랩 유저정보", value="명령어를 친 유저의 정보를 확인합니다.", inline=False)
        helpembed.add_field(name="랩 초대", value="봇 초대 링크를 확인합니다.", inline=False)
        helpembed.add_field(name="랩 개발자", value="봇 개발자를 확인합니다.", inline=False)
        helpembed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=helpembed)
    # CHANGED-2   if message.content == "!유저정보":
        #embed=discord.Embed(color=0xff00, title=f'{msg.name}님의 정보', description=f'이름:{msg.name}\n태그:{msg}id:{msg.id}\n계정 만든 일:{msg.created_at}\n서버 참가 일:{msg.joined_at}가장 높은 역할:{msg.roles["name"]}', timestamp=message.created_at)
        #embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        #await message.channel.send(embed=embed)
#2 유저 정보 표시
    if message.content == "랩 유저정보":
        userinfoembed=discord.Embed(color=0x00f1ff, title=f'{msg.name}님의 정보', description=f'{msg.name}님의 정보입니다.', timestamp=message.created_at)
        userinfoembed.add_field(name='이름', value=f'{msg}', inline=False)
        userinfoembed.add_field(name='계정 생성일', value=f'{msg.created_at}', inline=False)
        userinfoembed.add_field(name='서버 참가일', value=f'{msg.joined_at}', inline=False)
        userinfoembed.add_field(name='가장 높은 역할', value=f'<@&{msg.top_role.id}>', inline=False)
        userinfoembed.add_field(name='id', value=f'{msg.id}', inline=False)
        userstatus = str(f'{msg.status}')
        if str(userstatus) == "dnd":
            stok = "<:dnd:705595487163514890> 다른 용무 중"
        if str(userstatus) == "idle":
            stok = "<:Idle:705595487218302996> 자리비움"
        if str(userstatus) == "online":
            stok = "<:online:705595486932959323>  온라인"
        if str(userstatus) == "streaming":
            stok = "<:streaming:705595487155257364>  방송중"
        if str(userstatus) == "offline":
            stok = "<:offline:705595487176228914> 오프라인"
        userinfoembed.add_field(name='상태', value= stok, inline=False)
        userinfoembed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=userinfoembed)
#3 봇 초대
    if message.content == "랩 초대":
        botplus=discord.Embed(color=0x00f1ff, title='', description='[초대하기](https://discord.com/api/oauth2/authorize?client_id=711817927103479898&permissions=8&scope=bot)')
        await message.channel.send(embed=botplus)
        print(f'{msg}가 봇 초대링크를 받음.')


app.run(token)
