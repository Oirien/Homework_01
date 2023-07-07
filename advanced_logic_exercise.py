# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

def even_numbers(list_of_numbers):
    return list(filter(lambda x: (x % 2 == 0), list_of_numbers))

print(even_numbers(numbers))

# 2. Print the difference between the largest and smallest value:

def difference(list_of_numbers):
    return max(list_of_numbers) - min(list_of_numbers)

print(difference(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

def check(lst):
    last = lst[0]
    for num in lst[1:]:
        if num == last:
            if num == 2:
                return True
        last = num
    return False

print(check(numbers))

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 






