# Dynamic Programming: 10 Interview Questions

## 1. What is Dynamic Programming?

Dynamic Programming is a technique for solving problems by storing answers to repeated subproblems.

## 2. What are overlapping subproblems?

Overlapping subproblems occur when the same smaller problem is solved multiple times, such as repeated Fibonacci calls.

## 3. What is optimal substructure?

Optimal substructure means the best answer to a problem can be built from best answers to smaller subproblems.

## 4. What is memoization?

Memoization is top-down DP where recursive results are stored in a cache such as a dictionary.

## 5. What is tabulation?

Tabulation is bottom-up DP where smaller answers are filled first in a table or array.

## 6. How do you define a DP state?

A DP state describes the meaning of each stored value, such as `dp[i]` meaning the best answer up to index `i`.

## 7. What is the recurrence relation?

The recurrence relation explains how to compute a DP state from smaller states.

## 8. Why does loop direction matter in knapsack?

In 0/1 knapsack, capacity must usually be processed backward so the same item is not reused multiple times.

## 9. What is the difference between Coin Change minimum coins and Coin Change count ways?

Minimum coins minimizes the number of coins, while count ways counts valid combinations that form the amount.

## 10. How do you approach a DP problem in interviews?

Define the state, recurrence, base cases, table order, final answer, and time-space complexity.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
