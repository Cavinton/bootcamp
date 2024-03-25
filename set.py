'===============================================Set================================='
#множества - изменяемый, неупорядочный,итерируемый тип данных предназначенный для хранения
#уникальных значений, множества могут хранить в себе только неизменяемый тип данных.Если внутри set используется tuple то и внутри тюплa должны быть неизменяемый типы данных  ({'1,2,3,4, ('str), 12, Truee})
#в Set работает в правило - f10 (first in first out)


set_1={1,2,True,"hi"}#TRUE
set_2={True,1,"hi",2}#1



"===================FIFO/LIFO=========================="


#FIFO-first in first out(очередь в банк,выйдет первым тот кто был первым)

#LIFO- last in first out(последнее выйдет первым)



'========================методы set============================'


'add-добавляет элементы в set'

set1 = {1,2,3}
set1.add(3) # {1,2,3} - ничего не поменяется
set1.add(5) # {1,2,3,5} 

'pop - удаляет случайный элемент из set{} по принципу FIFO'
set2 = {1,2,3}
popped = set2.pop()
print(set2) # {2,3}


'remove - удаляет элемент из сета по значению. '
set3 = {1,2,3}
set3.remove(3)
print(set3) # {1,2}
print(dir(set))


'union - обьединяет set1 и set2'

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2)) # {1,2,3,4,5,6}
print(set1) # {1,2,3}

'update - обьединяет set1 и set2,и сохраняет изменения set1'

set1 = {1,2,3}
set2 = {4,5,6}
set1.update(set2) 
print(set1) # {1,2,3,4,5,6}

'difference (-) - находит разницу из сет1 при помощи сет2'

set1 = {1,2,3}
set2 = {3,4,5,6}
print(set1.difference(set2)) # {1,2}
print(set1 - set2) # тоже самое

' symmetric_difference - находит разницу между сет1 и сет2 '

set1 = {1,2,3}
set2 = {3,4,5,6}
print(set1.symmetric_difference(set2)) #{1, 2, 4, 5, 6}

'intesection (&) - находит схожие элементы из двух сетов set1, set2'

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2)) # {3,4}
print(set1 & set2) # {3,4}





set1 = {i for i in range(0,11)}
set2 = {i for i in range(11,22)}
full_set = set1.union(set2)
if len(full_set)<20:
 print(f"В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}")
elif len(full_set) == 20:
 print("Ваш объединенный сет полностью уникальный!")





set1 = {i for i in range(0,11) if i % 2 == 0}
set2 = {i for i in range(0,11) if i % 2 == 1}
if set1.intersection(set2): 
    print('Множества пересекаются!') 
else: 
    print('Множества не пересекаются!') 

