
# input - babad / cbbd > bab / bb

#앞 > < 뒤 검사  똑같은 글자가 있으면 거기 인덱싱으로 앞 뒤로 돌려서 확인


def longestPalindrome(s) -> int:
    lst1 = []
    for i in range(1,len(s)+1):    #i 를 문자열 수만큼으로 돌림   
        if s[i-1] == s[-i]:        #앞 뒤 같은 문자를 출력
            lst1.append(s[i-1])    #lst 에 넣음
    
    
    return ''.join(lst1)           #문자열로 받기 위해 join 사용

print(longestPalindrome("abccccdd"))     # 문제점 : 똑같은 글자가 없는 단어열에서 작동하지 않음