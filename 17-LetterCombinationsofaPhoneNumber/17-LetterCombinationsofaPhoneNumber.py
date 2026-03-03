# Last updated: 3/3/2026, 10:54:39 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5        
6        # Keypad mapping
7        phone = {
8            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
9            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
10        }
11        
12        res = []
13        
14        def backtrack(index, current_path):
15            # Base case: if the path is the same length as digits, we are done
16            if len(current_path) == len(digits):
17                res.append("".join(current_path))
18                return
19            
20            # Get the letters for the current digit
21            possible_letters = phone[digits[index]]
22            
23            for letter in possible_letters:
24                # Add the letter and move to the next digit
25                current_path.append(letter)
26                backtrack(index + 1, current_path)
27                # Backtrack: remove the letter before trying the next one
28                current_path.pop()
29        
30        backtrack(0, [])
31        return res