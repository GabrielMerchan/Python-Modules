#!/usr/bin/env python3

def garden_operation(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')

    elif operation_number == 1:
        10/0

    elif operation_number == 2:
        open('/non/existent/file')

    elif operation_number == 3:
        'Hola' + 42


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        try:
            print(f"Testing operation {i}...")
            garden_operation(i)
            print('Operation completed succesfully')
            i += 1
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
            i += 1

    print('\nAll error types tested succesfully!')


if __name__ == "__main__":
    test_error_types()
