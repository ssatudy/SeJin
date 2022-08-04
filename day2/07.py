'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자의 인덱스를 리턴
'''

nums = [2, 7, 11, 15]
target = 9
# [0, 1]

#두 숫자만 가능함 
def findnum(nums,target):         
    findall = []
    for i in nums:               
        findnum = target - i             #찾을 숫자를 설정
        if findnum in nums:              #숫자열에서 찾음
            findall.append(i)

    return nums.index(findall[0]) , nums.index(findall[1])  #인덱스를 출력

print(findnum(nums,target))   # 문제점 : 한 숫자열에서만 작동을 안함;
