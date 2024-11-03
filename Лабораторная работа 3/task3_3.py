# TODO  Напишите функцию count_letters

def count_letters(text):# Функция принимает в качестве аргумента текст
    dict_of_letters = {} # Создаем пустой словарь
    text = text.lower() # Приводим все символы в строке к нижнему регистру
    for symbol in text: # В цикле идем по каждому символу в строке и проверяем, является ли он буквой
        if symbol.isalpha() == True:
            dict_of_letters[symbol] = text.count(symbol) # Если символ - буква, то добавляем в словарь пару ключ-значение
    return dict_of_letters # Возвращаем словарь с буквами и их количеством в тексте



# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict_): # Функция принимает на вход словарь с буквами и их количеством в тексте
    new_dict_ = {} # Создаем пустой словарь
    for letter in dict_: # Идем по ключам в словаре
        new_dict_[letter] = dict_.get(letter) / sum(dict_.values()) # Добавляем в новый словарь пару ключ (буква) - значение (частоту каждой буквы),
    # которая считается как отношение значения из старого словаря и общего числа букв в тексте (суммируются все значения словаря)
    return new_dict_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
for item in calculate_frequency(count_letters(main_str)):
    print(f"{item}: {calculate_frequency(count_letters(main_str)).get(item):.2f}")