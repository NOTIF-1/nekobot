import asyncio
import discord
from discord.ext import commands
import json
import random
import time
import subprocess

bot = commands.Bot(command_prefix='#')

bot.remove_command('help')
# ниже каманды бота

@bot.event
async def on_ready():
    bet = discord.Game(name='2.1.7 [BETA]', type=2)
    await bot.change_presence(status=discord.Status.idle,activity=bet)
    print(f'бот стартовал')
    time_now_id = 'GzrT.etgaREW.E234'
    l = subprocess.Popen("prstart.bat")
    #while True:
    #    with open('data/bm.json', 'r') as f:
    #        h1 = json.load(f)
    #    tm = str(time.strftime("%H:%M"))
    #    h1[time_now_id] = tm
    #    with open('bm.json', 'w') as f:
    #        json.dump(h1,f)
    #    await asyncio.sleep(1)

@bot.command()
async def help(ctx):
    await ctx.send(
        embed=discord.Embed(
            title='каманды бота',
            description=f'#help\n#job\n#rank\nадминские каманды\n#ban\n#mute',
            color=0xff0000
        )
    )

@bot.command()
async def job(ctx):
    with open('data/Money.json', 'r') as f:
        h1 = json.load(f)
    num_r = random.randint(1,10)
    if not str(ctx.author.id) in h1:
        h1[str(ctx.author.id)] = {}
        h1[str(ctx.author.id)]['Money'] = 0
    h1[str(ctx.author.id)]['Money'] += num_r
    await ctx.send(
        embed=discord.Embed(
            title='вы зароботали деньги!',
            description=f'ваш баланс сотовляет {h1[str(ctx.author.id)]["Money"]} + заработанные {num_r}💰',
            color=0xffd700
        )
    )
    with open('data/Money.json', 'w') as f:
        json.dump(h1,f, indent=2)

@bot.command()
async def ban(ctx, user:discord.Member, tim:int, *, reason:str):
    log = bot.get_channel(881467842061537350)
    ban = user.guild.get_role(881210136968958033)
    await log.send(f'пользователь {ctx.author.name} забанел пользователя: **{user.display_name}** по пирчине **{reason}** и на срок **{tim} минут**')
    await user.add_roles(ban)
    await asyncio.sleep(tim*60)
    await user.remove_roles(ban)
    await log.send(f'{user.display_name} был разбанен')

@bot.command()
async def mute(ctx, user:discord.Member, tim:int, *, reason):
    log = bot.get_channel(881467842061537350)
    mutes = user.guild.get_role(881209703802228856)
    await log.send(f'пользователь: {user.display_name} был замьютен на срок **{tim} минут** по причине: **{reason}**')
    await user.add_roles(mutes)
    await asyncio.sleep(tim*60)
    await user.remove_roles(mutes)
    await log.send(f'{user.display_name} был размучен так как срок мута вышел')

r_token = open('token.txt', 'r')
rt = r_token.read()

bot.run(f'{rt}')
