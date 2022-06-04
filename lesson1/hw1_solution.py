# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#O(n)
def sum_to_n_1(n):
    final_result = 0
    for x in range(n + 1):
        final_result += x
    return final_result
#O(1)much faster
def sum_to_n_2(n):
    return (n*(n + 1)) / 2
test_n = 5
#print(sum_to_n_2(test_n)) # 15

# 2. Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.
# O(1) always need to same time run this code
#number_1 = int(input('Input number 1: '))
#number_2 = int(input('Input number 2: '))
#number_3 = int(input('Input number 3: '))

def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
#print(find_max(number_1, number_2, number_3))

# 3. Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
#O(n) length of the entered number: 34560
def count_odd_even(n):
    odds = []
    evens = []

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds.append(current_digit)
        else:
            evens.append(current_digit)
        n = n // 10
    return ['Evens: ' + str(evens), 'Odds: ' + str(odds)]

print(count_odd_even(34560))    # Evens: 4, 6, and 0 and Odds: 3 and 5