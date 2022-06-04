import math
#O(n)
number = int(input('Input a number: '))
result = 1
#for i in range(1, number + 1):
   # result = result * i # resullt += 1
result = math.factorial(number)
print(f'result: {result}')




