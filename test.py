from conversions import *
from conversions_refactored import convert

import unittest


class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 0
        result = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)

    def test_convertCelsiusToFahrenheit(self):

        result = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)

    def test_convertFahrenheitToCelsius(self):

        result = convertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(40)
        expected = 4.444444
        self.assertAlmostEqual(result, expected, places=6)

    def test_convertFahrenheitToKelvin(self):

        result = convertFahrenheitToKelvin(32)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertFahrenheitToKelvin(40)
        expected = 277.594444
        self.assertAlmostEqual(result, expected, places=6)

    def test_convertKelvinToCelsius(self):
        kelvin = 0
        result = convertKelvinToCelsius(kelvin)
        expected = -273.15
        self.assertEqual(result, expected)

        kelvin = 300
        result = convertKelvinToCelsius(kelvin)
        expected = 26.85
        self.assertEqual(result, expected)

    def test_convertKelvintoFahrenheit(self):
        kelvin = 0
        result = convertKelvintoFahrenheit(kelvin)
        expected = -459.67
        self.assertEqual(result, expected)

        kelvin = 300
        result = convertKelvintoFahrenheit(kelvin)
        expected = 80.33
        self.assertEqual(result, expected)

    def test_convertMilesToMeters(self):
        miles = 0
        result = convertMilesToMeters(miles)
        expected = 0
        self.assertEqual(result, expected)

        miles = 1
        result = convertMilesToMeters(miles)
        expected = 1609.34
        self.assertEqual(result, expected)

    def test_convertMetersToMiles(self):
        meters = 0
        result = convertMetersToMiles(meters)
        expected = 0
        self.assertEqual(result, expected)

        meters = 1609.34
        result = convertMetersToMiles(meters)
        expected = 1
        self.assertEqual(result, expected)
        
    def test_convertYardsToMeters(self):
        yards = 0
        result = convertYardsToMeters(yards)
        expected = 0
        self.assertEqual(result, expected)

        yards = 1
        result = convertYardsToMeters(yards)
        expected = 0.9144
        self.assertEqual(result, expected)
        
    def test_convertMetersToYards(self):
        meters = 0
        result = convertMetersToYards(meters)
        expected = 0
        self.assertEqual(result, expected)

        meters = 0.9144
        result = convertMetersToYards(meters)
        expected = 1
        self.assertEqual(result, expected)
    

    def test_convert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)

        celsius = 0
        result = convert("Celsius", "Fahrenheit", celsius)
        expected = 32
        self.assertEqual(result, expected)
        
        fahrenheit = 32
        result = convert("Fahrenheit", "Celsius", fahrenheit)
        expected = 0
        self.assertEqual(result, expected)
        
        fahrenheit = 32
        result = convert("Fahrenheit", "Kelvin", fahrenheit)
        expected = 273.15
        self.assertEqual(result, expected)

        kelvin = 0
        result = convert("Kelvin", "Celsius", kelvin)
        expected = -273.15
        self.assertEqual(result, expected)
        
        kelvin = 0
        result = convert("Kelvin", "Fahrenheit", kelvin)
        expected = -459.67
        self.assertEqual(result, expected)
        
        miles = 0
        result = convert("Miles", "Meters", miles)
        expected = 0
        self.assertEqual(result, expected)
        
        miles = 1   
        result = convert("Miles", "Meters", miles)
        expected = 1609.34
        self.assertEqual(result, expected)
        
        meters = 0
        result = convert("Meters", "Miles", meters)
        expected = 0
        self.assertEqual(result, expected)
        
        meters = 1609.34
        result = convert("Meters", "Miles", meters)
        expected = 1
        self.assertEqual(result, expected)
        
        yards = 0
        result = convert("Yards", "Meters", yards)
        expected = 0
        self.assertEqual(result, expected)
        
        yards = 1
        result = convert("Yards", "Meters", yards)
        expected = 0.9144
        self.assertEqual(result, expected)

            
        meters = 0
        result = convert("Meters", "Yards", meters)
        expected = 0
        self.assertEqual(result, expected)

        meters = 0.9144
        result = convert("Meters", "Yards", meters)
        expected = 1
        self.assertEqual(result, expected)
        
            


if __name__ == "__main__":
    unittest.main()

