'=========циклы========'

# цикл - это конструкция который повторяет несколько раз код несколько раз
# ЕСТЬ ДВА ВИДА ЦИКЛА В ПАЙТОНЕ, 

# '1. for - цикл который работает с итерируемым обьектом. Цикл заканчивает работу, когда доходит до последнего элемента итерируемого обьекта '
# '2. while - это цикл который работает до тех пор пока условие верное(True)'

# 'итерируемый обьект - это какая-то последовательность, например: [2,123,'djd'], 'makers', (123, True, 1), dict. set'

# итерация - процесс перебора итерируемого обьекта(когда мы по очереди вытаскиваем элементы в последовательности)

# '======FOR==='

# list_ = [12, 'hi', True, None, [0,0,0] ]
# for i in list_:
#  print(i) - 12 hi True None [0, 0, 0]


# for letter in 'hello world':
#     print(letter) 

'=========='

# for number in [12, 3, 4, 0 , -1, 20]:
#     print(number * 2) -
# 24
# 6
# 8
# 0
# -2
# 40

# list_ = [2, 12, 5, 3]
# for i in list_:
#     print(i ** 2)

# text = 'makers'
# for letter in text:
#     print(letter)
'===='

# list_ = [2, 5, 20, 10, 9 , -1]
# for i in list_:
#     if i % 2 == 0:
#         print(i)
#     else :
#         print('stupid')


'===while=='

# n = 1
# while n < 78:
#     print('loh')
#     n = n + 1

# n = 0
# while n :
#     print('hi')
#     n += 1 # n = n + 1, тоже самое

'==Ключевые слова в циклах==='
# break - это принудительная остановка кода(цикла)
# continue пропускает итерацию, продолжает со следующей итерации
# range - генератор 

# for i in range(1, 11):
#     if i == 3:
#         continue
#     print(i) #- 1,2,  4,5,6,7,8,9,10 

# for i in range(11):
#     print(i)
#     if i == 2:
#         break 

# n = 1
# while n < 10 :
#     n += 1
#     if n == 2:
#         continue
#     print(n) # 3,4,5,6,7,8,9,10

# n = 0 
# while n > -10:
#     break
#     print(n)


# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# res = [] 
# for i in nums: 
#     if i<5: 
#         res.extend(i) 
#     print(res)
    
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list3 = sum(list1 + list2) 
# print(list3)


# for i in range(1, 10):
#     i -= 5 
#     print(i)

# a = [1,3]
# print(int(a))

 