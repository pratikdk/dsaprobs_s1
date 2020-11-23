# def group_anagrams(lst):
#     ags = []
#     ags.append([lst.pop(0)])
#     map = {}
#     for string in lst:
#         # Compare with each group's first string in ags
#         matched = False
#         for group in ags:
#             # compare string with first string
#             map.clear()
#             odd_count = 0
#             for c in group[0]+string:
#                 map[c] = map.get(c, 0) + 1
#                 if map[c] % 2: # odd
#                     odd_count += 1
#                 else: # even
#                     odd_count -= 1
#             if odd_count == 0:
#                 group.append(string)
#                 matched = True
#                 break
#         if not matched:
#             ags.append([string])
#     return ags

# Using collections
# import collections
# def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()

# Dictionary version
def group_anagrams(strs):
        ans = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            ans[sorted_s] = ans.get(sorted_s, [])+[s]
        return list(ans.values())

data = [
    ["eat","tea","tan"],
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
    ["abbbbbbbbbbb", "aaaaaaaaaaab"],
    ["abbb", "aaab"]
]
for test_list in data:
    print(group_anagrams(test_list))
