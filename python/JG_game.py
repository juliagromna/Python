import JG_bulls_and_cows

en = JG_bulls_and_cows.Engine()
x = 0
while x != 7:
    print("1 - Nowa Gra, 2 - Zasady Gry, 3 - Zmień Liczbę Prób, 4 - Zmień Trudność, 5 - Zapisz Wynik, "
          "6 - Dodaj Izogram Do Bazy, 7 - Koniec")
    x = int(input())
    if x == 1:
        en.play()
    elif x == 2:
        print(f"Komputer losuje słowo, które jest izogramem\n"
              f"Aktualny poziom trudności: {en.difficulty}\n"
              f"Na odgadnięcie słowa masz {en.attempts} prób\n"
              f"Po każdej próbie otrzymasz informację zwrotną w postaci liczb:\n"
              f"Bulls - poprawna liczba liter na poprawnej pozycji\n"
              f"Cows - liczba liter występujących w słowie, lecz na złej pozycji\n")
    elif x == 3:
        print("Podaj liczbę prób")
        a = int(input())
        en.change_attempts(a)
        print(f"Zmieniono liczbę prób na {en.attempts}")
    elif x == 4:
        print("Podaj poziom trudności (1-3)")
        d = int(input())
        while d > 3 or d < 1:
            print("Nie ma takiego poziomu trudności\n"
                  "Podaj poziom trudności")
            d = int(input())
        en.difficulty = d
        print(f"Poziom trudności zmieniono na {en.difficulty}")
    elif x == 5:
        en.export_score()
    elif x == 6:
        print("Podaj izogram")
        iz = input()
        en.add_word(iz)
    elif x == 7:
        print("Koniec gry")
    else:
        print("Wprowadzono liczbę z poza skali")
