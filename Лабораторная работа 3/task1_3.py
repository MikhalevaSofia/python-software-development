# TODO Напишите функцию для поиска индекса товара

def find_item_in_list(items, item_for_find): # Функция принимает на вход два аргумента: список товаров и товар, который нужно найти
    for index, item in enumerate(items):
        if item == item_for_find:
            return index # Функция возвращает индекс найденного товара
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_in_list(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
