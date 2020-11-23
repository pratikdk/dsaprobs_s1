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
        print('N:', N)
        return ['']
    ans = []
    for i, c in enumerate(range(N)):
        print("i:", i, " c:", c)
        for left in generateParenthesis(c):
            print('>> ', "i:", i, " c:", c)
            for right in generateParenthesis(N-1-c):
                print('>>>> ', "i:", i, " c:", c)
                ans.append('({}){}'.format(left, right))
                print(ans)
    return ans
print(generateParenthesis(2))

# ((()))
# (())()
# ()(())
# ()()()
