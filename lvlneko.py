import discord
from discord.ext import commands
import random
import json

bot = commands.Bot(command_prefix='_')
bot.remove_command('help')

@bot.event
async def on_ready():
    bet = discord.Game(name='2.1.7 [BETA]', type=2)
    await bot.change_presence(status=discord.Status.idle,activity=bet)
    print('стартовала функция уровня!')

@bot.event
async def on_message(message):
    with open('data/lvl.json', 'r') as f:
            h1 = json.load(f)
    aut = message.author.id
    ex = random.randint(1,20)
    if not str(message.author.id) in h1:
        h1[str(message.author.id)] = {}
        h1[str(message.author.id)]['lvl'] = 0
        h1[str(message.author.id)]['exp'] = 0
        h1[str(message.author.id)]['expmax'] = 100
        h1[str(message.author.id)]['lvlstage'] = 0
    lvl = h1[str(message.author.id)]['lvl']

    if h1[str(message.author.id)]['lvlstage'] == 0:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 100:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 100
        if h1[str(message.author.id)]['lvl'] == 10:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 150

    
    if h1[str(message.author.id)]['lvlstage'] == 1:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 150:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 150
        if h1[str(message.author.id)]['lvl'] == 20:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 200
    
    if h1[str(message.author.id)]['lvlstage'] == 2:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 200:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 200
        if h1[str(message.author.id)]['lvl'] == 30:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 250
    
    if h1[str(message.author.id)]['lvlstage'] == 3:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 250:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 250
        if h1[str(message.author.id)]['lvl'] == 40:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 300

    if h1[str(message.author.id)]['lvlstage'] == 4:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 300:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 300
        if h1[str(message.author.id)]['lvl'] == 50:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 500
    
    if h1[str(message.author.id)]['lvlstage'] == 5:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 500:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 500
        if h1[str(message.author.id)]['lvl'] == 60:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 750
 
    if h1[str(message.author.id)]['lvlstage'] == 6:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 750:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 750
        if h1[str(message.author.id)]['lvl'] == 70:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 1000
        
    if h1[str(message.author.id)]['lvlstage'] == 7:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 1000:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 1000
        if h1[str(message.author.id)]['lvl'] == 80:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 2000

    if h1[str(message.author.id)]['lvlstage'] == 8:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 2000:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 1000
        if h1[str(message.author.id)]['lvl'] == 90:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 5000
    
    if h1[str(message.author.id)]['lvlstage'] == 9:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 5000:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 1000
        if h1[str(message.author.id)]['lvl'] == 100:
            h1[str(message.author.id)]['lvlstage'] += 1
            h1[str(message.author.id)]['expmax'] = 7500

    if h1[str(message.author.id)]['lvlstage'] == 10:
        h1[str(message.author.id)]['exp'] += ex
        if h1[str(message.author.id)]['exp'] >= 10000:
            h1[str(message.author.id)]['lvl'] += 1
            await message.channel.send(f'{message.author.name} повысил уровень до {lvl + 1}')
            h1[str(message.author.id)]['exp'] -= 10000
    with open('data/lvl.json', 'w') as f:
        json.dump(h1,f, indent=4)

@bot.event
async def on_command_error(ctx,error):
    pass

r_token = open('token.txt', 'r')
rt = r_token.read()
bot.run(f'{rt}')