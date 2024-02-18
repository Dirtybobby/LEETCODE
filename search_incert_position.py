from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in nums:
            if target == num:
                return nums.index(num)
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

solution = Solution()

nums = [1, 3, 6]
target = 5
print(solution.searchInsert(nums, target))
