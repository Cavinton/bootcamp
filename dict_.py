'=====================словри==================='
# dict - изменяемый, итерируемый, неупорядочный (псевдопорядок)тип данных, для хранения данных в парах{ключ:знпчение}

#user = {'name':'Anonym', 'age':30, 'last_name':'Makers'}
#print(user['name']) #Anonym
#print(user['age']) #30
#print(user['last_name']) #Makers

# ключами в словаре могут быть не изменяемые типы данных
# ключи в словарях должны быть уникальным

'=========================сознание словарей========================'
#dict_ = {'a':1, 'b':1}
#dict_ = dict({('a',1),('b',2)})
#print(dict_)
#dict_ = dict(['a1', 'b2', 'c3'])
#print(dict_)


# dict_ = {}
# dict_['name'] = 'makers'
# dict_['age'] = 50

# dict_['last name'] = 'bootcamp'
# print(dict_)  #{'name': 'makers', 'age': 50, 'last name': 'bootcamp'}

'====Методы словаря======'

'==get==' # это метод, который получает значения по ключу, если указанного ключа нет, то выходит None-по умолчанию, мы можем его поменять 

# user = {
#     'name': 'Anonym', 
#     'age': 15, 
#     'last name':'makers'
# }
# #print(user('id')) #False
# print(user.get('id')) #None
# print(user.get('id', 'Такого ключа нет')) #Такого ключа нет

'===pop==='

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# popped = dict_.pop('b')
# print(dict_) # {'a': 1, 'c': 3}
# print(popped) # 2

'==popitem=='
# удаляет последнюю пару и возвращает ее

dict_ = {'a': 1, 'b': 2, 'c': 3}
popped = dict_.popitem()
print(dict_, popped)



'==Итерирование словарей=='

# при итерации словаря будут приходить ключи

user = {
    'name': 'Anonym',
    'age': 15,
    'last name': 'Boot'
}
for i in user.keys():
    print(i) # name age last name

for value in user.values():
    print(value) # Anonym 15 Boot

# при итерации словаря с методом values() приходят значения
    
for item in user.items():
    print(item) #('name', 'Anonym') ('age', 15) ('last name', 'Boot')

# при итерации словаря методом items() приходит tuple с ключем и значением 
    

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict_2 = {}
for k, v in dict_1.items():
    dict_2[v] = k
print(dict_2) #{'a': 1, 'b': 2, 'c': 3} 



a = {'x': 1, 'y': 2, 'z': 1}
print(list(a.keys())[2]) # z


'==удаление пустых значений=='
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} 
for k,v in list(a.items()): 
    if v == None: 
        a.pop(k) 
print(a) 


'===деление значений==='
a = {'m': 40, 'h': 38, 'w': 120}
c = {}
for k, v in a.items():
    b = v/5
    c.setdefault(k,b)
print(c)


'===обьединяет два списка в словарь=='
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
dict_ = {}
dict_ = dict(zip(list1, list2))
print(dict_)

'===обьединяет словари=='
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {** dict1, ** dict2, ** dict3}
print(dict4)


'===Дан список. Создайте словарь dict_, ключами которого будут строки из списка, а значениями их длины===='

list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
dict_ = {}
for k in list_:
    dict_.setdefault(k, len(k))
print(dict_)

'===возведение в степень значений в словаре==='
dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dict2 = {}
for k,v in dict1.items():
    dict2.setdefault(k, v ** 3)
print(dict2)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# d = {k:y for k,v in dict_.items() for x,y in v.items() if type(y) == int}
# print(d) #27

dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}
# for k,v in dict_1.items():
#     if type(v) == int:
#         dict2.setdefault(k,v)
# print(dict_2)
dict3 = {k:y if type(y) == int else y ** y for k,v in dict1.items() for x,y in v.items()}
print(dict3)