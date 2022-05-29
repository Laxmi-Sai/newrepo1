#O(1)
a = int(input('Input value a: '))
b = int(input('Input value b: ' ))

#print(f'a = {a}, b = {b}')

#temp = a
#a = b
#b = temp
#print(f'a ={a}, b = {b}')'''
#a, b = b, a
#print(f'a ={a}, b = {b}')
a, b = b, a
#print(f'a = {a}, b = {b}')
a = a + b  # 10 + 5 = 15
b = a - b  # 15 - 5 = 10
a = a - b  # 15 - 10 = 5
print(f'a = {a}, b = {b}')