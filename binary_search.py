"""
Given an array of integers, nums, sorted in ascending order, and an integer value, target.
If the target exists in the array, return its index.
If the target does not exist, then return -1.
"""


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        # find the middle index
        # floor division can also be used: for mid = low + ((high - low) // 2)
        mid = (low + high) // 2
        # if target is the mid-element
        if target == nums[mid]:
            return mid
        # search in left sub array
        if target < nums[mid]:
            high = mid - 1
        # search in right sub array
        if target > nums[mid]:
            low = mid + 1

    # Target value is not found
    return -1


def driver_prog():
    nums_lists = [[], [0, 1], [1, 2, 3], [-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]]
    target_list = [99, 1, 333, 9, 255]
    for i in range(len(nums_lists)):
        nums = nums_lists[i]
        target = target_list[i]
        index = binary_search(nums, target)
        print(str(i + 1) + ". Array to search: " + str(nums))
        print("   Target: " + str(target))
        if index != -1:
            print("   " + str(target) + " exists in the array at index", index)
        else:
            print("   " + str(target) + " does not exist in the array so the return value is", index)
        print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    driver_prog()
