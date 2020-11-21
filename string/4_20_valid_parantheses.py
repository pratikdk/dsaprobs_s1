def valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]" : "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

data = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}"
]

for test_string in data:
    print(valid(list(test_string)))
