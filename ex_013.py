celsius = float(input('Qual é a temperatura em °C'))
# Fórmula de Celcius para Fahrenheit
faren = (celsius*9/5) + 32
# Fórmula de Celcius para Kelvin
kelvin = celsius + 273.15

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F e a {:.1f}K'.format(celsius,faren,kelvin))
