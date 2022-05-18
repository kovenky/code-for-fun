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


# def binary_search_rotated(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     if low > high:
#         return -1
#
#     while low <= high:
#         # calc mid
#         mid = low + (high - low) // 2
#
#         if target == arr[mid]:
#             return mid
#
#         # check if left half is sorted
#         if arr[low] <= arr[mid]:
#             # check if target is within low-mid range
#             if arr[low] <= target < arr[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             # check if target lies within mid-high range
#             if arr[mid] < target <= arr[high]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#
#         return -1
def binary_search_rotated(nums, target):
    start = 0
    end = len(nums) - 1

    if start > end:
        return -1

    while start <= end:

        # Finding the mid using floor division
        mid = start + (end - start) // 2

        # Target value is present at the middle of the array
        if nums[mid] == target:
            return mid

        # start to mid is sorted
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # mid to end is sorted
        else:
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
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

    target_list = [3, 6, 3, 6]
    nums_list = [[6, 7, 1, 2, 3, 4, 5], [6, 7, 1, 2, 3, 4, 5],
                 [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3]]

    for i in range(len(target_list)):
        print(str(i + 1) + ". Rotated array: ", nums_list[i])
        print("   target", target_list[i],  "found at index " +
              str(binary_search_rotated(nums_list[i], target_list[i])))
        print("*"*100)


if __name__ == '__main__':
    driver_prog()
