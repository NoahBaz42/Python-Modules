#!/usr/bin/env python3
# ============= Class Plant and method show =====================

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        self.is_innit : bool = False

        self.set_age(age)
        self.set_height(height)
        self.is_innit = True

    def show(self) -> None:
        self.height = round(self.height, 1)
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 2.1

    def age(self, days: int = 1) -> None:
        self.age += 1

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if self.is_innit:
                print("Height update rejected")
        else:
            self.height = height
            if self.is_innit:
                print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self.is_innit:
                print("Age update rejected")
        else:
            self.age = age
            if self.is_innit:
                print(f"Age updated: {age}days")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self.is_innit:
                print("Age update rejected")
        else:
            self.age = age
            if self.is_innit:
                print(f"Age updated: {age}days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        print("=== Flower")
        self.color = color
        self.blooming: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        print("=== Tree")
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of {self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name, height, age)
        print("=== Vegetable")
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def grow_age(self, days_old: int) -> None:
        print(f"[make {self.name} grow and age for {days_old} days]")
        self.nutritional_value += days_old
        while days_old:
            days_old -= 1
            super().grow()
            super().age(days_old)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    flower = Flower("rose", 15, 10, "red")
    flower.show()
    flower.bloom()
    flower.show()

    print()
    tree = Tree("oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()

    print()
    veggy = Vegetable("tomato", 5, 10, "April")
    veggy.show()
    veggy.grow_age(20)
    veggy.show()

if __name__ == "__main__":
    ft_plant_types()