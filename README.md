# Python Sorting Algorithm

A clean implementation of selection sort without using Python's built-in sorting functions.

## About

This project implements a fundamental sorting algorithm from scratch to demonstrate understanding of:
- Algorithm design and implementation
- Time and space complexity analysis
- Python fundamentals (loops, conditionals, lists)

Built as a learning exercise to solidify core computer science concepts.

## How It Works

The algorithm uses **selection sort**:
1. Find the smallest element in the unsorted list
2. Add it to the sorted list
3. Remove it from the unsorted list
4. Repeat until all elements are sorted

## Usage

```python
from sorting_algorithm import selection_sort

# Sort numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]

# Sort letters
letters = ['c', 'l', 'y', 'z', 'x', 'o', 'a', 'b']
sorted_letters = selection_sort(letters)
print(sorted_letters)  # ['a', 'b', 'c', 'l', 'o', 'x', 'y', 'z']
```

Or run directly:
```bash
python sorting_algorithm.py
```

## Complexity

| Metric | Complexity |
|--------|------------|
| Time   | O(n³)      |
| Space  | O(n)       |

**Note:** This implementation is O(n³) due to the `list.remove()` operation which scans the list. Standard selection sort is O(n²).

## What I Learned

- How sorting algorithms work at a fundamental level
- The impact of different operations on time complexity
- Designing algorithms without relying on built-in functions
- Writing clean, readable code with proper documentation

## Requirements

- Python 3.x
- No external dependencies

## License

MIT
