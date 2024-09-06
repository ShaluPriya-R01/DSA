class Solution:
    def rotate(self, nums, k):
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))

STEPS:
1. Find the actual number of steps to rotate by using `k %= len(nums)` (this handles cases where `k` is larger than the list length).
2. Reverse the whole list.
3. Reverse the part after the rotation point.
4. Reverse the first part of the list.
