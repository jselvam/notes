# Maximum Sum Subarray of Size K

## Problem

Given an integer list `nums` and an integer `k`, find the maximum sum of any contiguous subarray of exactly size `k`.

For **Week 1 Day 3 - DSA Problem 1**:

```text
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

Expected output:

```text
9
```

The answer is `9` because the subarray `[5, 1, 3]` has the highest sum among all subarrays of size `3`.

## Pattern

This is a **fixed-size sliding window** problem.

Instead of calculating every subarray sum from scratch, keep a running window sum:

1. Add the current right-side element.
2. Once the window becomes larger than `k`, remove the left-side element.
3. When the window size is exactly `k`, update the maximum sum.

This avoids repeated work.

## Dry Run

For:

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3
```

| Window | Sum | Maximum |
| --- | ---: | ---: |
| `[2, 1, 5]` | `8` | `8` |
| `[1, 5, 1]` | `7` | `8` |
| `[5, 1, 3]` | `9` | `9` |
| `[1, 3, 2]` | `6` | `9` |

Final answer:

```text
9
```

## Correct Python Program

```python
def max_subarray_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    max_sum = float("-inf")
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)

    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3

print(max_subarray_sum(nums, k))
```

Output:

```text
9
```

## Why This Version Is Safer

Avoid using `max` and `sum` as variable names because they hide Python's built-in `max()` and `sum()` functions.

Also, initialize the answer with `float("-inf")` instead of `0`. If all numbers are negative, starting from `0` gives the wrong answer.

Example:

```python
nums = [-5, -2, -8]
k = 2

print(max_subarray_sum(nums, k))
```

Output:

```text
-7
```

The best subarray is `[-5, -2]`.

## More Test Cases

```python
print(max_subarray_sum([1, 2, 3], 1))          # 3
print(max_subarray_sum([1, 2, 3], 3))          # 6
print(max_subarray_sum([5, -1, 2, -3, 4], 2))  # 4
print(max_subarray_sum([-5, -2, -8], 2))       # -7
```

## Complexity

- Time: **O(n)** because each element is added once and removed at most once.
- Space: **O(1)** because only a few variables are used.

## Interview Notes

- Use this pattern when the problem asks for a subarray or substring of a fixed size.
- Use two pointers, usually named `left` and `right`, to represent the current window.
- Add the new right element and remove the old left element when the window grows beyond `k`.
- For variable-size windows, the condition usually changes from fixed length to a rule such as sum, count, or uniqueness.

## See also

- [Minimum size subarray sum](minimum-size-subarray-sum.md)
- [Python list interview problems](../../list/interview-problems.md)
- [Dynamic programming interview problems](../dynamic-programming/interview-problems.md)
