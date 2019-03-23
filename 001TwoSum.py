def twoSum(nums,target):
    if len(nums) <= 1:
        return False
    diction = {}
    for i in range(0, len(nums)):
        dif = target-nums[i]
        if dif in diction:
            return [diction[dif],i]
        else:
            diction[nums[i]]=i

if __name__=='__main__':
    nums=[3,2,4]
    target = 6
    print(twoSum(nums,target))