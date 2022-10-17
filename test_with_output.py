from conversions import *
from conversions_refactored import convert

import unittest


class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 0
        result = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        celsius = 300
        result = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")

    def test_convertCelsiusToFahrenheit(self):
        celsius = 0
        result = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")

        result = convertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")

    def test_convertFahrenheitToCelsius(self):

        result = convertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        result = convertFahrenheitToCelsius(40)
        expected = 4.444444444444445
        self.assertAlmostEqual(result, expected, places=6)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")        

    def test_convertFahrenheitToKelvin(self):

        result = convertFahrenheitToKelvin(32)
        expected = 273.15
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        result = convertFahrenheitToKelvin(40)
        expected = 277.59444444444443
        self.assertAlmostEqual(result, expected, places=6)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
    def test_convertKelvinToCelsius(self):
        kelvin = 0
        result = convertKelvinToCelsius(kelvin)
        expected = -273.15
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        kelvin = 300
        result = convertKelvinToCelsius(kelvin)
        expected = 26.85
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
    def test_convertKelvintoFahrenheit(self):
        kelvin = 0
        result = convertKelvintoFahrenheit(kelvin)
        expected = -459.67
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        kelvin = 300
        result = convertKelvintoFahrenheit(kelvin)
        expected = 80.33
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
    def test_convertMilesToMeters(self):
        miles = 0
        result = convertMilesToMeters(miles)
        expected = 0
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        miles = 1
        result = convertMilesToMeters(miles)
        expected = 1609.34
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")

    def test_convertMetersToMiles(self):
        meters = 0
        result = convertMetersToMiles(meters)
        expected = 0
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        meters = 1609.34
        result = convertMetersToMiles(meters)
        expected = 1
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
              
    def test_convertYardsToMeters(self):
        yards = 0
        result = convertYardsToMeters(yards)
        expected = 0
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        yards = 1
        result = convertYardsToMeters(yards)
        expected = 0.9144
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
             
    def test_convertMetersToYards(self):
        meters = 0
        result = convertMetersToYards(meters)
        expected = 0
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")
        
        meters = 0.9144
        result = convertMetersToYards(meters)
        expected = 1
        self.assertEqual(result, expected)
        print("\n====================================")
        print("Expected: " + str(expected))
        print("Result: " + str(result))
        print("Test passed: " + str(result == expected))
        print("====================================")  

    def test_convert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)

        celsius = 0
        result = convert("Celsius", "Fahrenheit", celsius)
        expected = 32
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
