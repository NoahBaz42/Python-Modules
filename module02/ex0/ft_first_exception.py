def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():

    print("=== Garden Temperature ===")
    print()

    good_test = "25"
    print(f"Input data is '{good_test}'")
    try:
        temp = input_temperature(good_test)
        print(f"Temperature is now {temp}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()

    bad_test = "abc"
    print(f"Input data is '{bad_test}'")
    try:
        temp = input_temperature(bad_test)
        print(f"Temperature is now {temp}°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()
    except Exception as er:
        print(f"Caught input_temperature error: {er}")
    finally:
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
