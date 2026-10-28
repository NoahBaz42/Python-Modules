#!/usr/bin/env python3
# ============= Class Plant and method show =====================

class Plant:

    @staticmethod
    def older_then_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Status:

        def __init__(self) -> None:
            self.log_grow: int = 0
            self.log_age: int = 0
            self.log_show: int = 0

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height: float = 0
        self._age: int = 0
        self.is_innit: bool = False
        self.stats = self.Status()

        self.set_age(age)
        self.set_height(height)
        self.is_innit = True

    def display(self) -> None:
        print(f"Stats: {self.stats.log_grow} grow, "
              f"{self.stats.log_age} age, "
              f"{self.stats.log_show} show")

    def show(self) -> None:
        self._height = round(self._height, 1)
        print(
            f"{self.name.capitalize()}: "
            f"{self._height:.1f}cm, {self._age} days old")
        self.stats.log_show += 1

    def grow(self, size: float = 0.8) -> None:
        self._height += size
        self.stats.log_grow += 1

    def age(self, days: int = 1) -> None:
        self._age += days
        self.stats.log_age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            if self.is_innit:
                print("Height update rejected")
        else:
            self._height = height
            if self.is_innit:
                print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self.is_innit:
                print("Age update rejected")
        else:
            self._age = age
            if self.is_innit:
                print(f"Age updated: {age}days")
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            if self.is_innit:
                print("Age update rejected")
        else:
            self._age = age
            if self.is_innit:
                print(f"Age updated: {age}days")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.blooming: bool = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):

    class Status(Plant.Status):

        def __init__(self) -> None:
            super().__init__()
            self.log_shade: int = 0

        def count_shade(self) -> None:
            self.log_shade += 1

    def display(self) -> None:
        super().display()
        print(f"{self.status.log_shade} shade")

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.status = self.Status()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces "
              f"a shade of {self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")
        self.status.count_shade()

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


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int = 0):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        if self.seeds == 0:
            self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.display()


def ft_garden_analytics() -> None:

    print("=== Garden Statistics ===")

    print("=== Check year-old")

    print(f"Is 30 days more than a year? -> {Plant.older_then_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_then_year(400)}")

    print()

    print("=== Flower")
    flower = Flower("rose", 15, 10, "red")
    flower.show()
    display_stats(flower)
    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow(8.0)
    flower.bloom()
    flower.show()
    display_stats(flower)

    print()

    print("=== Tree")
    tree = Tree("oak", 200, 365, 5)
    display_stats(tree)
    tree.produce_shade()
    display_stats(tree)

    print()
    print("=== Seed")
    seed = Seed("sunflower", 80, 45, "yellow")
    print(f"[make {seed.name} grow, age and bloom]")
    seed.grow(30.0)
    seed.age(20)
    seed.bloom()
    seed.show()
    display_stats(seed)

    print()
    print("=== Anonymous")

    secret = Plant.anonymous_plant()
    secret.show()
    display_stats(secret)


if __name__ == "__main__":
    ft_garden_analytics()
