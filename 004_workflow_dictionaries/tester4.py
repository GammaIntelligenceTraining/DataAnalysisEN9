# side = float(input('Enter side a: '))

try:
    sideA = float(input('Enter side a: '))
    sideB = float(input('Enter side b: '))
    sideC = float(input('Enter side c: '))
    idcode = input("Enter ID code: ")
    if len(idcode) != 11:
        raise Exception
except ValueError:
    print("Side must be a number!")
except ZeroDivisionError:
    print("Can't divide by 0")
except Exception:
    print('ID code must be 11 digits long')
else:
    print('A =', sideA)
    print('B =', sideB)
    print('C =', sideC)
finally:
    print('Finally clause')
