nums = [1,3,-1,-3,5,3,6,7]
k = 3

def SlidingWindowMax(nums, k):
    i=0
    res = []
    while(k<=len(nums)):
        newarr = nums[i:k]
        res.append(max(newarr))
        i+=1
        k+=1
    return res
print(SlidingWindowMax(nums, k))