def j():
    def Cel_To_Fah(n):
        m = (n * 9 / 5) + 32
        return m


    def Celsius_to_Kelvin(C):
        return (C + 273.15)

    inp = input('enter 1 Cel_To_Fah enter 2 Celsius_to_Kelvin')
    if (inp == 1				):
        m = input('enter Celsius')
        n=float(m)

        print(Cel_To_Fah(n))
    else:
        m= input('enter Celsius')
        C=float(m)
        print("Temperature in Kelvin ( K ) = ",
              Celsius_to_Kelvin(C))


j()
j()


