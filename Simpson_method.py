import math as m


def simpson_method(function, a, b, n):
    h = (b-a)/n
    list_of_x = []

    x = 0
    result = 0
    odd_sum = 0
    evan_sum = 0

    for i in range(0, n+1):
        list_of_x.append(a+(i*h))

    for i in range(len(list_of_x)):
        if i == 0:
            x = list_of_x[i]

            try:
                result += eval(function)
            except ZeroDivisionError:
                print("\nFixed the gap by average value in point: ", x)
                x += 0.00001
                result += eval(function)
            except ValueError:
                return "Wrong interval"

        elif i == len(list_of_x) - 1:
            x = list_of_x[i]
            try:
                result += eval(function)
            except ZeroDivisionError:
                print("\nFixed the gap by average value in point: ", x)
                x -= 0.00001
                result += eval(function)
            except ValueError:
                return "Wrong interval"

        elif i % 2 == 0:
            x = list_of_x[i]
            try:
                evan_sum += eval(function)
            except ZeroDivisionError:
                print("\nFixed the gap by average value in point: ", x)
                x = list_of_x[i] + 0.00001
                fir = eval(function)
                x = list_of_x[i] - 0.00001
                sec = eval(function)
                x = (fir+sec)/2
                evan_sum += x
            except ValueError:
                return "Wrong interval"
        else:
            x = list_of_x[i]
            try:
                odd_sum += eval(function)
            except ZeroDivisionError:
                print("\nFixed the gap by average value in point: ", x)
                x = list_of_x[i] + 0.00001
                fir = eval(function)
                x = list_of_x[i] - 0.00001
                sec = eval(function)
                x = (fir + sec) / 2
                odd_sum += x
            except ValueError:
                return "Wrong interval"

    evan_sum *= 2
    odd_sum *= 4

    result += evan_sum + odd_sum
    result *= h/3

    return result
