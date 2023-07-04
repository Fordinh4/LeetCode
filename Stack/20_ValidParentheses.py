def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    opens = "([{"
    closers = ")]}"
    
    for bracket in s:
        
        if bracket in "([{":
            # To stack all the open brackets
            stack.append(bracket)
        else:
            if stack == []:
                # If there aren't any open brackets
                return False
            else:
                open = stack.pop()
                if opens.index(open) != closers.index(bracket):
                    # To check if the index between the open bracket and the close bracket match each other or not
                    return False
    if stack != []:
        return False
    return True

s = "["
print(isValid(s))