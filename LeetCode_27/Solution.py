from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


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