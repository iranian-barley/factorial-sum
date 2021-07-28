import math


def factorialSum(num):
    rem = sum = 0

    # Calculates the sum of factorials of digits
    while num > 0:
        rem = num % 10
        sum = sum + (math.factorial(rem))
        num = num // 10
    return sum


num = 1
result = num

# print("List of numbers not in big circle ")
for i in range(1, 1000000):  # range to 1000000 in this example
    my_result = i
    while (
            my_result != 1 and my_result != 2 and my_result != 169 and my_result != 871 and my_result != 145 and my_result != 872 and my_result != 40585):
        my_result = factorialSum(my_result)
    # print(str(i))
    if my_result == 145:  # lists all numbers resulting in cycle n=145 in this example
        print(str(i))
