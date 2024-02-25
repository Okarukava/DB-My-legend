import json

path = r"C:\Users\Okarukava\Desktop\Bot for My Legend\Code reading data\Scores_1.json"
with open(path, 'r', encoding='utf-8') as file:
    data = json.load(file)

#Свобода, Бандиты, Монолит, Долг, Военные, Наемники.

max_score = 0

for i in range(len(data["scores"])):
    score = data["scores"][i]["total"]
    #print (data["scores"][i]["total"])

    if max_score < score:
        max_score = score
        counter_leader = data["scores"][i]["flag"].lower()[8:]
#print (counter_leader)

if counter_leader == "svoboda":
    print ("Свобода")
elif counter_leader == "bandit":
    print ("Бандит")
elif counter_leader == "monolit":
    print ("Монолит")
elif counter_leader == "dolg":
    print ("Долг")
elif counter_leader == "voeniy":
    print ("Военные")
elif counter_leader == "naemnik":
    print ("Наемники")
else:
    print ("КАСЯК!!!!")

