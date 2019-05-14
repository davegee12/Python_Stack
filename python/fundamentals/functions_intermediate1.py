import random
def randInt(min = 0 , max = 100):
    if min > max:
        return "Error: Min must be < Max"
    elif max < 0:
        return "Error: Max must be > 0"
    num = random.random()* (max-min) + min
    return num

# print(randInt(max = 50))
# print(randInt(min = 50))
# print(randInt(min=50, max=500))
# print(randInt(min=100, max=50))