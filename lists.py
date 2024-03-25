'=list=='
# списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, прдназначенный для хранения любых данных в определенныом порядке

# list_1 = [1, 2, 3, 'hello', True, [10, 6, 3 ], None] 
         #0  1  2    3        4        5        6      - индексы


# list_1 [5] [-1] - покажет 6 в списке под индексом 5
# list_1 [3] [-2] - покажет l с хэлоу
# list_! [5] - [10, 6, 3]

# list('hello') -> ['h', 'e', 'l', 'l', 'o']


# range(start, end(не включительно), step) - это функция генератор, которая создает диапазон от start дo end(не включительно)

# list_ = list(range(0, 101)) - от 0 до ста, 101 не вкл

# print(list(range(0, 11, 2))) - [0 ,2, 4, 6, 8, 10]
# [0, 3, 6, 9] - step 3
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] - step -1

'===методы списков===='
# append - добавление элементов в конец списка

# list_ = []
# list_.append(1) - 1
# list_.append('hello') - 'hello'
# list_.append(True) - True 


'pop - удаление элемента из списка по индексу, он так же возвращает удаленный элемент/ если не указать индекс, удалит с конца'

# list_ = [90, True, None, 'Hi']
# popped = list_.pop(1) 
# print(list_, popped) - [90, None, 'Hi'] True

'remove - это удаление элемента из списка по значению'

# list_ = [1,2,3,1. 'hi', 5,99,0,-11]
# list_.remove(99) - удаляет 99
# list_.remove(1) - удаляет первую единицу
# list_.remove(False) - удаляет 0
# list_.remove(True) - удаляет первый положительный

# print(bool([])) - false


' count - считает кол-во принятого элемента в списке'

# list_ = [1, 213, 124, 214,'hi', 'hi', 1, 1, 1,  1, 2, 3]
# print(list_.count(1)) - 5, показал кол-во единиц
# print(list_.count('hi')) - 2

'index - возвращает первое вхождение принятого элемента'

# list_ = ['hi', 1 ,2,0,  4, 99, ]
# print(list_.index(0)) - 5, показывает под каким индексом стоит введеный элемент

'extend - расширяет список при помщи другого списка'
# list1 = [1,2,3]
# list2 = [,0,0,]
# list1.append(list2) - [1,2,3 [0,0,0]]
# list1.extend(list2) - [1,2,3,0,0,0]

'reverse - отзеркаливает'
# list_ = [1,2,3]
# print(list_.reverse()) - [3,2,1] 

'sort - сортирует список, состоящий из элементов одного типа данных'

# list_ = [131,123123,1, 2]
# print(list_.sort(reverse=True)) - 123123, 131, 2, 1

# list_ = ['a', 'b', 's', 's', 'w', 'A', 'B']
# list_.sort(reverse=True)
# print(list_) - ['w', 's', 's', 'b', 'a', 'B', 'A']


'===insert==='

# insert(index, element)
# users = ['john', 'leny', 'andy']
# users.insert(1, 'rahel')
# print(users) # ['john', 'rahel', 'leny', 'andy']


'clear - очищает список'
# list_ = [12,3123,1,4]
# print(list_.clear()) - []

# len([12, 4, 5, [1, 2, 3]]) - 4 элемента


# pack1 = []
# pack2 = []

# list_ = [23, 'hi', 'makers', 2, 1]

# for i in list_ :
#     if i == 23 :
#         pack1.append(i)
#     elif i == 'hi' :
#         pack2.append(i)
# print(pack1, pack2) - - [23] ['hi']


# list_ = ['hello', 'world']
# new_list = [list_[1],list_[0]]
# print(new_list)

# num = int(input())
# print(chr(num))

a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
d = {k:y for k,v in a.items() for x,y in v.items()}
print(d)
