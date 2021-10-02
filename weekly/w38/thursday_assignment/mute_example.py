#Snabb bonus! Hur vi hanterar och ser på mutables. 
#Vi gör ett mutable objekt av något slag - en lista blir gott nog för våra syften.
mutable1 = [1,2,3,4,5]

#Lägger denna i varsin lista
list1 = [mutable1, 2]
list2 = [mutable1, 3]

#MODIFIERAR vi en mutable i en lista ändrar vi på objektet
list2[0].extend([1,2,3,4])
print(f'Contents of list1[0]: {list1[0]}')
print(f'Contents of list2[0]: {list2[0]}')
print(id(1))
print(id(mutable1[0]))

#Vi kan styrka detta genom att kolla ID på vad vi refererar till:
print(f'Memory location of object in list1[0]: {id(list1[0])}')
print(f'Memory location of object in list2[0]: {id(list2[0])}')

#Ändrar vi VAD som ska finnas i index 0 i list2 kommer vi att ha en ny referens till ett nytt objekt
list2[0] = [9, 10]
print(f'Contents of list1[0]: {list1[0]}')
print(f'Contents of list2[0]: {list2[0]}')

print(f'Memory location of object in list1[0]: {id(list1[0])}')
print(f'Memory location of object in list2[0]: {id(list2[0])}')
