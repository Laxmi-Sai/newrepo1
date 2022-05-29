#O(n)
def reverse_string(s):
    reverse_s = ''
    index = len(s) - 1
    while index >= 0:
         reverse_s += s[index]
         index -= 1
    return reverse_s
test_s = 'abcde'
print(reverse_string(test_s))
