from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        # iterate arbitrarily over the first string
        for idx, c in enumerate(strs[0]):
            for str_ in strs[1:]:
                if idx == len(str_) or c != str_[idx]:
                    return res
            res += c
        return res

def main():
    s = Solution()
    print(str(['ab', 'a']) + ': ' + s.longestCommonPrefix(['ab', 'a']))
    print(str(['flower', 'flow', 'flight']) + ' : ' + s.longestCommonPrefix(['flower', 'flow', 'flight']))
    print(str(['dog', 'car', 'airplane']) + ': ' + s.longestCommonPrefix(['dog', 'car', 'airplane']))
    
if __name__ == '__main__':
    main()

