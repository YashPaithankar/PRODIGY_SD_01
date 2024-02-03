def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter():
    print("Welcome to the Temperature Converter!")

    # Get user input
    choice = input("Choose conversion direction (1: Celsius to Fahrenheit, 2: Fahrenheit to Celsius, 3: Celsius to Kelvin, 4: Kelvin to Celsius, 5: Fahrenheit to Kelvin, 6: Kelvin to Fahrenheit): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        temperature = float(input("Enter the temperature value: "))

        if choice == '1':
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is equal to {result} Fahrenheit.")
        elif choice == '2':
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is equal to {result} Celsius.")
        elif choice == '3':
            result = celsius_to_kelvin(temperature)
            print(f"{temperature} Celsius is equal to {result} Kelvin.")
        elif choice == '4':
            result = kelvin_to_celsius(temperature)
            print(f"{temperature} Kelvin is equal to {result} Celsius.")
        elif choice == '5':
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} Fahrenheit is equal to {result} Kelvin.")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} Kelvin is equal to {result} Fahrenheit.")
    else:
        print("Invalid choice. Please choose a valid option.")

# Run the temperature converter
temperature_converter()