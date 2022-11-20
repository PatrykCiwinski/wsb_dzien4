NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532}
centrum = {7648, 2345, 2356, 1243, 3987, 3476, 3254}
zbior_pusty = set()

#1.ile osob chorowalo na krzykach?

chorzy_na_krzykach_tamten_rok=chorzy_rok.intersection(krzyki)

print(len(chorzy_na_krzykach_tamten_rok))

# 2.ile osob na Krzykach chorowalo w tamtym miesiacy na Krzykach

chorzy_na_krzykach_tamten_miesiac=chorzy_miesiac.intersection(krzyki)
print(len(chorzy_na_krzykach_tamten_miesiac))

# 3.ile osob chorowalo w tamtym msc w centrum

chorzy_w_centrum_tamten_miesiac=chorzy_miesiac.intersection(centrum)
print(len(chorzy_w_centrum_tamten_miesiac))

#Kobiety vs mężczyźni w NFZ, kobiety ostatnią cyfrę mają parzystą mężczyźni nieparzystą
def podziel_zbiory(zbior):
    damski=set()
    meski=set()
    for element in zbior:
        if element%2 ==0:
            damski.add(element)
        else:
            meski.add(element)
    return damski, meski

zbior_wszystko=chorzy_miesiac.union(chorzy_rok, krzyki, centrum)

print(f'kobiety to {podziel_zbiory(zbior_wszystko)[0]}, a mężczyźni to {podziel_zbiory(zbior_wszystko)[1]}')

damski={element for element in zbior_wszystko if element%2==0}
print(f'kobiety to:{damski}')
meski={element for element in zbior_wszystko if element%2!=0}
print(f'mezczyzni to:{meski}')

# 4.ile osob chorowalo w tamtym roku w centrum

chorzy_w_centrum_tamten_rok=chorzy_rok.intersection(centrum)
print(len(chorzy_w_centrum_tamten_rok))

# 5.ile osob mieszka na Krzykach i w centrum

krzyki_i_centrum=centrum.union(krzyki)
print(len(krzyki_i_centrum))

# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.
if chorzy_rok.intersection(chorzy_miesiac) == chorzy_miesiac:
    print('każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku.')
else:
    print('BŁĄD !')
# nikt nie powinien mieszkać jednocześnie w Centrum i na Krzykach – jeśli tak, trzeba usunąć.
if krzyki.intersection(centrum):
    print("Ktoś mieszka na krzykach i w centrum: ", krzyki.intersection(centrum))
# każdy: chory, zdrowy, z Krzyków i z Centrum, powinien być w bazie NFZ, jeśli nie ma, trzeba dopisać.
osoby_do_dopisania_do_NFZ = set()
for nazwa, zbior in {'chorzy_rok': chorzy_rok, 'chorzy_miesiac': chorzy_miesiac, 'krzyki': krzyki, 'centrum': centrum}.items():
    if NFZ.intersection(zbior) != zbior:
        kto_jest_poza_nfz = zbior.difference(NFZ.intersection(zbior))
        assert NFZ.union(kto_jest_poza_nfz).intersection(zbior) == zbior
        print("ktoś jest poza bazą NFZ, ze zbioru: ", nazwa, " te osoby to ", kto_jest_poza_nfz)
        osoby_do_dopisania_do_NFZ = osoby_do_dopisania_do_NFZ.union(kto_jest_poza_nfz)
print("dopisze do NFZ osoby: ", osoby_do_dopisania_do_NFZ)
NFZ = NFZ.union(osoby_do_dopisania_do_NFZ)
print('teraz NFZ to: ', NFZ)

# kobiety z Krzyków które były chore w tamtym roku
damski2={element for element in damski.intersection(chorzy_rok.intersection(krzyki))}

print(damski2)

meski2={element for element in meski.intersection(chorzy_rok.difference(centrum))}
print(meski2)
