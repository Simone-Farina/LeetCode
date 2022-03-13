class Solution:
    def __init__(self) -> None:
        self.mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        # get a list where each roman letter is converted to int
        values = list(map(lambda x: self.mapping[x], list(s)))

        result = 0
        for idx, value in enumerate(values):
            if len(values) > idx+1 and value < values[idx+1]:
                result += values[idx+1] - value
                del values[idx+1]
            else:
                result += value
            
        return result


def main():
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('MCMXCVIII'))

if __name__ == '__main__':
    main()

        
