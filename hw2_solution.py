#Split in Half
# 1. Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’

# aaaccc -> cccaaa
# aaabccc -> cccaaab
#O(1)
def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0

    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]
    print(f'left = {left}')
    print(f'right = {right}')

    print(right + left)

test_data_even = 'aaaccc'    # -> cccaaa
test_data_odd = 'aaabccc'    # -> cccaaab
(split_in_half(test_data_even))
(split_in_half(test_data_odd))


#Unique Characters in String
# 2. Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

# abcde -> True
# abcdd -> False

def uni_char(s):
    return (len(set(s))) == len(s)

test_data_all_uni = 'abcde'
test_data_dup = 'abcdd'

print(uni_char(test_data_all_uni))
print(uni_char(test_data_dup))
# abc
# {a, b, c} 3 == 3 -> True
# abb, {a, b} 2 == 3 -> False
