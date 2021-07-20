def binary_search(nums,target):
    high = len(nums)
    low = 0

    while low < high:
        import pdb;pdb.set_trace()
        mid = int(high/2)
        if nums[mid] == target:
            return mid
        else:
            if target>nums[mid]:
                low = mid
            elif target<nums[mid]:
                high = mid
    return 0





nums = [1,3,5,6]
target = 2

print(binary_search(nums,target))