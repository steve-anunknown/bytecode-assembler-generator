
def isLowerCase(c):
    return c >= 'a' and c <= 'z'
def isUpperCase(c):
    return c >= 'A' and c <= 'Z'
def isDigit(c):
    return c >= '0' and c <= '9'
def isUnderscore(c):
    return c == '_'
def isIdentifier(s):
    for char in s:
        if not (isLowerCase(char) or 
                isUpperCase(char) or 
                isDigit(char) or 
                isUnderscore(char)):
            return False
    return True

def isHexDigit(c):
    return (isDigit(c) or
            (c >= 'a' and c <= 'f') or
            (c >= 'A' and c <= 'F'))

def isOpcode(s):
    return (len(s) == 4 and s[0] == '0' and
            (s[1] == 'x' or s[1] == 'X') and
            isHexDigit(s[2]) and isHexDigit(s[3]))

def isPositiveInteger(s):
    for char in s:
        if not isDigit(char):
            return False
    return True