import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Phone:
    def __init__(self, memory_capacity: (int, float), full_memory: (int, float)):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param memory_capacity: Объём памяти телефона
        :param full_memore: Занятый объём памяти

        Примеры:
        >>> phone = Phone(256, 120)  # инициализация экземпляра класса
        """
        if not isinstance(memory_capacity, (int, float)):
            raise TypeError("Объем памяти должен быть типа int или float")
        if memory_capacity <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.memory_capacity = memory_capacity

        if not isinstance(full_memory, (int, float)):
            raise TypeError("Заполненная память должна быть типа int или float")
        if full_memory < 0:
            raise ValueError("Заполенная память не может быть отрицательным числом")
        self.full_memory = full_memory


    def filling_up_memory(self, memory: (int, float)) -> None:
        """
        Функция, которая увеличивает заполненную память телефона
        :param memory: Объем добавляемой памяти

        :raise ValueError: Если количество добавляемой памяти превышает свободное место в телефоне, то вызываем ошибку
        Примеры:
        >>> phone = Phone(256, 120)
        >>> phone.filling_up_memory(30)
        """

        if not isinstance(memory, (int, float)):
            raise TypeError("Память должна быть int или float")
        if memory < 0:
            raise ValueError("Память не может быть отрицательной")
        ...


    def clearing_cache(self, cache: (int, float)) -> None:
        """
        Функция, которая очищает кэш
        :param cache: Объем удаляемого кэша

        :raise ValueError: Если количество удаляемого кэша превышает объём памяти телефона, то вызываем ошибку
        Примеры:
        >>> phone = Phone(256, 120)
        >>> phone.clearing_cache(5)
        """
        if not isinstance(cache, (int, float)):
            raise TypeError("Кэш должен быть int или float")
        if cache < 0:
            raise ValueError("Кэш не может быть отрицательным")
        ...


class Triangle:
    """
    Создание и подготовка к работе объекта "Треугольник"

    :param side1: Первая сторона треугольника
    :param side2: Вторая сторона треугольника
    :param side3: Третья сторона треугольника

    Примеры:
    >>> triangle = Triangle(5, 12, 13)  # инициализация экземпляра класса
    """
    def __init__(self, side1: int, side2: int, side3: int):
        if not isinstance(side1, int):
            raise TypeError("Сторона треугольника должна быть int")
        if not isinstance(side2, int):
            raise TypeError("Сторона треугольника должна быть int")
        if not isinstance(side3, int):
            raise TypeError("Сторона треугольника должна быть int")
        if side1 <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        if side2 <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        if side3 <= 0:
            raise ValueError("Сторона треугольника должна быть положительным числом")
        if ((side1 + side2) <= side3) or ((side1 + side3) <= side2) or ((side3 + side2) <= side1):
            raise ValueError("Должно выполняться неравенство треугольника, иначе треугольник не существует")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    def checking_isosceles_triangle(self, side1: int, side2: int, side3: int) -> bool:
        """
        Функция, которая проверяет, является ли треугольник равнобедренным

        :param side1: Первая сторона треугольника
        :param side2: Вторая сторона треугольника
        :param side3: Третья сторона треугольника

        :return: Является ли треугольник равнобедренным
        Примеры:
        >>> triangle = Triangle(5, 12, 13)
        >>> triangle.checking_isosceles_triangle(5, 12, 13)
        """
        ...

    def checking_right_triangle(self, side1: int, side2: int, side3: int) -> bool:
        """
        Функция, которая проверяет, является ли треугольник прямоугольным

        :param side1: Первая сторона треугольника
        :param side2: Вторая сторона треугольника
        :param side3: Третья сторона треугольника

        :return: Является ли треугольник прямоугольным
        Примеры:
        >>> triangle = Triangle(5, 12, 13)
        >>> triangle.checking_right_triangle(5, 12, 13)
        """
        ...

class ShelfBooks:
    """
    Создание и подготовка к работе объекта "Книжная полка"

    :param shelf_capacity: Объём полки
    :param occupied_part_of_shelf: Занятая часть полки

    Примеры:
    >>> shelf_books = ShelfBooks(50, 20)  # инициализация экземпляра класса
    """
    def __init__(self, shelf_capacity: int, occupied_part_of_shelf: int):
        if not isinstance(shelf_capacity, int):
            raise TypeError("Вместимость полки должна быть int")
        if shelf_capacity <= 0:
            raise ValueError("Вместимость полки должна быть положительным числом")
        self.shelf_capacity = shelf_capacity

        if not isinstance(occupied_part_of_shelf, int):
            raise TypeError("Занятая часть полки должна быть int")
        if occupied_part_of_shelf < 0:
            raise ValueError("Занятая часть полки не должна быть отрицательным числом")
        self.occupied_part_of_shelf = occupied_part_of_shelf


    def adding_books(self, number_of_books) -> None:
        """
        Функция, которая добавляет книги на полку

        :param number_of_books: Количество добавляемых книг
        :raise ValueError: Если количество добавляемых книг превышает свободное место на полке, то вызываем ошибку
        Примеры:
        >>> shelf_books = ShelfBooks(50, 20)
        >>> shelf_books.adding_books(10)
        """
        if not isinstance(number_of_books, int):
            raise TypeError("Количество добавляемых книг должно быть int")
        if number_of_books < 0:
            raise ValueError("Количество добавляемых книг не может быть отрицательным")
        ...



    def removing_books(self, number_of_books) -> None:
        """
        Функция, которая убирает книги с полки

        :param number_of_books: Количество убираемых книг
        :raise ValueError: Если количество убираемых книг превышает текущее количество книг на полке, то вызываем ошибку
        Примеры:
        >>> shelf_books = ShelfBooks(50, 20)
        >>> shelf_books.removing_books(20)
        """
        if not isinstance(number_of_books, int):
            raise TypeError("Количество удаляемых книг должно быть int")
        if number_of_books < 0:
            raise ValueError("Количество удаляемых книг не может быть отрицательным")
        ...



if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
