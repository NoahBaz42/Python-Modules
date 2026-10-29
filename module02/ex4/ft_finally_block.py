#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, error: str = "Unknown garden error") -> None:
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, error: str = "Unknown plant error") -> None:
        super().__init__(error)


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants) -> None:

    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as er:
        print(f"Caught PlantError: {er}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print()
    print("Testing valid plants...")
    plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plants)

    print()
    print("Testing invalid plants...")
    plants = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(plants)

    print()
    print("Cleanup always happens, even with errors!")
