def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # =>X this one is wrong because if the input is "aacc" and "ccac" then it would return as True instead of False
    # if set(s) == set(t) and len(s) == len(t):
    #     return True
    # return False
    
    # ======= O(n log n)
    # list_s = list(s)
    # list_s.sort()
    # list_t = list(t)
    # list_t.sort()
    # return list_s == list_t
    # OR:
    # return sorted(s) == sorted(t)

    # ====== O(n)
    if len(s) != len(t):
        return False
    
    CountS, CountT = {}, {}

    # Count each letter in each string
    for i in range(len(s)): 
        # If len of both string are the same then just use one for iteration
        CountS[s[i]] = 1 + CountS.get(s[i], 0) 
        #=> if s[i] is not the key in the dict, get() will return as 0
        CountT[t[i]] = 1 + CountT.get(t[i], 0)

    # Check if each letter of the dict CountS and CountT are the same or not
    for j in CountS:
        if CountS[j] != CountT.get(j, 0): 
            # I have to use get() cuz what if there is a key that in CountS and not in CountT
            return False
    return True


    



s = "anagram"
t = "nagaram"
print(isAnagram(s,t))