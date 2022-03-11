from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for idx, c in enumerate(strs[0]):
            for str_ in strs[1:]:
                if idx == len(str_) or c != str_[idx]:
                    return res
            res += c
        return res

def main():
    s = Solution()
    print(s.longestCommonPrefix(['ab', 'a']))
    
if __name__ == '__main__':
    main()

