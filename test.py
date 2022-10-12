from conversions import*
from conversions_refactored import convert

print("Celsius to kelvin and fahrenheit")
print(convertCelsiusToKelvin(300.00),"K")
print(convertCelsiusToFahrnite(300.00),"F")

print("fahrenheit to celsius and kelvin")
print(round(convertFahrenheittoCelsius(300.00),3),"C")
print(round(convertFahrenheitToKelvin(300.00),3),"K")


print("************Using single function perform all conversion************")
print(convert("celsius","kelvin",300.00),"K")
print(convert("celsius","fahrenheit",300.00),"C")


print(convert("meter","yard",50.00),"yards")
print(convert("yard","meter",300.00),"m")

print(convert("celsius","metre",4));


