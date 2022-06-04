#The equation for fibonacci sequence:
#Equation:
# f0 = 0
# f1 = 1
# f2 = 1
# Fn = Fn-1 + Fn-2

#Fibonacci Sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21,
#O(n)
fib_number = int(input('Provide a number: '))
index = 3
fib_1 = 1
fib_2 = 1
result = [fib_1, fib_2]
while index <= fib_number:
    result.append(fib_1 + fib_2)
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index = index + 1 # index += 1
print(result)