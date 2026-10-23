#!/usr/bin/env python3
# ============= Class Plant and method show =====================

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.age} days old")


# ============= Garden data function ============================

def garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    sunflower = Plant("Sunflower", 80, 45)
    sunflower.show()
    cactus = Plant("Cactus", 15, 120)
    cactus.show()

# ============== Testing the Program ============================


if __name__ == "__main__":
    garden_data()
