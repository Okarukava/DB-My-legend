import json

#Пути для основного и замещаемого документа
path_main = r"C:\Users\Okarukava\Desktop\Bot for My Legend\testing\price_list.json"
path_replace = r"C:\Users\Okarukava\Desktop\Bot for My Legend\testing\dolg_price.json"
#Запись данных в переменную
with open(path_main, 'r', encoding='utf-8') as file:
    price_main = json.load(file)
with open(path_replace, 'r', encoding='utf-8') as file:
    price_replace = json.load(file)
#Поиндексное пределение данных, которые необходимо удалить
removeIndex = []
for i in range(len(price_main["TraderCategories"])):
    if "долг" in price_main["TraderCategories"][i]["CategoryName"].lower():
        removeIndex.append(i)
#Поиндексное удаление данных
removeIndex.reverse()
for i in range(len(removeIndex)):
    price_main["TraderCategories"].pop(removeIndex[i])
#Поиндексное добавление данных в основную переменную
for i in range(len(price_replace["TraderCategories"])):
    if "долг" in price_replace["TraderCategories"][i]["CategoryName"].lower():
        price_main["TraderCategories"].append(price_replace["TraderCategories"][i])
    else:
        print("ПОШЕЛ НАХУЙ! -{error}- НЕПРАВИЛЬНАЯ КАТЕГОРИЯ!!!!".format(error = price_replace["TraderCategories"][i]["CategoryName"].lower()))
#Запись данных в основной документ
with open(path_main, 'w', encoding='utf-8') as file:
    json.dump(price_main, file, indent=4, ensure_ascii=False,)