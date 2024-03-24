from penztar import vissza
import json
import os

def admin():
    drinks_file = os.path.join('data', 'drinks.json')
    with open(drinks_file, 'r', encoding='utf-8') as file:
        drinkdata = json.load(file)
    print("0 - Vissza")
    sorszam = 1
    for drink in drinkdata:
        print(sorszam," - ", drink['name'],": ", drink['price']," Ft/",drink['unit'])
        sorszam+=1
    print(sorszam," - Új ital hozzáadása: ")
    guestdrink = int(input("Válasszon italt: "))
    if vissza(guestdrink):
        admin()
    print("Add meg az új ital adatait!")
    if 1 <= guestdrink <= sorszam-1:
        print("name","[",drinkdata[guestdrink-1]['name'],"]:", end='')
        nameinput=(input())
        if nameinput == "":
            pass
        else:
            drinkdata[guestdrink-1]['name']=nameinput
        print("unit","[",drinkdata[guestdrink-1]['unit'],"]:", end='')
        unitinput=(input())
        if unitinput == "":
            pass
        else:
            drinkdata[guestdrink-1]['unit']=unitinput
        print("price","[",drinkdata[guestdrink-1]['price'],"]:", end='')
        priceinput=int(input())
        if priceinput == "":
            pass
        else:
            drinkdata[guestdrink-1]['price']=priceinput
        print("stock","[",drinkdata[guestdrink-1]['stock'],"]:", end='')
        stockinput=int(input())
        if stockinput == "":
            pass
        else:
            drinkdata[guestdrink-1]['stock']=stockinput
    if guestdrink == sorszam:
        newdrink()
    with open(drinks_file, 'w', encoding='utf-8') as file:
        json.dump(drinkdata, file, ensure_ascii=False, indent=4)



def newdrink():
    drinks_file = os.path.join('data', 'drinks.json')
    with open(drinks_file, 'r', encoding='utf-8') as file:
        drinkdata = json.load(file)
    new = {}
    new.update({"name:": (input("Add meg az új ital nevét: "))})
    new.update({"unit:": (input("Add meg az új ital mértékegységét: "))})
    new.update({"price:": (input("Add meg az új ital árát: "))})
    new.update({"stock:": (input("Add meg az új ital mennyiségét: "))})
    drinkdata.append(new)
    with open(drinks_file, 'w', encoding='utf-8') as file:
        json.dump(drinkdata, file, ensure_ascii=False, indent=4)