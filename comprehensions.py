# comprehension - это генератор с помощью которого можно создать последовательность используя цикл for в одну строку

# range()
# []
# {}
# {:}

# результат for элемент in последовательность 

# list1 = [x + 2 for x in range(11)]
# print(list1) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# list1 = [x + 2 for x in [23,0,5,10]]
# print(list1) # [25, 2, 7, 12]

# list1 = [1 for x in [23,0,5,10]]
# print(list1) # [1,1,1,1]



# list2 = [x if x % 2 == 0 else x*5 for x in range(0,11)]
# print(list2)  # [0, 5, 2, 15, 4, 25, 6, 35, 8, 45, 10]


# list2 = [x for x in range(0,11) if x % 2 == 0 ]
# print(list2)  # [0, 2, 4, 6, 8, 10]


# 'B comprehension можно добавлять условия есть два вида'
# '1.Тертарный оператор - пишется перед циклом т к используется и if, else'
# '2. Фильтр пишется после цикла т к используется только if'

# list_1 = [12, True,None, 'hi', 0, False, 'makers', 'world']
# list2 = [i for i in list_1 if type(i) == str]
# print(list2) #['hi', 'makers', 'world']


# '==виды comprehension=='
# '1. list comprehension'
# '2. dict comprehension'
# '3. set comprehension'

# 'dict comprehension'

# dict_ = {i:i for i in range(1,11)}
# print(dict_)  # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

# ict_ = {i:i**2 for i in range(1,11)}
# print(ict_) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


dict_1 = {1: 'a', 2: 'b', 3: 'c'}
dict3 = {v:k for k,v in dict_1.items() }
print(dict3)

dict1 = {
    'a':[1,2,3], 
    'b':[12,0,1],
    'c':[32,0,0,10]
}
dict2 = {k:sum(v) for k,v in dict1.items()}
print(dict2) # {'a': 6, 'b': 13, 'c': 42}

'==set comprehension=='

# set_ = {i for i in range(1,11)}
# print(set_) {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set_ = {i for i in 'makers'}
# print(set_) {'a', 's', 'k', 'e', 'm', 'r'}

# set1 = {12,3,4,15,1}
# set2 = {i ** 2 for i in set1}
# # print(set2) - {1, 225, 9, 16, 144}
# set1 = {12,3,4,15,1}
# # set2 = {i ** i for i in set1}
# # print(set2)   -  {256, 1, 8916100448256, 437893890380859375, 27}
# set2 = {str(i) for i in set1}
# print(set2) = {'1', '4', '12', '3', '15'}

# set1 = {1,12, 'hi', 34,True, 'makers'}
# set2 = {i for i in set1 if type(i) == str}
# print(set2)  - {'makers', 'hi'}

# set1 = {'1','12', 'hi', 34,True, 'makers'}
# set2 = {int(i) if i.isdigit() else i for i in set1 if type(i) == str}
# print(set2)  - {'makers', 12, 'hi', 1}

# dict1 = {i:[i for i in range(1,i+1)]for i in range(1,6)}
# print(dict1)  #- {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# list_ = [i ** i for i in range(0,11,2 )]
# print(list_)


