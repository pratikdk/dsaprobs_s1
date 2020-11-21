def reverse(s):
    n = len(s)
    for i in range(n//2):
        x = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = x
    return "".join(s)


data = [
    "abcd",
    "Pratik",
    "abcdef",
    "123456",
    "1234"
]

for test_string in data:
    print(reverse(list(test_string)))
