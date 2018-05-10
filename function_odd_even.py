def odd_even(number):
    if number % 2 == 0:
        return 0
    else:
        return 1

def single_double(number):
    if number>0 and number<10:
        return 1
    elif number>9 and number<100:
        return 2
    else:
        return 3