def longest_palindrome(s):
    start = 0
    end = 0
    for i in range(len(s)):
        # Capture odd palindrome at i
        len1 = expand_around_center(s, i, i)
        # Capture even palindrome at i
        len2 = expand_around_center(s, i, i+1)
        # Consider palindrome with maximum len
        length = max(len1, len2)
        # Update start and end indices to max palindrome
        if (length > end-start): # if new max len
            start = i - (length-1)//2
            end = i + length//2
    return s[start:(end+1)]

def expand_around_center(s, left, right):
    L = left
    R = right
    while (L >= 0) and (R < len(s)) and (s[L] == s[R]):
        L -= 1
        R += 1
    return R-L-1

print(longest_palindrome("fabbac"))
