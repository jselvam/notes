# Recursion: 10 Interview Questions

## 1. What is recursion?

Recursion is a technique where a function calls itself to solve a smaller version of the same problem.

## 2. What is a base case?

A base case is the stopping condition that prevents the recursive function from calling itself forever.

## 3. What is a recursive call?

A recursive call is the part of the function where it calls itself with a smaller or simpler input.

## 4. What happens if recursion has no base case?

The function keeps calling itself until Python raises `RecursionError`.

## 5. What is the call stack in recursion?

The call stack stores unfinished function calls. Each recursive call stays on the stack until its smaller call returns.

## 6. What is backtracking?

Backtracking is recursion where you make a choice, explore it, and undo the choice before trying another option.

## 7. Why do we use `path.pop()` in backtracking?

`path.pop()` removes the last choice so the next recursive branch starts with the correct state.

## 8. When is recursion better than iteration?

Recursion is often clearer for trees, DFS, divide-and-conquer, subsets, permutations, and backtracking problems.

## 9. What is a common disadvantage of recursion in Python?

Deep recursion can hit Python's recursion depth limit and uses extra call stack memory.

## 10. How do you identify recursion complexity?

Count how many recursive calls happen per level and how deep the recursion goes. For example, subsets usually take `O(2^n)`.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
