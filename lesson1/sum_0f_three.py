from random import randint
random_number = randint(100, 999)
print(f'My random is: {random_number}')

result = 0
#for digit in str(random_number): # 349 -> [3, 4, 9]string

    #result = result + int(digit)
#print(f'result: {result}')
#O(n) time comflexcity. n = length of the random_number
while random_number != 0:
    result = result + (random_number % 10)
    random_number = random_number // 10
print(f'result: {result}')
