# 1). Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def number_division(num_1, num_2):
    try:
        result = num_1/num_2
        return round(result, 2)
    except ZeroDivisionError:
        return 'На ноль делить нельзя! '


number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
print(number_division(number_1,number_2))


# 2). Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

# Вариант с использованием **kwargs , моё мнение он является самым подходящим , так как в дальнейшем с этим результатом
# (словарём) будет проще всего работать.
def user_data(**kwargs):
    return kwargs


print(user_data(name='Denis', surname='Salman', borndata=1997, CityOfResidence='Moscow', email='thedenis.s@outlook.com',
                telefon=+79160280247))


# # Вариант через *args , но он сомнительный потому что параметры не именнованые ,класс кортеж
def user_data_2(*args):
    return args


print(user_data_2('name:Denis', 'surname:Salman', 'borndata:1997', 'CityOfResidence: Moscow',
                  'email:thedenis.s@outlook.com', 'telefon: +7-916-0280-02-47'))


# # Вариант через функцию (простую) c именованными параметрами c классом строка
def user_data_3(name, surname, yearofbirth, CityOfResidence, email, telefon):
    return f'name - {name}, surname - {surname}, yearofbirth - {yearofbirth}, CityOfResidence - {CityOfResidence}, ' \
           f'email - {email}, telefon - {telefon}'


print(user_data_3('Denis', 'Salman', 1997, 'Moscow', 'thedenis.s@outlook.com', 79160280247))



# 3). Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b ,c ):
    max_1 = max(a,b,c)
    max_2 = max((min(a,b),min(a,c),min(b,c)))
    return max_1 + max_2



print(my_func(2, 1, 7))

# 4). Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


#Способ 1
def exponentiation(x, y):
    if y > 0:
        return 'Ведите отрицательное число'
    try:
        return x**y
    except TypeError:
        return 'Можно вводить только числа(int)'




print(exponentiation(11, -1))

#Способ 2 через цикл

def exponentiation_2(n,p):
    if p > 0:
        number = 1
        while p > 0:
            number = number * n
            p -= 1

        return f'Введите отрицательное число , но ответ на заданное условия я все же дам: {number}'

    else:
        number_negativ = 1
        while p < 0:
            number_negativ =number_negativ *  1/n
            p += 1

        return f' результат: {number_negativ}'



print(exponentiation_2(10, 15))


# 5). Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.



# Не понял как сделать      "Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."
def sum_number():
    symbol = True
    all_sum = 0
    while symbol == True:
        number_str = input('Ведите числа разделенные пробелом или нажмите q для выхода: ').split()
        result = 0

        for el in range(len(number_str)):
            if number_str[el] == 'q' or number_str[el] == 'Q':
                symbol = False
                break
            else:
                result= result + int(number_str[el])

        all_sum = all_sum +result
        print( all_sum)



sum_number()

# 6). Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но
# каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# 1 часть задания

def int_func(text):
    text_1 = text[0].upper() + text[1:].lower()
    return text_1

print(int_func('text'))
#2 часть задания

def int_func_2(text):
    len_text = len(text.split())
    if len_text > 1:
        return text.title()
    else:
        text_1 = text[0].upper() + text[1:].lower()
        return text_1


print(int_func_2('text letter '))






