import os
import pickle

pathDataBase = {
    "Traiders" : [{"Военные":["test", "test", "test"]}]
} 

def test():
    one = str(input())
    two = str(input())
    pathDataBase["Traiders"].append({one:[{"name":two},{"path":[]}]})
    print(pathDataBase)

pathDataBase["Traiders"][0].pop("Военные")
print(pathDataBase)





{'Traiders': [
    {'Монолит': [
        {'key': 'mono'},
        {'path': [
            {'test1': 'test1'},
            {'test1': 'test1'},
            {'test1': 'test1'},
            {'test1': 'test1'},
            {'test1': 'test1'}
        ]
        }
    ]},
    {'Бандиты': [
        {'key': 'band'}, 
        {'path': [

        ]
        }
    ]}
    ]
}






"""
pathDataBase = dict()
pathDataBase["voeniy"] = [{"path":"afsafasfasf"}]
print(pathDataBase)
pathDataBase["voeniy"].append({"test":"testetsetsetse"})
print(pathDataBase)
#print(pathDataBase["voeniy"][1]["path"])

#"voeniy", "svoboda", "dolg", "naemnik", "bandit", "monolit"

pathDataBase = {
    "voeniy" : [{"name" : "Военные"},{"path" : "None"}],
    "svoboda" : [{"name" : "Свобода"},{"path" : "None"}],
    "dolg" : [{"name" : "Долг"},{"path" : "None"}],
    "naemnik" : [{"name" : "Наемники"},{"path" : "None"}],
    "bandit" : [{"name" : "Бандиты"},{"path" : "None"}],
    "monolit" : [{"name" : "Монолит"},{"path" : "None"}]
}
if os.path.exists("pathDataBase.pkl"):
    with open("pathDataBase.pkl", "rb") as file:
        pathDataBase = pickle.load(file)
print (pathDataBase.key)


pathDataBase = {
    "Traiders" : [
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
}
"""