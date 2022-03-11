from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for idx, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[n] = idx
        return


def main():
    s = Solution()
    result = s.twoSum([2, 1, 5, 3], 4)
    print(result)

if __name__ == '__main__':
    main()

    