class Person:
    def __init__(self, first_name, last_name, b_year):
        self.first_name = first_name
        self.last_name = last_name
        self.b_year = b_year

    @property
    def full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def age(self):
        return 2024 - self.b_year

    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(" ")


p1 = Person("azizbek", "boltaev", 2004)
print(p1.full_name)
p1.full_name = "A B"
print(p1.full_name)