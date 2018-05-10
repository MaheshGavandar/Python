def print_string(string):
    print('Hello ', string)
    return


print_string('Mahesh')
print_string('Andrew')

def print_info(name,age='27'):
    print('Name is ',name)
    print('Age is ', age)
    return

print('Mahesh')
print('Andrew',40)

def find_arguments(arg1,*arglist):
    print(arg1)
    for l in arglist:
        print(l)

find_arguments(1,2,3,4,5,6,7,8,9)
