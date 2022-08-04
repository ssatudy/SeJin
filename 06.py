
# input - babad / cbbd > bab / bb

#앞 > < 뒤 검사  똑같은 글자가 있으면 거기 인덱싱으로 앞 뒤로 돌려서 확인


def longestPalindrome(s) -> int:
    lst1 = []
    for i in range(1,len(s)+1):             
        if s[i-1] == s[-i]:
            lst1.append(s[i-1])
    
    
    return ''.join(lst1)

print(longestPalindrome("abccccdd"))