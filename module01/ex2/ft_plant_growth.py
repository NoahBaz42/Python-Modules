#!/usr/bin/env python3
# ============= Class Plant and method show =====================

class Plant:
    def __init__(self, plant_name: str, plant_height: int, plant_age: int):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def show(self) -> None:
        self.plant_height = round(self.plant_height, 1)
        print(
            f"{self.plant_name.capitalize()}: "
            f"{self.plant_height}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.plant_height += 0.8

    def age(self) -> None:
        self.plant_age += 1

# ============= Garden Growth function ============================


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30)

    growth = round(rose.plant_height, 1)
    rose.show()
    for x in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {x} ===")
        rose.show()
    growth = round(rose.plant_height - growth, 1)
    print(f"Growth this week: {growth}cm")

# ============== Testing the Program ============================


if __name__ == "__main__":
    ft_plant_growth()
