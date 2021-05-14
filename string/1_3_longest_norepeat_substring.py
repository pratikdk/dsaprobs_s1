import unittest

def solution(s):
    charset_flag = 0
    char_pos = [0 for _ in range(128)]
    max_count = 0
    counter = 0
    lookup_threshold = 0
    for i, char in enumerate(s):
        char_ord = ord(char)
        mask = 1 << char_ord
        if (charset_flag & mask) == 0:
            charset_flag |= mask # toggle flag
            counter += 1
        else:
            if lookup_threshold == 0 or char_pos[char_ord] >= lookup_threshold:
                counter = (i+1) - char_pos[char_ord]
                lookup_threshold = char_pos[char_ord]
                char_pos[char_ord] = i+1
            else:
                counter += 1
                char_pos[char_ord] = i+1

        if max_count < counter:
            max_count = counter
        char_pos[char_ord] = i+1

    return max_count

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
        # dfvdf
        # dvfdf
        # dvfdaf
        # abcabl
        # abcabcd
        # dvdf
        # abcbadc
    ]

    def test_solution(self):
        for test_string, length in self.data:
            result = solution(test_string)
            self.assertEqual(result, length)

if __name__ == "__main__":
    #unittest.main()
    print(solution(' '))
