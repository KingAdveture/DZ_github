def delen(num1,num2):
    return num1 / num2

number1 = int(input("Введите делимое: "))
number2 = int(input("Введите делитель: "))
if number2 != 0:
    print(delen(number1, number2))
else:
    print("Ошибка! Деление на ноль!")

#-----------------------------------------------------------------------

def second_func(surname, name, year, city,number, email):
    print(f"{name} {surname} {year} {city} {email} {number}")


second_func(surname=input("Фамилия: "), name=input("Имя: "), year=int(input("Год рождения: ")),
            city=input("Город проживания: "), email=input("email: "), number=input("номер телефона: "))

#-----------------------------------------------------------------------

def my_func(number_1,number_2,number_3):
    result = 0
    if number_1 > number_2:
        if number_1 > number_3:
            result += number_1
        else:
            result += number_1 + number_3
        if number_2 > number_3:
            result += number_2
        else:
            result += number_3
    else:
        if number_1 > number_3:
            result += number_1
            if number_2 > number_3:
                result += number_2
            else:
                result += number_3
        else:
            result += number_2 + number_3
    return result

print(my_func(int(input("Введите первое число: ")),int(input("Введите второе число: ")),int(input("Введите третье число: "))))

#-------------------------------------------------------------------------

def my_func(x,y):
    result = 1
    for step in range(0,abs(y)):
        result *= 1/(x)
    return result

print(my_func(int(input("Введите действительное положительное число: ")),int(input("Введите целое отрицательно число: "))))

#-------------------------------------------------------

def func_sum(stroka):
    result = 0
    while stroka.find(' ') != -1:
        while stroka[0] == ' ':
            stroka = stroka[1: len(stroka)]
        while stroka[-1] == ' ':
            stroka = stroka[0:len(stroka) - 1]
        if stroka.find(' ') != -1:
            result += int(stroka[0:stroka.index(' ')])
            stroka = stroka[stroka.index(' ') + 1: len(stroka)]
    result += int(stroka)
    return result

stroka = input("Введите несколько чисел через пробел: ")
sum = 0
while stroka.find('~') == -1:
    sum += func_sum(stroka)
    print(sum)
    stroka = input("Введите несколько чисел через пробел: ")
ind = stroka.index('~')
if ind != 0:
    stroka = stroka.replace('~', ' ')
    while stroka[-1] == ' ':
        stroka = stroka[0:len(stroka)-1]
    sum += func_sum(stroka)
    print(sum)

#--------------------------------------------------------

def int_func(text):
    return text.capitalize()

print(int_func(input("Введите любой текст: ")))

#------------------------------------------------------------

def int_func(text):
    new_text = ''
    while text.find(' ') != -1:
        new_text += text[0: text.index(' ')].capitalize() + ' '
        text = text[text.index(' ')+1: len(text)]
        print(new_text)
    new_text += text.capitalize()
    return new_text

print(int_func(input("Введите любой текст: ")))