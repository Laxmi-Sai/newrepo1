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
        if letter in count:
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
