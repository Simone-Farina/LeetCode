from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
        
        return res


def main():
    s = Solution()
    print(str(['ab', 'a']) + ': ' + s.longestCommonPrefix(['ab', 'a']))
    print(str(['flower', 'flow', 'flight']) + ' : ' + s.longestCommonPrefix(['flower', 'flow', 'flight']))
    print(str(['dog', 'car', 'airplane']) + ': ' + s.longestCommonPrefix(['dog', 'car', 'airplane']))
    
if __name__ == '__main__':
    main()
