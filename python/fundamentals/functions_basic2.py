# Countdown

def Countdown(x):
    empty_list = []
    for i in range(x, -1, -1):
        empty_list.append(i)
    return empty_list

Countdown(5)

# Print and Return

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([7,3])

# First Plus Length

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second

def values_greater_than_second(list):
    newList = []
    if len(list) <= 2:
        return False
    for i in range(len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    print(len(newList))
    return newList

print(values_greater_than_second([5,2,3,2,1,4]))

# This Length, That Value

def length_and_value(a,b):
    berry = []
    for i in range(0, a, 1):
        berry.append(b)
    return berry

print(length_and_value(6,2))