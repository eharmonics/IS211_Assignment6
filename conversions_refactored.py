def convert(fromUnit,toUnit,val):
    if(fromUnit=="celsius" and toUnit=="fahrenheit"):
        return 1.8*val+32
    elif fromUnit=="celsius" and toUnit=="kelvin":
        return val + 273.15
    elif toUnit=="celsius" and fromUnit=="fahrenheit":
        return float(5/9)*(val-32)
    elif toUnit=="kelvin" and fromUnit=="fahrenheit":
        return float(5/9)*(val+459.67)
    elif fromUnit=="kelvin" and toUnit=="fahrenheit":
       return (val-273.15)*float(9/5)+32
    elif fromUnit=="kelvin" and toUnit=="celsius":
        return val - 273.15

    #distance conversion
    elif fromUnit=="mile" and toUnit=="yard":
        return val*1760 
    elif fromUnit=="yard" and toUnit=="mile":
        return val/1760
    elif fromUnit=="mile" and toUnit=="meter":
        return val*1609.34
    elif fromUnit=="meter" and toUnit=="mile":
        return val/1609.34
    elif fromUnit=="meter" and toUnit=="yard":
        return val*1.094
    elif fromUnit=="yard" and toUnit=="meter":
        return val/1.094
    return Exception


