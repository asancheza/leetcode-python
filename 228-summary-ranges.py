def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    # First element in the range
    start = nums[0]
    
    # End element in the range
    end = nums[0]

    res = []
    
    # Iterate every number starting from second one
    for i in xrange(1, len(nums)):
        print i
        # if second == first + 1 
        if nums[i] == nums[i-1] + 1:
            # Update end with the current 
            end = nums[i]
        else:
            # If not append start and end
            res.append(str(start) + "->" + str(end))
            start = nums[i]
            end = nums[i]
            print start,end
            
        if start == end and i == len(nums) - 1:
            res.append(str(start))

    return res

print summaryRanges([1,2,4,5,6,7,10])