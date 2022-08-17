'''
애너그램 판별
'''
s1 = 'anagram'
t1 = 'nagaram'
# True

s2 = 'rat'
t2 = 'car'
# False


def ana(s1,t1):
    want = list(t1.strip())
    for i in want:
        if i in s1:
            return True
        else:
            return False

print(ana(s2,t2))