# def generateParenthesis(n):
#     def generate(A = []):
#         if len(A) == 2*n:
#             print(A)
#             if valid(A):
#                 ans.append("".join(A))
#         else:
#             A.append('(')
#             generate(A)
#             A.pop()
#             A.append(')')
#             generate(A)
#             A.pop()
#
#     def valid(A):
#         bal = 0
#         for c in A:
#             if c == '(': bal += 1
#             else: bal -= 1
#             if bal < 0: return False
#         return bal == 0
#
#     ans = []
#     generate()
#     return ans
#
# print(generateParenthesis(3))


# def generateParenthesis(N):
#     ans = []
#     def backtrack(S = '', left = 0, right = 0):
#         if len(S) == 2 * N:
#             ans.append(S)
#             return
#         if left < N:
#             backtrack(S+'(', left+1, right)
#         if right < left:
#             backtrack(S+')', left, right+1)
#
#     backtrack()
#     return ans
# print(generateParenthesis(3))


def generateParenthesis(N):
    if N == 0:
        print('N ==', N, '[]')
        return ['']
    ans = []
    for i, c in enumerate(range(N)):
        print("L:", c, "N:", N)
        for left in generateParenthesis(c):
            print('\t>> ', "i:", i, " c:", c)
            for right in generateParenthesis(N-1-c):
                print('\t\t>>>> ', " c:", c)
                ans.append(f"({left}){right}")#.format(, ))
                print(ans)
    return ans
print(generateParenthesis(2))

# 1 -> 0 0
# 2 -> 0 1, 1 0
# 3 -> 0 2, 1 1, 2 0

# def generate_wave(n):
#     for i in range(1, n+1):
#         for j in range()
#         print(i)
#
# generate_wave(3)

# ((()))
# (())()
# ()(())
# ()()()
