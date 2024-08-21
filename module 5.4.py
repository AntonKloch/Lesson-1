class House:
    houses_history = []
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor <= self.number_of_floors) and (new_floor >= 1):
            for i in range(1, new_floor + 1):
                print(i)
        else:
                print('Такого этажа не существует')


    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, other):
        self.number_of_floors += other
        return self

    def __radd__(self, value):
        return self.add(value)

    def __iadd__(self, value):
        return self.add(value)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors,int):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории!')

h1 = House('ЖК Окна', 20)
h2 = House('ЖК Меркурий', 17)
h3 = House('ЖК Белые росы', 20)


h1.go_to(19)

h2.go_to(19)
print(h2.number_of_floors)
print(h1)
print(h2)

del h1
del h2
del h3