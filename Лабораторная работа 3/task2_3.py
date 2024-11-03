# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=","): # Функция принимает 3 аргумента:
    # две строки с именами участников и разделитель
    group1 = set(group1.split(separator)) # Строка разбивается по разделителю и преобразуется в множество
    group2 = set(group2.split(separator))
    common_list = list(group1.intersection(group2)) # Находим пересечение множеств и формируем из него список
    common_list.sort() # Сортируем список в алфавитном порядке
    return common_list



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
