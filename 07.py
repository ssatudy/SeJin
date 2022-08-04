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
        findnum = target - i
        if findnum in nums:
            findall.append(i)

    return nums.index(findall[0]) , nums.index(findall[1])

print(findnum(nums,target))
