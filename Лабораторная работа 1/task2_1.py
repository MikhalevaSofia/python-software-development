# TODO Найдите количество книг, которое можно разместить на дискете
VALUE = 1.44 # Объем дискеты в Мб
PAGES = 100
LINES_ON_PAGE = 50
SYMBOLS_IN_LINE = 25
VALUE_FOR_ONE_SYMBOL = 4 # Объем для хранения одного символа в байтах

value_for_book = SYMBOLS_IN_LINE * LINES_ON_PAGE * PAGES * VALUE_FOR_ONE_SYMBOL
total_books = int(VALUE * 1024 ** 2 / value_for_book)

print("Количество книг, помещающихся на дискету:", total_books)

