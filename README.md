# LeetCode

Solutions to Questions on LeetCode in Python

Categories:

1. Accepted: My accepted submissions for the problem
2. Solution: LeetCode provided Solutions
3. Top Voted: Solutions from discussion section
4. Sample: From faster time/space complexity samples

## Easy

| #    | Title                         | Basic idea (One line)                                          |
| ---- | ----------------------------- | -------------------------------------------------------------- |
| 1    | Two Sum                       | Dict (num, index), O(n) time, O(n) space                       |
| 21   | Merge Two Sorted Lists        | Iterative (compare and append to list), O(n) time, O(1) space. |
| 94   | Binary Tree Inorder Traversal | Recursive/Iterative O(n) time, O(n) space                      |
| 136  | Single Number                 | Counter (Hash) or Math, O(n) time, O(n) space. XOR O(1) space! |
| 169  | Majority Element              | Boyer-Moore Voting Algorithm, O(n) time, O(1) space            |
| 559  | Maximum Depth of N-ary Tree   | DFS, O(n) time, O(n) space. BFS, O(n) time, O(n) space         |
| 938  | Range Sum of BST              | DFS if parent strictly in range, O(n) time, O(h) space         |
| 977  | Squares of a Sorted Array     | Two Pointers at either ends, O(n) time, O(n) space             |
| 997  | Find the Town Judge           | Trusted - Trusts == n-1 for Judge, O(n + t) time, O(n) space   |
| 1025 | Divisor Game                  | Even wins, odd loses O(1). Bottom up DP O(n \* sqrt(n)) time   |
| 1108 | Defanging an IP Address       | Use Python .replace('.', '[.]'), O(n\*m) time, O(n) space      |
| 1351 | Count Negative Numbers in SM  | Negative Values form Staircase, O(n + m) time, O(n) space      |
| 1512 | Number of Good Pairs          | Hash + Math n \* (n-1) / 2, O(n) time, O(n) space              |
