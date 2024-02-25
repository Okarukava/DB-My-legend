import os
import discord
from discord.ext import commands
from discord.ui import Select, Button, View
import pickle
import json
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.getenv("GUILD_ID"))])

pathDataBase = {
    "faction" : [
        {"voeniy" : [
            {"name" : "Военные"},
            {"path" : [
                
            ]}
            ]},
        {"svoboda" : [
            {"name" : "Свобода"},
            {"path" : [
                
            ]}
            ]},
        {"dolg" : [
            {"name" : "Долг"},
            {"path" : [
                
            ]}
            ]},
        {"naemnik" : [
            {"name" : "Наемники"},
            {"path" : [
                
            ]}
            ]},
        {"bandit" : [
            {"name" : "Бандиты"},
            {"path" : [
                
            ]}
            ]},
        {"monolit" : [
            {"name" : "Монолит"},
            {"path" : [
                
            ]}
            ]}
    ]
} #База данных, с адресами замены
if os.path.exists("pathDataBase.pkl"):
    with open("pathDataBase.pkl", "rb") as file:
        pathDataBase = pickle.load(file)

test = ["Свобода", "Долг", "Наемники"]
    

@bot.command()
async def button(ctx: discord.ApplicationContext):
    ecodButton = Button(label="Test button", style = discord.ButtonStyle.green)

#    async def cardCallback(interaction: discord.Interaction):
#        await interaction.response. kadabra()

    buttonManager = View(ecodButton)
    ecodButton.callback = kadabra

    await ctx.respond("Проверка работоспособности", view=buttonManager)

async def kadabra(
    ctx: discord.ApplicationContext, 
    faction: discord.Option(
        str,
        choice = ["Военные"],
        name = "группировка",
        description = "Выберете группировку, которой необходимо добавить данные",
        ),
    path: discord.Option(
        str,
        choice = ["Свобода", "Долг", "Наемники"],
        name = "путь_до_файла",
        description = r"Напишите путь до файла с данными группировки. Пример: C:\Users\User\Document...main.py"
        )
    ):
    print("TETSTTSTETSET")
    pass

@bot.command()
@commands.cooldown(2, 8)
async def add_path(
    ctx: discord.ApplicationContext, 
    faction: discord.Option(
        str,
        autocomplete = test,
        name = "группировка",
        description = "Выберете группировку, которой необходимо добавить данные",
        ),
    path: discord.Option(
        str,
        name = "путь_до_файла",
        description = r"Напишите путь до файла с данными группировки. Пример: C:\Users\User\Document...main.py"
        )
    ):
    print("Была вызвана команда -add_path-")
    if faction is not None and path is not None:
        if faction == "Военные":
            pathDataBase["voeniy"][1]["path"] = None
            pathDataBase["voeniy"][1]["path"] = path
        elif faction == "Свобода":
            pathDataBase["svoboda"][1]["path"] = None
            pathDataBase["svoboda"][1]["path"] = path
        elif faction == "Долг":
            pathDataBase["dolg"][1]["path"] = None
            pathDataBase["dolg"][1]["path"] = path
        elif faction == "Наемники":
            pathDataBase["naemnik"][1]["path"] = None
            pathDataBase["naemnik"][1]["path"] = path
        elif faction == "Бандиты": 
            pathDataBase["bandit"][1]["path"] = None
            pathDataBase["bandit"][1]["path"] = path
        elif faction == "Монолит":
            pathDataBase["monolit"][1]["path"] = None
            pathDataBase["monolit"][1]["path"] = path
        else:
            print ("The command -add_path- does not work...")
        print(f"Группировке: {faction} были добавлены данные по пути: {path}")
        await ctx.respond(f"Группировке: {faction} были добавлены данные по пути: {path}")
    else:
        print("Действие команды -add_path- отменено в связи с отсутствием необходимых данных")
        await ctx.respond("Действие команды отменено в связи с отсутствием необходимых данных")

