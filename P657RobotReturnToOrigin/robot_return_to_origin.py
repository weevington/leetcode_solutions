class Solution:
    """
    There is a robot starting at position (0, 0), the origin, on a 2D plane.
    Returns whether or not a robot ends up back at (0, 0) after it completes
    a series of moves.

    Parameters
    ----------
    moves : str
        The move sequence is represented by a string, and the character moves[i]
        represents its ith move. Valid moves are "R" (right), "L" (left), "U"
        (up), and "D" (down)

    Returns
    -------
    bool
        True if the robot returns to (0, 0) after a series if moves, else
        False.
    
    Examples
    --------
    Input: "UD"
    Output: True

    Input: "LL"
    Output: False
    """
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        
        for i, mv in enumerate(moves):
            if mv == 'R':
                pos[0] += 1
            elif mv == 'L':
                pos[0] -= 1
            elif mv == 'U':
                pos[1] += 1
            elif mv == 'D':
                pos[1] -= 1
        
        return pos == [0, 0]