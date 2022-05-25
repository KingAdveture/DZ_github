list = [2, 'Привет', 36.6, None]
for num in range(0, len(list)):
    print(type(list[num]))
---------------------------------------------------------------

first_list = []
second_list = []
elem = input("Введите данные для вставки в первый список:")
while elem != '':
    first_list.append(elem)
    elem = input("Введите данные для вставки в первый список:")

elem = input("Введите данные для вставки во второй список:")
while elem != '':
    second_list.append(elem)
    elem = input("Введите данные для вставки во второй список:")

if len(first_list) <= len(second_list):
    for num in range(0, len(first_list)):
        elem = first_list[num]
        first_list[num] = second_list[num]
        second_list[num] = elem
else:
    for num in range(0, len(second_list)):
        elem = second_list[num]
        second_list[num] = first_list[num]
        first_list[num] = elem

#------------------------------------------------------------------

list_month = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
              7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(list_month.get(int(input("Введите месяц числом: "))))

#------------------------------------------------------------------

stroka = input("Напишите несколько слов: ")
if stroka.index(' ') == 0:
    print("Ошибка. строка начинает с пробела")
else:
    while stroka.find(' ') != -1:
        if stroka.index(' ')-1 > 10:
            print(stroka[0:10])
            stroka = stroka[stroka.index(' ') + 1: len(stroka)]
        else:
            print(stroka[0:stroka.index(' ')])
            stroka = stroka[stroka.index(' ')+1: len(stroka)]
print(stroka)

#------------------------------------------------------------------

list = [7, 5, 3, 3, 2]
element = int(input("Введите натуральное число"))
list.reverse()
for num in list:
    if num == element:
        list.insert(list.index(num), element)
        break
    elif element < num:
        list.insert(list.index(num), element)
        break
    if num == len(list):
        list.append(element)
        break
ist.reverse()
print(list)

#---------------------------------------------------------