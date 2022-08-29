class InsuredPerson:

    def __init__(self, first_name, last_name, age, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.age = age

    def __str__(self):
        return f"Jméno: {self.first_name} {self.last_name}\nTelefonní číslo: {self.phone_number}\nVěk: {self.age}"

    __hash__ = None

    def __repr__(self):
        return self.__str__()
