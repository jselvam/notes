# Dynamic Programming: Interview Problems

This page contains **20 interview problems** on Dynamic Programming in Python.

It covers memoization, tabulation, Fibonacci, Climbing Stairs, House Robber, Coin Change, Longest Increasing Subsequence, Longest Common Subsequence, and Knapsack.

## 1. Fibonacci With Memoization

### Problem

Find the `n`th Fibonacci number using memoization.

### Explanation

Cache each Fibonacci value so repeated subproblems are solved once.

### Solution

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


print(fibonacci(7))
```

Output:

```text
13
```

## 2. Fibonacci With Tabulation

### Problem

Find the `n`th Fibonacci number using bottom-up DP.

### Explanation

Build the answer from `0` and `1` up to `n`.

### Solution

```python
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]

    return dp[n]


print(fibonacci(7))
```

Output:

```text
13
```

## 3. Climbing Stairs

### Problem

Find how many ways a customer can climb `n` checkout steps by taking 1 or 2 steps.

### Explanation

Ways to reach stair `i` equals ways from `i - 1` plus ways from `i - 2`.

### Solution

```python
def climb_stairs(n):
    if n <= 2:
        return n

    previous_two = 1
    previous_one = 2

    for _ in range(3, n + 1):
        current = previous_one + previous_two
        previous_two = previous_one
        previous_one = current

    return previous_one


print(climb_stairs(5))
```

Output:

```text
8
```

## 4. Min Cost Climbing Stairs

### Problem

Find the minimum cost to reach the top of checkout steps.

### Explanation

At each step, choose the cheaper previous path.

### Solution

```python
def min_cost_climbing_stairs(cost):
    previous_two = 0
    previous_one = 0

    for index in range(2, len(cost) + 1):
        current = min(previous_one + cost[index - 1], previous_two + cost[index - 2])
        previous_two = previous_one
        previous_one = current

    return previous_one


print(min_cost_climbing_stairs([10, 15, 20]))
```

Output:

```text
15
```

## 5. House Robber

### Problem

Choose non-adjacent promotional shelves to maximize value.

### Explanation

For each shelf, either skip it or take it with the best value before the previous shelf.

### Solution

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

## 6. House Robber II

### Problem

Choose non-adjacent shelves arranged in a circle.

### Explanation

Because first and last shelves are adjacent, solve twice: skip first or skip last.

### Solution

```python
def rob_line(values):
    previous_two = 0
    previous_one = 0

    for value in values:
        current = max(previous_one, previous_two + value)
        previous_two = previous_one
        previous_one = current

    return previous_one


def house_robber_circle(values):
    if len(values) == 1:
        return values[0]

    return max(rob_line(values[:-1]), rob_line(values[1:]))


print(house_robber_circle([2, 3, 2]))
```

Output:

```text
3
```

## 7. Coin Change: Minimum Coins

### Problem

Find the minimum number of coins needed to make a payment amount.

### Explanation

For each amount, try every coin and keep the minimum result.

### Solution

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

## 8. Coin Change: Count Ways

### Problem

Count how many ways an amount can be paid using given coin values.

### Explanation

Process coins one by one to avoid counting the same combination in different orders.

### Solution

```python
def count_coin_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] += dp[value - coin]

    return dp[amount]


print(count_coin_ways([1, 2, 5], 5))
```

Output:

```text
4
```

## 9. Longest Increasing Subsequence

### Problem

Find the length of the longest increasing product-price sequence.

### Explanation

For each value, look back at smaller previous values and extend their best subsequence.

### Solution

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

## 10. Longest Increasing Subsequence With Binary Search

### Problem

Find LIS length in `O(n log n)`.

### Explanation

Maintain the smallest possible ending value for each subsequence length.

### Solution

```python
import bisect


def lis_fast(values):
    tails = []

    for value in values:
        position = bisect.bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value

    return len(tails)


