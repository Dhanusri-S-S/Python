# Simple weather checker (no internet needed)

# Ask user for temperature
temperature = float(input("Enter the temperature in °C: "))

# Check weather condition using if-else
if temperature > 35:
    print("It's very hot outside")
elif temperature > 25:
    print("It's warm outside")
elif temperature > 15:
    print("It's a nice cool weather")
else:
    print("It's cold outside")