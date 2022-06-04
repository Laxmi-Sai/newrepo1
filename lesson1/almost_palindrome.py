def is_almost_palindrome(s):
    for i in range(len(s)):
        temp_s = s[:1] + s[i + 1:]
        if temp_s == temp_s[::-1]:
            return True

    return False
test_s_pos = 'radkar'
test_s_neg = 'radario'
print(is_almost_palindrome(test_s_pos))
print(is_almost_palindrome(test_s_neg))