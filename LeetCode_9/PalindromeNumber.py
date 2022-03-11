class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


def main():
    s = Solution()
    print('1221: ' + str(s.isPalindrome(1221)))
    print('1234: ' + str(s.isPalindrome(1234)))

if __name__ == '__main__':
    main()