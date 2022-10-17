from conversions import *

class ConversionNotPossible(Exception):

    def __init__(self, message):
        self.message = message

        def __str__(self):
            return self.message


def convert(from_units, to_units, value):

    from_lcase = from_units.lower()
    to_lcase = to_units.lower()

    if from_lcase == 'celsius' and to_lcase == "kelvin":
        return convertCelsiusToKelvin(value)
    elif from_lcase == 'celsius' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    elif from_lcase == "miles" and to_lcase == "meters":
        return convertMilesToMeters(value)
    elif from_lcase == "miles" and to_lcase == "yards":
        return convertMilesToYards(value)
    elif from_lcase == "yards" and to_lcase == "miles":
        return convertYardsToMiles(value)
    elif from_lcase == "yards" and to_lcase == "meters":
        return convertYardsToMeters(value)
    elif from_lcase == "meters" and to_lcase == "miles":
        return convertMetersToMiles(value)
    elif from_lcase == "meters" and to_lcase == "yards":
        return convertMetersToYards(value)
    elif from_lcase == "fahrenheit" and to_lcase == "celsius":
        return convertFahrenheitToCelsius(value)
    elif from_lcase == "fahrenheit" and to_lcase == "kelvin":
        return convertFahrenheitToKelvin(value)
    elif from_lcase == "kelvin" and to_lcase == "celsius":
        return convertKelvinToCelsius(value)
    elif from_lcase == "kelvin" and to_lcase == "fahrenheit":
        return convertKelvintoFahrenheit(value)
    
    elif from_lcase == "miles" and to_lcase == "fahrenheit":
        raise ConversionNotPossible("Cannot convert miles to fahrenheit")
    elif from_lcase == "miles" and to_lcase == "kelvin":
        raise ConversionNotPossible("Cannot convert miles to kelvin")
    elif from_lcase == "yards" and to_lcase == "fahrenheit":
        raise ConversionNotPossible("Cannot convert yards to fahrenheit")
    elif from_lcase == "yards" and to_lcase == "kelvin":
        raise ConversionNotPossible("Cannot convert yards to kelvin")
    elif from_lcase == "meters" and to_lcase == "fahrenheit":
        raise ConversionNotPossible("Cannot convert meters to fahrenheit")
    elif from_lcase == "meters" and to_lcase == "kelvin":
        raise ConversionNotPossible("Cannot convert meters to kelvin")
    elif from_lcase == "fahrenheit" and to_lcase == "miles":
        raise ConversionNotPossible("Cannot convert fahrenheit to miles")
    elif from_lcase == "fahrenheit" and to_lcase == "yards":
        raise ConversionNotPossible("Cannot convert fahrenheit to yards")
    elif from_lcase == "fahrenheit" and to_lcase == "meters":
        raise ConversionNotPossible("Cannot convert fahrenheit to meters")
    elif from_lcase == "kelvin" and to_lcase == "miles":
        raise ConversionNotPossible("Cannot convert kelvin to miles")
    elif from_lcase == "kelvin" and to_lcase == "yards":
        raise ConversionNotPossible("Cannot convert kelvin to yards")
    elif from_lcase == "kelvin" and to_lcase == "meters":
        raise ConversionNotPossible("Cannot convert kelvin to meters")
    else:
        return None


