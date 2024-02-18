from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        # Пошук пар чисел, що складаються до цільового значення
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)

        return result


# Приклад використання
if __name__ == "__main__":
    solution = Solution()

    # Приклад вхідних даних
    input_nums = [2, 7, 11, 15]
    target_sum = 9

    # Виклик методу twoSum
    result_indices = solution.twoSum(input_nums, target_sum)

    # Виведення результату
    print("Результат:", result_indices)
