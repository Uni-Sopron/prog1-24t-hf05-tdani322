from penztar import penztar,vissza,order,newguest,payment
from admin import admin,newdrink

"""The entry point of the application."""


def run():
    while True:
        print("""0 - Kilépés
1 - Pénztáros mód
2 - Admin mód""")
        choice = int(input("Válasszon menüpontot: "))
        if choice == 0:
            break
        if choice == 1:
            penztar()
        if choice == 2:
            admin()


if __name__ == "__main__":
    run()
