from collections import Counter
# Извлечение из списка повторяющихся элементов
def longest(s1, s2):
    list_1 = s1 + s2
    list_1 = sorted(list_1)
    new_list = [k for k,v in Counter(list_1).items() if v>=1]
    return ''.join(new_list)


print(longest("aretheyhere", "yestheyarehere"))
# Если вам нужно знать индексы,

from collections import defaultdict
D = defaultdict(list)
for i,item in enumerate(mylist):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}


# Если нужно найти 2 максимальных числа в ряде числ
def my_func(a, b ,c ):
    max_1 = max(a,b,c)
    max_2 = max((min(a,b),min(a,c),min(b,c)))
    return max_1 + max_2



print(my_func(9, 9, 9))

#Кодирование сообщение по методу  ROT 13 Цезаря
import string
def rot13(message):
    intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    outtab = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    transtab = str.maketrans(intab,outtab)
    str_1 = message
    return (str_1.translate(transtab))

print(rot13("Test"))

# Кодирование под скобочки
def duplicate_encode(word):
    result = []
    word = word.lower()
    q = ')'
    w = '('
    for  e in word:
        if word.count(e) > 1:
            result.append(q)
        else:
            result.append(w)
    return ''.join(result)

print(duplicate_encode('Success'))

# Группировка элементов всех и вывод вхождения количества элементов
from itertools import groupby
def duplicate_count(text):
    count = 0
    p= list(sorted(text.lower()))
    l = [list(j) for i, j in groupby(p)]

    for idx, el in enumerate(l):
        if len(el) > 1:
            count +=1
        else:
            continue
    return count


print(duplicate_count('abcdea'))

# Убирает одинаковые элементы в списке
from itertools import groupby
def unique_in_order(iterable):
    new_lst = list(iterable)
    result = [el for el, _ in groupby(new_lst)]
    return (result)




print(unique_in_order('AAAABBBCCDAABBB'))


#Каждая четная буква большая
def to_weird_case(string):
    f = []
    lst = [x for x in string.split()]
    if len(lst) >1:
        for i, x in enumerate(lst):
            g = []
            for idx , val in enumerate( x):
                if idx %2 == 0:
                    g.append(val.upper())
                else:
                    g.append(val.lower())
            f.append(''.join(g))
        return ' '.join(f)
    else:
        for i, x in enumerate(string):
            if i % 2 == 0:
                f.append(x.upper())
            else:
                f.append(x.lower())
        return ''.join(f)



print(to_weird_case('This is a test'))

# Можно использовать как вариант кодирование буквы в цифры от 1 до 27 , и вывод случайного ряда букв
import  string
from random import randint
def alphabet_position(text):
        lst_3 = []
        for x in text.lower().strip():

            if x not in string.punctuation:
                lst_3.append(x)
        message = ''.join(lst_3).replace(' ','')
        position = [ord(char) -96 for char in message]
        return ' '.join(map(str, position))
    else:
        position_num =[chr(randint(97, 123)) for i in range(text)]
        return ' '.join(map(str,position_num))


# Количество операций  возможных умножений чисел
from functools import reduce

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
# Второй вариань
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

print(persistence(999))