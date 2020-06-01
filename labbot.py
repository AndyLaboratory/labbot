import discord
import asyncio
import os

app = discord.Client()
onoff = os.environ["ON_OR_OFF"]

token = os.environ["BOT_TOKEN"]



@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    messages = ['호스팅에 심각한 오류가 발견되어서 봇이 온라인이여도 명령어는 이용하실 수 없습니다', '명령어 이용 불가', '점검 중']
    #messages = [f'{len(app.guilds)}개의 서버에 참여중', '도움말 : 랩 도움말', f'{len(app.users)}명의 유저가 사용함', '봇의 접두사는 랩 입니다', f'{len(app.guilds)}개의 서버와 {len(app.users)}명의 유저와 함께합니다!']
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
    if message.content == "랩 도움말":
        helpembed=discord.Embed(color=0x00f1ff, title='도움말', description="도움말입니다.", timestamp=message.created_at)
        helpembed.add_field(name="랩 유저정보", value="명령어를 친 유저의 정보를 확인합니다.", inline=False)
        helpembed.add_field(name="랩 초대", value="봇 초대 링크를 확인합니다.", inline=False)
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
#4 SCP
    if message.content == "랩 SCP 실험종료":
        if message.author.id == 604927195772878878:
            scpembed=discord.Embed(color=0x00f1ff, title='실험 안내', description='실험이 종료 되었습니다.')
            scpembed.add_field(name='실험 종료됨', value='재단 설립자가 실험을 종료하였습니다.', inline=False)
            scpembed.set_footer(text='재단설립자', icon_url=message.author.avatar_url)
            await message.channel.send(embed=scpembed)
    if message.content == "랩 SCP 실험시작":
        if message.author.id == 604927195772878878:
            scpembed=discord.Embed(color=0x00f1ff, title='실험 안내', description='실험이 시작 되었습니다.')
            scpembed.add_field(name='실험 시작됨', value='재단 설립자가 실험을 시작하였습니다.', inline=False)
            scpembed.set_footer(text='재단설립자', icon_url=message.author.avatar_url)
            await message.channel.send(embed=scpembed)
    if message.content == "랩 SCP 연구허가":
        print('check')
        print(f'{msg.id}')
        print(message.author.id)
        userid = message.author.id
        print(userid)
        if message.author.id == 604927195772878878:
            print('check22')
            scpembed=discord.Embed(color=0x00f1ff, title='연구허가서 안내', description='연구가 허가 되었습니다.')
            scpembed.add_field(name='연구 허가됨', value='재단 설립자가 실험을 허가 하였습니다.', inline=False)
            scpembed.set_footer(text='재단설립자', icon_url=message.author.avatar_url)
            await message.channel.send(embed=scpembed)'''
    if(message.content.split(" ")[0] == "랩"): 
#SCP 구문들
        if(message.content.split(" ")[1] == "SCP"):
            if(message.content.split(" ")[2] == "실험허가"):
                if(message.author.id == 604927195772878878):
                    user = message.guild.get_member(int(message.content.split(' ')[3] [3:21]))
                    scpembed=discord.Embed(color=0x00f1ff, title='연구허가서 안내', description=f'{user.mention}님의 연구 허가됨')
                    scpembed.add_field(name='연구 허가됨', value='재단 설립자가 실험을 허가 하였습니다.', inline=False)
                    scpembed.set_footer(text='재단설립자', icon_url=message.author.avatar_url)
                    await message.channel.send(embed=scpembed)
    
@app.event
async def on_message(message):
    msg : message.content
                    

        if(message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="킥", description = f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```', color = 0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="킥 성공", description = f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```", color = 0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.", color = 0xff0000))
            return


#TESTING

@commandapp.command(name="유저정보", pass_context=True)
async def 유저정보(ctx, user_name: discord.Member):
    print(user_name)
    if int(user_name.bot) == False:
        botok = "X"
    else:
        botok = "O"
    if str(user_name.status) == "dnd":
        stok = ":dnd: 다른 용무 중"
   if str(user_name.status) == "idle":
        stok = ":Idle: 자리비움"
    if str(user_name.status) == "online":
        stok = ":online: 온라인"
    if str(user_name.status) == "streaming":
        stok = ":streaming: 방송중"
    if str(user_name.status) == "offline":
        stok = ":offline: 오프라인"

    roles = [role for role in user_name.roles]
    date = datetime.datetime.utcfromtimestamp(((int(user_name.id) >> 22) + 1420070400000) / 1000)
    now = datetime.datetime.now()
    embed = discord.Embed(color=0x7CC8FF, description="닉네임 : {}\n현재 서버 닉네임 : {}\n아이디 : {}\n디스코드 가입일 : {}\n봇 : {}\n높은 역활 : <@&{}>\n상태 : {}".format(user_name, user_name.display_name, user_name.id, str(date.year) + "년도" + str(date.month) + "월" + str(date.day) + "일", botok, user_name.top_role.id, str(stok)))
    embed.set_thumbnail(url=user_name.avatar_url)
    await ctx.send(embed=embed)
    embed = discord.Embed(color=0x7CC8FF)
    embed.add_field(name="역활({}개)".format(len(user_name.roles) - 1), value=" ".join([role.mention for role in roles]), inline=True)
    await ctx.send(embed=embed)
'''
if onoff is "ON":
    app.run(token)

