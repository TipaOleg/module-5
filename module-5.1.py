
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance


    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __eq__(self, other):
        return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value: int):
        return House(self.name, self.numbers_of_floors + value)

    def __radd__(self, value: int):
        return House(self.name, self.numbers_of_floors + value)

    def __iadd__(self, value: int):
        self.numbers_of_floors += value
        return self

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


    def go_to(self, new_floor: int):
        if 1 <= new_floor <= self.numbers_of_floors:
            for i in range(1, new_floor + 1):
                print(f"Этаж {i}")
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)
del h2
del h3
print(House.houses_history)

# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2)
# h1 = h1 + 10
# print(h1)
#
# print(h1 == h2)
#
# h1 += 10
# print(h1)
#
# h2 = 10 + h2
# print(h2)
#
# print(h1 > h2)
# print(h1 >= h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 != h2)


# h1 = House('ЖК Горский', 18)
#
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(5)
#
# h2.go_to(10)
#
# h1 = House('ЖК Эльбрус', 10)
#
# h2 = House('ЖК Акация', 20)
#
# print(h1)
#
# print(h2)
#
# print(len(h1))
#
# print(len(h2))