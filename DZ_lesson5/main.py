f_obj = open("zadanie1.txt", "w")
text = input("Введите пару слов: ")
while text != '':
    text = text.replace(' ', "\n")
    f_obj.write(text)
    text = input("Введите пару слов: ")
f_obj.close()

#---------------------------------------------

text = open("zadanie2.txt", "r")
my_text = text.readlines()
print(f"Количество строк в файле: ", len(my_text))
for ind in range(0, len(my_text)):
    text_for = my_text[ind]
    word = 0
    while text_for.find(' ') != -1:
        text_for = text_for[text_for.index(' ')+1:len(text_for)]
        word += 1
    word += 1
    print(f"Количество слов в {ind+1} строке: ", word)
print(my_text)
text.close()

#----------------------------------------------

text = open("zadanie3.txt", "r")
my_text = text.readlines()
sum = 0
for ind in range(0, len(my_text)):
    text_for = my_text[ind]
    money = float(text_for[text_for.index(' ')+1:len(text_for)-2])
    sum += money
    if money < 20000:
        text_for = text_for[0:text_for.index(' ')]
        print(text_for)
sum = sum / (len(my_text))
print(f"Средняя зарплата у {len(my_text)} сотрудников:", sum)
text.close()

#----------------------------------------------

text = open("zadanie4.txt", "r")
my_text = text.readlines()
text.close()
for ind in range(0, len(my_text)):
    text_for = my_text[ind]
    my_text[ind] = my_text[ind].replace('One', 'Один')
    my_text[ind] = my_text[ind].replace('Two', 'Два')
    my_text[ind] = my_text[ind].replace('Three', 'Три')
    my_text[ind] = my_text[ind].replace('Four', 'Четыре')
    print(my_text)
text = open("result4.txt", "w")

for elem in my_text:
    text.write(elem)
text.close()

#----------------------------------------------

text = open("zadanie5_result.txt", "w")
my_text = input("Введите числа через пробел: ")
text.write(my_text)
my_text = my_text.split()
print(my_text)
sum = 0
for elem in my_text:
    sum += int(elem)
sum =" Сумма чисел = " + str(sum)
text.write(sum)
text.close()

#---------------------------------------------------

text = open("zadanie6.txt", "r")
my_text = text.readlines()
text.close()
word_list = dict(Informatika=0, Fizika=0, Fizkyltypa=0)
word = ''
for ind in range(0, len(my_text)):
    sum = 0
    text_for = my_text[ind]
    word = text_for[0:text_for.index(':')]
    text_for = text_for.split()
    print(text_for)

    for elem in range(1, len(text_for)):
        try_text = text_for[elem]
        sum += int(try_text[0:try_text.index('(')])
    word_list[word] = sum
print(word_list)

#----------------------------------------------------------

import json

text = open("zadanie7.txt", "r")
my_text = text.readline()
print(my_text)
sum = 0
company = dict()
average_profit = dict()
all = 0
while my_text[-1] =='\n':
    all += 1
    text_for = my_text.split()
    print(text_for)
    if int(text_for[2]) - int(text_for[3]) > 0:
        sum += int(text_for[2]) - int(text_for[3])
        company[my_text[0:my_text.index(' ')]] = int(text_for[2]) - int(text_for[3])
    else:
        company[my_text[0:my_text.index(' ')]] = int(text_for[2]) - int(text_for[3])
    my_text = text.readline()
print(sum)
sum /= all
average_profit['profit'] = sum
print(company)
list_all = [company, average_profit]
print(list_all)

with open("result_zadanie7.json", "w") as write_f:
    json.dump(list_all, write_f)
