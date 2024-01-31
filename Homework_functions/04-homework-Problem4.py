def celsius(temp_xf):
    return (temp_xf - 32) * 5 / 9


def fahrenheit(temp_xc):
    return temp_xc * (9 / 5) + 32


print(f'The temperature in °C is: {celsius(40):.1f}')
print(f'The temperature in °F is: {fahrenheit(4):.1f}')
