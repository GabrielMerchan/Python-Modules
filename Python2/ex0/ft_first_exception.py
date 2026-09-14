#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    num = int(temp_str)
    return num


def test_temperature() -> None:
    num = input("Write a number")
    print(f"Input data is '{num}'")
    try:
        input_temperature(num)
        print(f"Temperature is now {num}°C")
    except ValueError as e:
        print(f"Caught {e.__class__.__name__} error: {e}")
    finally:
        print("All test completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
