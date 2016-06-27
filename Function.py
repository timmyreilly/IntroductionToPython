def calculate_temperature(kelvin):
    celsius = kelvin - 273.0
    fahrenheit = celsius * 9 / 5 + 32 
    return celsius, fahrenheit

c, f = calculate_temperature(340)

print c, f 