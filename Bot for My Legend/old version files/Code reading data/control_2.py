import re
import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

path = "C:/Users/BAZA PC/Desktop/Clear Sky профайлс работа/profiles/HillKing/Scores.json"

with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)

@bot.event
async def on_message(message):
    if message.content.startswith('!'):
        #свобода
        if message.channel.id == 1156308334564085781:
            i = json.dumps(data)
            result = re.findall(r'XZone_flag_Svobida..\s.total..\s\d{1,}', i)
            await bot.get_channel(1156308334564085781).send((result))
        #долг
        if message.channel.id == 1156306433323839570:
            i = json.dumps(data)
            result = re.findall(r'XZone_flag_Dolg1..\s.total..\s\d{1,}', i)
            await bot.get_channel(1156306433323839570).send((result))
        #наймы
        if message.channel.id == 1172643705061113918:
            i = json.dumps(data)
            result = re.findall(r'XZone_flag_Naimi..\s.total..\s\d{1,}', i)
            await bot.get_channel(1172643705061113918).send((result))
        #бандиты
        if message.channel.id == 1169715804535791721:
            i = json.dumps(data)
            result = re.findall(r'Flag_Pirates..\s.total..\s\d{1,}', i)
            await bot.get_channel(1169715804535791721).send((result))
        #оксоп
        if message.channel.id == 1156305722817118279:
            i = json.dumps(data)
            result = re.findall(r'XZone_flag_SOP1..\s.total..\s\d{1,}', i)
            await bot.get_channel(1156305722817118279).send((result))
        else: await bot.get_channel(1013757215141801995).send()

input("Press Enter to exit...")

bot.run('---')

