import unittest
#
# def solution(s):
#     map = {}
#     ans = 0
#     i = 0
#     for j in range(len(s)):
#         # assign valid i value
#         if s[j] in map:
#             i = max(i, map[s[j]])
#         ans = max(ans, j + 1 - i)
#         map[s[j]] = j + 1
#     return ans

def solution(s):
    map = {}
    ans = 0
    i = 0
    for j in range(len(s)):
        # assign i a valid value:
        # When a char repeats, it means past sequence is no longer unique(if new char/s are considered),
        # then it's better to ignore past seq and hence move i to occurance of the repeat char in past
        if s[j] in map:
            i = max(i, map[s[j]])
        ans = max(ans, j+1 - i)
        map[s[j]] = j+1
    return ans


class Test(unittest.TestCase):
    data = [
        ("abcabcbbfglpio", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("abcdefg", 7),
        ("dvdf", 3),
        ("ckilbkd", 5),
        ("abba", 2)
    ]

    def test_solution(self):
        for test_string, length in self.data:
            result = solution(test_string)
            self.assertEqual(result, length)

if __name__ == "__main__":
    #unittest.main()
    print(solution('abcadef'))
    print(solution('abbaadc'))
    # probs = ["abcabcbb",
    #         "bbbbb",
    #         "pwwkew",
    #         "",
    #         " ",
    #         "abcdefg",
    #         "dvdf",
    #         "ckilbkd",
    #         "abba"]
    # for prob in probs[:1]:
    #     find_substring(prob)
