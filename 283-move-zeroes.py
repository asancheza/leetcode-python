def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    print nums

    pos = 0
    for i in xrange(len(nums)):
        if nums[i]:
            print "Data", nums[i], nums[pos], nums[pos], nums[i]
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
            print nums

    return nums

print moveZeroes([0, 1, 0, 3, 12])
