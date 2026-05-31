# Recursion in Python: Core Concepts

Recursion is a technique where a function solves a problem by calling itself on a smaller version of the same problem.

This page covers:

- Base case
- Recursive calls
- Backtracking

Examples use an online computer shopping system.

## What Is Recursion?

A recursive function has two important parts:

| Part | Meaning |
|------|---------|
| Base case | condition that stops recursion |
| Recursive call | function call that moves toward the base case |

```python
def count_items(items):
    if not items:  # base case
        return 0

    return 1 + count_items(items[1:])  # recursive call


print(count_items(["mouse", "keyboard", "monitor"]))
```

Output:

```text
3
```

## Base Case

The base case prevents infinite recursion.

```python
def show_cart_items(items, index=0):
    if index == len(items):
        return

    print(items[index])
    show_cart_items(items, index + 1)


show_cart_items(["laptop", "mouse", "bag"])
```

Output:

```text
laptop
mouse
bag
```

Without the base case, Python eventually raises `RecursionError`.

## Recursive Calls

Each recursive call should make the problem smaller.

```python
def total_price(prices):
    if not prices:
        return 0

    return prices[0] + total_price(prices[1:])


print(total_price([50000, 1200, 2500]))
```

Output:

```text
53700
```

Here the list becomes smaller on every call.

## Call Stack

Python stores unfinished function calls in the call stack.

```python
def apply_discount(price, times):
    if times == 0:
        return price

    return apply_discount(price - 100, times - 1)


print(apply_discount(1000, 3))
```

Output:

```text
700
```

Each call waits until the smaller call returns.

## Recursion vs Iteration

| Recursion | Iteration |
|-----------|-----------|
| uses function calls | uses loops |
| useful for trees, DFS, backtracking | useful for simple repeated tasks |
| may hit recursion depth limit | usually more memory-friendly |
| often clean for divide-and-conquer | often faster in Python |

## Backtracking

Backtracking is recursion with choices.

The pattern is:

1. Choose
2. Explore recursively
3. Undo the choice

```python
def build_bundles(items, path=None, index=0):
    if path is None:
        path = []

    if index == len(items):
        print(path)
        return

    path.append(items[index])
    build_bundles(items, path, index + 1)
    path.pop()

    build_bundles(items, path, index + 1)


build_bundles(["mouse", "bag"])
```

Output:

```text
['mouse', 'bag']
['mouse']
['bag']
[]
```

Backtracking is used for combinations, permutations, subsets, constraint problems, and search problems.

## Recursive Problem Types

| Problem type | Example |
|--------------|---------|
| Linear recursion | sum prices in a list |
| Divide and conquer | binary search, merge sort |
| Tree recursion | traverse categories |
| Backtracking | generate product bundles |
| DFS recursion | explore connected pages or graph routes |

## Common Recursion Mistakes

| Mistake | Problem |
|---------|---------|
| Missing base case | infinite recursion |
| Problem not getting smaller | infinite recursion |
| Too much list slicing | extra memory/time |
| Mutating shared list without undo | wrong backtracking result |
| Recursing too deeply | `RecursionError` |

## Safer Recursive Style

Prefer passing an index instead of slicing large lists.

```python
def sum_prices(prices, index=0):
    if index == len(prices):
        return 0

    return prices[index] + sum_prices(prices, index + 1)


print(sum_prices([100, 200, 300]))
```

Output:

```text
600
```

## Time and Space Complexity

| Pattern | Time | Space |
|---------|------|-------|
| one recursive call per item | `O(n)` | `O(n)` call stack |
| binary recursion | often `O(2^n)` | depends on depth |
| backtracking subsets | `O(2^n)` | `O(n)` path plus output |
| permutations | `O(n!)` | `O(n)` path plus output |

## Interview Checklist

For recursion problems, always explain:

- What is the base case?
- How does the recursive call reduce the problem?
- What does each call return?
- What is stored in the call stack?
- For backtracking, when do you undo the choice?

## See also

- [Interview problems](interview-problems.md)
- [Interview questions](interview-questions.md)
- [Trees](../trees/core-concepts.md)
- [Graphs](../graphs/core-concepts.md)
