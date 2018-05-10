from function_odd_even import odd_even,single_double

value=odd_even(9)
if value:
    print('Odd')
else:
    print('Even')

var = single_double(10)
if var is 1:
    print('Number is Single digit')
elif var is 2:
    print('Number is double digit')
else:
    print('Number is neither single digit nor double digit')