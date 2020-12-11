#from stack import Stack

def eval_rpn(tokens):
    s = []
    for token in tokens:
        char = sanitize_rpn(token)
        value = 0
        if char == "+":
            left = s.pop()
            value = s.pop() + left
        elif char == "-":
            left = s.pop()
            value = s.pop() - left
        elif char == "*":
            left = s.pop()
            value = s.pop() * left
        elif char == "/":
            left = s.pop()
            value = int(s.pop() / left)
        else:
            value = char
        s.append(value)
    return None if not s else s.pop()

def sanitize_rpn(token):
    zero = ord('0')
    nine = ord('9')
    sign = "+"
    val = None
    for char in token:
        if zero <= ord(char) and ord(char) <= nine:
            if not val: val = 0
            val = val*10 + (ord(char)-zero)
        else:
            sign = char
    if val == None: return sign
    else:
        if sign == '+': return val
        else: return -val


if __name__ == "__main__":
    data = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        []
    ]
    for test_list in data:
        print(eval_rpn(test_list))

    #x = "-12"
    # x = "-"
    # sign = "+"
    # zero = ord('0')
    # nine = ord('9')
    # val = None
    # for char in x:
    #     if zero <= ord(char) and ord(char) <= nine:
    #         if not val: val = 0
    #         val = val*10 + (ord(char)-zero)
    #     else:
    #         sign = char
    # if val == None:
    #     return sign
    # else:
    #     if sign == '+': return val
    #     else: return -val
    # print(sign)
    # print(val)
    eval_rpn(["4", "13", "5", "/", "+"])



# def eval_rpn(tokens):
#     s = Stack()
#     for token in tokens:
#         char = sanitize_rpn(token)
#         value = 0
#         if char == "+":
#             left = s.pop()
#             value = s.pop() + left
#         elif char == "-":
#             left = s.pop()
#             value = s.pop() - left
#         elif char == "*":
#             left = s.pop()
#             value = s.pop() * left
#         elif char == "/":
#             left = s.pop()
#             value = int(s.pop() / left)
#         else:
#             value = char
#         s.push(value)
#     return None if s.is_empty() else s.pop()
