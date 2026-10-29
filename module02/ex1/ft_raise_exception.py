#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    graus = int(temp_str)
    if graus > 40:
        raise Exception(f"{graus}°C is too hot for plants (max 40°C)")
    elif graus < 0:
        raise Exception(f"{graus}°C is too cold for plants (min 0°C)")
    else:
        return graus


def test_temperature():

    print("=== Garden Temperature Checker ===")
    print()

    test_values = ["25", "abc", "100", "-50"]
    for tests in test_values:
        print(f"Input data is '{tests}'")
        try:
            temp = input_temperature(tests)
            print(f"Temperature is now {temp}°C")
        except Exception as error:
            print(f"Caught input_temperature error: {error}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
