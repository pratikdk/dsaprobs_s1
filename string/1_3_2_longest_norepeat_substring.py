import unittest

def solution(s):
    map = {}
    ans = 0
    i = 0
    for j in range(len(s)):
        # assign valid i value
        if s[j] in map:
            i = max(i, map[s[j]])
        ans = max(ans, j + 1 - i)
        map[s[j]] = j + 1
    return ans

class Test(unittest.TestCase):
    data = [
        ("abcabcbb", 3),
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
    unittest.main()
