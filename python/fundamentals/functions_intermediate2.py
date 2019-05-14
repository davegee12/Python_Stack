#1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0] ['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#2 Iterate through a list of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for i in range(len(list)):
        display_str = ''
        for key, val in list[i].items():
            display_str += f"{key} - {val}"
        display_str = display_str[len(display_str)]
        print(display_str)

iterateDictionary(students)

#3 Get Values from a list of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterateDictionary2(key_name, list):
    for thing in list:
        print(thing[key_name])

iterateDictionary2('first_name', students)

#4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f"{len(val)} {key.upper()}")
        for x in val:
            print(x)

printInfo(dojo)

# BubbleSort

def bubbleSort(input_list):
    for i in input_list:
        for j in input_list:
            if input_list[j] > input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

hippo = [3,5,1,8,7,2,4,6]

# Selection Sort

def selectionSort(pizza):
    for j in range(len(pizza)):
        mini = j
        for i in range(len(pizza)):
        if pizza[i] < pizza[mini]:
            mini = i
    pizza[j], pizza[mini] = pizza[mini], pizza[j]
    return pizza

print(selectionSort(hippo))
