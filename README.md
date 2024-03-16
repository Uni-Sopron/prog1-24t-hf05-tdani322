[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wF9LoxO6)
## 5. házi feladat

Egy söröző törzsvendégeinek fogyasztását nyilvántartó programot kell elkészíteni.

Az alkalmi vendégek azonnal fizetnek, azt egy külső program kezeli, és frissíti a készleteket.
Most a törzsvendégekre kell koncentrálni, akiknek névre szóló számlájuk van, és akár hitelre is fogyaszthatnak.

A program indulásakor jelenjen meg a főmenü:

    0 - Kilépés
    1 - Pénztáros mód
    2 - Admin mód
    Válasszon menüpontot:

### Pénztáros mód

Ebben a módban lehet a törzsvendégek fogyasztását rögzíteni, a menü így néz ki:

    0 - Vissza a főmenübe
    1 - Új törzsvendég
    2 - Rendelés
    3 - Befizetés
    Válasszon menüpontot:

#### Új törzsvendég

A program bekéri az új törzsvendég nevét, eltárolja 0 Ft egyenleggel, és visszatér Pénztáros módba.
Ha olyan nevet adtak meg, ami már létezik, akkor visszatérés előtt írjon ki egy hibaüzenetet, és ne módosítsa a meglévő vendég egyenlegét.

A törzsvendégek adatait a [data/guests.json](data/guests.json) tárolja.
Amikor az adatok változnak a programban, azonnal frissüljön a fájl tartalma!

#### Rendelés

A program először kilistázza a törzsvendégeket az egyenlegeikkel, majd bekéri a vendég sorszámát:

    0 - Vissza
    1 - Nagy Ivó Kálmán: 3000 Ft
    2 - Seres Nikolett: 4400 Ft
    3 - Bornemissza Gergely: -6000 Ft
    Válasszon vendéget: 3

A program ezután kilistázza a készleten lévő italokat, majd bekéri a választott ital sorszámát, mennyiségét:

    0 - Vissza
    1 - Csapolt Soproni: 120 Ft/dl
    2 - Soproni IPA: 700 Ft/doboz
    3 - Soproni Bivaly: 750 Ft/üveg
    Válasszon italt: 1
    Mennyiség dl egységben: -1
    Nemnegatív egész számot adjon meg!
    Mennyiség dl egységben: 500
    Nincs elég készlet! (A visszalépéshez adjon meg 0 mennyiséget.)
    Mennyiség dl egységben: 5
    +600 Ft Bornemissza Gergely számlájára írva, egyenleg: -6600 Ft
    0 - Vissza
    1 - Nagy Ivó Kálmán: 3000 Ft
    2 - Seres Nikolett: 4400 Ft
    3 - Bornemissza Gergely: -6600 Ft
    Válasszon vendéget:

Az italkészletet a [data/drinks.json](data/drinks.json) tárolja egy tömbben, melynek minden eleme egy ilyen felépítésű objektum:

```json
{
    "name": "Csapolt Soproni",
    "unit": "dl",
    "price": 120,
    "stock": 300
}
```

Csak azon italok jelenjenek meg a listában, amelyekből a készlet nem 0.
A rendelés után csökkenjen a készlet és a vendég egyenlege (a fájlokban is)!

#### Befizetés

A Rendelés első lépéséhez hasonlóan listázza a vendégeket a kiválasztáshoz, majd kérje be a befizetett pénzmennyiséget.
Ezt adja hozzá a vendég egyenlegéhez.

### Admin mód

Itt lehet az italkészlet adatait módosítani.
A program kilistázza a meglévő italokat, és egy extra opciót új ital hozzáadásához:

    0 - Vissza
    1 - Csapolt Soproni: 120 Ft/dl
    2 - Soproni IPA: 700 Ft/doboz
    3 - Soproni Bivaly: 750 Ft/üveg
    4 - Új ital hozzáadása
    Válasszon italt: 1

Ezután bekéri a kiválasztott ital új adatait.
Ha meglévő ital lett kiválasztva, üres bemenetre maradjon változatlan a jelenlegi érték, ami szögletes zárójelben kerüljön is kiírásra:

    name[Csapolt Soproni]: 
    unit[dl]: 
    price[120]: 130
    stock[295]: 500

Szorgalmi feladat ellenőrizni, hogy pozitív-e a megadott szám, és hogy van-e már azonos nevű, azonos kiszerelésű (unit) ital.

A módosítás kerüljön fájlba írásra is!

A módosítás után a program térjen vissza Admin módba.

Egy hosszabb példa be- és kimenete megtalálható a [tests/output.txt](tests/output.txt) fájlban, ami lefuttatható pytesttel is.
