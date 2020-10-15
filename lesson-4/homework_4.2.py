# 2). Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор
# списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

original_list= [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
#Список через цикл
for x in range(len(original_list)-1):
    if original_list[x] < original_list[x+1]:
        new_list.append(original_list[x+1])
print(new_list)
#Список через генератор
new_list_2 = [original_list[x+1] for x in range(len(original_list)-1) if original_list[x] < original_list[x+1]]
print(new_list_2)

# 3). Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор списка .

new_list_3 = [x for x in range(20,240) if x %20 == 0 or x%21 ==0]
print(new_list_3)

# 4). Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# в порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор списка. (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

original_list_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list_4 = [x for x in original_list_2 if original_list_2.count(x)==1]
print(new_list_4)

# 5). Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
new_list_5 = [x for x in range(1, 1001) if x %2 == 0]
print(new_list_5)
def composition(first, second):
    return first * second
result = reduce(composition, new_list_5)
print(result)

# 6). Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
# a)
for x in count(3,1):
    if x > 10:
        break
    else:
        print(x)
# б)
lst_1 = [23, 1, 3, 10, 4, 11]
aisle = 0
for x in cycle(lst_1):
    if aisle > 10:
        break

    else:
        print(x)
        aisle +=1


# 7). Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим
# образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24. На вебинаре реализовали похожий пример для чисел Фиббоначи.

def fact(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        yield n
        n -= 1
print(fact(4))

for el in fact(4):
    print(el)
# Это по сути обратный способ (для проверки просто)
l = [el for el in fact(4)]
print(l)
def s(first, second):
    return first*second
print(reduce(s,l))









