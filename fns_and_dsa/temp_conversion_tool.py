FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0


if __name__ == "__main__":
    temp_str = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temp_value = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit == 'F':
        c = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {c}°C")
    elif unit == 'C':
        f = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {f}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
