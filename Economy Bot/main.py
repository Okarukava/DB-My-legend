#python -m venv .venv
#.venv/Scripts/activate
#Импорт модулей и библиотек
import discord
from discord.ext import commands
from discord.ui import Select, Button, View
import os, logging, datetime, time 
import json, pickle
from dotenv import load_dotenv
load_dotenv()

#Logging
if os.path.isdir("logs"):
    pass
else:
    os.mkdir("logs")

logging.basicConfig(
    level=logging.INFO, 
    filename = str("logs/" + (time.strftime("""%d.%m.%Y_%H%M%S""", (time.localtime()))) + " logs.log"), 
    encoding = "utf-8",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
    datefmt='%H:%M:%S',
    )

#Инициализация бота, список разрешений
bot = discord.Bot(debug_guilds=[int(os.getenv("GUILD_ID"))])
logging.info("Bot is initialize")


#Инициализация баз данных
economyPathDataBase = {
    "Traiders" : []
}
if os.path.exists("economyPathDataBase.pkl"):
    with open("economyPathDataBase.pkl", "rb") as file:
        economyPathDataBase = pickle.load(file)
        logging.info("economyPathDataBase.pkl is open")

#Autocomplete функции команд
async def autovomplete_categoty_value(ctx:discord.AutocompleteContext):
    categoty_value = []
    for i in range(len(economyPathDataBase["Traiders"])):
        for k in economyPathDataBase["Traiders"][i].keys():
            categoty_value.append(k)
    if not categoty_value:
        return False
    else:
        return categoty_value

#Прочие функции
#Отсутствуют

#Список команд и логика
@bot.command(description="Добавить новую категорию данных")
@commands.cooldown(2, 8)
async def add_category(
    ctx: discord.ApplicationContext, 
    category_name:discord.Option(
            str,
            name = "название_категории",
            description = "Введите наименование категории на русском языке. Используется для поиска категорий"
        ),
    category_key:discord.Option(
            str,
            name = "ключ-значение",
            description = "Введите ключ-значение категории на английском языке. Используется в качестве переменных"
        ),
    check_verification:discord.Option(
            str,
            name = "подтверждение",
            choices = ["Нет", "Да"],
            description = "Подтвердите ваши действия. Да, Нет"
        )
    ):
    logging.info("{author}вызвал комманду -add_category-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -add_category-")
    if check_verification == "Да":
        economyPathDataBase["Traiders"].append({category_name.capitalize():[{"key":category_key.lower()},{"path":[]}]})
        logging.info((f"Добавлена категория {category_name.capitalize()} с ключом {category_key.lower()}"))
        print(f"Добавлена категория {category_name.capitalize()} с ключом {category_key.lower()}")
        await ctx.respond(f"Добавлена категория ** *{category_name.capitalize()}* ** с ключом ** *{category_key.lower()}* **")
    else:
        logging.info(("Выполнение команды -add_category- отменено"))
        print("Выполнение команды -add_category- отменено")
        await ctx.respond("Выполнение команды ** *-add_category-* ** отменено")

@bot.command()
@commands.cooldown(2, 8)
async def add_variand_and_path(
    ctx: discord.ApplicationContext,
    category_name:discord.Option(
            str,
            name = "название_категории",
            autocomplete = autovomplete_categoty_value,
            description = "Выберете категорию, который вы хотите добавить вариант выбора"
        ), 
    variant_name:discord.Option(
            str,
            name = "название_варианта",
            description = "Введите наименование варианта"
        ),
    path:discord.Option(
            str,
            name = "путь",
            description = "Введите путь до указанного варианта"
        ),
    check_verification:discord.Option(
            str,
            name = "подтверждение",
            choices = ["Нет", "Да"],
            description = "Подтвердите ваши действия. Да, Нет"
        ), 
    ):
    logging.info("{author}вызвал комманду -add_variand_and_path-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -add_variand_and_path-")
    if check_verification == "Да":
        for i in range(len(economyPathDataBase["Traiders"])):
            for key_category in economyPathDataBase["Traiders"][i].keys():
                if category_name == key_category:
                    economyPathDataBase["Traiders"][i][key_category][1]["path"].append({variant_name:path})
                    break
            else:
                continue
            break
        logging.info(f"В категорию {category_name} добавлен вариант {variant_name} расположенный по пути {path}")
        print(f"В категорию {category_name} добавлен вариант {variant_name} расположенный по пути {path}")
        await ctx.respond(f"В категорию ** *{category_name}* ** добавлен вариант ** *{variant_name}* ** расположенный по пути ** *{path}* **")
    else:
        logging.info("Выполнение команды -add_variand_and_path- отменено")
        print("Выполнение команды -add_variand_and_path- отменено")
        await ctx.respond("Выполнение команды ** *-add_variand_and_path-* ** отменено")

