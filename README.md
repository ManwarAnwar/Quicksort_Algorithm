# Quicksort Algorithm: Implementation and Analysis

## Overview
This project demonstrates the implementation, analysis, and empirical comparison of:
- **Deterministic Quicksort** (fixed pivot: last element)
- **Randomized Quicksort** (random pivot selection)

It highlights how algorithmic design impacts performance based on input characteristics and provides timing comparisons for both approaches across different input sizes.

---

##  Key Concepts

- **Quicksort** is a Divide-and-Conquer algorithm that:
  - Selects a pivot
  - Partitions the array
  - Recursively sorts subarrays

- **Randomized Quicksort** avoids worst-case performance on sorted inputs by choosing a random pivot.

---

## 🧪 Experimental Setup

The script runs both algorithms on arrays of varying sizes (`100`, `500`, `1000`, `2000`) with random integers and compares timing.

---

## 📊 Summary of Findings

| Input Size | Deterministic Time (s) | Randomized Time (s) |
|------------|------------------------|---------------------|
| 100        | ~0.001s                | ~0.001s             |
| 500        | ~0.003s                | ~0.003s             |
| 1000       | ~0.008s                | ~0.008s             |
| 2000       | ~0.02s                 | ~0.02s              |

- Both algorithms perform similarly on random input.
- **Randomized Quicksort** offers better resilience against **worst-case input** like sorted or reverse-sorted arrays.
- Time complexity remains around `O(n log n)` on average for both.

---

## ▶️ How to Run the Code

### Requirements
- Python 3.x
- `numpy` (install via `pip install numpy`)

### Steps
1. Open terminal and navigate to the project folder:
   ```bash
   cd path/to/quicksort_project
