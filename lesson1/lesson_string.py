def function(n):
    for i in range(1, n + 1):
       for k in range(1, n + 1):
           print(f' i = {i}')
           print(f' k = {k}')
           print(i * k)
function(3)



str = "This is a \"string\""
print(str)

str = "This is a string"
if 'b' in str:
    print("b is in our string!")
else:
    print("b is not in our string!")
print(str[0]) # T
print(str[-1]) #g
print(str[:3]) #Thi
print(str[5:8]) # start to stop
print(str[8:])
#concatenation
str_1 = "My name is Laxmi."
str_2 = "I am a Software Engineer."
print(str_1 + " " + str_2)
for char in str_1:
    print(char)

str_3 = "hello"
for letter in str_3:
    print(letter)
print(len(str_3))

str_4 = "HELLO"
print(str_4.lower())

str_5 = "software qa engineer"
print(str_5.upper())

str_6 = "This is a split method"
print(str_6.split())
print(str_6.split('i'))

list_str = ['This', 'is', 'a', 'list', 'of', 'string']
print(" ".join(list_str))

strip_7 = "  This is a strip method  " # all the white spaces from the begining and end removed
print(strip_7.strip())

strip_8 = "111  Hello world  1 11"
print(strip_8.strip('1'))
str_8 = "This is a replace method"
print(str_8.replace('i', '!'))
print(str_8.find('p'))
string_w_argument = '5 + 5 = {}'
print(string_w_argument.format('10'))
value = 6 + 4
print(f'6 + 4 = {value}')

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}

    for letter in s1:
        if letter in count:
            count[letter]  += 1
        else:
             count[letter] = 1

    for letter in s2:
        if letter in s2:
            count[letter]  -= 1
        else:
             count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False

    return True
        #return sorted(s1) == sorted(s2)
test1_pos = 'abcd'
test2_pos = 'badc'
test1_neg = 'abcd'
test2_neg = 'abca'
print(is_anagram(test1_pos, test2_pos))
print(is_anagram(test1_neg, test2_neg))


def is_palindrome(s):
    return s == s[::-1] # string[:start:stop:step]
test_s_pos = 'radar'
test_s_neg = 'radax'
print(is_palindrome(test_s_pos))
print(is_palindrome(test_s_neg))

def is_almost_palindrome(s):
    for i in range(len(s)):
        temp_s = s[:1] + s[i + 1:]
        if temp_s == temp_s[::-1]:
            return True

    return False
test_s_pos = 'radar'
test_s_neg = 'radario'
print(is_almost_palindrome(test_s_pos))
print(is_almost_palindrome(test_s_neg))