@bot.command()
@commands.cooldown(1, 10)
async def check_category(ctx: discord.ApplicationContext):
    logging.info("{author}вызвал комманду -check_category-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -check_category-")

    categoty_embed = discord.Embed(title="Категории и варианты выбора",color = 0xf5d120)
    categoty_embed.set_author(name=os.getenv("AUTHOR_MESSAGE"), icon_url=os.getenv("AUTOR_IMAGE_URL"))
    #categoty_embed.set_thumbnail(url=os.getenv("AUTOR_IMAGE_URL"))

    for i in range(len(economyPathDataBase["Traiders"])):
        for key_category in economyPathDataBase["Traiders"][i].keys():
            category_key = economyPathDataBase["Traiders"][i][key_category][0]["key"]
            categoty_embed.add_field(name=key_category,value=f"В категории **{key_category}** с ключом **{category_key}** вам доступны следующие варианты выбора:", inline=False)
            for j in range(len(economyPathDataBase["Traiders"][i][key_category][1]["path"])):
                for key_variant in economyPathDataBase["Traiders"][i][key_category][1]["path"][j].keys():
                    categoty_embed.add_field(
                        name=f"*{key_variant}*",
                        value="Который находится по пути ||*{path_variant}*||".format(path_variant=economyPathDataBase["Traiders"][i][key_category][1]["path"][j].setdefault(key_variant, None)), 
                        inline=True
                    )
    logging.info("Доступны следующие категории {economyPathDataBase}".format(economyPathDataBase = economyPathDataBase["Traiders"]))
    print("Доступны следующие категории ", economyPathDataBase["Traiders"])
    await ctx.respond(embed=categoty_embed)

@bot.command()
@commands.cooldown(2, 8)
async def delete_category(
    ctx: discord.ApplicationContext,
    category_name:discord.Option(
            str,
            name = "название_категории",
            autocomplete = autovomplete_categoty_value,
            description = "Выберете категорию, которую вы хотите удалить"
        ),
    check_verification:discord.Option(
            str,
            name = "подтверждение",
            choices = ["Нет", "Да"],
            description = "Подтвердите ваши действия. Да, Нет"
        )
    ):
    logging.info("{author}вызвал комманду -delete_category-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -delete_category-")
    if check_verification == "Да":
        delete_index = None
        for i in range(len(economyPathDataBase["Traiders"])):
            for key_category in economyPathDataBase["Traiders"][i].keys():
                if category_name == key_category:
                    delete_index = i
                    break
            else:
                continue
            break
        if delete_index is not None:
            logging.info(f"Категория {category_name} удалена")
            print(f"Категория {category_name} удалена")
            await ctx.respond(f"Категория ** *{category_name}* ** удалена")
            economyPathDataBase["Traiders"].pop(delete_index)
    else:
        logging.info("Выполнение команды -delete_category- отменено")
        print("Выполнение команды -delete_category- отменено")
        await ctx.respond("Выполнение команды ** *-delete_category-* ** отменено")

@bot.command()
@commands.cooldown(2, 8)
async def delete_variant_and_path(
    ctx: discord.ApplicationContext,
    category_name:discord.Option(
            str,
            name = "название_категории",
            autocomplete = autovomplete_categoty_value,
            description = "Выберете категори из которой вы хотите удалить вариант выбора"
        ),
    variant_name:discord.Option(
            str,
            name = "название_варианта",
            description = "Введите наименование варианта который вы хотите удалить"
        ),
    check_verification:discord.Option(
            str,
            name = "подтверждение",
            choices = ["Нет", "Да"],
            description = "Подтвердите ваши действия. Да, Нет"
        )
    ):
    logging.info("{author}вызвал комманду -delete_variant_and_path-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -delete_variant_and_path-")
    if check_verification == "Да":
        category_index = None
        delete_index = None
        for i in range(len(economyPathDataBase["Traiders"])):
            for key_category in economyPathDataBase["Traiders"][i].keys():
                if category_name == key_category:
                    for j in range(len(economyPathDataBase["Traiders"][i][key_category][1]["path"])):
                        for key_variant in economyPathDataBase["Traiders"][i][key_category][1]["path"][j].keys():
                            if key_variant == variant_name:
                                category_index = i
                                delete_index = j
                                break
                        else:
                            continue
                        break
                break
            else:
                continue
            break
        if category_index is not None and delete_index is not None:
            logging.info(f"Из категории {category_name} был удален следующий вариант выбора: {variant_name}")
            print(f"Из категории {category_name} был удален следующий вариант выбора: {variant_name}")
            await ctx.respond(f"Из категории ** *{category_name}* ** был удален следующий вариант выбора: ** *{variant_name}* **")
            economyPathDataBase["Traiders"][category_index][category_name][1]["path"].pop(delete_index)
    else:
        logging.info("Выполнение команды -delete_variant_and_path- отменено")
        print("Выполнение команды -delete_variant_and_path- отменено")
        await ctx.respond("Выполнение команды ** *-delete_variant_and_path-* ** отменено")

