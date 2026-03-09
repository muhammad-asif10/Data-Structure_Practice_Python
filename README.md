# Data Structures & Sorting Algorithms in Python

A collection of fundamental **data structure** operations and **sorting algorithm** implementations written in Python, aimed at building a strong foundation in computer science concepts.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Data Structures](#data-structures)
  - [Array](#array)
  - [List](#list)
  - [Graph](#graph)
- [Sorting Algorithms](#sorting-algorithms)
  - [Bubble Sort](#bubble-sort)
  - [Insertion Sort](#insertion-sort)
  - [Selection Sort](#selection-sort)
  - [Quick Sort](#quick-sort)
  - [Counting Sort](#counting-sort)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Complexity Reference](#complexity-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository serves as a hands-on practice ground for implementing and understanding core data structures and sorting algorithms in Python. Each file is self-contained and can be run independently, making it easy to study and experiment with individual concepts.

---

## Data Structures

### Array

**File:** `Array.py`

Demonstrates the use of Python's built-in `array` module to create a typed array of integers and print its contents.

```python
import array
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
```

### List

**File:** `List.py`

Covers common Python list operations:

| Operation | Method | Description |
|-----------|--------|-------------|
| Add to end | `append()` | Appends a single element to the end |
| Insert at index | `insert()` | Inserts an element at a specified index |
| Remove last | `pop()` | Removes and returns the last element |
| Add multiple | `extend()` | Extends the list with another iterable |
| Reverse | `reverse()` | Reverses the list in-place |
| Length | `len()` | Returns the number of elements |
| Maximum | `max()` | Returns the maximum value |
| Minimum | `min()` | Returns the minimum value |
| Sum | `sum()` | Returns the sum of all elements |

### Graph

**File:** `graph.py`

Placeholder for graph data structure implementations (work in progress).

---

## Sorting Algorithms

### Bubble Sort

**File:** `Bubble Sort.py`

Repeatedly compares adjacent elements and swaps them if they are in the wrong order. Includes an early-exit optimization using a `swapped` flag.

- **Best Case:** O(n) — already sorted
- **Average / Worst Case:** O(n²)
- **Space:** O(1)

### Insertion Sort

**File:** `Insertion Sort.py`

Builds the sorted array one element at a time by inserting each element into its correct position among the previously sorted elements.

- **Best Case:** O(n) — nearly sorted input
- **Average / Worst Case:** O(n²)
- **Space:** O(1)

### Selection Sort

**File:** `Selection Sort.py`

Divides the array into a sorted and an unsorted portion. In each pass it finds the minimum element from the unsorted portion and moves it to the end of the sorted portion.

- **Best / Average / Worst Case:** O(n²)
- **Space:** O(1)

### Quick Sort

**File:** `Quick-sort.py`

A divide-and-conquer algorithm that selects a pivot, partitions the array around it, and recursively sorts the sub-arrays. Uses the rightmost element as the pivot.

- **Best / Average Case:** O(n log n)
- **Worst Case:** O(n²) — already sorted / reverse-sorted input
- **Space:** O(log n) — recursive call stack

### Counting Sort

**File:** `Counting_Sort.py`

A non-comparison-based algorithm that counts the occurrences of each value and reconstructs the sorted array. Efficient when the range of input values is known and small.

- **Best / Average / Worst Case:** O(n + k), where k is the range of input values
- **Space:** O(k)

---

## Getting Started

### Prerequisites

- Python **3.6** or higher

Verify your Python installation:

```bash
python --version
```

No additional packages or dependencies are required — all implementations rely solely on the Python standard library.

### Usage

Clone the repository and run any script directly:

```bash
git clone https://github.com/muhammad-asif10/Data-Structure_Practice_Python.git
cd Data-Structure_Practice_Python
```

Run a specific file:

```bash
python "Bubble Sort.py"
python "Insertion Sort.py"
python "Selection Sort.py"
python "Quick-sort.py"
python Counting_Sort.py
python Array.py
python List.py
```

---

## Complexity Reference

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) |

---

## Contributing

Contributions are welcome! If you would like to add new data structures, sorting algorithms, or improve existing implementations:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

Please keep each implementation self-contained in its own file and follow the existing coding style.

---

## License

This project is open source and available under the [MIT License](LICENSE).
