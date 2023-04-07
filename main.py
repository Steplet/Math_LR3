import Parser as p
import Simpson_method as s


file = open("input_file", 'r')

function = file.readline()
function = p.pars(function)

a = float(input("Left border: "))
b = float(input("Right border: "))

while (True):
    n = int(input("Number of dividesion: "))
    if n % 2 != 0:
        print("Number of dividesion must be evan")
    else:
        break


result = s.simpson_method(function, a, b, n)


print('\nResult: ', result)


