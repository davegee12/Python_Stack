# Biggie Size

def biggie_size(list):
    for i in range(0,len(list),1):
        if list[i] > 0:
            list[i] = "big"
    return list

apple = [-1, 3, 5, -5]
print(biggie_size(apple))

# Count Positives

def count_positives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list[len(list) - 1] = count
    return list

exam1 = [-1,1,1,1]
exam2 = [1,6,-4,-2,-7,-2]
print(count_positives(exam2))

# Sum Total

def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

test1 = [1,2,3,4]
test2 = [6,3,-2]
print(sum_total(test2))

# Average

def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    avg = sum / float(len(list))
    return avg

banana = [1,2,3,4]
print(average(banana))

# Length

def length(list):
    return len(list)

pizza1 = [37,2,1,-9]
pizza2 = []
print(length(pizza2))

# Minimum

def minimum(list):
    if len(list) < 1:
        return False
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]

    return min

cake1 = [37,2,1,-9]
cake2 = []
print(minimum(cake2))

# Maximum

def maximum(list):
    if len(list) < 1:
        return False
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]

    return max

cake1 = [37,2,1,-9]
cake2 = []
print(maximum(cake2))

# Ultimate Analysis

def ultimate_analysis(list):
    sum = 0
    max = list[0]
    min = list[0]
    length = len(list)
    for i in range(len(list)):
        sum += list[i]
        if list[i] < min:
            min = list[i]
        elif list[i] > max:
            max = list[i]
    avg = float(sum / length)
    ult_an = {
    "sumTotal": sum,
    "average": avg,
    "minimum": min,
    "maximum": max,
    "length": length
    }
    return ult_an

cake1 = [37,2,1,-9]
print(ultimate_analysis(cake1))

# Reverse List

def reverse_list(list):
    j = len(list)-1
    for i in range(len(list)/2):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        j = j - 1
    return list

cake1 = [37,2,1,-9]
print(reverse_list(cake1))