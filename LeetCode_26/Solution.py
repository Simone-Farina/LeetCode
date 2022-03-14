from typing import List

'''
Solution using two pointers technique
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 1

        while right != len(nums):
            if nums[right] != nums[right-1]:
               nums[left] = nums[right]
               left += 1
            
            right += 1
        
        return left


def main():
    s = Solution()
    l = [0, 0, 1, 1, 1, 2, 3, 3, 4]
    print(s.removeDuplicates(l))
    print(l)

if __name__ == '__main__':
    main()