class Worker:
    name: str
    surname: str
    position: str
    _income: dict
    def __init__(self, name: str, surname: str, position: str, salary: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())
j = Position("Иван", "Иванов", "Слесарь", 10000, 2000)
print(j.get_full_name(), j.get_total_income())
f = Position("Петр", "Петров", "Токарь", 20000, 5000)
print(f.get_full_name(), f.get_total_income())