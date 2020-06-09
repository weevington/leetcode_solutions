class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses a string represented as a list of characters
        in-place. No function methods from the list class such as reverse() 
        are used.
        
        This approach uses two pointers (not literal pointers in the 
        C/C++ sense), one for the front (lo), and one that iterates 
        from the end (hi). The characters at positions lo and hi are
        swapped, the lo pointer is incremeneted to the next character,
        while the hi pointer is decremented to the character before the
        current hi position. The algorithm terminates once lo is equal to hi
        (in the case of a string with odd length) or greater than hi (in the
        case of a string of even length). The time complexity is O(n) and 
        the space complexity is constant O(1).
        
        Consider the example "hello, world". 
                               swap characters        move pointers
    
        "hello, world"   -->   "dello, worlh"  -->   "dello, worlh" 
         ^          ^           ^          ^           ^        ^
        lo          hi         lo          hi         lo        hi

        "dello, worlh"   -->   "dlllo, woreh"  -->   "dlllo, woreh" 
          ^        ^             ^        ^             ^      ^
          lo       hi           lo        hi           lo      hi
        
        "dlllo, woreh"   -->   "dlrlo, woleh"  -->   "dlrlo, woleh" 
           ^      ^               ^      ^               ^    ^   
          lo      hi             lo      hi             lo    hi
        
        "dlrlo, woleh"   -->   "dlroo, wlleh"  -->   "dlroo, wlleh" 
            ^    ^                 ^    ^                 ^  ^   
           lo    hi               lo    hi               lo  hi
        
        "dlroo, wlleh"   -->   "dlrow, olleh"  -->   "dlrow, olleh" 
             ^  ^                   ^  ^                   ^^   
            lo  hi                 lo  hi                 lohi
        
        "dlrow, olleh"   -->   "dlrow ,olleh"  -->   "dlrow, olleh" 
              ^^                     ^^                    ^^   
             lohi                   lohi                  hilo <- break (hi < lo)

        Parameters
        ----------
        s: List
            List of characters to be reversed in-place
    
        Examples
        --------
        Input: ["H","a","n","n","a","h"]
        Output: ["h","a","n","n","a","H"]

        Input: ["w","i","n","t","e","r"]
        Output ["r","e","t","n","i","w"]
        """
        lo = 0
        hi = len(s) - 1
        
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            
            lo += 1
            hi -= 1