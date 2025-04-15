nums = [1,3,-1,-3,5,3,6,7]
k = 3

def SlidingWindowMax(nums, k):
    i=0
    MSum = 0
    while(k<=len(nums)):
        crsm = sum(nums[i:k])
        MSum = max(crsm, MSum)
        i+=1
        k+=1
    return MSum

print(SlidingWindowMax(nums, k))