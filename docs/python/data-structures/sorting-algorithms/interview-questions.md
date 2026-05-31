# Sorting Algorithms: 10 Interview Questions

## 1. What is Bubble Sort?

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

## 2. What is Selection Sort?

Selection Sort repeatedly finds the smallest element from the unsorted section and places it at the beginning.

## 3. What is Insertion Sort?

Insertion Sort builds a sorted section one item at a time by inserting each new item into its correct position.

## 4. What is Merge Sort?

Merge Sort is a divide-and-conquer algorithm that splits the list, sorts each half, and merges sorted halves.

## 5. What is Quick Sort?

Quick Sort chooses a pivot, partitions values around the pivot, and recursively sorts the partitions.

## 6. What is Heap Sort?

Heap Sort uses a heap to repeatedly remove the smallest or largest element and build a sorted result.

## 7. Which sorting algorithms are stable?

Bubble Sort, Insertion Sort, and Merge Sort are commonly stable. Selection Sort, Quick Sort, and Heap Sort are not usually stable.

## 8. Which sorting algorithms are `O(n log n)`?

Merge Sort, average-case Quick Sort, and Heap Sort are `O(n log n)`.

## 9. When is Insertion Sort useful?

Insertion Sort is useful for small lists or nearly sorted data because it can run close to `O(n)` in best cases.

## 10. What should you use for sorting in production Python?

Use Python's built-in `sorted()` or list `.sort()`, which use stable Timsort.

## See also

- [Core concepts](core-concepts.md)
- [Interview problems](interview-problems.md)
