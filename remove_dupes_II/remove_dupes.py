def remove_dupes(nums): 
    n = len(nums)
    read = 2 
    write = 2

    while read < n: 
        if nums[write - 2] != nums[read]: 
            nums[write] = nums[read]
            write += 1 
        read += 1
    return write 

