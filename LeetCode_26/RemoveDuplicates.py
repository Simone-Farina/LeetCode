from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0

        for idx, i in enumerate(nums):
            if i in nums[idx+1:]:
                nums[idx] = '_'
            else:
                result += 1

        return result

def main():
    s = Solution()
    l = [1, 1, 1]
    l1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(l1))
    print(s.removeDuplicates(l))
    print(l1)
    print(l)


if __name__ == '__main__':
    main()