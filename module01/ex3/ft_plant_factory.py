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
    garden_plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in garden_plants:
        print("Created: ", end="")
        plant.show()

# ============== Testing the Program ============================


if __name__ == "__main__":
    ft_plant_growth()
