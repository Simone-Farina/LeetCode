from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        for idx, i in enumerate(nums):
            n = target - i
            n_idx = Solution.findIndex(nums, n, idx)

            if n_idx != None:
                return [idx, n_idx]

    @staticmethod
    def findIndex(nums: List[int], target: int, current: int):
        for idx, n in enumerate(nums):
            if n == target and current != idx:
                return idx
        return None


def main():
    n = Solution.twoSum(nums=[3, 2, 4], target=6)
    print(n)


if __name__ == '__main__':
    main()


