class Human:

    def __init__(self, name, date_birth, address):
        self.name = name
        self.date_birth = date_birth
        self.address = address


class TrainingGroup:

    def __init__(self, name, humans):
        self.name = name
        self.humans = humans