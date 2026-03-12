def fun(nums, max_operations):
    def f(mid):
        b=0
        for i in nums:
            b=b+(i-1)//mid
        return b<=max_operations
    low=1
    high=max(nums)
    ans=high
    while low<=high:
        mid=(low+high)//2
        if f(mid):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[2,4,8,2]
print(fun(nums,4))
