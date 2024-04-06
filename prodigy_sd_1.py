def c_to_f(celsius):
    return (celsius * 9/5) + 32

def c_to_k(celsius):
    return celsius + 273.15

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def f_to_k(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def k_to_c(kelvin):
    return kelvin - 273.15

def k_to_f(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit of measurement (C, F, or K): ").upper()

    if original_unit == "C":
        fahrenheit = c_to_f(temperature)
        kelvin = c_to_k(temperature)
        print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif original_unit == "F":
        celsius = f_to_c(temperature)
        kelvin = f_to_k(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif original_unit == "K":
        celsius = k_to_c(temperature)
        fahrenheit = k_to_f(temperature)
        print(f"{temperature} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
