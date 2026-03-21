def rotate_array(nums): 
    nums_copy = nums.copy() 
    n = len(nums)

    for i in range(n): 
        nums[(i + k) % n] = nums_copy[i]


