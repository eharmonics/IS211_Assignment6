def temp_conversion(temp, current_unit, to_be_convered):

    if to_be_convered == "F" and current_unit == "C":
        new_temp = round(9 / 5 * temp + 32, 3)
        print("The converted temperature in Fahrenhite scale is " + str(new_temp) + " degrees")

    elif to_be_convered == "C" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32), 3)
        print("The converted temperature in Celcius scale is " + str(new_temp) + " degrees")

    elif to_be_convered == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")

    elif to_be_convered == "C" and current_unit == "K":
        new_temp = round(temp - 273.15, 3)
        print("The converted temperature in Celcius scale is " + str(new_temp) + " degrees")

    elif to_be_convered == "F" and current_unit == "K":
        new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
        print("The converted temperature in Fahrenhite scale is " + str(new_temp) + " degrees")

    else:
        new_temp = round(5 / 9 * (temp - 32) + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")


temp_conversion(108, "C", "F")
temp_conversion(235.685, "K", "F")


