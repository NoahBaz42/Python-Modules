#!/usr/bin/env python3
# ============= Class Plant and method show =====================

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        self.is_innit: bool = False

        self.set_age(age)
        self.set_height(height)
        self.is_innit = True
        self.show("Plant created: ")

    def show(self, plant_state: str) -> None:
        self._height = round(self._height, 1)
        print(
            f"{plant_state}"
            f"{self.name.capitalize()}: "
            f"{self._height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age += 1

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
            self.height = height
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


# ========= function to set attributes to Plant ==================

def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)

    print()
    plant.set_height(25)
    plant.set_age(30)

    print()
    plant.set_height(-42)
    plant.set_age(-69)
    print()

    plant.show("Current state: ")


# ============== Testing the Program ============================

if __name__ == "__main__":
    ft_garden_security()
