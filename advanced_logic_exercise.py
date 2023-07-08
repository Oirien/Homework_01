# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
dataset = [11, 6, 4, 99, 7, 11]
test_data = [5, 13, 2]
# 1. Print out a list of the even integers:

def even_numbers(list_of_numbers):
    return list(filter(lambda x: (x % 2 == 0), list_of_numbers))

print(even_numbers(numbers))

# 2. Print the difference between the largest and smallest value:

def difference(list_of_numbers):
    return max(list_of_numbers) - min(list_of_numbers)

print(difference(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

def two_twos(list_of_numbers):
    last = list_of_numbers[0]
    for num in list_of_numbers[1:]:
        if num == last:
            if num == 2:
                return True
        last = num
    return False

print(two_twos(numbers))

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

def sum_skipping(list_of_numbers):
    sum_total = iter(list_of_numbers)
    total = 0
    for num in sum_total:
        if num == 6:
            7 in sum_total
        else:
            total += num
    return total
    
print(sum_skipping(numbers))

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# def unlucky_sum(list_of_numbers):
#     sum_total = iter(list_of_numbers)
#     total = 0
#     for num in list_of_numbers:
#         if num == 13:
#             13 in sum_total
#         else:
#             total += num
#     return total

# def unlucky_sum(list_of_numbers):
#     skip_until = -1
#     total = 0
#     for num in list_of_numbers:
#         if num == 13:
#             skip_until += 13
#         else:
#             total += num
#     return total

def unlucky_sum(list_of_numbers):
    total = 0
    iteration = 0
    while iteration < len(list_of_numbers):
        if list_of_numbers[iteration] == 13:
            iteration += 2
        else:
            total += list_of_numbers[iteration]
            iteration += 1
    return total

# sum([i for i in list_of_numbers if i != 13 and i-1 != 13]))
# solution I got given as an example after I had completed it.

print(unlucky_sum(test_data))
print(unlucky_sum(numbers))