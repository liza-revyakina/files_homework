# Открытие файла, подсчет строк, добавление в список, добавление переноса строк и числа строк
with open('1.txt', encoding='utf-8') as file:
    lines_1 = 0
    first = ['1.txt\n']
    for line in file:
        lines_1 += 1
        first.append(line)
    first.append('\n')
    first.insert(1, str(lines_1)+'\n')

with open('2.txt', encoding='utf-8') as file:
    lines_2 = 0
    second = ['2.txt\n']
    for line in file:
        lines_2 += 1
        second.append(line)
    second.append('\n')
    second.insert(1, str(lines_2)+'\n')

with open('3.txt', encoding='utf-8') as file:
    lines_3 = 0
    third = ['3.txt\n']
    for line in file:
        lines_3 += 1
        third.append(line)
    third.append('\n')
    third.insert(1, str(lines_3)+'\n')


# В функцию передаются списки со строками, создается или перезаписывается файл text.txt
def minimal(one, two, three):
    with open('text.txt', 'w+', encoding='utf-8') as new_file:
        # Осуществляется перебор по циклам, идет проверка по длине, запись по возрастанию длины
        for each in one, two, three:
            if min(len(one), len(two), len(three)) == len(each):
                for each_line in each:
                    new_file.write(each_line)
                break
            else:
                continue
        for each in one, two, three:
            if len(each) != min(len(one), len(two), len(three)) and \
               len(each) != max(len(one), len(two), len(three)):
                for each_line in each:
                    new_file.write(each_line)
                break
            else:
                continue
        for each in one, two, three:
            if len(each) == max(len(one), len(two), len(three)):
                for each_line in each:
                    new_file.write(each_line)
                break
            else:
                continue


minimal(first, second, third)