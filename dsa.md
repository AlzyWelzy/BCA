# Data Structures and Algorithms Cheatsheet with Explanation and Code Snippets in Python, Java, C/C++, and JavaScript

## Table of Contents

- [Data Structures and Algorithms Cheatsheet](#data-structures-and-algorithms-cheatsheet)
  - [Table of Contents](#table-of-contents)
  - [Data Structures](#data-structures)
    - [Arrays](#arrays)
      - [Array Declaration](#array-declaration)
      - [Array Traversal](#array-traversal)
      - [Array Insertion](#array-insertion)
      - [Array Deletion](#array-deletion)
    - [Linked Lists](#linked-lists)
      - [Linked List Declaration](#linked-list-declaration)
      - [Linked List Traversal](#linked-list-traversal)
      - [Linked List Insertion](#linked-list-insertion)
      - [Linked List Deletion](#linked-list-deletion)
  - [Algorithms](#algorithms)
    - [Sorting](#sorting)
      - [Bubble Sort](#bubble-sort)
      - [Selection Sort](#selection-sort)
      - [Insertion Sort](#insertion-sort)
      - [Merge Sort](#merge-sort)
      - [Quick Sort](#quick-sort)
    - [Searching](#searching)
      - [Linear Search](#linear-search)
      - [Binary Search](#binary-search)
      - [Jump Search](#jump-search)
      - [Interpolation Search](#interpolation-search)
      - [Exponential Search](#exponential-search)
      - [Fibonacci Search](#fibonacci-search)
    - [Graphs](#graphs)
      - [Breadth First Search](#breadth-first-search)
      - [Depth First Search](#depth-first-search)
      - [Dijkstra's Algorithm](#dijkstras-algorithm)
      - [Floyd Warshall](#floyd-warshall)
      - [Kruskal's Algorithm](#kruskals-algorithm)
      - [Prim's Algorithm](#prims-algorithm)
    - [Dynamic Programming](#dynamic-programming)
      - [Knapsack Problem](#knapsack-problem)
      - [Longest Common Subsequence](#longest-common-subsequence)
      - [Matrix Chain Multiplication](#matrix-chain-multiplication)
      - [Rod Cutting](#rod-cutting)
      - [Subset Sum](#subset-sum)
    - [Mathematics](#mathematics)

## Data Structures

Data structures are a way of organizing data in a computer so that it can be used efficiently. There are many different types of data structures, each with its own advantages and disadvantages. Some of the most common data structures are arrays, linked lists, stacks, queues, trees, and graphs. In this section, we will discuss the most common data structures and their implementations in Python, Java, C/C++, and JavaScript. We will also discuss the time and space complexity of each data structure.

### Arrays

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

#### Array Declaration

In Python:

```python
array = [1, 2, 3, 4, 5]
```

In Java:

```java
int[] array = new int[]{1, 2, 3, 4, 5};
```

In C/C++:

```c
int array[] = {1, 2, 3, 4, 5};
```

In JavaScript:

```javascript
const array = [1, 2, 3, 4, 5];
```

#### Array Traversal

In Python:

```python
for i in range(len(array)):
  print(array[i])
```

In Java:

```java
for (int i = 0; i < array.length; i++) {
  System.out.println(array[i]);
}
```

In C/C++:

```c
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
  printf("%d ", array[i]);
}
```

In JavaScript:

```javascript
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```

#### Array Insertion
