# LeetCode

Solutions to Questions on LeetCode in Python

Categories:

1. Accepted: My accepted submissions for the problem
2. Revisited: Submissions from revisiting questions
3. Solution: LeetCode provided Solutions
4. Top Voted: Solutions from discussion section
5. Sample: From faster time/space complexity samples

## Easy

| #    | Title                          | Basic idea (One line)                                          |
| ---- | ------------------------------ | -------------------------------------------------------------- |
| 1    | Two Sum                        | Dict (num, index), O(n) time, O(n) space                       |
| 21   | Merge Two Sorted Lists         | Iterative (compare and append to list), O(n) time, O(1) space. |
| 53   | Maximum Subarray               | DP/Kandane's T: O(n), S: O(1). D&C T: O(n), S: O(log n)        |
| 94   | Binary Tree Inorder Traversal  | Recursive/Iterative O(n) time, O(n) space                      |
| 111  | Minimum Depth of Binary Tree   | BFS/DFS, BFS in most cases is better than DFS, T&S: O(n)       |
| 121  | Best Time to Buy & Sell Stock  | Track min and profit / Kandane's Algorithm, T: O(n), S: O(1)   |
| 136  | Single Number                  | Counter (Hash) or Math, O(n) time, O(n) space. XOR O(1) space! |
| 141  | Linked List Cycle              | Tortoise and Hare, O(n) time, O(1) space                       |
| 169  | Majority Element               | Boyer-Moore Voting Algorithm, O(n) time, O(1) space            |
| 292  | Nim Game                       | Win if n % 4 != 0, O(n) time and space.                        |
| 303  | Range Sum Query - Immutable    | Memorisation of Accumulations, T&S: O(n)                       |
| 338  | Counting Bits                  | DP: ans[i] = ans[i >> 1] + (i & 1), T&S: O(n)                  |
| 392  | Is Subsequence                 | Two pointers and/or iterator, T: O(t), S: O(1)                 |
| 401  | Binary Watch                   | Collect One Bits List Comprehension / Backtracking, T&S: O(1)  |
| 521  | Longest Uncommon Subsequence I | Same -> -1, o/w return longer string, T: (min(x, y)), S: O(1)  |
| 559  | Maximum Depth of N-ary Tree    | DFS, O(n) time, O(n) space. BFS, O(n) time, O(n) space         |
| 720  | Longest Word in Dictionary     | Trie + DFS, T&S: O(n \* s). Sort + Set, T: O(n log n), S: O(n) |
| 746  | Min Cost Climbing Stairs       | Bottom Up DP 3 Vars, T: O(n), S: O(1)                          |
| 852  | Peak Index in a Mountain Array | Binary Seach, Golden-Section Search, T: O(log n), S: O(1)      |
| 897  | Increasing Order Search Tree   | DFS + Dummy, T&S: O(n). DFS + Relinking, T: O(n), S: O(h)      |
| 933  | Number of Recent Calls         | Queue, O(1) time and space due to problem constraints          |
| 938  | Range Sum of BST               | DFS if parent strictly in range, O(n) time, O(h) space         |
| 977  | Squares of a Sorted Array      | Two Pointers at either ends, O(n) time, O(n) space             |
| 993  | Cousins in Binary Tree         | Tuple with BFS, T&S: O(n). Tuple with DFS, T: O(n), S: O(h)    |
| 997  | Find the Town Judge            | Trusted - Trusts == n-1 for Judge, O(n + t) time, O(n) space   |
| 1021 | Remove Outermost Parentheses   | Open = Closed, O(n) time and space                             |
| 1025 | Divisor Game                   | Even wins, odd loses O(1). Bottom up DP O(n \* sqrt(n)) time   |
| 1046 | Last Stone Weight              | Heap T: O(nlogn), S: O(n). bisect.insort T: O(n^2), S: O(1)    |
| 1108 | Defanging an IP Address        | Use Python .replace('.', '[.]'), O(n\*m) time, O(n) space      |
| 1221 | Split a Str in Balanced Strs   | Increment Res when num L - num R = 0, O(n) time, O(1) space    |
| 1266 | Min Time Visiting All Points   | Sum the max abs difference between points, T: O(n), S: O(1)    |
| 1281 | Product - Sum of Digits of Int | Map & Reduce, T&S: O(log n). Mod & Div, T: O(log n), S: O(1)   |
| 1290 | Convert Binary to Int in LL    | Bit Shift Left and Bitwise Or, T: O(n), S: O(1)                |
| 1337 | The K Weakest Rows in a Matrix | Binary Search + Heap (Best). Column, T: O(m \* n), S: O(k)     |
| 1342 | Num Steps to Reduce Num to 0   | Binary Representation, O(bits) space and time                  |
| 1351 | Count Negative Numbers in SM   | Negative Values form Staircase, O(n + m) time, O(n) space      |
| 1480 | Running Sum of 1d Array        | Use Prior Element, sum in place, T: O(n), S: O(1)              |
| 1512 | Number of Good Pairs           | Hash + Math n \* (n-1) / 2, O(n) time, O(n) space              |
| 1528 | Shuffle String                 | Create list, insert s with indicies, O(n) time and space       |
| 1603 | Design Parking System          | Array, Instance Var, or hashmap for spaces, T&S: O(1)          |
| 1688 | Count of Matches in Tournament | n-1 matches, T&S: O(1). Even/odd if/else: T: O(log n), S: O(1) |
| 1863 | Sum of All Subset XOR Totals   | Backtrack O(2^n) time, O(n) space. Bit O(n) time, O(1) space   |

## Medium

| #    | Title                                  | Basic idea (One line)                              |
| ---- | -------------------------------------- | -------------------------------------------------- |
| 33   | Search in Rotated Sorted Array         | Modified Binary Search, T: O(log n), S: O(1)       |
| 80   | Remove Duplicates from Sorted Array II | Set first n valid values, T: O(n), S: O(1)         |
| 92   | Reverse Linked List II                 | Iterative in place updates, T: O(n), S: O(1)       |
| 131  | Palindrome Partitioning                | DFS palindrome backtrack, T: O(n \* 2^n), S: O(n)  |
| 147  | Insertion Sort List                    | Dummy + Predecessor + Disorder, T: O(n^2), S: O(1) |
| 464  | Can I Win                              | Top Down DP choices key, T: O(n \* 2^k), S: O(k!)  |
| 676  | Implement Magic Dictionary             | Diff = 1 for List/dict, Candidates, T&S: O(n \* s) |
| 787  | Cheapest Flights Within K Stops        | BFS, T&S Unknown                                   |
| 955  | Delete Columns to Make Sorted II       | Track unsorted strs using set, T: O(n\*m), S: O(n) |
| 1552 | Magnetic Force Between Two Balls       | Binary Search, T: O(n \* (log n + log m)), S: O(1) |
| 1727 | Largest Submatrix With Rearrangements  | Sum column stacks, T: O(n \* m log m), S: O(1)     |
| 1864 | Min Swaps for alternating Binary Str   | Count Wrong Positions, T: O(n), S: O(1)            |
| 1877 | Minimize Maximum Pair Sum in Array     | Sort, Min + Max, T: O(n log n), S: O(1)            |
