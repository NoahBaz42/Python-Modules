#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, error: str = "Unknown garden error") -> None:
        self.error = error
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "Unknown plant error") -> None:
        self.error = error


class WaterError(GardenError):
    def __init__(self, error: str = "Unknown water error") -> None:
        self.error = error


def tomato_exceptions(tomato: int) -> None:
    # tomato lasts 2 weeks in the fridge; more and it will start wilting
    if tomato > 14:
        raise PlantError("The tomato plant is wilting!")


def water_exceptions(tank_water: int) -> None:
    # how many liters in the tank: less then 5 is too little
    if tank_water < 5:
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:

    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")

    try:
        tomato_exceptions(15)
    except PlantError as error:
        print(f"Caught PLantError: {error}")

    print()
    print("Testing WaterError...")

    try:
        water_exceptions(2)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print()
    print("Testing catching all garden errors...")

    try:
        tomato_exceptions(50)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water_exceptions(1)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
