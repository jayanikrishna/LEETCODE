# Last updated: 3/8/2026, 12:15:14 PM
1from collections import Counter
2
3class Solution:
4    def findSubstring(self, s: str, words: list[str]) -> list[int]:
5        if not s or not words:
6            return []
7        
8        word_len = len(words[0])
9        word_count = len(words)
10        total_len = word_len * word_count
11        word_map = Counter(words)
12        res = []
13        
14        # We only need to start from 0 to word_len - 1
15        for i in range(word_len):
16            left = i
17            right = i
18            curr_map = Counter()
19            count = 0
20            
21            while right + word_len <= len(s):
22                # Extract the next word block
23                word = s[right:right + word_len]
24                right += word_len
25                
26                if word in word_map:
27                    curr_map[word] += 1
28                    count += 1
29                    
30                    # If we have too many of one word, shift left pointer
31                    while curr_map[word] > word_map[word]:
32                        left_word = s[left:left + word_len]
33                        curr_map[left_word] -= 1
34                        count -= 1
35                        left += word_len
36                    
37                    # If count matches total words, we found a permutation
38                    if count == word_count:
39                        res.append(left)
40                else:
41                    # Not a valid word, reset window
42                    curr_map.clear()
43                    count = 0
44                    left = right
45                    
46        return res