class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # dictionary to map opening and closing brackets
        matching_pairs = {'(':')', '[':']', '{':'}'}
        # stack to hold opening brackets
        stack = []
        # iterate through each character in the string
        for character in s:
            if character in matching_pairs:
                # if it's an opening bracket
                # push it onto the stack
                stack.append(character)
            else:
                if not stack:
                    # check if stack is empty
                    # no matching opening bracket
                    return False
                # otherwise if the stack is not empty
                # pop the top of the stack 
                top = stack.pop()
                # for example if top = '['
                if matching_pairs[top] != character:
                    # then look up matching_pairs['['] (ideal match ']')
                    # if the value popped from the stack
                    # is not equal to the character looking for it's match
                    # then the parentheses are mismatched and it returns false
                    return False
        # at the end, if the stack is empty, all brackets were matched
        return not stack

# Test cases
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([])"))  # Output: True
