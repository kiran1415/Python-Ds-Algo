def binary_search(nums, target):
    low = 0
    high = len(nums)-1

    while low < high:
        mid = (low+high) //2
        if nums[mid] <= target:
            low = mid+1
        else:
            high = mid
    return low, high



nums = [1,4,4,4,5,6,7,8,9,10]
target = 4

print(binary_search(nums, target))
