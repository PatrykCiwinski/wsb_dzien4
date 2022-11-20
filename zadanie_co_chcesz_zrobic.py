def wypisz_menu():
    print('1. Dodaj rzecz do zrobienia')
    print('2. Oznacz rzecz jako zrobioną')
    print('3. Pokaż rzeczy do zrobienia i zrobione')
    print('4. Usuń rzecz do zrobienia')
    print('5. Ustaw konkretną rzecz na początek')
    print('6. Wyjdź z programu')


def pobierz_opcje_do_zrobienia():
    while True:
        i = input('Co chcesz zrobić? (1-6): ')
        try:
            liczba = int(i)
        except ValueError:
            print('To musi być liczba')
            continue
        if 1 <= liczba <= 6:
            return liczba
        print('To musi być liczba od 1 do 6')


class ListaRzeczyDoZrobienia:
    def __init__(self):
        self.lista_rzeczy_do_zrobienia = []
        self.lista_rzeczy_zrobionych = []
    def dodaj_rzecz_do_zrobienia(self):
        self.lista_rzeczy_do_zrobienia.append(input('Podaj rzecz do zrobienia: '))
    def pokaz_rzeczy_do_zrobienia(self):
        print('Do zrobienia jest: ', self.lista_rzeczy_do_zrobienia)
        print('Zrobione jest: ', self.lista_rzeczy_zrobionych)
    def oznacz_rzecz_jako_zrobioną(self):
        while True:
            try:
                index_zrobionej=int(input('co zostało zrobione: '))
            except ValueError:
                print('to musi być liczba')
                continue
            self.lista_rzeczy_zrobionych(self.lista_rzeczy_zrobionych[index_zrobionej])
            del self.lista_rzeczy_do_zrobienia[index_zrobionej]
            return
    def usun_z_listy(self):
        index_do_usuniecia = int(input('co zostało zrobione: '))
        print('co chcesz usunąć? ', self.lista_rzeczy_do_zrobienia)
        del self.lista_rzeczy_do_zrobienia[index_do_usuniecia]

    def ustaw_rzecz_na_poczatek(self):
        print(self.lista_rzeczy_do_zrobienia)
        index_do_przesunięcia = int(input('co chcesz przesunąć: '))-1
        element_na_poczatek=self.lista_rzeczy_do_zrobienia[index_do_przesunięcia]
        del self.lista_rzeczy_do_zrobienia[index_do_przesunięcia]
        self.lista_rzeczy_do_zrobienia.insert(0, element_na_poczatek)
        return


def petla_glowna_programu():
    instancje_rzeczy_do_zrobienia = ListaRzeczyDoZrobienia()
    while True:
        wypisz_menu()
        opcja = pobierz_opcje_do_zrobienia()
        if opcja == 1:
            instancje_rzeczy_do_zrobienia.dodaj_rzecz_do_zrobienia()
        elif opcja == 2:
            instancje_rzeczy_do_zrobienia.oznacz_rzecz_jako_zrobioną()

        elif opcja == 3:

            instancje_rzeczy_do_zrobienia.pokaz_rzeczy_do_zrobienia()
        elif opcja == 4:
            instancje_rzeczy_do_zrobienia.usun_z_listy()
        elif opcja == 5:
            instancje_rzeczy_do_zrobienia.ustaw_rzecz_na_poczatek()
        elif opcja == 6:
            return
petla_glowna_programu()