# Dynamic Programming in Python: Core Concepts

Dynamic Programming, usually called DP, is a technique for solving problems by saving answers to repeated subproblems.

DP is one of the most important interview topics because it appears in optimization, counting, sequence, and decision problems.

This page covers:

- Memoization
- Tabulation
- Fibonacci
- Climbing Stairs
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Longest Common Subsequence
- Knapsack

Examples use an online computer shopping system.

## What Is Dynamic Programming?

Dynamic Programming is useful when a problem has:

| Property | Meaning |
|----------|---------|
| Overlapping subproblems | the same smaller problem is solved many times |
| Optimal substructure | the best answer can be built from best answers of smaller problems |

Example: to compute `fib(5)`, recursion repeatedly computes `fib(3)`, `fib(2)`, and `fib(1)`.

## Recursion Before DP

Plain recursion can be slow because it repeats work.

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
```

Output:

```text
8
```

This is simple but inefficient for large `n`.

## Memoization

Memoization is top-down DP.

You start with recursion and store solved subproblems in a dictionary or cache.

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(6))
```

Output:

```text
8
```

Memoization is often easiest when the recursive relation is clear.

## Tabulation

Tabulation is bottom-up DP.

You build answers from the smallest subproblem to the final answer.

```python
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]

    return dp[n]


print(fibonacci(6))
```

Output:

```text
8
```

Tabulation avoids recursive call-stack overhead.

## Memoization vs Tabulation

| Feature | Memoization | Tabulation |
|---------|-------------|------------|
| Direction | top-down | bottom-up |
| Style | recursion + cache | loop + table |
| Good when | recurrence is natural | order is easy |
| Stack use | uses call stack | no recursion stack |
| May skip states | yes | usually computes all states |

## How to Think About DP

Use this checklist:

1. Define the state.
2. Define the recurrence.
3. Define the base cases.
4. Decide memoization or tabulation.
5. Identify the answer position.
6. Analyze time and space complexity.

## Example: Climbing Stairs

State: `dp[i]` means number of ways to reach stair `i`.

Recurrence: `dp[i] = dp[i - 1] + dp[i - 2]`.

```python
def climb_stairs(n):
    if n <= 2:
        return n

    prev2 = 1
    prev1 = 2

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


print(climb_stairs(5))
```

Output:

```text
8
```

## Example: House Robber

In a shopping system, imagine choosing promotional shelves where adjacent shelves cannot both be selected.

State: `dp[i]` means max value from shelves up to index `i`.

Recurrence: choose max between skipping or taking the current shelf.

```python
def house_robber(values):
    previous_two = 0
    previous_one = 0

    for value in values:
        current = max(previous_one, previous_two + value)
        previous_two = previous_one
        previous_one = current

    return previous_one


print(house_robber([2, 7, 9, 3, 1]))
```

Output:

```text
12
```

## Example: Coin Change

Find minimum coins needed to form a payment amount.

```python
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if value >= coin:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


print(coin_change([1, 2, 5], 11))
```

Output:

```text
3
```

## Example: Longest Increasing Subsequence

Find the longest sequence of increasing prices or ratings.

```python
def lis(values):
    dp = [1] * len(values)

    for right in range(len(values)):
        for left in range(right):
            if values[left] < values[right]:
                dp[right] = max(dp[right], dp[left] + 1)

    return max(dp)


print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
```

Output:

```text
4
```

## Example: Longest Common Subsequence

Find common order between two product-code strings.

```python
def lcs(first, second):
    rows = len(first)
    cols = len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if first[row - 1] == second[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp[rows][cols]


print(lcs("LAPTOP", "TABLET"))
```

Output:

```text
2
```

## Example: 0/1 Knapsack

Choose items with maximum value without exceeding bag capacity.

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for item in range(1, n + 1):
        for current_capacity in range(1, capacity + 1):
            if weights[item - 1] <= current_capacity:
                dp[item][current_capacity] = max(
                    dp[item - 1][current_capacity],
                    values[item - 1] + dp[item - 1][current_capacity - weights[item - 1]],
                )
            else:
                dp[item][current_capacity] = dp[item - 1][current_capacity]

    return dp[n][capacity]


print(knapsack([1, 3, 4], [1500, 4000, 5000], 4))
```

Output:

```text
5500
```

## Common DP Patterns

| Pattern | Examples |
|---------|----------|
| One-dimensional DP | Fibonacci, Climbing Stairs, House Robber |
| Unbounded choice | Coin Change |
| Sequence DP | LIS, LCS |
| Grid DP | unique paths, minimum path sum |
| 0/1 choice | Knapsack |
| State compression | reducing `O(n)` space to `O(1)` or `O(capacity)` |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| unclear state | define what `dp[i]` or `dp[i][j]` means |
| missing base case | initialize `dp[0]`, first row, or first column |
| wrong loop order | match loop order to dependency |
| mixing 0/1 and unbounded choice | update states in the correct direction |
| returning wrong cell | identify where the final answer lives |

## Complexity Summary

| Problem | Common time | Common space |
|---------|-------------|--------------|
| Fibonacci | `O(n)` | `O(n)` or `O(1)` |
| Climbing Stairs | `O(n)` | `O(1)` |
| House Robber | `O(n)` | `O(1)` |
| Coin Change | `O(amount * coins)` | `O(amount)` |
| LIS basic DP | `O(n^2)` | `O(n)` |
| LCS | `O(mn)` | `O(mn)` |
| Knapsack | `O(n * capacity)` | `O(n * capacity)` or `O(capacity)` |

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Recursion](../recursion/core-concepts.md)
