def maxSum(nums, k):
    MOD = 10**9 + 7
    bit_count = [0] * 32
    
    for num in nums:
        for b in range(32):
            if num & (1 << b):
                bit_count[b] += 1
    ans = 0

    for q in range(k):
        val = 0
        for b in range(32):
            if bit_count[b] > 0:
                val |= (1 << b)
                bit_count[b] -= 1
        
        ans = (ans + val * val) % MOD

    return ans
print(maxSum([2,5,6,8],2))
