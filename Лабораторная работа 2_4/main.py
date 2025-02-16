if __name__ == "__main__":
    # Write your solution here
    pass
from typing import List


class Employee:
    """
    Базовый класс для сотрудников компании.
    """

    def __init__(self, name: str, position: str, salary: float) -> None:
        self.name = name
        self.position = position
        self._salary = salary  # Инкапсулируем, чтобы ограничить доступ

    def __str__(self) -> str:
        return f"{self.name} - {self.position}, зарплата: {self._salary} руб."

    def __repr__(self) -> str:
        return f"Employee(name={self.name}, position={self.position}, salary={self._salary})"

    def get_salary(self) -> float:
        """Возвращает зарплату сотрудника."""
        return self._salary

    def work(self) -> str:
        """Метод, описывающий работу сотрудника."""
        return f"{self.name} выполняет свои обязанности как {self.position}."


class Manager(Employee):
    """
    Дочерний класс, представляющий менеджера.
    """

    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, "Менеджер", salary)
        self.department = department

    def __str__(self) -> str:
        return f"Менеджер {self.name} (Отдел: {self.department}), зарплата: {self._salary} руб."

    def manage(self) -> str:
        """Метод управления отделом."""
        return f"{self.name} управляет отделом {self.department}."

    def work(self) -> str:
        """
        Перегруженный метод работы менеджера.
        Менеджер не только работает, но и управляет процессами.
        """
        return f"{self.name} организует работу отдела {self.department}."


class Developer(Employee):
    """
    Дочерний класс, представляющий разработчика.
    """

    def __init__(self, name: str, salary: float, programming_languages: List[str]) -> None:
        super().__init__(name, "Разработчик", salary)
        self.programming_languages = programming_languages

    def __str__(self) -> str:
        return f"Разработчик {self.name} (Языки: {', '.join(self.programming_languages)}), зарплата: {self._salary} руб."

    def code(self) -> str:
        """Метод написания кода."""
        return f"{self.name} пишет код на {', '.join(self.programming_languages)}."

    def work(self) -> str:
        """
        Перегруженный метод работы разработчика.
        Разработчик пишет код и участвует в разработке.
        """
        return f"{self.name} разрабатывает программное обеспечение на {', '.join(self.programming_languages)}."