@bot.command()
@commands.cooldown(2, 8)
async def update_economy(
    ctx: discord.ApplicationContext,
    category_name:discord.Option(
            str,
            name = "название_категории",
            autocomplete = autovomplete_categoty_value,
            description = "Выберите категорию данные которой вы ходите заменить"
        ),
    variant_name:discord.Option(
            str,
            name = "название_варианта",
            description = "Введите наименование варианта на который вы хотите заменить данные"
        ),
    check_verification:discord.Option(
            str,
            name = "подтверждение",
            choices = ["Нет", "Да"],
            description = "Подтвердите ваши действия. Да, Нет"
        )
    ):
    logging.info("{author}вызвал комманду -update_economy-".format(author = ctx.author))
    print(ctx.author, "вызвал комманду -update_economy-")
    if check_verification == "Да":
        #Пути для основного и замещаемого документа
        path_main = str(os.getenv("PRICE_PATH"))
        path_replace = None
        logging.info(f"Назначен путь для замены данных: {path_main}")
        for i in range(len(economyPathDataBase["Traiders"])):
            for key_category in economyPathDataBase["Traiders"][i].keys():
                if category_name == key_category:
                    for j in range(len(economyPathDataBase["Traiders"][i][key_category][1]["path"])):
                        for key_variant in economyPathDataBase["Traiders"][i][key_category][1]["path"][j].keys():
                            if key_variant == variant_name:
                                path_replace = economyPathDataBase["Traiders"][i][key_category][1]["path"][j].setdefault(key_variant, None)
                                logging.info(f"Назначен путь с данными для замены: {path_replace}")
        if path_replace is not None:
            #Запись данных в переменную
            with open(path_main, 'r', encoding='utf-8') as file:
                price_main = json.load(file)
                logging.info(f"Открыт файл: {path_main}")
            with open(path_replace, 'r', encoding='utf-8') as file:
                price_replace = json.load(file)
                logging.info(f"Открыт файл: {path_replace}")
            #Поиндексное пределение данных, которые необходимо удалить
            removeIndex = []
            for i in range(len(price_main["TraderCategories"])):
                if category_name.lower() in price_main["TraderCategories"][i]["CategoryName"].lower():
                    removeIndex.append(i)
            #Поиндексное удаление данных
            removeIndex.reverse()
            for i in range(len(removeIndex)):
                price_main["TraderCategories"].pop(removeIndex[i])
            #Поиндексное добавление данных в основную переменную
            for i in range(len(price_replace["TraderCategories"])):
                if category_name.lower() in price_replace["TraderCategories"][i]["CategoryName"].lower():
                    price_main["TraderCategories"].append(price_replace["TraderCategories"][i])
                else:
                    logging.info("В настройках варианта {variant} присутствует неправильная категория -{error}-".format(variant = variant_name, error = price_replace["TraderCategories"][i]["CategoryName"].lower()))
                    print("В настройках варианта {variant} присутствует неправильная категория -{error}-".format(variant = variant_name, error = price_replace["TraderCategories"][i]["CategoryName"].lower()))
            #Запись данных в основной документ
            with open(path_main, 'w', encoding='utf-8') as file:
                json.dump(price_main, file, indent=4, ensure_ascii=False,)
                logging.info(f"Данные по следующему пути заменены и загружены: {path_main}")
            logging.info(f"Данные для категории {category_name} были изменены в соответствии с настройками варианта {variant_name}")
            print(f"Данные для категории {category_name} были изменены в соответствии с настройками варианта {variant_name}")
            await ctx.respond(f"Данные для категории ** *{category_name}* ** были изменены в соответствии с настройками варианта ** *{variant_name}* **")
        else:
            logging.info(f"Выполнение команды -update_economy- отменено в связи с тем, что указанной категории: -{variant_name}- не существует")
            print(f"Выполнение команды -update_economy- отменено в связи с тем, что указанной категории: -{variant_name}- не существует")
            await ctx.respond(f"Выполнение команды ** *-update_economy-* ** отменено в связи с тем, что *указанной категории: **{variant_name}** не существует*")
    else:
        logging.info("Выполнение команды -update_economy- отменено")
        print("Выполнение команды -update_economy- отменено")
        await ctx.respond("Выполнение команды ** *-update_economy-* ** отменено")

#Обработчик подключений бота
@bot.event
async def on_ready():
    logging.info("Economy bot is ready to work...")
    print("Economy bot is ready to work...")

#Обработчики ошибок
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(f"Комманда находится на перезарядке. Попробуйте через {error.retry_after, 2} секунд")
    else:
        raise error

#Включение бота и запись данных
try:
    if __name__ == "__main__":
        logging.info("Economy bot is runing")
        bot.run(os.getenv("TOKEN"))
finally:
    logging.info("Economy bot deactivated...")
    print("Economy bot deactivated...")
    with open("economyPathDataBase.pkl", "wb") as file:
        pickle.dump(economyPathDataBase, file, pickle.HIGHEST_PROTOCOL)