from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = r = 0

        while r != len(nums):
            if nums[r] == val:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1

        return l


def main():
    s = Solution()
    l = [0, 1, 2, 2, 3, 0, 4, 2]
    l1 = [3, 2, 2, 3]
    print(s.removeElement(l, 2))
    print(l)
    print(s.removeElement(l1, 3))
    print(l1)
    
if __name__ == '__main__':
    main()

