class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        indexes = [x for x, c in enumerate(haystack) if c == needle[0] and len(haystack[x:]) >= len(needle)]

        count = 0
        for idx in indexes:
            for i, c in enumerate(haystack[idx:]):
                if c == needle[count]:
                    count += 1
                else:
                    count = 0
                    break

                if count == len(needle):
                    return idx
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
