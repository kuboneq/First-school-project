from random import randint
from time import sleep

def pobierz():
  liczba = int(input("Podaj liczbę gier, ktorą chcesz zagrać: \n"))
  return liczba

def porownanie(zgadywanax, wylosowanay):
  while zgadywanax != wylosowanay:
    global proba
    
    zgadywanax = input("Podaj liczbę od 1 do 100: \n")
    if not zgadywanax.isalpha():
      zgadywanax = int(zgadywanax)

      if zgadywanax <= 0:
        print("====Podaj liczbe wieksza od 0!====")
      elif zgadywanax > 100:
        print("====Podaj liczbe mniejsza niz 100!====")
      elif zgadywanax > 0 and zgadywanax < 101:
        if zgadywanax > wylosowanay:
          print("Mniej!")
        elif zgadywanax < wylosowanay:
          print("Więcej!")
        proba += 1
    else:
      print("Podaj liczbe!")

zgadywana = 0

print("====Zgadnij liczbę!====\n")
liczba_gier = pobierz()
rozegrane_gry = 0

while rozegrane_gry != liczba_gier:
  
  wylosowana = randint(1, 101)
  print(f'====Gra numer {rozegrane_gry + 1} / {liczba_gier} !====')
  print(wylosowana)
  proba = 0
  porownanie(zgadywana, wylosowana)

  print(f"====Brawo! Zgadłes za {proba} probą!====\n")
    
  rozegrane_gry += 1

# wiadomosc koncowa
sleep(1)
if rozegrane_gry == 1:
  print(f"Rozegrałeś łącznie {rozegrane_gry} grę!")
elif rozegrane_gry == 2 or rozegrane_gry == 3 or rozegrane_gry == 4:
  print(f"Rozegrałeś łącznie {rozegrane_gry} gry!")
else:
  print(f"Rozegrałeś łącznie {rozegrane_gry} gier!")
