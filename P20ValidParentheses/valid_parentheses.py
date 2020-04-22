class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if a given string containing just the characters '(', ')',
        '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:
            - Open brackets are closed by the same type of brackets.
            - Open brackets are closed in the correct order.

        An empty string is also considered valid.

        Parameters
        ----------
        s : str
            A string consisting of opening and closing parentheses/brackets.

        Returns
        -------
        is_valid : bool
            True if the string is a well-formed

        Examples
        --------
        Input: "()"
        Output: True

        Input: "()[]{}"
        Output: True

        Input: "(]"
        Output: False

        Input: "([)]"
        Output: False

        Input: "{[]}"
        Output: True
        """
        parens = {')':'(', '}':'{', ']':'['}
                        
        stack = []
        
        for i, par in enumerate(s):
            if not len(stack):
                stack.append(par)
            else:
                if par in parens.keys():
                    if parens[par] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(par)

        return len(stack) == 0