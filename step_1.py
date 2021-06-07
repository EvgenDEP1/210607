class Human:

    def __init__(self, name, date_birth, address):
        self.name = name
        self.date_birth = date_birth
        self.address = address


class TrainingGroup:

    def __init__(self, name):
        self.name = name
        self.humans = []

    def add(self, human: Human) -> None:
        self.humans.append(human)

        # print('Студент добавлен  {}'.format(self.__hash__()))
        # print()
