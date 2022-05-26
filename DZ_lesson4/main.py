from sys import argv
param_1, param_2, param_3 = argv
param_1 = int(input("Выработка в часах: "))
param_2 = int(input("Ставка в час: "))
param_3 = int(input("Премия: "))

result = (param_1 * param_2) + param_3
print("Зарплата сотрудника: ", result)

#-------------------------------------------------

list = [300, 2, 12, 44, 1, 1, 4, 10, 0, 1, 78, 123, 55]
new_list = [list[ind] for ind in range(1, len(list)) if list[ind] > list[ind-1]]
print(list)
print(new_list)
#-------------------------------------------------

my_dict = [el for el in range(20, 240) if (el % 20 == 0) or (el % 21 == 0)]
print(my_dict)

#-------------------------------------------------

new_list = []
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
for num in list:
    all = 0
    for ind in range(1,len(list)):
        if list[ind] == num:
            all+=1
    if all == 1:
        new_list.append(num)
    else:
        all = 0

print(list)
print(new_list)

#-------------------------------------------------

from functools import reduce

def my_func(prev_el, el):
    return prev_el + el

list = [num for num in range(100, 1001)]
print(reduce(my_func, list))

#-----------------------------------------------------

from itertools import count
start = int(input("Введите число с которого начать генерацию целых чисел: "))
for num in count(start):
    if num > 15:
        break
    else:
        print(num)


from itertools import cycle
с = 0
list = ["1", "2", "3", "4", "5"]
for el in cycle(list):
    if с > 15:
        break
    print(el)
    с += 1

#----------------------------------------------------------------

def fact(n):
    num = 1
    for el in range(1, n+1):
        num *= el
        yield num

n = int(input("Введите число: "))

g = fact(n)
print(g)

for el in g:
    print(el)

print(type(g))
