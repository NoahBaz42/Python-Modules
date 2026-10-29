#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        operation_number /= 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        operation_number = "ABC" + 10
    else:
        return


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===")

    for tests in range(5):
        print(f"Testing operation {tests}...")
        try:
            garden_operations(tests)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
