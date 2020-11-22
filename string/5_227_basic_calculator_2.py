# Half implementation
def evaluate(s):
    operand_queue = []
    operator_queue = []
    operand_stack = []
    operator_stack = []
    p_head = 0
    operator_priority = {
        "+": p_head-1,
        "-": p_head-1,
        "*": p_head,
        "/": p_head
    }
    exp_len = len(s)
    i = 0
    # Parse the expression string
    while i < exp_len:
        char_ord = ord(s[i])
        if s[i] in operator_priority: # symbol
            operator_queue.append(s[i])
            i += 1
        elif 48 <= char_ord <= 57: # digit
            j = i+1
            while (i < (exp_len-1)) and (48 <= ord(s[j]) <= 57):
                j += 1
            operand_queue.append(int(s[i: j]))
            i = j
        else:
            i += 1
    # print(operand_queue)
    # print(operator_queue)
    # Start scanning operator queue
    for i in range(len(operator_queue)):
        current_priority = operator_priority[operator_queue[i]]
        if i == len(operator_queue)-1: # if its end of expression assign same priority
            next_priority = current_priority
        else:
            next_priority = operator_priority[operator_queue[i+1]]

        # Evalutate
        if current_priority == next_priority: # current has same priority
            if operand_stack:
            else:
                operand_queue.pop(0) operand_queue.pop(0)


        elif current_priority > next_priority: # current has high priority
            pass
        else: # current has less priority
            pass

data = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "2 + 2+2 * 2* 2+2 / 2",
    "100 * 2 /100-2"
]
