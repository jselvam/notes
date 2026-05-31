# Searching Algorithms: 10 Interview Questions

## 1. What is linear search?

Linear search checks each element one by one until it finds the target or reaches the end.

## 2. What is the time complexity of linear search?

Linear search takes `O(n)` time and `O(1)` extra space.

## 3. What is binary search?

Binary search repeatedly checks the middle element of a sorted search space and eliminates half of the remaining values.

## 4. What is the time complexity of binary search?

Binary search takes `O(log n)` time and `O(1)` extra space for the iterative version.

## 5. Why must data be sorted for binary search?

Binary search decides which half to discard by comparing the target with the middle value. That decision is valid only when the data is ordered.

## 6. How do you find the first occurrence of a target with binary search?

When the target is found, store the index and continue searching on the left side.

## 7. How do you find the last occurrence of a target with binary search?

When the target is found, store the index and continue searching on the right side.

## 8. How does search in rotated sorted array work?

At each step, identify which half is sorted and check whether the target lies inside that sorted half.

## 9. What is a peak element?

A peak element is an element that is greater than its neighbor or neighbors.

## 10. What are common binary search mistakes?

Common mistakes include wrong loop condition, incorrect boundary updates, infinite loops, and off-by-one errors.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
