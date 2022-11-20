NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532}
centrum = {7648, 2345, 2356, 1243, 3987, 3476, 3254}
wszystkie_zbiory = {'NFZ': NFZ, 'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}


def czy_ok(pesel):
    return pesel>=10**3 and pesel<=10**4


def wprowadz_pesel():
    while True:
        p=input('podaj pesel ').strip()
        try:
            moze_pesel=int(p)
            if not czy_ok(moze_pesel):
                print('pesel musi miec 4 cyfry')
                continue
            return moze_pesel
        except ValueError:
            print('prosze podac dobry pesel')
pesel=wprowadz_pesel()
if pesel % 2 == 0:
    print('podany pesel ', pesel, ' należy do kobiety')
else:
    print('podany pesel ', pesel, ' należy do mężczyzny')

def sprawdz_PESEL(pesel):
    for name,zbior in wszystkie_zbiory.items():
        if pesel in zbior:
            print(f"Podany pesel to: {pesel} jest z {name}")

print(sprawdz_PESEL(pesel))