@bot.command()
@commands.cooldown(2, 8)
async def check_path(
    ctx: discord.ApplicationContext, 
    faction: discord.Option(
        str,
        autocomplete = test,
        #["Военные", "Свобода", "Долг", "Наемники", "Бандиты", "Монолит",]
        name = "группировка",
        description = "Выберете группировку у которой необходимо проверить данные",
        ),
    ):
    print("Была вызвана команда -check_path-")
    if faction == "Военные":
        print (("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["voeniy"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["voeniy"][1]["path"]))
    elif faction == "Свобода":
        print (("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["svoboda"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["svoboda"][1]["path"]))
    elif faction == "Долг":
        print (("анные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["dolg"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["dolg"][1]["path"]))
    elif faction == "Наемники":
        print (("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["naemnik"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["naemnik"][1]["path"]))
    elif faction == "Бандиты":
        print (("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["bandit"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["bandit"][1]["path"]))
    elif faction == "Монолит":
        print (("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["monolit"][1]["path"])))
        await ctx.respond("Данные группировки {f} находятся по следующему пути {p}".format(f = faction, p = pathDataBase["monolit"][1]["path"]))
    else:
        print ("The command -check_path- does not work...")

@bot.command()
@commands.cooldown(2, 8)
async def delete_path(
    ctx: discord.ApplicationContext, 
    faction: discord.Option(
        str,
        autocomplete = test,
        name = "группировка",
        description = "Выберете группировку, которой необходимо удалить данные",
        ),
    verification: discord.Option(
        str,
        choices = ["Нет", "Да"],
        name = "подтверждение",
        description = "Подтвердите сделанный вами выбор",
        ),
    ):
    print("Была вызвана команда -delete_path-")
    if verification == "Да":

        if faction == "Военные":
            pathDataBase["voeniy"][1]["path"] = None
        elif faction == "Свобода":
            pathDataBase["svoboda"][1]["path"] = None
        elif faction == "Долг":
            pathDataBase["dolg"][1]["path"] = None
        elif faction == "Наемники":
            pathDataBase["naemnik"][1]["path"] = None
        elif faction == "Бандиты": 
            pathDataBase["bandit"][1]["path"] = None
        elif faction == "Монолит":
            pathDataBase["monolit"][1]["path"] = None

        print (f"Данные группировки {faction} были удалены")
        await ctx.respond(f"Данные группировки {faction} были удалены")
    elif verification == "Нет":
        print ("Команда -delete_path- была отменена")
        await ctx.respond("Команда была отменена")
    else:
        print ("The command -delete_path- does not work...")

@bot.command()
@commands.cooldown(1, 120)
async def update_economy(ctx: discord.ApplicationContext):
    print("Была вызвана команда -update_economy-")
    oldPricePath = os.getenv(f"PRICE_PATH")#
    #Функция перезаписи
    def updatePriceeData(newPricePath, oldPricePath):
        with open(newPricePath, "r") as new_price, open(oldPricePath, "w")  as old_price:
            old_price.write(new_price.read())
    #Функция определения лидера по очкам
    flag_value = os.getenv(r"FLAG_VALUE_PATH")
    with open(flag_value, 'r', encoding='utf-8') as file:
        data = json.load(file)
    max_score = 0
    for i in range(len(data["scores"])):
        score = data["scores"][i]["total"]
        if max_score < score:
            max_score = score
            counter_leader = data["scores"][i]["flag"].lower()[8:]
    for i in pathDataBase.keys():
        if i == counter_leader:
            if pathDataBase[counter_leader][1]["path"] is not None:
                updatePriceeData(pathDataBase[counter_leader][1]["path"], oldPricePath)
                print("Старые данные изменены на новые в соответствии с текущим лидером: {leader}".format(leader=pathDataBase[counter_leader][0]["name"]))
                await ctx.respond("Старые данные изменены на новые в соответствии с текущим лидером: {leader}".format(leader=pathDataBase[counter_leader][0]["name"]))
            else:
                print("Старые данные небыли скорректированны в связи с тем, что лидирующей группировке {leader} не назначены данные".format(leader=pathDataBase[counter_leader][0]["name"]))
                await ctx.respond("Старые данные небыли скорректированны в связи с тем, что лидирующей группировке {leader} не назначены данные".format(leader=pathDataBase[counter_leader][0]["name"]))

#Обработчик подключений бота
@bot.event
async def on_ready():
    print("Bot for flag Economy is ready...")
"""
@bot.event
async def on_connect():
    print("Bot connect for discord server...")
@bot.event
async def on_error():
    print("Bot have error...")
@bot.event
async def on_disconnect():
    print("Bot has not have connect for discord server...")
@bot.event
async def on_resumed():
    print("Bot reconnect for discord server...")
"""
#Обработчики ошибок
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"Комманда находится на перезарядке. Попробуйте через {error.retry_after, 2} секунд")
    else:
        raise error

#Включение бота и запись данных
try:
    #if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
finally:
    print("Bot for flag Economy deactivated...")
    with open("pathDataBase.pkl", "wb") as file:
        pickle.dump(pathDataBase, file, pickle.HIGHEST_PROTOCOL)