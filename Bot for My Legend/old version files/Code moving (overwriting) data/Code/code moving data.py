import os

newDataPath = r"C:\Users\Okarukava\Desktop\Bot for My Legend\Code moving (overwriting) data\File for read\Ipsum.txt"
oldDataPath = r"C:\Users\Okarukava\Desktop\Bot for My Legend\Code moving (overwriting) data\File for record\Record.txt"

#Функция перезаписи
def updateData(newDataPath, oldDataPath):
    with open(newDataPath, "r") as new_value, open(oldDataPath, "w")  as old_value:
        old_value.write(new_value.read())

updateData(newDataPath, oldDataPath)