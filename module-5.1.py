from traceback import print_tb


class House:
    def __init__(self, name=str, numbers_of_floors=int):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def go_to(self, new_floor=int):
        if new_floor >= 1 and new_floor <= self.numbers_of_floors:
            for i in range(1, new_floor+1):
                print(i)

        else:
            print("Такого этажа не существует")



h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)