# 1). Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
user_data = input('Введите данные : ').split()
print(user_data)
with open('textFile/text1.txt', 'w') as f_obj:
    for line in user_data:
        f_obj.writelines(line + '\n')


# 2). Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
count = 0
with open('textFile/text2.txt', 'r') as f_obj:
    for line in f_obj:
        count += 1
        word = len(line.split())
        print(f'Строка № {count}')
        print(f'Количество слов {word}')
        print(f'Сама строка  {line}')

# 3). Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
summ_salary = 0
count_staff = 0
staff = []
with open('textFile/text3.txt', 'r') as f_obj:
    for line in f_obj:
        lst_1 = line.split()[0]
        count_staff += 1
        lst_2 = int(line.split()[-1])
        lst_3 = [lst_1] + [lst_2]
        summ_salary += lst_2
        if lst_3[-1] < 20000 :
            staff.append(lst_3[0])


average_salary = summ_salary/count_staff
print(f'Сотрудники с заработной платой меньше 20тыс: {staff}')
print(f'Средняя заработная плата сотрудников: {average_salary.__round__(2)} руб.')

# 4). Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
lst_num = ['один','два','три','четыре']
new_lst = []
idx_lst_num = 0
with open('textFile/text4.txt', 'r') as f_obj:
    for line in f_obj:
        lst_file = line.split()
        lst_file[0] = lst_num[idx_lst_num]
        idx_lst_num += 1
        new_lst.append(' '.join(lst_file))

with open('textFile/text5.txt', 'w', encoding='utf-8') as f_obj:
    for line in new_lst:
        f_obj.writelines(line + '\n')


# 5). Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('textFile/text6.txt', 'w') as f_obj:
    new_lst = [str(x) for x in range(1, 50)]
    for line in new_lst:
        f_obj.write(line + ' ')

with open('textFile/text6.txt', 'r') as f_obk:
    new_str = f_obk.readline()
    new_list = [int(x) for x in new_str.split()]
    all_sum = sum(new_list)
    print(f'Сумма : {all_sum}')

# 6). Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
all_sum = []
all_subject = []
with open('textFile/text7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        subject_list = [x for x in line.split()]
        subject = subject_list[0]
        all_subject.append(subject)
        num_list =[int(x) for x in line.split() if x.isdigit()]
        sum_num = sum(num_list)
        all_sum.append(sum_num)
dictionary = dict(zip(all_subject, all_sum))
print(dictionary)

# 7). Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
profit = []
average_profit = []
with open('textFile/text8.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:

        firm_name = [x for x in line.split()][0]
        firm_name = [firm_name]
        firm_num = [int(x) for x in line.split() if x.isdigit()]
        pr = firm_num[0] - firm_num[1]
        if pr > 0:
            average_profit.append(pr)
            profit.append(dict(zip(firm_name, [pr])))
        elif pr < 0:
            profit.append(dict(zip(['material_losses'], [pr])))
        else:
            continue
    profit.append(dict(zip(['avrage_profit'], [sum(average_profit)])))

import json
with open('textFile/text.json', 'w', encoding='utf-8') as f_obj:
    json.dump(profit, f_obj)



























