class Solution(object):
    def isValid(self, s):
        empty_stack = []
        parentheses_dictionary = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in "{[(":
                empty_stack.append(char)
            elif char in "}])" and len(empty_stack) == 0:
                return False
            elif char in "}])" and len(empty_stack) > 0:
                x = empty_stack.pop()
                if parentheses_dictionary[x] != char:
                    return False
        return len(empty_stack) == 0
solution = Solution()
print(solution.isValid("(([]){})"))