class Solution:
    """
    Returns whether two strings are equal after accounting for backspace characters.
    The character # represents a backspace character.

    This method uses a nested function to evaluate the string after accounting 
    for backspace characters. A stack data structure is used for the
    characters. If the stack has non-zero length and if the next character is 
    a "#", pop the last element of the stack, else, if the current character
    when parsing the array is not a "#", push it onto the stack.

    Parameters
    ----------
    S : str

    T : str

    Returns
    -------
    backspace_equal : bool
        True if the two strings are the same after

    Examples
    --------
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".
    """
    def backspaceCompare(self, S: str, T: str) -> bool:

        def process_backspace(x: str) -> List[str]:
            x_stack = []
            for i, xchar in enumerate(x):
                if xchar == '#' and len(x_stack):
                    x_stack.pop()
                elif xchar != '#':
                    x_stack.append(xchar)

            return x_stack

        return process_backspace(S) == process_backspace(T)