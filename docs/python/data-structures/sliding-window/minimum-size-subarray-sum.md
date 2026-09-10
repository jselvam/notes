# Minimum Size Subarray Sum

## Problem

Given an array of **positive integers** `nums` and a **positive integer** `target`, find the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

This is **Problem 2** in the Sliding Window section.

## Examples

```text
Input:  nums = [2, 3, 1, 2, 4, 3], target = 7
Output: 2
```

Explanation: `[4, 3]` has sum `7` and length `2`.

```text
Input:  nums = [1, 4, 4], target = 4
Output: 1
```

```text
Input:  nums = [1, 1, 1, 1], target = 10
Output: 0
```

## Brute-Force Idea

Start at every index and keep adding numbers until the running sum becomes greater than or equal to `target`.

When the sum reaches the target, update the minimum length and stop expanding that start position.

## Your Brute-Force Version

```python
nums = [2, 3, 1, 2, 4, 3]
target = 7


def minSubAarrayLen(nums, target):
    min = 0

    for outerIndex in range(len(nums)):
        sum = nums[outerIndex]
        length = 0

        if sum >= target:
            min = 1
            return min

        length += 1

        for innerIndex in range(outerIndex + 1, len(nums)):
            sum += nums[innerIndex]
            length += 1

            if sum >= target:
                if length < min or min == 0:
                    min = length

                break

    return min


print(minSubAarrayLen(nums, target))
```

Output:

```text
2
```

### Brute-Force Complexity

- Time: **O(n^2)** because each start index may scan many later elements.
- Space: **O(1)** because only counters and running totals are stored.

## Optimized Sliding Window Idea

Because all numbers are positive, expanding the window always increases the sum and shrinking from the left always decreases it.

That makes a variable-size sliding window possible:

1. Expand the window by moving `right`.
2. Add `nums[right]` to the current sum.
3. While the sum is greater than or equal to `target`, record the window length.
4. Shrink from the left to check whether a smaller valid window exists.

## Your Optimized Version

```python
nums = [2, 3, 1, 2, 4, 3]
target = 7


def minimumSizeSubArray(nums, target):
    min = 0
    sumOfNumbers = 0
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] >= target:
            min = 1
            return min

        sumOfNumbers += nums[right]

        while sumOfNumbers >= target:
            length = right - left + 1

            if min == 0 or length < min:
                min = length

            sumOfNumbers -= nums[left]
            left += 1

        right += 1

    return min


print(minimumSizeSubArray(nums, target))
```

Output:

```text
2
```

### Optimized Complexity

- Time: **O(n)** because each element is added once and removed at most once.
- Space: **O(1)** because the algorithm uses a fixed number of variables.

## Clean Interview Version

This version keeps the same logic but uses clearer Python naming and avoids variable names such as `min` and `sum`, which hide Python built-in functions.

```python
def min_subarray_len(nums, target):
    min_length = 0
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            current_length = right - left + 1

            if min_length == 0 or current_length < min_length:
                min_length = current_length

            window_sum -= nums[left]
            left += 1

    return min_length


print(min_subarray_len([2, 3, 1, 2, 4, 3], 7))
print(min_subarray_len([1, 4, 4], 4))
print(min_subarray_len([1, 1, 1, 1], 10))
```

Output:

```text
2
1
0
```

## Dry Run

For:

```python
nums = [2, 3, 1, 2, 4, 3]
target = 7
```

| Step | Window | Sum | Action | Minimum length |
| --- | --- | ---: | --- | ---: |
| 1 | `[2]` | `2` | expand | `0` |
| 2 | `[2, 3]` | `5` | expand | `0` |
| 3 | `[2, 3, 1]` | `6` | expand | `0` |
| 4 | `[2, 3, 1, 2]` | `8` | valid, shrink left | `4` |
| 5 | `[3, 1, 2]` | `6` | stop shrinking | `4` |
| 6 | `[3, 1, 2, 4]` | `10` | valid, shrink left | `4` |
| 7 | `[1, 2, 4]` | `7` | valid, shrink left | `3` |
| 8 | `[2, 4]` | `6` | stop shrinking | `3` |
| 9 | `[2, 4, 3]` | `9` | valid, shrink left | `3` |
| 10 | `[4, 3]` | `7` | valid, shrink left | `2` |

Final answer:

```text
2
```

## Interview Takeaway

Once the window sum reaches the target, keep shrinking from the left while the sum is still greater than or equal to the target, recording the minimum window length.

That converts the brute-force **O(n^2)** approach into an **O(n)** sliding-window solution.

## See also

- [Maximum sum subarray of size k](maximum-sum-subarray-size-k.md)
- [Python list interview problems](../../list/interview-problems.md)
