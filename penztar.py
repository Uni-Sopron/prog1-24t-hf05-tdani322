import json
import os

def vissza(szam):
    if szam == 0:
        print("Visszalépés")
        return True
    else:
        return False



def penztar():
    while True:
        print("""0 - Vissza a főmenübe
1 - Új törzsvendég
2 - Rendelés
3 - Befizetés""")
        choice = int(input("Válasszon menüpontot: "))
        if choice == 0:
            if vissza(choice):
                break
        if choice == 1:
            return newguest()
        if choice == 2:
            return order()
        if choice == 3:
            return payment()

def newguest():
    guest=input("Add meg a törzsvendég nevét: ")
    guests_file = os.path.join('data', 'guests.json')

    with open(guests_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

    for item in data:
        if item["name"] == guest:
            raise NameError("A vendég már szerepel a listában!")
        
    new_data = {
        "name": guest,
        "balance": 0
    }
    data.append(new_data)        
    with open(guests_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return print("Törzsvendég hozzáadva:", new_data)

def order():
    guests_file = os.path.join('data', 'guests.json')
    drinks_file = os.path.join('data', 'drinks.json')
    while True:
        try:
            with open(guests_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print("0 - Vissza")
            for idx, guest in enumerate(data, start=1):
                print(idx, " - ", guest['name'], ": ", guest['balance'], " Ft")
            guestchoice = int(input("Válasszon vendéget: "))
            if guestchoice == 0:
                return penztar()
            with open(drinks_file, 'r', encoding='utf-8') as file:
                drinkdata = json.load(file)
            print("0 - Vissza")
            for idx, drink in enumerate(drinkdata, start=1):
                print(idx, " - ", drink['name'], ": ", drink['price'], " Ft/", drink['unit'])
            guestdrink = int(input("Válasszon italt: "))
            if guestdrink == 0:
                continue
            unit = drinkdata[guestdrink - 1]['unit']
            print("Mennyiség " + str(unit) + " egységben: ", end='')
            quantity = int(input())
            if quantity <= 0 or quantity > drinkdata[guestdrink - 1]['stock']:
                print("Hibás mennyiség vagy készlet.")
                continue
            price = drinkdata[guestdrink - 1]['price']
            ar = price * quantity
            newbalance = data[guestchoice - 1]['balance'] - ar
            data[guestchoice - 1]['balance'] = newbalance
            drinkdata[guestdrink - 1]['stock'] -= quantity
            with open(guests_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            with open(drinks_file, 'w', encoding='utf-8') as file:
                json.dump(drinkdata, file, ensure_ascii=False, indent=4)
            print("+", ar, " Ft", data[guestchoice - 1]['name'], "számlájára írva, egyenleg: ", data[guestchoice - 1]['balance'])
        except ValueError:
            print("Hibás bemenet, kérem válasszon számot.")
        except IndexError:
            print("Hibás választás, kérem válasszon újra.")
        except Exception as e:
            print("Hiba történt:", e)


             

def payment():
    guests_file = os.path.join('data', 'guests.json')
    with open(guests_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    print("0 - Vissza")
    sorszam = 1
    for guest in data:
            print(sorszam," - ", guest['name'],": ",guest['balance'], " Ft")
            sorszam+=1
    guestchoice=int(input("Válasszon vendéget: "))
    paid=int(input("Adja meg a befizetett pénzmennyiséget: "))
    data[guestchoice - 1]['balance']+=paid
    with open(guests_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return print("Pénz hozzáadva!")
