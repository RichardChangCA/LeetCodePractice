# Question:
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:

# Input: "()"
# Output: True
# Example 2:

# Input: "(*)"
# Output: True
# Example 3:

# Input: "(*))"
# Output: True
# Note:

# The string size will be in the range [1, 100].

class Solution:
    def checkValidString(self, s: str) -> bool:
        output = []
        for i in range(len(s)):
            if(s[i]=='(' or s[i]=='*'):
                output.append(s[i])
            else:
                if(len(output)==0):
                    return False
                else:
                    if('(' in output):
                        # find last (
                        tag = -1
                        while(output[tag]!='('):
                            tag += -1
                        if(tag == -1):
                            output = output[:-1]
                        else:
                            output = output[:tag]+output[tag+1:]
                    else:
                        output = output[:-1]
        output_again = []
        for i in range(len(output)):
            if(output[i]=='('):
                output_again.append(output[i])
            else:
                if(len(output_again)>0):
                    output_again = output_again[:-1]
                else:
                    output_again.append(output[i])
        output = output_again
        if(len(output)==0):
            return True
        elif(len(output)>0 and len(set(output))==1 and output[0]=='*'):
            return True
        else:
            return False
                