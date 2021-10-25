class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя работника - {self.name} {self.surname}')

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        print(f'Общий доход с учетом премии - {total} р.')


fedya = Position('Федор', 'Емельянов', 'инженер', 30000, 2000)

fedya.get_full_name()
fedya.get_total_income()
