dict = {
    "SIGMA":"Osoba wzbudzająca szacunek u innych",
    "RIZZ":"Określenie oznaczające podryw",
    "LOL":"odpowiedź na coś zabawnego"
    "CRINGE":"coś dziwnego lub wstydliwego"
    "ROFL":"odpowiedź na żart"
    "SHEESH":"lekka dezaprobata"
    "CREEPY":"straszny, złowieszczy"
    "AGGRO":"stać się agresywnym/zły"
      }

while True:
    word = input("Wpisz słowo, ktorego nie rozumiesz: ")
    word = word.upper()
    word = word.strip()
    if word in dict.keys():
        print(dict[word])
    else:
        print("Nie ma takiego słowa")
