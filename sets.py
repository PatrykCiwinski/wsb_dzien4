zbiorA={1,2,3,4}
zbiorB={1,2,30,40}

print(zbiorA.union(zbiorB)) #suma sbiorów, nie duplikuje

print(zbiorA.intersection(zbiorB))#części wspólne

print(zbiorA.difference(zbiorB))#różnica zbioru A do zbioru B

print(zbiorB.difference(zbiorA))#j.w. tylko odwrotnie

print(zbiorA.symmetric_difference(zbiorB))#różnica symetryczna

print(len(zbiorA))#długość zbioru A

