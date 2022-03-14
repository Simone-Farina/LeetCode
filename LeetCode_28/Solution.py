class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


def main():
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("heloll", "ll"))
    print(s.strStr("helo", "ll"))
    print(s.strStr("hello", ""))
    print(s.strStr("", ""))
    print(s.strStr("aa", "aaa"))
    print(s.strStr("mississippi", "issip"))

if __name__ == '__main__':
    main()