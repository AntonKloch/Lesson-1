class House:
    def init(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor <= self.number_of_floors) and (new_floor >= 1):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def len(self):
        return self.number_of_floors

    def str(self):
        return f"Название {self.name}, кол-во этажей: {self.number_of_floors}"

    def add(self, other):
        self.number_of_floors += other

    def radd(self, value):
        return self.add(value)

    def iadd(self, value):
        return self.add(value)

    def eq(self, other):
        return self.number_of_floors == other.number_of_floors

    def lt(self, other):
        if isinstance(other.number_of_floors,int):
            return self.number_of_floors < other.number_of_floors
        # else:
        #     return NotImplemented

    def le(self, other):
        return self.number_of_floors <= other.number_of_floors





h1 = House('ЖК Окна', 25)
h2 = House('ЖК Меркурий', 17)

# h1.go_to(25)
# h2 + 10 # add
# h2.go_to(19)
# print(h2.number_of_floors)
# print(len(h1))
#
# print(h1)
# print(h2)
print(h1 < h2)