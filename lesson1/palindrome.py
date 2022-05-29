def is_palindrome(s):
    return s == s[::-1] # string[:start:stop:step]
test_s_pos = 'radar'
test_s_neg = 'radax'
print(is_palindrome(test_s_pos))
print(is_palindrome(test_s_neg))