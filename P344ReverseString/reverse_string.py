class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string represented as a list of characters
        in-place. No function methods from the list class like reverse() 
        are used.
        
        This approach uses two pointers (not literal pointers in the 
        C/C++ sense), one for the front (lo), and one that iterates 
        from the end (hi). The characters at positions lo and hi are
        swapped, the lo pointer is incremeneted to the next character,
        while the hi pointer is decremented to the character before the
        current hi position. The time complexity is O(n) and the space
        complexity is constant O(1).
        
        Consider the example "hello, world". 

        "hello, world"   -->   "dello, worlh"  -->   "dello, worlh" 
         ^          ^           ^          ^           ^        ^
        lo          hi          lo         hi          lo       hi

        "dello, worlh"   -->   "dlllo, woreh"  -->   "dlllo, woreh" 
          ^        ^             ^        ^             ^      ^
          lo       hi            lo       hi            lo     hi
        
        "dlllo, woreh"   -->   "dlrlo, woleh"  -->   "dlrlo, woleh" 
           ^      ^               ^      ^               ^    ^   
           lo     hi              lo     hi              lo   hi
        
        ...
        ...

        Parameters
        ----------
        s: List
            List of characters to be reversed in-place
    
        Examples
        --------
        Input: ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]

        Input: ["w","i","n","t","e","r"]
        Output ["r","e","t","n","i","w"]]
        """
        lo = 0
        hi = len(s) - 1
        
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            
            lo += 1
            hi -= 1