#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    num = int(temp_str)
    if num >= 0 and num <= 40:
        return num
    elif num < 0:
        raise ValueError(f"{num}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{num}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    num = input("Write a number")
    print(f"Input data is '{num}'")
    try:
        input_temperature(num)
        print(f"Temperature is now {num}°C")
    except ValueError as e:
        print(f"Caught {input_temperature.__name__} error: {e}")
    finally:
        print("All test completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
