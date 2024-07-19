class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor <= self.number_of_floors) and (new_floor >= 1):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self,number_of_floors):
        return self.number_of_floors


    def __str__(self):
        return f"Название {self.name}, количество этажей: {self.number_of_floors}"

h1 = House('ЖК Окна', 25)
h2 = House('ЖК Меркурий', 17)

h1.go_to(25)
h2.go_to(19)



print(h1)
print(h2)
