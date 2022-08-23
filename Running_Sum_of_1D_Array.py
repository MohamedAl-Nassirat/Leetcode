
for i in range(len(nums)):
    total += nums[i]
    nums[i] = total
    
return(nums)