print(lis_fast([10, 9, 2, 5, 3, 7, 101, 18]))
```

Output:

```text
4
```

## 11. Longest Common Subsequence

### Problem

Find the longest common subsequence length between two product-code strings.

### Explanation

If characters match, extend diagonal value. Otherwise take the best from top or left.

### Solution

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

## 12. Print One Longest Common Subsequence

### Problem

Return one actual LCS string.

### Explanation

After building the DP table, move backward from the bottom-right cell.

### Solution

```python
def lcs_string(first, second):
    rows = len(first)
    cols = len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if first[row - 1] == second[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    row = rows
    col = cols
    answer = []

    while row > 0 and col > 0:
        if first[row - 1] == second[col - 1]:
            answer.append(first[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] >= dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return "".join(reversed(answer))


print(lcs_string("LAPTOP", "TABLET"))
```

Output:

```text
AT
```

## 13. 0/1 Knapsack

### Problem

Choose products with maximum value without exceeding bag capacity.

### Explanation

For every product, choose between taking it or skipping it.

### Solution

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

## 14. 0/1 Knapsack With Space Optimization

### Problem

Solve 0/1 knapsack with one DP array.

### Explanation

Iterate capacity backward so each item is used at most once.

### Solution

```python
def knapsack_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                value + dp[current_capacity - weight],
            )

    return dp[capacity]


print(knapsack_optimized([1, 3, 4], [1500, 4000, 5000], 4))
```

Output:

```text
5500
```

## 15. Unique Paths in Warehouse Grid

### Problem

Count paths from top-left to bottom-right moving only right or down.

### Explanation

Ways to reach a cell equals ways from top plus ways from left.

### Solution

```python
def unique_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[rows - 1][cols - 1]


print(unique_paths(3, 3))
```

Output:

```text
6
```

## 16. Minimum Path Sum in Delivery Grid

### Problem

Find the minimum cost path from top-left to bottom-right.

### Explanation

Each cell stores its cost plus the cheaper path from top or left.

### Solution

```python
def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                continue
            top = grid[row - 1][col] if row > 0 else float("inf")
            left = grid[row][col - 1] if col > 0 else float("inf")
            grid[row][col] += min(top, left)

    return grid[-1][-1]


print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
```

Output:

```text
7
```

## 17. Maximum Subarray

### Problem

Find the maximum profit segment from daily profit changes.

### Explanation

At each index, either extend the previous segment or start a new one.

### Solution

```python
def max_subarray(values):
    best_here = values[0]
    best_total = values[0]

    for value in values[1:]:
        best_here = max(value, best_here + value)
        best_total = max(best_total, best_here)

    return best_total


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```

Output:

```text
6
```

## 18. Decode Ways for Product Code

### Problem

Count ways to decode a numeric product code where `1=A` and `26=Z`.

### Explanation

At each position, use one digit or two valid digits.

### Solution

```python
def decode_ways(code):
    if not code or code[0] == "0":
        return 0

    dp = [0] * (len(code) + 1)
    dp[0] = 1
    dp[1] = 1

    for index in range(2, len(code) + 1):
        one_digit = int(code[index - 1:index])
        two_digits = int(code[index - 2:index])

        if 1 <= one_digit <= 9:
            dp[index] += dp[index - 1]
        if 10 <= two_digits <= 26:
            dp[index] += dp[index - 2]

    return dp[-1]


print(decode_ways("226"))
```

Output:

```text
3
```

## 19. Word Break for Search Query

### Problem

Check whether a search query can be split into known words.

### Explanation

`dp[i]` means the prefix ending at `i` can be segmented.

### Solution

```python
def word_break(text, words):
    word_set = set(words)
    dp = [False] * (len(text) + 1)
    dp[0] = True

    for end in range(1, len(text) + 1):
        for start in range(end):
            if dp[start] and text[start:end] in word_set:
                dp[end] = True
                break

    return dp[-1]


print(word_break("gaminglaptop", ["gaming", "laptop", "mouse"]))
```

Output:

```text
True
```

## 20. Partition Equal Subset Sum

### Problem

Check whether order weights can be split into two equal groups.

### Explanation

This is a subset-sum DP problem targeting half of the total.

### Solution

```python
def can_partition(weights):
    total = sum(weights)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for weight in weights:
        for value in range(target, weight - 1, -1):
            dp[value] = dp[value] or dp[value - weight]

    return dp[target]


print(can_partition([1, 5, 11, 5]))
```

Output:

```text
True
```

## Final Notes

- Memoization is top-down recursion with cache.
- Tabulation is bottom-up table building.
- DP problems become easier after defining the state and recurrence.
- Loop direction matters, especially in coin change and knapsack.
