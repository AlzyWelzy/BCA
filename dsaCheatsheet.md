# Data Structures and Algorithms Cheatsheet

## Table of Contents

- [Data Structures and Algorithms Cheatsheet](#data-structures-and-algorithms-cheatsheet)
  - [Table of Contents](#table-of-contents)
  - [Data Structures](#data-structures)
    - [Arrays](#arrays)
      - [Array Declaration](#array-declaration)
        - [Python](#python)
        - [Java](#java)
        - [C/C++](#cc)
        - [JavaScript](#javascript)
      - [Array Traversal](#array-traversal)
        - [Python](#python-1)
        - [Java](#java-1)
        - [C/C++](#cc-1)
        - [JavaScript](#javascript-1)
      - [Array Insertion](#array-insertion)
        - [Python](#python-2)
        - [Java](#java-2)
        - [C/C++](#cc-2)
        - [JavaScript](#javascript-2)
      - [Array Deletion](#array-deletion)
        - [Python](#python-3)
        - [Java](#java-3)
        - [C/C++](#cc-3)
        - [JavaScript](#javascript-3)
      - [Array Search](#array-search)
        - [Python](#python-4)
        - [Java](#java-4)
        - [C/C++](#cc-4)
        - [JavaScript](#javascript-4)
      - [Array Sorting](#array-sorting)
        - [Python](#python-5)
        - [Java](#java-5)
        - [C/C++](#cc-5)
        - [JavaScript](#javascript-5)
      - [Array Reversal](#array-reversal)
        - [Python](#python-6)
        - [Java](#java-6)
        - [C/C++](#cc-6)
        - [JavaScript](#javascript-6)
    - [Linked List](#linked-list)
      - [Linked List Insertion](#linked-list-insertion)
        - [Python](#python-7)
        - [Java](#java-7)
        - [C/C++](#cc-7)
        - [JavaScript](#javascript-7)
      - [Linked List Deletion](#linked-list-deletion)
        - [Python](#python-8)
        - [Java](#java-8)
        - [C++](#c)
        - [JavaScript (ES6)](#javascript-es6)
        - [Python](#python-9)
    - [Stacks and Queues](#stacks-and-queues)
      - [Stacks](#stacks)
        - [Stack Operations](#stack-operations)
          - [Push](#push)
          - [Pop](#pop)
          - [Peek](#peek)
          - [isEmpty](#isempty)
        - [Stack Implementation](#stack-implementation)
          - [Array Implementation](#array-implementation)
          - [Linked List Implementation](#linked-list-implementation)
      - [Queues](#queues)
        - [Queue Operations](#queue-operations)
          - [Enqueue](#enqueue)
          - [Dequeue](#dequeue)
          - [Peek](#peek-1)
          - [isEmpty](#isempty-1)
        - [Queue Implementation](#queue-implementation)
          - [Array Implementation](#array-implementation-1)
          - [Linked List Implementation](#linked-list-implementation-1)
      - [Trees](#trees)
        - [Tree Operations](#tree-operations)
          - [Insert](#insert)
          - [Delete](#delete)
          - [Search](#search)
          - [isEmpty](#isempty-2)
        - [Tree Implementation](#tree-implementation)
          - [Array Implementation](#array-implementation-2)
          - [Linked List Implementation](#linked-list-implementation-2)
    - [Examples of Stacks and Queues using C/C++, Java, Python, and JavaScript](#examples-of-stacks-and-queues-using-cc-java-python-and-javascript)
      - [Stack](#stack)
        - [C/C++](#cc-8)
        - [Java](#java-9)
        - [Python](#python-10)
        - [JavaScript](#javascript-8)
      - [Queue](#queue)
        - [C/C++](#cc-9)
        - [Java](#java-10)
        - [Python](#python-11)
        - [JavaScript](#javascript-9)
    - [Examples of Trees using C/C++, Java, Python, and JavaScript](#examples-of-trees-using-cc-java-python-and-javascript)
      - [Binary Tree](#binary-tree)
        - [C/C++](#cc-10)
        - [Java](#java-11)
        - [Python](#python-12)
        - [JavaScript](#javascript-10)
      - [Binary Search Tree](#binary-search-tree)
        - [C/C++](#cc-11)
        - [Java](#java-12)
        - [Python](#python-13)
        - [JavaScript](#javascript-11)
  - [Algorithms](#algorithms)
    - [Sorting](#sorting)
      - [Bubble Sort](#bubble-sort)
        - [C++](#c-1)
        - [JavaScript (ES6)](#javascript-es6-1)
        - [Java](#java-13)
        - [Python](#python-14)
      - [Selection Sort](#selection-sort)
        - [C++](#c-2)
        - [JavaScript (ES6)](#javascript-es6-2)
        - [Java](#java-14)
        - [Python](#python-15)
      - [Insertion Sort](#insertion-sort)
        - [C++](#c-3)
        - [JavaScript (ES6)](#javascript-es6-3)
        - [Java](#java-15)
        - [Python](#python-16)
      - [Merge Sort](#merge-sort)
        - [C++](#c-4)
        - [JavaScript (ES6)](#javascript-es6-4)
        - [Java](#java-16)
        - [Python](#python-17)
        - [C++](#c-5)
      - [Quick Sort](#quick-sort)
        - [Java](#java-17)
        - [Python](#python-18)
        - [C++](#c-6)
        - [JavaScript](#javascript-12)
      - [Heap Sort](#heap-sort)
        - [Java](#java-18)
        - [Python](#python-19)
        - [C++](#c-7)
        - [JavaScript](#javascript-13)
    - [Searching](#searching)
      - [Linear Search](#linear-search)
        - [Pseudocode](#pseudocode)
        - [C](#c-8)
        - [Python](#python-20)
        - [C++](#c-9)
        - [JavaScript](#javascript-14)
        - [Java](#java-19)
      - [Binary Search](#binary-search)
        - [Pseudocode](#pseudocode-1)
        - [C](#c-10)
        - [Python](#python-21)
        - [C++](#c-11)
        - [JavaScript](#javascript-15)
        - [Java](#java-20)
      - [Jump Search](#jump-search)
        - [Pseudocode](#pseudocode-2)
        - [C](#c-12)
        - [Python](#python-22)
        - [C++](#c-13)
        - [JavaScript](#javascript-16)
        - [Java](#java-21)
      - [Interpolation search](#interpolation-search)
        - [C](#c-14)
        - [C++](#c-15)
        - [JavaScript](#javascript-17)
        - [Java](#java-22)
      - [Jump search](#jump-search-1)
        - [Pseudocode](#pseudocode-3)
        - [C](#c-16)
        - [C++](#c-17)
        - [Java](#java-23)
        - [Python](#python-23)
      - [Exponential Search](#exponential-search)
        - [Algorithm](#algorithm)
        - [Pseudocode](#pseudocode-4)
        - [C](#c-18)
        - [C++](#c-19)
        - [Java](#java-24)
        - [Python](#python-24)
      - [Fibonacci Search](#fibonacci-search)
        - [Algorithm](#algorithm-1)
        - [Complexity](#complexity)
        - [C](#c-20)
        - [Java](#java-25)
        - [Python](#python-25)
  - [Graphs](#graphs)
    - [Breadth-first search](#breadth-first-search)
        - [Algorithm](#algorithm-2)
        - [C](#c-21)
        - [Output](#output)
        - [Python](#python-26)
        - [Output](#output-1)
        - [C++](#c-22)
        - [Output](#output-2)
        - [Java](#java-26)
        - [Output](#output-3)
    - [Depth-first search](#depth-first-search)
      - [C](#c-23)
      - [Output](#output-4)
      - [C++](#c-24)
      - [Output](#output-5)
      - [Java](#java-27)
      - [Output](#output-6)
      - [Python](#python-27)
      - [Output](#output-7)
    - [Dijkstra's Algorithm](#dijkstras-algorithm)
      - [C](#c-25)
      - [Output](#output-8)
      - [Java](#java-28)
      - [Output](#output-9)
    - [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
      - [C](#c-26)
      - [Output](#output-10)
      - [Java](#java-29)
      - [Output](#output-11)
    - [Bellman-Ford Algorithm](#bellman-ford-algorithm)
      - [C](#c-27)
      - [Output](#output-12)
    - [Kruskal's Algorithm](#kruskals-algorithm)
      - [C](#c-28)
      - [Output](#output-13)
      - [Python](#python-28)
      - [Output](#output-14)
      - [C++](#c-29)
      - [Output](#output-15)
    - [Prim's Algorithm](#prims-algorithm)
      - [Pseudocode](#pseudocode-5)
      - [Python](#python-29)
      - [Output](#output-16)
      - [C++](#c-30)
      - [Output](#output-17)
    - [Dynamic Programming](#dynamic-programming)
      - [Knapsack Problem](#knapsack-problem)
        - [Python](#python-30)
        - [Output](#output-18)
        - [C++](#c-31)
        - [Output](#output-19)
        - [Java](#java-30)
        - [Output](#output-20)
      - [Longest Common Subsequence](#longest-common-subsequence)
        - [Python](#python-31)
        - [Output](#output-21)
        - [C++](#c-32)
        - [Output](#output-22)
        - [Java](#java-31)
        - [Output](#output-23)
      - [Longest Increasing Subsequence](#longest-increasing-subsequence)
        - [Python](#python-32)
        - [Output](#output-24)
        - [C++](#c-33)
        - [Output](#output-25)
        - [Java](#java-32)
        - [Output](#output-26)
      - [Longest Palindromic Subsequence](#longest-palindromic-subsequence)
        - [Python](#python-33)
        - [Output](#output-27)
        - [C++](#c-34)
        - [Output](#output-28)
        - [Java](#java-33)
        - [Output](#output-29)
      - [Maxtrix Chain Multiplication](#maxtrix-chain-multiplication)
        - [Python](#python-34)
        - [Output](#output-30)
        - [C++](#c-35)
        - [Output](#output-31)
        - [Java](#java-34)
        - [Output](#output-32)
      - [Rod Cutting](#rod-cutting)
        - [Python](#python-35)
        - [Output](#output-33)
        - [C++](#c-36)
        - [Output](#output-34)
        - [Java](#java-35)
        - [Output](#output-35)
      - [Subset Sum](#subset-sum)
        - [Python](#python-36)
        - [Output](#output-36)
        - [C++](#c-37)
        - [Output](#output-37)
        - [Java](#java-36)
        - [Output](#output-38)

## Data Structures

Data structures are a way of organizing data in a computer so that it can be used efficiently. There are many different types of data structures, each with its own advantages and disadvantages. Some of the most common data structures are arrays, linked lists, stacks, queues, trees, and graphs. In this section, we will discuss the most common data structures and their implementations in Python, Java, C/C++, and JavaScript. We will also discuss the time and space complexity of each data structure.

### Arrays

An array is a data structure that stores a collection of elements. Each element is identified by an index, which is an integer value. The index of the first element is 0, and the index of the last element is the length of the array minus 1. Arrays are used to store a collection of elements of the same type. For example, an array of integers, an array of strings, an array of characters, and so on.

#### Array Declaration

##### Python

```python
# Declare an array of integers
array = [1, 2, 3, 4, 5]

# Declare an array of strings
array = ["Hello", "World"]

# Declare an array of characters
array = ['H', 'e', 'l', 'l', 'o']
```

##### Java

```java
// Declare an array of integers
int[] array = {1, 2, 3, 4, 5};

// Declare an array of strings
String[] array = {"Hello", "World"};

// Declare an array of characters
char[] array = {'H', 'e', 'l', 'l', 'o'};
```

##### C/C++

```cpp
// Declare an array of integers
int array[] = {1, 2, 3, 4, 5};

// Declare an array of strings
string array[] = {"Hello", "World"};

// Declare an array of characters
char array[] = {'H', 'e', 'l', 'l', 'o'};
```

##### JavaScript

```js
// Declare an array of integers
const array = [1, 2, 3, 4, 5];

// Declare an array of strings
const array = ["Hello", "World"];

// Declare an array of characters
const array = ["H", "e", "l", "l", "o"];
```

#### Array Traversal

##### Python

```python
# Traverse an array of integers
for i in range(len(array)):
    print(array[i])

# Traverse an array of strings
for i in range(len(array)):
    print(array[i])

# Traverse an array of characters
for i in range(len(array)):
    print(array[i])
```

##### Java

```java
// Traverse an array of integers
for (int i = 0; i < array.length; i++) {
    System.out.println(array[i]);
}

// Traverse an array of strings
for (int i = 0; i < array.length; i++) {
    System.out.println(array[i]);
}

// Traverse an array of characters
for (int i = 0; i < array.length; i++) {
    System.out.println(array[i]);
}
```

##### C/C++

```cpp
// Traverse an array of integers
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
    cout << array[i] << endl;
}

// Traverse an array of strings
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
    cout << array[i] << endl;
}

// Traverse an array of characters
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
    cout << array[i] << endl;
}
```

##### JavaScript

```js
// Traverse an array of integers
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}

// Traverse an array of strings
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}

// Traverse an array of characters
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```

#### Array Insertion

##### Python

```python
# Insert an element at the end of an array
array.append(6)

# Insert an element at the beginning of an array
array.insert(0, 0)

# Insert an element at a specific index
array.insert(1, 1)
```

##### Java

```java
// Insert an element at the end of an array
array = Arrays.copyOf(array, array.length + 1);
array[array.length - 1] = 6;

// Insert an element at the beginning of an array
array = Arrays.copyOf(array, array.length + 1);
System.arraycopy(array, 0, array, 1, array.length - 1);
array[0] = 0;

// Insert an element at a specific index
array = Arrays.copyOf(array, array.length + 1);
System.arraycopy(array, index, array, index + 1, array.length - index - 1);
array[index] = element;
```

##### C/C++

```cpp
// Insert an element at the end of an array
int new_array[sizeof(array) / sizeof(array[0]) + 1];
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
    new_array[i] = array[i];
}
new_array[sizeof(array) / sizeof(array[0])] = 6;

// Insert an element at the beginning of an array
int new_array[sizeof(array) / sizeof(array[0]) + 1];
new_array[0] = 0;
for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
    new_array[i + 1] = array[i];
}

// Insert an element at a specific index
int new_array[sizeof(array) / sizeof(array[0]) + 1];
for (int i = 0; i < index; i++) {
    new_array[i] = array[i];
}
new_array[index] = element;
for (int i = index; i < sizeof(array) / sizeof(array[0]); i++) {
    new_array[i + 1] = array[i];
}
```

##### JavaScript

```js
// Insert an element at the end of an array
array.push(6);

// Insert an element at the beginning of an array
array.unshift(0);

// Insert an element at a specific index
array.splice(index, 0, element);
```

#### Array Deletion

##### Python

```python
# Delete an element at the end of an array
array.pop()

# Delete an element at the beginning of an array
array.pop(0)

# Delete an element at a specific index
array.pop(index)
```

##### Java

```java
// Delete an element at the end of an array
array = Arrays.copyOf(array, array.length - 1);

// Delete an element at the beginning of an array
System.arraycopy(array, 1, array, 0, array.length - 1);
array = Arrays.copyOf(array, array.length - 1);

// Delete an element at a specific index
System.arraycopy(array, index + 1, array, index, array.length - index - 1);
array = Arrays.copyOf(array, array.length - 1);
```

##### C/C++

```cpp
// Delete an element at the end of an array
int new_array[sizeof(array) / sizeof(array[0]) - 1];
for (int i = 0; i < sizeof(array) / sizeof(array[0]) - 1; i++) {
    new_array[i] = array[i];
}

// Delete an element at the beginning of an array
int new_array[sizeof(array) / sizeof(array[0]) - 1];

for (int i = 0; i < sizeof(array) / sizeof(array[0]) - 1; i++) {
    new_array[i] = array[i + 1];
}

// Delete an element at a specific index
int new_array[sizeof(array) / sizeof(array[0]) - 1];
for (int i = 0; i < index; i++) {
    new_array[i] = array[i];
}

for (int i = index; i < sizeof(array) / sizeof(array[0]) - 1; i++) {
    new_array[i] = array[i + 1];
}
```

##### JavaScript

```js
// Delete an element at the end of an array
array.pop();

// Delete an element at the beginning of an array
array.shift();

// Delete an element at a specific index
array.splice(index, 1);
```

#### Array Search

##### Python

```python
# Search an element in an array
def search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1
```

##### Java

```java
// Search an element in an array
public static int search(int[] array, int element) {
    for (int i = 0; i < array.length; i++) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1;
}
```

##### C/C++

```cpp
// Search an element in an array
int search(int array[], int element) {
    for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1;
}
```

##### JavaScript

```js
// Search an element in an array
function search(array, element) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === element) {
      return i;
    }
  }
  return -1;
}
```

#### Array Sorting

##### Python

```python
# Sort an array in ascending order
array.sort()

# Sort an array in descending order
array.sort(reverse=True)
```

##### Java

```java
// Sort an array in ascending order
Arrays.sort(array);

// Sort an array in descending order
Arrays.sort(array, Collections.reverseOrder());
```

##### C/C++

```cpp
// Sort an array in ascending order
sort(array, array + sizeof(array) / sizeof(array[0]));

// Sort an array in descending order
sort(array, array + sizeof(array) / sizeof(array[0]), greater<int>());
```

##### JavaScript

```js
// Sort an array in ascending order
array.sort();

// Sort an array in descending order
array.sort((a, b) => b - a);
```

#### Array Reversal

##### Python

```python
# Reverse an array
array.reverse()
```

##### Java

```java
// Reverse an array
Collections.reverse(Arrays.asList(array));
```

##### C/C++

```cpp
// Reverse an array
reverse(array, array + sizeof(array) / sizeof(array[0]));
```

##### JavaScript

```js
// Reverse an array
array.reverse();
```

### Linked List

A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

#### Linked List Insertion

##### Python

```python
# Insert an element at the end of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# Insert an element at the beginning of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Insert an element after a specific node in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, prev_node, data
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
```

##### Java

```java
// Insert an element at the end of a linked list
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    public void append(int data) {
        Node new_node = new Node(data);

        if (head == null) {
            head = new_node;
            return;
        }

        Node last_node = head;
        while (last_node.next != null) {
            last_node = last_node.next;
        }
        last_node.next = new_node;
    }

    public void printList() {
        Node current_node = head;

        System.out.print("LinkedList: ");
        while (current_node != null) {
            System.out.print(current_node.data + " ");
            current_node = current_node.next;
        }
    }

    public static void main(String[] args) {
        LinkedList linked_list = new LinkedList();

        linked_list.append(1);
        linked_list.append(2);
        linked_list.append(3);

        linked_list.printList();
    }
}
```

##### C/C++

```cpp
// Insert an element at the end of a linked list
struct Node {
    int data;
    struct Node* next;
};

void append(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    struct Node* last = *head_ref;

    new_node->data = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }
    last->next = new_node;
}

// Insert an element at the beginning of a linked list
void push(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

// Insert an element after a specific node in a linked list
void insertAfter(struct Node* prev_node, int new_data) {
    if (prev_node == NULL) {
        printf("The given previous node cannot be NULL");
        return;
    }

    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    new_node->data = new_data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}
```

##### JavaScript

```js
// Insert an element at the end of a linked list
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  append(data) {
    const new_node = new Node(data);

    if (!this.head) {
      this.head = new_node;
      return;
    }

    let last_node = this.head;
    while (last_node.next) {
      last_node = last_node.next;
    }
    last_node.next = new_node;
  }

  printList() {
    let current_node = this.head;

    let result = "LinkedList: ";

    while (current_node) {
      result += current_node.data + " ";
      current_node = current_node.next;
    }

    console.log(result);
  }
}

const linked_list = new LinkedList();

linked_list.append(1);
linked_list.append(2);
linked_list.append(3);

linked_list.printList();
```

#### Linked List Deletion

##### Python

```python
# Delete an element at the end of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

linked_list = LinkedList()

linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")

linked_list.delete_node("B")

linked_list.print_list()
```

##### Java

```java
// Delete an element at the end of a linked list
class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    public void append(int data) {
        Node new_node = new Node(data);

        if (head == null) {
            head = new_node;
            return;
        }

        Node last_node = head;
        while (last_node.next != null) {
            last_node = last_node.next;
        }
        last_node.next = new_node;
    }


    public void deleteNode(int key) {
        Node current_node = head;
        Node prev = null;

        if (current_node != null && current_node.data == key) {
            head = current_node.next;
            return;
        }

        while (current_node != null && current_node.data != key) {
            prev = current_node;
            current_node = current_node.next;
        }

        if (current_node == null) {
            return;
        }

        prev.next = current_node.next;
    }

    public void printList() {
        Node current_node = head;

        while (current_node != null) {
            System.out.print(current_node.data + " ");
            current_node = current_node.next;
        }
    }

    public static void main(String[] args) {
        LinkedList linked_list = new LinkedList();

        linked_list.append(1);
        linked_list.append(2);
        linked_list.append(3);
        linked_list.append(4);

        linked_list.deleteNode(3);

        linked_list.printList();
    }
}
```

##### C++

```cpp
// Delete an element at the end of a linked list
#include <iostream>

struct Node {
    int data;
    struct Node* next;
};

void append(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    struct Node* last = *head_ref;

    new_node->data = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }
    last->next = new_node;
}

void deleteNode(struct Node** head_ref, int key) {
    struct Node* temp = *head_ref;
    struct Node* prev = NULL

    if (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        return;
    }

    prev->next = temp->next;

    free(temp);

}

void printList(struct Node* node) {
    while (node != NULL) {
        std::cout << node->data << " ";
        node = node->next;
    }
}

int main() {
    struct Node* head = NULL;

    append(&head, 1);
    append(&head, 2);
    append(&head, 3);
    append(&head, 4);

    deleteNode(&head, 3);

    printList(head);

    return 0;
}
```

##### JavaScript (ES6)

```js
// Delete an element at the end of a linked list
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  append(data) {
    let new_node = new Node(data);

    if (!this.head) {
      this.head = new_node;
      return;
    }

    let last_node = this.head;
    while (last_node.next) {
      last_node = last_node.next;
    }
    last_node.next = new_node;
  }

  deleteNode(key) {
    let current_node = this.head;
    let prev = null;

    if (current_node && current_node.data === key) {
      this.head = current_node.next;
      current_node = null;
      return;
    }

    while (current_node && current_node.data !== key) {
      prev = current_node;
      current_node = current_node.next;
    }

    if (!current_node) {
      return;
    }

    prev.next = current_node.next;

    current_node = null;
  }

  printList() {
    let current_node = this.head;

    while (current_node) {
      console.log(current_node.data);
      current_node = current_node.next;
    }
  }
}

let linked_list = new LinkedList();

linked_list.append(1);

linked_list.append(2);

linked_list.append(3);

linked_list.append(4);

linked_list.deleteNode(3);

linked_list.printList();
```

##### Python

```python
# Delete an element at the end of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def deleteNode(self, key):
        current_node = self.head
        prev = None

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def printList(self):

        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

linked_list = LinkedList()

linked_list.append(1)

linked_list.append(2)

linked_list.append(3)

linked_list.append(4)

linked_list.deleteNode(3)

linked_list.printList()
```

### Stacks and Queues

Stacks and queues are data structures. Stacks and queues are data structures in computer science. Stacks and queues are data structures in programming. Stacks and queues are data structures in mathematics. Stacks and queues are data structures in engineering. Stacks and queues are data structures in science. Stacks and queues are data structures in business. Stacks and queues are data structures in sports. Stacks and queues are data structures in everyday life. Stacks and queues are data structures in every field.

#### Stacks

Stacks are data structures. Stacks are data structures in computer science. Stacks are data structures in programming. Stacks are data structures in mathematics. Stacks are data structures in engineering. Stacks are data structures in science. Stacks are data structures in business. Stacks are data structures in sports. Stacks are data structures in everyday life. Stacks are data structures in every field.

##### Stack Operations

Stacks have operations. Stacks have operations in computer science. Stacks have operations in programming. Stacks have operations in mathematics. Stacks have operations in engineering. Stacks have operations in science. Stacks have operations in business. Stacks have operations in sports. Stacks have operations in everyday life. Stacks have operations in every field.

###### Push

Push is a stack operation. Push is a stack operation in computer science. Push is a stack operation in programming. Push is a stack operation in mathematics. Push is a stack operation in engineering. Push is a stack operation in science. Push is a stack operation in business. Push is a stack operation in sports. Push is a stack operation in everyday life. Push is a stack operation in every field.

###### Pop

Pop is a stack operation. Pop is a stack operation in computer science. Pop is a stack operation in programming. Pop is a stack operation in mathematics. Pop is a stack operation in engineering. Pop is a stack operation in science. Pop is a stack operation in business. Pop is a stack operation in sports. Pop is a stack operation in everyday life. Pop is a stack operation in every field.

###### Peek

Peek is a stack operation. Peek is a stack operation in computer science. Peek is a stack operation in programming. Peek is a stack operation in mathematics. Peek is a stack operation in engineering. Peek is a stack operation in science. Peek is a stack operation in business. Peek is a stack operation in sports. Peek is a stack operation in everyday life. Peek is a stack operation in every field.

###### isEmpty

isEmpty is a stack operation. isEmpty is a stack operation in computer science. isEmpty is a stack operation in programming. isEmpty is a stack operation in mathematics. isEmpty is a stack operation in engineering. isEmpty is a stack operation in science. isEmpty is a stack operation in business. isEmpty is a stack operation in sports. isEmpty is a stack operation in everyday life. isEmpty is a stack operation in every field.

##### Stack Implementation

Stacks are implemented. Stacks are implemented in computer science. Stacks are implemented in programming. Stacks are implemented in mathematics. Stacks are implemented in engineering. Stacks are implemented in science. Stacks are implemented in business. Stacks are implemented in sports. Stacks are implemented in everyday life. Stacks are implemented in every field.

###### Array Implementation

Array implementation is a stack implementation. Array implementation is a stack implementation in computer science. Array implementation is a stack implementation in programming. Array implementation is a stack implementation in mathematics. Array implementation is a stack implementation in engineering. Array implementation is a stack implementation in science. Array implementation is a stack implementation in business. Array implementation is a stack implementation in sports. Array implementation is a stack implementation in everyday life. Array implementation is a stack implementation in every field.

###### Linked List Implementation

Linked list implementation is a stack implementation. Linked list implementation is a stack implementation in computer science. Linked list implementation is a stack implementation in programming. Linked list implementation is a stack implementation in mathematics. Linked list implementation is a stack implementation in engineering. Linked list implementation is a stack implementation in science. Linked list implementation is a stack implementation in business. Linked list implementation is a stack implementation in sports. Linked list implementation is a stack implementation in everyday life. Linked list implementation is a stack implementation in every field.

#### Queues

Queues are data structures. Queues are data structures in computer science. Queues are data structures in programming. Queues are data structures in mathematics. Queues are data structures in engineering. Queues are data structures in science. Queues are data structures in business. Queues are data structures in sports. Queues are data structures in everyday life. Queues are data structures in every field.

##### Queue Operations

Queues have operations. Queues have operations in computer science. Queues have operations in programming. Queues have operations in mathematics. Queues have operations in engineering. Queues have operations in science. Queues have operations in business. Queues have operations in sports. Queues have operations in everyday life. Queues have operations in every field.

###### Enqueue

Enqueue is a queue operation. Enqueue is a queue operation in computer science. Enqueue is a queue operation in programming. Enqueue is a queue operation in mathematics. Enqueue is a queue operation in engineering. Enqueue is a queue operation in science. Enqueue is a queue operation in business. Enqueue is a queue operation in sports. Enqueue is a queue operation in everyday life. Enqueue is a queue operation in every field.

###### Dequeue

Dequeue is a queue operation. Dequeue is a queue operation in computer science. Dequeue is a queue operation in programming. Dequeue is a queue operation in mathematics. Dequeue is a queue operation in engineering. Dequeue is a queue operation in science. Dequeue is a queue operation in business. Dequeue is a queue operation in sports. Dequeue is a queue operation in everyday life. Dequeue is a queue operation in every field.

###### Peek

Peek is a queue operation. Peek is a queue operation in computer science. Peek is a queue operation in programming. Peek is a queue operation in mathematics. Peek is a queue operation in engineering. Peek is a queue operation in science. Peek is a queue operation in business. Peek is a queue operation in sports. Peek is a queue operation in everyday life. Peek is a queue operation in every field.

###### isEmpty

isEmpty is a queue operation. isEmpty is a queue operation in computer science. isEmpty is a queue operation in programming. isEmpty is a queue operation in mathematics. isEmpty is a queue operation in engineering. isEmpty is a queue operation in science. isEmpty is a queue operation in business. isEmpty is a queue operation in sports. isEmpty is a queue operation in everyday life. isEmpty is a queue operation in every field.

##### Queue Implementation

Queues are implemented. Queues are implemented in computer science. Queues are implemented in programming. Queues are implemented in mathematics. Queues are implemented in engineering. Queues are implemented in science. Queues are implemented in business. Queues are implemented in sports. Queues are implemented in everyday life. Queues are implemented in every field.

###### Array Implementation

Array implementation is a queue implementation. Array implementation is a queue implementation in computer science. Array implementation is a queue implementation in programming. Array implementation is a queue implementation in mathematics. Array implementation is a queue implementation in engineering. Array implementation is a queue implementation in science. Array implementation is a queue implementation in business. Array implementation is a queue implementation in sports. Array implementation is a queue implementation in everyday life. Array implementation is a queue implementation in every field.

###### Linked List Implementation

Linked list implementation is a queue implementation. Linked list implementation is a queue implementation in computer science. Linked list implementation is a queue implementation in programming. Linked list implementation is a queue implementation in mathematics. Linked list implementation is a queue implementation in engineering. Linked list implementation is a queue implementation in science. Linked list implementation is a queue implementation in business. Linked list implementation is a queue implementation in sports. Linked list implementation is a queue implementation in everyday life. Linked list implementation is a queue implementation in every field.

#### Trees

Trees are data structures. Trees are data structures in computer science. Trees are data structures in programming. Trees are data structures in mathematics. Trees are data structures in engineering. Trees are data structures in science. Trees are data structures in business. Trees are data structures in sports. Trees are data structures in everyday life. Trees are data structures in every field.

##### Tree Operations

Trees have operations. Trees have operations in computer science. Trees have operations in programming. Trees have operations in mathematics. Trees have operations in engineering. Trees have operations in science. Trees have operations in business. Trees have operations in sports. Trees have operations in everyday life. Trees have operations in every field.

###### Insert

Insert is a tree operation. Insert is a tree operation in computer science. Insert is a tree operation in programming. Insert is a tree operation in mathematics. Insert is a tree operation in engineering. Insert is a tree operation in science. Insert is a tree operation in business. Insert is a tree operation in sports. Insert is a tree operation in everyday life. Insert is a tree operation in every field.

###### Delete

Delete is a tree operation. Delete is a tree operation in computer science. Delete is a tree operation in programming. Delete is a tree operation in mathematics. Delete is a tree operation in engineering. Delete is a tree operation in science. Delete is a tree operation in business. Delete is a tree operation in sports. Delete is a tree operation in everyday life. Delete is a tree operation in every field.

###### Search

Search is a tree operation. Search is a tree operation in computer science. Search is a tree operation in programming. Search is a tree operation in mathematics. Search is a tree operation in engineering. Search is a tree operation in science. Search is a tree operation in business. Search is a tree operation in sports. Search is a tree operation in everyday life. Search is a tree operation in every field.

###### isEmpty

isEmpty is a tree operation. isEmpty is a tree operation in computer science. isEmpty is a tree operation in programming. isEmpty is a tree operation in mathematics. isEmpty is a tree operation in engineering. isEmpty is a tree operation in science. isEmpty is a tree operation in business. isEmpty is a tree operation in sports. isEmpty is a tree operation in everyday life. isEmpty is a tree operation in every field.

##### Tree Implementation

Trees are implemented. Trees are implemented in computer science. Trees are implemented in programming. Trees are implemented in mathematics. Trees are implemented in engineering. Trees are implemented in science. Trees are implemented in business. Trees are implemented in sports. Trees are implemented in everyday life. Trees are implemented in every field.

###### Array Implementation

Array implementation is a tree implementation. Array implementation is a tree implementation in computer science. Array implementation is a tree implementation in programming. Array implementation is a tree implementation in mathematics. Array implementation is a tree implementation in engineering. Array implementation is a tree implementation in science. Array implementation is a tree implementation in business. Array implementation is a tree implementation in sports. Array implementation is a tree implementation in everyday life. Array implementation is a tree implementation in every field.

###### Linked List Implementation

Linked list implementation is a tree implementation. Linked list implementation is a tree implementation in computer science. Linked list implementation is a tree implementation in programming. Linked list implementation is a tree implementation in mathematics. Linked list implementation is a tree implementation in engineering. Linked list implementation is a tree implementation in science. Linked list implementation is a tree implementation in business. Linked list implementation is a tree implementation in sports. Linked list implementation is a tree implementation in everyday life. Linked list implementation is a tree implementation in every field.

### Examples of Stacks and Queues using C/C++, Java, Python, and JavaScript

#### Stack

##### C/C++

```c++
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    while (!s.empty()) {
        cout << s.top() << endl;
        s.pop();
    }
    return 0;
}
```

##### Java

```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.push(5);
        while (!s.empty()) {
            System.out.println(s.peek());
            s.pop();
        }
    }
}
```

##### Python

```python
s = []
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
while len(s) > 0:
    print(s[-1])
    s.pop()
```

##### JavaScript

```javascript
let s = [];
s.push(1);
s.push(2);
s.push(3);
s.push(4);
s.push(5);
while (s.length > 0) {
  console.log(s[s.length - 1]);
  s.pop();
}
```

#### Queue

##### C/C++

```c++
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);
    while (!q.empty()) {
        cout << q.front() << endl;
        q.pop();
    }
    return 0;
}
```

##### Java

```java
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<Integer> q = new LinkedList<>();
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);
        q.add(5);
        while (!q.isEmpty()) {
            System.out.println(q.peek());
            q.remove();
        }
    }
}
```

##### Python

```python
q = []
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
while len(q) > 0:
    print(q[0])
    q.pop(0)
```

##### JavaScript

```javascript
let q = [];
q.push(1);
q.push(2);
q.push(3);
q.push(4);
q.push(5);
while (q.length > 0) {
  console.log(q[0]);
  q.shift();
}
```

### Examples of Trees using C/C++, Java, Python, and JavaScript

#### Binary Tree

##### C/C++

```c++
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
};

Node *newNode(int data) {
    Node *node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void printInOrder(Node *node) {
    if (node == NULL) {
        return;
    }
    printInOrder(node->left);
    cout << node->data << endl;
    printInOrder(node->right);
}

int main() {
    Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    printInOrder(root);
    return 0;
}
```

##### Java

```java
public class Main {
    public static class Node {
        int data;
        Node left;
        Node right;
    }

    public static Node newNode(int data) {
        Node node = new Node();
        node.data = data;
        node.left = null;
        node.right = null;
        return node;
    }

    public static void printInOrder(Node node) {
        if (node == null) {
            return;
        }
        printInOrder(node.left);
        System.out.println(node.data);
        printInOrder(node.right);
    }

    public static void main(String[] args) {
        Node root = newNode(1);
        root.left = newNode(2);
        root.right = newNode(3);
        root.left.left = newNode(4);
        root.left.right = newNode(5);
        printInOrder(root);
    }
}
```

##### Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode(data):
    node = Node(data)
    return node

def printInOrder(node):
    if node == None:
        return
    printInOrder(node.left)
    print(node.data)
    printInOrder(node.right)

root = newNode(1)

root.left = newNode(2)
root.right = newNode(3)

root.left.left = newNode(4)
root.left.right = newNode(5)

printInOrder(root)
```

##### JavaScript

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

function newNode(data) {
  let node = new Node(data);
  return node;
}

function printInOrder(node) {
  if (node == null) {
    return;
  }
  printInOrder(node.left);
  console.log(node.data);
  printInOrder(node.right);
}

let root = newNode(1);

root.left = newNode(2);

root.right = newNode(3);

root.left.left = newNode(4);

root.left.right = newNode(5);

printInOrder(root);
```

#### Binary Search Tree

##### C/C++

```c++

#include <iostream>

using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
};

Node *newNode(int data) {
    Node *node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

Node *insert(Node *node, int data) {
    if (node == NULL) {
        return newNode(data);
    }
    if (data < node->data) {
        node->left = insert(node->left, data);
    } else if (data > node->data) {
        node->right = insert(node->right, data);
    }
    return node;
}

void printInOrder(Node *node) {
    if (node == NULL) {
        return;
    }
    printInOrder(node->left);
    cout << node->data << endl;
    printInOrder(node->right);
}

int main() {
    Node *root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    printInOrder(root);
    return 0;
}
```

##### Java

```java
public class Main {
    public static class Node {
        int data;
        Node left;
        Node right;
    }

    public static Node newNode(int data) {
        Node node = new Node();
        node.data = data;
        node.left = null;
        node.right = null;
        return node;
    }

    public static Node insert(Node node, int data) {
        if (node == null) {
            return newNode(data);
        }
        if (data < node.data) {
            node.left = insert(node.left, data);
        } else if (data > node.data) {
            node.right = insert(node.right, data);
        }
        return node;
    }

    public static void printInOrder(Node node) {
        if (node == null) {
            return;
        }
        printInOrder(node.left);
        System.out.println(node.data);
        printInOrder(node.right);
    }

    public static void main(String[] args) {
        Node root = null;
        root = insert(root, 50);
        insert(root, 30);
        insert(root, 20);
        insert(root, 40);
        insert(root, 70);
        insert(root, 60);
        insert(root, 80);
        printInOrder(root);
    }
}
```

##### Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode(data):
    node = Node(data)
    return node

def insert(node, data):
    if node == None:
        return newNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node

def printInOrder(node):
    if node == None:
        return
    printInOrder(node.left)
    print(node.data)
    printInOrder(node.right)

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)

printInOrder(root)
```

##### JavaScript

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

function newNode(data) {
  let node = new Node(data);
  return node;
}

function insert(node, data) {
  if (node == null) {
    return newNode(data);
  }
  if (data < node.data) {
    node.left = insert(node.left, data);
  } else if (data > node.data) {
    node.right = insert(node.right, data);
  }
  return node;
}

function printInOrder(node) {
  if (node == null) {
    return;
  }
  printInOrder(node.left);
  console.log(node.data);
  printInOrder(node.right);
}

let root = null;

root = insert(root, 50);

insert(root, 30);

insert(root, 20);

insert(root, 40);

insert(root, 70);

insert(root, 60);

printInOrder(root);
```

## Algorithms

Algorithms area set of instructions to solve a problem. Algorithms are used in computer science to solve problems. Algorithms are used in programming to solve problems. Algorithms are used in mathematics to solve problems. Algorithms are used in engineering to solve problems. Algorithms are used in science to solve problems. Algorithms are used in business to solve problems. Algorithms are used in sports to solve problems. Algorithms are used in everyday life to solve problems. Algorithms are used in every field to solve problems. Algorithms are used to solve problems in every field.

### Sorting

Sorting algorithms are used to sort data. Sorting algorithms are used to sort data in computer science. Sorting algorithms are used to sort data in programming. Sorting algorithms are used to sort data in mathematics. Sorting algorithms are used to sort data in engineering. Sorting algorithms are used to sort data in science. Sorting algorithms are used to sort data in business. Sorting algorithms are used to sort data in sports. Sorting algorithms are used to sort data in everyday life. Sorting algorithms are used to sort data in every field. Sorting algorithms are used to sort data in every field of science.

#### Bubble Sort

Bubble sort is a sorting algorithm. Bubble sort is a sorting algorithm in computer science. Bubble sort is a sorting algorithm in programming. Bubble sort is a sorting algorithm in mathematics. Bubble sort is a sorting algorithm in engineering. Bubble sort is a sorting algorithm in science. Bubble sort is a sorting algorithm in business. Bubble sort is a sorting algorithm in sports. Bubble sort is a sorting algorithm in everyday life. Bubble sort is a sorting algorithm in every field. Bubble sort is a sorting algorithm in every field of science.

##### C++

```cpp
// Bubble sort
#include <iostream>

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int n = sizeof(arr) / sizeof(arr[0]);
    bubbleSort(arr, n);
    std::cout << "Sorted array: ";
    printArray(arr, n);
    return 0;
}
```

##### JavaScript (ES6)

```js
// Bubble sort

function bubbleSort(arr) {
  let len = arr.length;
  for (let i = len - 1; i >= 0; i--) {
    for (let j = 1; j <= i; j++) {
      if (arr[j - 1] > arr[j]) {
        let temp = arr[j - 1];
        arr[j - 1] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}

console.log(bubbleSort([5, 3, 8, 2, 1, 4]));
```

##### Java

```java
// Bubble sort

public class BubbleSort {
  public static void main(String[] args) {
    int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
    bubbleSort(arr);
    System.out.println("Sorted array");
    printArray(arr);
  }

  static void bubbleSort(int[] arr) {
    int n = arr.length;
    int temp = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 1; j < (n - i); j++) {
        if (arr[j - 1] > arr[j]) {
          temp = arr[j - 1];
          arr[j - 1] = arr[j];
          arr[j] = temp;
        }
      }
    }
  }

  static void printArray(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }
}
```

##### Python

```python
# Bubble sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")

for i in range(len(arr)):
    print ("%d" %arr[i]),
```

#### Selection Sort

Selection sort is a sorting algorithm. Selection sort is a sorting algorithm in computer science. Selection sort is a sorting algorithm in programming. Selection sort is a sorting algorithm in mathematics. Selection sort is a sorting algorithm in engineering. Selection sort is a sorting algorithm in science. Selection sort is a sorting algorithm in business. Selection sort is a sorting algorithm in sports. Selection sort is a sorting algorithm in everyday life. Selection sort is a sorting algorithm in every field. Selection sort is a sorting algorithm in every field of science.

##### C++

```cpp
// Selection sort
#include <iostream>

void selectionSort(int arr[], int n) {
    int i, j, min_idx;

    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = { 64, 25, 12, 22, 11 };
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    std::cout << "Sorted array: ";
    printArray(arr, n);
    return 0;
}
```

##### JavaScript (ES6)

```js
// Selection sort

function selectionSort(arr) {
  let len = arr.length;
  for (let i = 0; i < len; i++) {
    let min = i;
    for (let j = i + 1; j < len; j++) {
      if (arr[min] > arr[j]) {
        min = j;
      }
    }
    if (min !== i) {
      let tmp = arr[i];
      arr[i] = arr[min];
      arr[min] = tmp;
    }
  }
  return arr;
}

console.log(selectionSort([5, 3, 8, 2, 1, 4]));
```

##### Java

```java
// Selection sort

public class SelectionSort {
  public static void main(String[] args) {
    int[] arr = { 64, 25, 12, 22, 11 };
    selectionSort(arr);
    System.out.println("Sorted array");
    printArray(arr);
  }

  static void selectionSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
      int min_idx = i;
      for (int j = i + 1; j < n; j++) {
        if (arr[j] < arr[min_idx]) {
          min_idx = j;
        }
      }
      int temp = arr[min_idx];
      arr[min_idx] = arr[i];
      arr[i] = temp;
    }
  }

  static void printArray(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }
}
```

##### Python

```python
# Selection sort

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i]),
```

#### Insertion Sort

Insertion sort is a sorting algorithm. Insertion sort is a sorting algorithm in computer science. Insertion sort is a sorting algorithm in programming. Insertion sort is a sorting algorithm in mathematics. Insertion sort is a sorting algorithm in engineering. Insertion sort is a sorting algorithm in science. Insertion sort is a sorting algorithm in business. Insertion sort is a sorting algorithm in sports. Insertion sort is a sorting algorithm in everyday life. Insertion sort is a sorting algorithm in every field. Insertion sort is a sorting algorithm in every field of science.

##### C++

```cpp
// Insertion sort

#include <iostream>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = { 12, 11, 13, 5, 6 };
    int n = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, n);
    printArray(arr, n);
    return 0;
}
```

##### JavaScript (ES6)

```js
// Insertion sort

function insertionSort(arr) {
  let len = arr.length;
  for (let i = 0; i < len; i++) {
    let el = arr[i];
    let j;
    for (j = i - 1; j >= 0 && arr[j] > el; j--) {
      arr[j + 1] = arr[j];
    }
    arr[j + 1] = el;
  }
  return arr;
}

console.log(insertionSort([5, 3, 8, 2, 1, 4]));
```

##### Java

```java
// Insertion sort

public class InsertionSort {
  public static void main(String[] args) {
    int[] arr = { 12, 11, 13, 5, 6 };
    insertionSort(arr);
    printArray(arr);
  }

  static void insertionSort(int[] arr) {
    int n = arr.length;
    for (int i = 1; i < n; ++i) {
      int key = arr[i];
      int j = i - 1;
      while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j = j - 1;
      }
      arr[j + 1] = key;
    }
  }

  static void printArray(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }
}
```

##### Python

```python
# Insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]

insertionSort(arr)

for i in range(len(arr)):
    print ("% d" % arr[i])
```

#### Merge Sort

Merge sort is a sorting algorithm. Merge sort is a sorting algorithm in computer science. Merge sort is a sorting algorithm in programming. Merge sort is a sorting algorithm in mathematics. Merge sort is a sorting algorithm in engineering. Merge sort is a sorting algorithm in science. Merge sort is a sorting algorithm in business. Merge sort is a sorting algorithm in sports. Merge sort is a sorting algorithm in everyday life. Merge sort is a sorting algorithm in every field. Merge sort is a sorting algorithm in every field of science.

##### C++

```cpp
// Merge sort

#include <iostream>

void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++) {
        L[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++) {
        R[j] = arr[m + 1 + j];
    }

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

void printArray(int A[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Given array is " << std::endl;
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    std::cout << "Sorted array is " << std::endl;
    printArray(arr, arr_size);
    return 0;
}
```

##### JavaScript (ES6)

```js
// Merge sort

function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }
  let middle = parseInt(arr.length / 2);
  let left = arr.slice(0, middle);
  let right = arr.slice(middle, arr.length);
  return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
  let result = [];
  while (left.length && right.length) {
    if (left[0] <= right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  while (left.length) {
    result.push(left.shift());
  }
  while (right.length) {
    result.push(right.shift());
  }
  return result;
}

console.log(mergeSort([5, 3, 8, 2, 1, 4]));
```

##### Java

```java
// Merge sort

public class MergeSort {
  public static void main(String[] args) {
    int[] arr = { 12, 11, 13, 5, 6, 7 };
    mergeSort(arr, 0, arr.length - 1);
    printArray(arr);
  }

  static void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[] = new int[n1];
    int R[] = new int[n2];

    for (int i = 0; i < n1; ++i) {
      L[i] = arr[l + i];
    }
    for (int j = 0; j < n2; ++j) {
      R[j] = arr[m + 1 + j];
    }

    int i = 0, j = 0;

    int k = l;
    while (i < n1 && j < n2) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i++;
      } else {
        arr[k] = R[j];
        j++;
      }
      k++;
    }

    while (i < n1) {
      arr[k] = L[i];
      i++;
      k++;
    }

    while (j < n2) {
      arr[k] = R[j];
      j++;
      k++;
    }
  }

  static void mergeSort(int arr[], int l, int r) {
    if (l < r) {
      int m = (l + r) / 2;

      mergeSort(arr, l, m);
      mergeSort(arr, m + 1, r);

      merge(arr, l, m, r);
    }
  }

  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }
}
```

##### Python

```python
# Merge sort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
```

##### C++

```cpp
// Merge sort

#include <iostream>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++) {
        L[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++) {
        R[j] = arr[m + 1 + j];
    }

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

void printArray(int A[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        cout << A[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    cout << "Given array is " << endl;
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    cout << "Sorted array is " << endl;
    printArray(arr, arr_size);
    return 0;
}
```

#### Quick Sort

Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

- Always pick first element as pivot.
- Always pick last element as pivot (implemented below)
- Pick a random element as pivot.
- Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

##### Java

```java
// Quick sort

class QuickSort {
  int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j < high; j++) {
      if (arr[j] <= pivot) {
        i++;

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
  }

  void sort(int arr[], int low, int high) {
    if (low < high) {
      int pi = partition(arr, low, high);

      sort(arr, low, pi - 1);
      sort(arr, pi + 1, high);
    }
  }

  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

  public static void main(String args[]) {
    int arr[] = { 10, 7, 8, 9, 1, 5 };
    int n = arr.length;

    QuickSort ob = new QuickSort();
    ob.sort(arr, 0, n - 1);

    System.out.println("sorted array");
    printArray(arr);
  }
}
```

##### Python

```python
# Quick sort

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]

quickSort(arr, 0, len(arr) - 1)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
```

##### C++

```cpp
// Quick sort

#include <iostream>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    printArray(arr, n);
    return 0;
}
```

##### JavaScript

```js
// Quick sort

function partition(arr, low, high) {
  let pivot = arr[high];
  let i = low - 1;

  for (let j = low; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      let temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }

  let temp = arr[i + 1];
  arr[i + 1] = arr[high];
  arr[high] = temp;

  return i + 1;
}

function quickSort(arr, low, high) {
  if (low < high) {
    let pi = partition(arr, low, high);

    quickSort(arr, low, pi - 1);
    quickSort(arr, pi + 1, high);
  }
}

let arr = [10, 7, 8, 9, 1, 5];

quickSort(arr, 0, arr.length - 1);

console.log("Sorted array is:");
console.log(arr);
```

#### Heap Sort

Heap Sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

##### Java

```java
// Heap sort

class HeapSort {
  public void sort(int arr[]) {
    int n = arr.length;

    for (int i = n / 2 - 1; i >= 0; i--) {
      heapify(arr, n, i);
    }

    for (int i = n - 1; i >= 0; i--) {
      int temp = arr[0];
      arr[0] = arr[i];
      arr[i] = temp;

      heapify(arr, i, 0);
    }
  }

  void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest]) {
      largest = l;
    }

    if (r < n && arr[r] > arr[largest]) {
      largest = r;
    }

    if (largest != i) {
      int swap = arr[i];
      arr[i] = arr[largest];
      arr[largest] = swap;

      heapify(arr, n, largest);
    }
  }

  static void printArray(int arr[]) {
    int n = arr.length;
    for (int i = 0; i < n; ++i) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

  public static void main(String args[]) {
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int n = arr.length;

    HeapSort ob = new HeapSort();
    ob.sort(arr);

    System.out.println("Sorted array is");
    printArray(arr);
  }
}
```

##### Python

```python
# Heap sort

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),
```

##### C++

```cpp
// Heap sort

#include <iostream>
using namespace std;

void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest]) {
        largest = l;
    }

    if (r < n && arr[r] > arr[largest]) {
        largest = r;
    }

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);

    cout << "Sorted array is \n";
    printArray(arr, n);
}
```

##### JavaScript

```js
// Heap sort

function heapify(arr, n, i) {
  let largest = i;
  let l = 2 * i + 1;
  let r = 2 * i + 2;

  if (l < n && arr[l] > arr[largest]) {
    largest = l;
  }

  if (r < n && arr[r] > arr[largest]) {
    largest = r;
  }

  if (largest != i) {
    let temp = arr[i];
    arr[i] = arr[largest];
    arr[largest] = temp;

    heapify(arr, n, largest);
  }
}

function heapSort(arr) {
  let n = arr.length;

  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }

  for (let i = n - 1; i >= 0; i--) {
    let temp = arr[0];
    arr[0] = arr[i];
    arr[i] = temp;

    heapify(arr, i, 0);
  }
}

let arr = [12, 11, 13, 5, 6, 7];
heapSort(arr);
let n = arr.length;
console.log("Sorted array is");
for (let i = 0; i < n; ++i) {
  console.log(arr[i] + " ");
}
```

### Searching

Searching refers to the process of finding a specific value or a set of values in a collection of data. There are various search algorithms that can be used depending on the data structure and the requirements of the search operation.

#### Linear Search

Linear search is a simple search algorithm that searches for a target value within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched.

##### Pseudocode

```text

function linear_search(list, value)

   for each item in the list
      if match item == value
         return the item's location
      end if
   end for

end function
```

##### C

```c
// Linear search

#include <stdio.h>

int search(int arr[], int n, int x) {
  int i;
  for (i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

int main(void) {
  int arr[] = {2, 3, 4, 10, 40};
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = search(arr, n, x);
  (result == -1) ? printf("Element is not present in array") : printf("Element is present at index %d", result);
  return 0;
}
```

##### Python

```python
# Linear search

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1;

arr = [2, 3, 4, 10, 40]

x = 10

n = len(arr)

result = search(arr, n, x)

if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
```

##### C++

```cpp
// Linear search

#include <iostream>
using namespace std;

int search(int arr[], int n, int x) {
  int i;
  for (i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

int main(void) {
  int arr[] = {2, 3, 4, 10, 40};
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = search(arr, n, x);
  (result == -1) ? cout << "Element is not present in array" : cout << "Element is present at index " << result;
  return 0;
}
```

##### JavaScript

```js
// Linear search

function search(arr, n, x) {
  let i;
  for (i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

let arr = [2, 3, 4, 10, 40];
let x = 10;
let n = arr.length;
let result = search(arr, n, x);

if (result == -1) {
  console.log("Element is not present in array");
} else {
  console.log("Element is present at index " + result);
}
```

##### Java

```java
// Linear search

class LinearSearch {
  public static int search(int arr[], int n, int x) {
    int i;
    for (i = 0; i < n; i++) {
      if (arr[i] == x) {
        return i;
      }
    }
    return -1;
  }

  public static void main(String args[]) {
    int arr[] = { 2, 3, 4, 10, 40 };
    int x = 10;
    int n = arr.length;
    int result = search(arr, n, x);
    if (result == -1) {
      System.out.print("Element is not present in array");
    } else {
      System.out.print("Element is present at index " + result);
    }
  }
}
```

#### Binary Search

Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

##### Pseudocode

```text

function binary_search(list, value)

   low = 0
   high = length of list - 1

   while low <= high
      mid = (low + high) / 2
      if list[mid] > value
         high = mid - 1
      else if list[mid] < value
         low = mid + 1
      else:
         return mid
   end while

end function
```

##### C

```c
// Binary search

#include <stdio.h>

int binarySearch(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l) / 2;

    if (arr[mid] == x) {
      return mid;
    }

    if (arr[mid] > x) {
      return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

int main(void) {
  int arr[] = {2, 3, 4, 10, 40};
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = binarySearch(arr, 0, n - 1, x);
  (result == -1) ? printf("Element is not present in array") : printf("Element is present at index %d", result);
  return 0;
}
```

##### Python

```python
# Binary search

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) / 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        return binarySearch(arr, mid + 1, r, x)

    return -1

arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = binarySearch(arr, 0, n - 1, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
```

##### C++

```cpp
// Binary search

#include <iostream>
using namespace std;

int binarySearch(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l) / 2;

    if (arr[mid] == x) {
      return mid;
    }

    if (arr[mid] > x) {
      return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

int main(void) {
  int arr[] = {2, 3, 4, 10, 40};
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = binarySearch(arr, 0, n - 1, x);
  (result == -1) ? cout << "Element is not present in array" : cout << "Element is present at index " << result;
  return 0;
}
```

##### JavaScript

```js
// Binary search

function binarySearch(arr, l, r, x) {
  if (r >= l) {
    let mid = l + (r - l) / 2;

    if (arr[mid] == x) {
      return mid;
    }

    if (arr[mid] > x) {
      return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

let arr = [2, 3, 4, 10, 40];
let x = 10;
let n = arr.length;
let result = binarySearch(arr, 0, n - 1, x);

if (result == -1) {
  console.log("Element is not present in array");
} else {
  console.log("Element is present at index " + result);
}
```

##### Java

```java
// Binary search

class BinarySearch {
  int binarySearch(int arr[], int l, int r, int x) {
    if (r >= l) {
      int mid = l + (r - l) / 2;

      if (arr[mid] == x) {
        return mid;
      }

      if (arr[mid] > x) {
        return binarySearch(arr, l, mid - 1, x);
      }

      return binarySearch(arr, mid + 1, r, x);
    }

    return -1;
  }

  public static void main(String args[]) {
    BinarySearch ob = new BinarySearch();
    int arr[] = { 2, 3, 4, 10, 40 };
    int x = 10;
    int n = arr.length;
    int result = ob.binarySearch(arr, 0, n - 1, x);
    if (result == -1) {
      System.out.print("Element is not present in array");
    } else {
      System.out.print("Element is present at index " + result);
    }
  }
}
```

#### Jump Search

Jump search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements \(than linear search\) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

##### Pseudocode

```text

function jump_search(list, value)

   n = length of list
   step = sqrt(n)
   prev = 0
   while list[min(step, n)-1] < value
      prev = step
      step += sqrt(n)
      if prev >= n
         return -1
   end while

   while list[prev] < value
      prev = prev + 1
      if prev = min(step, n)
         return -1
   end while

   if list[prev] = value
      return prev
   end if

   return -1

end function
```

##### C

```c
// Jump search

#include <stdio.h>
#include <math.h>

int jumpSearch(int arr[], int x, int n) {
  int step = sqrt(n);

  int prev = 0;
  while (arr[min(step, n) - 1] < x) {
    prev = step;
    step += sqrt(n);
    if (prev >= n) {
      return -1;
    }
  }

  while (arr[prev] < x) {
    prev++;

    if (prev == min(step, n)) {
      return -1;
    }
  }

  if (arr[prev] == x) {
    return prev;
  }

  return -1;
}

int main() {
  int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
  int x = 55;
  int n = sizeof(arr) / sizeof(arr[0]);

  int index = jumpSearch(arr, x, n);

  printf("\nNumber %d is at index %d", x, index);
  return 0;
}
```

##### Python

```python
# Jump search

import math

def jumpSearch(arr, x, n):
    step = math.sqrt(n)

    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]

x = 55

n = len(arr)

index = jumpSearch(arr, x, n)

print("Number", x, "is at index", index)
```

##### C++

```cpp
// Jump search

#include <iostream>
#include <cmath>
using namespace std;

int jumpSearch(int arr[], int x, int n) {
  int step = sqrt(n);

  int prev = 0;
  while (arr[min(step, n) - 1] < x) {
    prev = step;
    step += sqrt(n);
    if (prev >= n) {
      return -1;
    }
  }

  while (arr[prev] < x) {
    prev++;

    if (prev == min(step, n)) {
      return -1;
    }
  }

  if (arr[prev] == x) {
    return prev;
  }

  return -1;
}

int main() {
  int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
  int x = 55;
  int n = sizeof(arr) / sizeof(arr[0]);

  int index = jumpSearch(arr, x, n);

  cout << "\nNumber " << x << " is at index " << index;
  return 0;
}
```

##### JavaScript

```js
// Jump search

function jumpSearch(arr, x, n) {
  let step = Math.sqrt(n);

  let prev = 0;
  while (arr[Math.min(step, n) - 1] < x) {
    prev = step;
    step += Math.sqrt(n);
    if (prev >= n) {
      return -1;
    }
  }

  while (arr[prev] < x) {
    prev++;

    if (prev == Math.min(step, n)) {
      return -1;
    }
  }

  if (arr[prev] == x) {
    return prev;
  }

  return -1;
}

let arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

let x = 55;

let n = arr.length;

let index = jumpSearch(arr, x, n);

console.log("Number", x, "is at index", index);
```

##### Java

```java
// Jump search

import java.lang.Math;

class JumpSearch {
  public static int jumpSearch(int arr[], int x, int n) {
    int step = (int) Math.floor(Math.sqrt(n));

    int prev = 0;
    while (arr[Math.min(step, n) - 1] < x) {
      prev = step;
      step += (int) Math.floor(Math.sqrt(n));
      if (prev >= n) {
        return -1;
      }
    }

    while (arr[prev] < x) {
      prev++;

      if (prev == Math.min(step, n)) {
        return -1;
      }
    }

    if (arr[prev] == x) {
      return prev;
    }

    return -1;
  }

  public static void main(String args[]) {
    int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
    int x = 55;
    int n = arr.length;

    int index = jumpSearch(arr, x, n);

    System.out.println("\nNumber " + x + " is at index " + index);
  }
}
```

#### Interpolation search

Interpolation search is an algorithm for searching for a given key in an array that has been ordered by numerical values assigned to the keys (key values). It is an improvement over binary search where the values in a sorted array are uniformly distributed. Binary search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

To find the position to be searched, it uses following formula.

```text
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
```

##### C

```c
// Interpolation search

#include <stdio.h>

int interpolationSearch(int arr[], int n, int x) {
  int lo = 0, hi = (n - 1);

  while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
    if (lo == hi) {
      if (arr[lo] == x) {
        return lo;
      }
      return -1;
    }

    int pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));

    if (arr[pos] == x) {
      return pos;
    }

    if (arr[pos] < x) {
      lo = pos + 1;
    } else {
      hi = pos - 1;
    }
  }
  return -1;
}

int main() {
  int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 };
  int n = sizeof(arr) / sizeof(arr[0]);

  int x = 18;
  int index = interpolationSearch(arr, n, x);

  if (index != -1) {
    printf("\nElement found at index %d", index);
  } else {
    printf("\nElement not found.");
  }
  return 0;
}
```

##### C++

```cpp
// Interpolation search

#include <iostream>
using namespace std;

int interpolationSearch(int arr[], int n, int x) {
  int lo = 0, hi = (n - 1);

  while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
    if (lo == hi) {
      if (arr[lo] == x) {
        return lo;
      }
      return -1;
    }

    int pos = lo + (((double)(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));

    if (arr[pos] == x) {
      return pos;
    }

    if (arr[pos] < x) {
      lo = pos + 1;
    } else {
      hi = pos - 1;
    }
  }
  return -1;
}

int main() {
  int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 };
  int n = sizeof(arr) / sizeof(arr[0]);

  int x = 18;
  int index = interpolationSearch(arr, n, x);

  if (index != -1) {
    cout << "\nElement found at index " << index;
  } else {
    cout << "\nElement not found.";
  }
  return 0;
}
```

##### JavaScript

```js
// Interpolation search

function interpolationSearch(arr, n, x) {
  let lo = 0,
    hi = n - 1;

  while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
    if (lo == hi) {
      if (arr[lo] == x) {
        return lo;
      }
      return -1;
    }

    let pos =
      lo + Math.floor(((hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));

    if (arr[pos] == x) {
      return pos;
    }

    if (arr[pos] < x) {
      lo = pos + 1;
    } else {
      hi = pos - 1;
    }
  }
  return -1;
}

let arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47];

let n = arr.length;

let x = 18;

let index = interpolationSearch(arr, n, x);

console.log("Element found at index", index);
```

##### Java

```java
// Interpolation search

class InterpolationSearch {
  public static int interpolationSearch(int arr[], int n, int x) {
    int lo = 0, hi = (n - 1);

    while (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
      if (lo == hi) {
        if (arr[lo] == x) {
          return lo;
        }
        return -1;
      }

      int pos = lo + (((hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]));

      if (arr[pos] == x) {
        return pos;
      }

      if (arr[pos] < x) {
        lo = pos + 1;
      } else {
        hi = pos - 1;
      }
    }
    return -1;
  }

  public static void main(String args[]) {
    int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 };
    int n = arr.length;

    int x = 18;
    int index = interpolationSearch(arr, n, x);

    System.out.println("\nElement found at index " + index);
  }
}
```

#### Jump search

Jump search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements \(than linear search\) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0], arr[m], arr[2m]…..arr[km] and so on. Once we find the interval \(arr[km] < x < arr[(k+1)m]\) we perform a linear search operation from the index km to find the element x.

Let’s consider the following array: \(arr[] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610}\). Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4.

1. STEP 1: Jump from index 0 to index 4;
2. STEP 2: Jump from index 4 to index 8;
3. STEP 3: Jump from index 8 to index 12;
4. STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.
5. STEP 5: Perform linear search from index 8 to get the element 55.

##### Pseudocode

```text

function jumpSearch(arr, x)
    n = length(arr)
    step = sqrt(n)
    prev = 0
    while arr[min(step, n)-1] < x
        prev = step
        step += sqrt(n)
        if prev >= n
            return -1
    while arr[prev] < x
        prev++
        if prev == min(step, n)
            return -1
    if arr[prev] == x
        return prev
    return -1
```

##### C

```c
// Jump search

#include <math.h>

int jumpSearch(int arr[], int x, int n) {
  int step = sqrt(n);

  int prev = 0;
  while (arr[min(step, n) - 1] < x) {
    prev = step;
    step += sqrt(n);
    if (prev >= n) {
      return -1;
    }
  }

  while (arr[prev] < x) {
    prev++;

    if (prev == min(step, n)) {
      return -1;
    }
  }

  if (arr[prev] == x) {
    return prev;
  }
  return -1;
}

int main() {
  int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
  int x = 55;
  int n = sizeof(arr) / sizeof(arr[0]);

  int index = jumpSearch(arr, x, n);

  cout << "\nNumber " << x << " is at index " << index;
  return 0;
}
```

##### C++

```cpp
// Jump search

#include <bits/stdc++.h>
using namespace std;

int jumpSearch(int arr[], int x, int n) {
  int step = sqrt(n);

  int prev = 0;
  while (arr[min(step, n) - 1] < x) {
    prev = step;
    step += sqrt(n);
    if (prev >= n) {
      return -1;
    }
  }

  while (arr[prev] < x) {
    prev++;

    if (prev == min(step, n)) {
      return -1;
    }
  }

  if (arr[prev] == x) {
    return prev;
  }
  return -1;
}

int main() {
  int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
  int x = 55;
  int n = sizeof(arr) / sizeof(arr[0]);

  int index = jumpSearch(arr, x, n);

  cout << "\nNumber " << x << " is at index " << index;
  return 0;
}
```

##### Java

```java
// Jump search

class JumpSearch {
  public static int jumpSearch(int arr[], int x, int n) {
    int step = (int) Math.floor(Math.sqrt(n));

    int prev = 0;
    while (arr[Math.min(step, n) - 1] < x) {
      prev = step;
      step += (int) Math.floor(Math.sqrt(n));
      if (prev >= n) {
        return -1;
      }
    }

    while (arr[prev] < x) {
      prev++;

      if (prev == Math.min(step, n)) {
        return -1;
      }
    }

    if (arr[prev] == x) {
      return prev;
    }
    return -1;
  }

  public static void main(String args[]) {
    int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 };
    int x = 55;
    int n = arr.length;

    int index = jumpSearch(arr, x, n);

    System.out.println("\nNumber " + x + " is at index " + index);
  }
}
```

##### Python

```python
# Jump search

import math

def jumpSearch(arr, x, n):
    step = math.floor(math.sqrt(n))

    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += math.floor(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

x = 55
n = len(arr)

index = jumpSearch(arr, x, n)

print("\nNumber", x, "is at index", index)
```

#### Exponential Search

In binary search, we divide the array into two parts and check whether the key element lies in the first half or the second half. We can similarly divide the array into two parts in exponential search. The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater. Once we find an index i \(after repeated doubling of i\), we know that the element must be present between i/2 and i \(Why i/2? because we could not find a greater value in previous iteration\).

##### Algorithm

1. Find range for binary search by repeated doubling
2. Do Binary Search in above found range.

##### Pseudocode

```text

function exponentialSearch(arr, n, x)
    if arr[0] == x
        return 0
    i = 1
    while i < n and arr[i] <= x
        i = i*2
    return binarySearch(arr, i/2, min(i, n), x)
```

##### C

```c

// Exponential search

#include <math.h>

int binarySearch(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l) / 2;

    if (arr[mid] == x) {
      return mid;
    }

    if (arr[mid] > x) {
      return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

int exponentialSearch(int arr[], int n, int x) {
  if (arr[0] == x) {
    return 0;
  }

  int i = 1;
  while (i < n && arr[i] <= x) {
    i = i * 2;
  }

  return binarySearch(arr, i / 2, min(i, n), x);
}

int main() {
  int arr[] = { 2, 3, 4, 10, 40 };
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);

  int result = exponentialSearch(arr, n, x);
  (result == -1) ? printf("Element is not present in array") : printf("Element is present at index %d", result);
  return 0;
}
```

##### C++

```cpp
// Exponential search

#include <bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l) / 2;

    if (arr[mid] == x) {
      return mid;
    }

    if (arr[mid] > x) {
      return binarySearch(arr, l, mid - 1, x);
    }

    return binarySearch(arr, mid + 1, r, x);
  }

  return -1;
}

int exponentialSearch(int arr[], int n, int x) {
  if (arr[0] == x) {
    return 0;
  }

  int i = 1;
  while (i < n && arr[i] <= x) {
    i = i * 2;
  }

  return binarySearch(arr, i / 2, min(i, n), x);
}

int main() {
  int arr[] = { 2, 3, 4, 10, 40 };
  int x = 10;
  int n = sizeof(arr) / sizeof(arr[0]);

  int result = exponentialSearch(arr, n, x);
  (result == -1) ? cout << "Element is not present in array" : cout << "Element is present at index " << result;
  return 0;
}
```

##### Java

```java
// Exponential search

class ExponentialSearch {
    static int binarySearch(int arr[], int l, int r, int x) {
        if (r >= l) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == x) {
            return mid;
        }

        if (arr[mid] > x) {
            return binarySearch(arr, l, mid - 1, x);
        }

        return binarySearch(arr, mid + 1, r, x);
        }

        return -1;
    }

    static int exponentialSearch(int arr[], int n, int x) {
        if (arr[0] == x) {
        return 0;
        }

        int i = 1;
        while (i < n && arr[i] <= x) {
        i = i * 2;
        }

        return binarySearch(arr, i / 2, Math.min(i, n), x);
    }

    public static void main(String args[]) {
        int arr[] = { 2, 3, 4, 10, 40 };
        int x = 10;
        int n = arr.length;

        int result = exponentialSearch(arr, n, x);
        System.out.println((result < 0) ? "Element is not present in array" : "Element is present at index " + result);
    }
}
```

##### Python

```python
# Exponential search

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        return binarySearch(arr, mid + 1, r, x)

    return -1

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    return binarySearch(arr, i / 2, min(i, n), x)

arr = [2, 3, 4, 10, 40]

x = 10
n = len(arr)

result = exponentialSearch(arr, n, x)
print("Element is present at index", result)
```

#### Fibonacci Search

Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.

##### Algorithm

1. Let 'fib2' be the smallest Fibonacci Number greater than or equal to the length of the array.
2. Initialize 'fib1' and 'fib2' to the two previous Fibonacci Numbers.
3. Initialize 'offset' to 0.
4. While 'fib2' is greater than 0:
   a. Calculate the midpoint of the current subarray using 'offset' and 'fib1'.
   b. If the element at the midpoint is the target element, return its index.
   c. If the target element is less than the element at the midpoint, set 'fib2' to 'fib1', 'fib1' to 'fib2' - 'fib1', and 'offset' to 'offset'.
   d. If the target element is greater than the element at the midpoint, set 'fib2' to 'fib2' - 'fib1', 'fib1' to 'fib1', and 'offset' to 'offset' + 'fib1'.
5. Return -1 if the element was not found.

##### Complexity

| Time Complexity | Space Complexity |
| :-------------- | :--------------- |
| O\(log n\)      | O\(1\)           |

##### C

```c
// Fibonacci search

#include <stdio.h>

int min(int x, int y) {
  return (x <= y) ? x : y;
}

int fibonacciSearch(int arr[], int x, int n) {
  int fib2 = 0;
  int fib1 = 1;
  int fibM = fib2 + fib1;

  while (fibM < n) {
    fib2 = fib1;
    fib1 = fibM;
    fibM = fib2 + fib1;
  }

  int offset = -1;

  while (fibM > 1) {
    int i = min(offset + fib2, n - 1);

    if (arr[i] < x) {
      fibM = fib1;
      fib1 = fib2;
      fib2 = fibM - fib1;
      offset = i;
    } else if (arr[i] > x) {
      fibM = fib2;
      fib1 = fib1 - fib2;
      fib2 = fibM - fib1;
    } else {
      return i;
    }
  }

  if (fib1 && arr[offset + 1] == x) {
    return offset + 1;
  }

  return -1;
}

int main() {
  int arr[] = { 10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100 };
  int n = sizeof(arr) / sizeof(arr[0]);
  int x = 85;
  printf("Found at index: %d", fibonacciSearch(arr, x, n));
  return 0;
}
```

##### Java

```java
// Fibonacci search

class FibonacciSearch {
    static int min(int x, int y) {
        return (x <= y) ? x : y;
    }

    static int fibonacciSearch(int arr[], int x, int n) {
        int fib2 = 0;
        int fib1 = 1;
        int fibM = fib2 + fib1;

        while (fibM < n) {
            fib2 = fib1;
            fib1 = fibM;
            fibM = fib2 + fib1;
        }

        int offset = -1;

        while (fibM > 1) {
            int i = min(offset + fib2, n - 1);

            if (arr[i] < x) {
                fibM = fib1;
                fib1 = fib2;
                fib2 = fibM - fib1;
                offset = i;
            } else if (arr[i] > x) {
                fibM = fib2;
                fib1 = fib1 - fib2;
                fib2 = fibM - fib1;
            } else {
                return i;
            }
        }

        if (fib1 && arr[offset + 1] == x) {
            return offset + 1;
        }

        return -1;
    }

    public static void main(String args[]) {
        int arr[] = { 10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100 };
        int n = arr.length;
        int x = 85;
        System.out.println("Found at index: " + fibonacciSearch(arr, x, n));
    }
}
```

##### Python

```python
# Fibonacci search

def fibonacciSearch(arr, x, n):
    fib2 = 0
    fib1 = 1
    fibM = fib2 + fib1

    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib2 + fib1

    offset = -1

    while fibM > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < x:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i] > x:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i

    if fib1 and arr[offset + 1] == x:
        return offset + 1

    return -1

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

x = 85
n = len(arr)

print("Found at index:", fibonacciSearch(arr, x, n))
```

## Graphs

A graph is a non-linear data structure that consists of nodes (also called vertices) and edges. The edges are lines or arcs that connect any two nodes in the graph. More formally, a graph consists of a finite set of vertices and a set of edges that connect pairs of nodes.

Graphs are used to solve many real-life problems, such as representing networks (e.g. paths in a city or telephone network, circuit network). They are also used in social networks (e.g. LinkedIn, Facebook) where each person is represented by a vertex and the edges represent relationships between people (e.g. friendships, family relationships).

There are several ways to represent a graph in computer memory, including:

- Adjacency list: stores a list of all the neighbors for each node
- Adjacency matrix: stores a matrix of 0s and 1s indicating the presence or absence of an edge between two nodes

There are also several algorithms for traversing and searching graphs, such as:

- Depth-first search
- Breadth-first search

These algorithms are used to find paths between nodes, compute the shortest path between two nodes, or search for specific nodes or edges in the graph.

### Breadth-first search

Breadth-first search \(BFS\) is an algorithm for traversing or searching a graph. It starts at the root node and explores all the neighboring nodes. Then, for each of those nodes, it explores their unexplored neighbors, and so on, until it finds the goal.

##### Algorithm

1. Dequeue a node from the queue and examine it.
2. If the node contains the goal, return the node.
3. Otherwise, enqueue all of the node's unexplored neighbors and mark the node as explored.
4. If the queue is empty and the goal has not been found, return null to indicate failure.
5. Repeat from step 2 until the goal is found or the queue is empty.

##### C

```c
// Breadth-first search

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct node {
  int vertex;
  struct node* next;
} node;

typedef struct queue {
  int items[MAX];
  int front;
  int rear;
} queue;

node* createNode(int);
queue* createQueue();
void enqueue(queue*, int);
int dequeue(queue*);
void printQueue(queue*);
int isEmpty(queue*);
void bfs(int, int);
void addEdge(int, int);
void display(int);

int visited[MAX];
int adjMatrix[MAX][MAX];
int vertexCount;

int main() {
  int i, j;
  vertexCount = 4;

  for (i = 0; i < vertexCount; i++) {
    for (j = 0; j < vertexCount; j++) {
      adjMatrix[i][j] = 0;
    }
  }

  addEdge(0, 1);
  addEdge(0, 2);
  addEdge(0, 3);
  addEdge(1, 2);
  addEdge(2, 0);
  addEdge(2, 3);
  addEdge(3, 3);

  display(vertexCount);

  bfs(2, 3);

  return 0;
}

node* createNode(int v) {
  node* newNode = malloc(sizeof(node));
  newNode->vertex = v;
  newNode->next = NULL;
  return newNode;
}

queue* createQueue() {
  queue* q = malloc(sizeof(queue));
  q->front = -1;
  q->rear = -1;
  return q;
}

int isEmpty(queue* q) {
  if (q->rear == -1) {
    return 1;
  } else {
    return 0;
  }
}

void enqueue(queue* q, int value) {
  if (q->rear == MAX - 1) {
    printf("Queue is Full");
  } else {
    if (q->front == -1) {
      q->front = 0;
    }
    q->rear++;
    q->items[q->rear] = value;
  }
}

int dequeue(queue* q) {
  int item;
  if (isEmpty(q)) {
    printf("Queue is empty");
    item = -1;
  } else {
    item = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
      printf("Resetting queue ");
      q->front = q->rear = -1;
    }
  }
  return item;
}

void printQueue(queue* q) {
  int i = q->front;

  if (isEmpty(q)) {
    printf("Queue is empty");
  } else {
    printf("Queue contains \n");
    for (i = q->front; i < q->rear + 1; i++) {
      printf("%d ", q->items[i]);
    }
  }
}

void bfs(int startVertex, int target) {
  queue* q = createQueue();

  visited[startVertex] = 1;
  enqueue(q, startVertex);

  while (!isEmpty(q)) {
    printQueue(q);
    int currentVertex = dequeue(q);
    printf("Visited %d \n", currentVertex);

    node* temp = adjLists[currentVertex];

    while (temp) {
      int adjVertex = temp->vertex;

      if (adjVertex == target) {
        printf("Found %d", target);
        return;
      }

      if (!visited[adjVertex]) {
        visited[adjVertex] = 1;
        enqueue(q, adjVertex);
      }
      temp = temp->next;
    }
  }
}

void addEdge(int src, int dest) {
  node* newNode = createNode(dest);
  newNode->next = adjLists[src];
  adjLists[src] = newNode;

  newNode = createNode(src);
  newNode->next = adjLists[dest];
  adjLists[dest] = newNode;
}

void display(int vertexCount) {
  int i;
  for (i = 0; i < vertexCount; i++) {
    node* temp = adjLists[i];
    printf("\n Vertex %d\n: ", i);
    while (temp) {
      printf("%d -> ", temp->vertex);
      temp = temp->next;
    }
    printf("NULL\n");
  }
}
```

##### Output

```text
Vertex 0
: 3 -> 2 -> 1 -> NULL

Vertex 1
: 2 -> 0 -> NULL

Vertex 2
: 3 -> 1 -> 0 -> NULL

Vertex 3
: 3 -> 2 -> 0 -> NULL

Queue contains
2
Visited 2
Queue contains
0
Visited 0
Queue contains
3
Visited 3
Found 3
```

##### Python

```python
# Breadth-first search

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
```

##### Output

```text

Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1
```

##### C++

```cpp
// Breadth-first search

#include <iostream>
#include <list>

using namespace std;

class Graph {
  int V;
  list<int> *adj;

public:
    Graph(int V);
    void addEdge(int v, int w);
    void BFS(int s);
    };

Graph::Graph(int V) {
    this->V = V;
    adj = new list<int>[V];
    }

void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
    }

void Graph::BFS(int s) {
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;

    list<int> queue;

    visited[s] = true;
    queue.push_back(s);

    list<int>::iterator i;

    while(!queue.empty()) {
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        for(i = adj[s].begin(); i != adj[s].end(); ++i) {
            if(!visited[*i]) {
                visited[*i] = true;
                queue.push_back(*i);
                }
            }
        }
    }

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "Following is Breadth First Traversal (starting from vertex 2)" << endl;
    g.BFS(2);

    return 0;
    }
```

##### Output

```text
Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1
```

##### Java

```java
// Breadth-first search

import java.util.Iterator;
import java.util.LinkedList;

public class Graph {
    private int V;
    private LinkedList<Integer> adj[];

    Graph(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
            adj[i] = new LinkedList();
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void BFS(int s) {
        boolean visited[] = new boolean[V];

        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();
            System.out.print(s + " ");

            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Following is Breadth First Traversal (starting from vertex 2)");

        g.BFS(2);
    }
}
```

##### Output

```text
Following is Breadth First Traversal (starting from vertex 2)
2 0 3 1
```

### Depth-first search

Depth-first search \(DFS\) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node \(selecting some arbitrary node as the root node in the case of a graph\) and explores as far as possible along each branch before backtracking.

#### C

```c
// Depth-first search

#include <stdio.h>
#include <stdlib.h>

struct node {
  int vertex;
  struct node* next;
};

struct node* createNode(int);

struct Graph {
  int numVertices;
  struct node** adjLists;
  int* visited;
};

// BFS algorithm
void DFS(struct Graph* graph, int vertex) {
  struct node* adjList = graph->adjLists[vertex];
  struct node* temp = adjList;

  graph->visited[vertex] = 1;
  printf("Visited %d \n", vertex);

  while (temp != NULL) {
    int connectedVertex = temp->vertex;

    if (graph->visited[connectedVertex] == 0) {
      DFS(graph, connectedVertex);
    }
    temp = temp->next;
  }
}

// Create a node

struct node* createNode(int v) {
  struct node* newNode = malloc(sizeof(struct node));
  newNode->vertex = v;
  newNode->next = NULL;
  return newNode;
}

// Create a graph

struct Graph* createGraph(int vertices) {
  struct Graph* graph = malloc(sizeof(struct Graph));
  graph->numVertices = vertices;

  graph->adjLists = malloc(vertices * sizeof(struct node*));
  graph->visited = malloc(vertices * sizeof(int));

  int i;
  for (i = 0; i < vertices; i++) {
    graph->adjLists[i] = NULL;
    graph->visited[i] = 0;
  }

  return graph;
}

// Add edge

void addEdge(struct Graph* graph, int src, int dest) {
  // Add edge from src to dest
  struct node* newNode = createNode(dest);
  newNode->next = graph->adjLists[src];
  graph->adjLists[src] = newNode;

  // Add edge from dest to src
  newNode = createNode(src);
  newNode->next = graph->adjLists[dest];
  graph->adjLists[dest] = newNode;
}

int main() {
  struct Graph* graph = createGraph(4);
  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 1, 2);
  addEdge(graph, 2, 3);

  DFS(graph, 2);

  return 0;
}
```

#### Output

```text
Visited 2
Visited 3
Visited 0
Visited 1
```

#### C++

```cpp
// Depth-first search

#include <iostream>
#include <list>


class Graph {
    int V;
    std::list<int> *adj;
    void DFSUtil(int v, bool visited[]);
public:
    Graph(int V);
    void addEdge(int v, int w);
    void DFS(int v);
};

Graph::Graph(int V) {
    this->V = V;
    adj = new std::list<int>[V];
}

void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

void Graph::DFSUtil(int v, bool visited[]) {
    visited[v] = true;
    std::cout << v << " ";

    std::list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFSUtil(*i, visited);
}

void Graph::DFS(int v) {
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;

    DFSUtil(v, visited);
}

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    std::cout << "Following is Depth First Traversal (starting from vertex 2) \n";
    g.DFS(2);

    return 0;
}
```

#### Output

```text
Following is Depth First Traversal (starting from vertex 2)
2 0 1 3
```

#### Java

```java
// Depth-first search

import java.io.*;
import java.util.*;


class Graph {
    private int V;
    private LinkedList<Integer> adj[];

    Graph(int v) {
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; ++i)
            adj[i] = new LinkedList();
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void DFSUtil(int v, boolean visited[]) {
        visited[v] = true;
        System.out.print(v + " ");

        int n;

        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            n = i.next();
            if (!visited[n])
                DFSUtil(n, visited);
        }
    }

    void DFS(int v) {
        boolean visited[] = new boolean[V];

        DFSUtil(v, visited);
    }

    public static void main(String args[]) {
        Graph g = new Graph(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Following is Depth First Traversal (starting from vertex 2)");

        g.DFS(2);
    }
}
```

#### Output

```text
Following is Depth First Traversal (starting from vertex 2)
2 0 1 3
```

#### Python

```python
# Depth-first search

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (max(self.graph) + 1)
        self.DFSUtil(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
g.DFS(2)
```

#### Output

```text
Following is Depth First Traversal (starting from vertex 2)
2 0 1 3
```

### Dijkstra's Algorithm

Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

#### C

```c
// Dijkstra's algorithm

#include <stdio.h>
#include <limits.h>

#define V 9

int minDistance(int dist[], int sptSet[]) {
  int min = INT_MAX, min_index;

  for (int v = 0; v < V; v++)
    if (sptSet[v] == 0 && dist[v] <= min)
      min = dist[v], min_index = v;

  return min_index;
}

int printSolution(int dist[]) {
  printf("Vertex \t\t Distance from Source");

    for (int i = 0; i < V; i++)
        printf("%d \t\t %d", i, dist[i]);
}

void dijkstra(int graph[V][V], int src) {
  int dist[V];
  int sptSet[V];

  for (int i = 0; i < V; i++)
    dist[i] = INT_MAX, sptSet[i] = 0;

  dist[src] = 0;

  for (int count = 0; count < V - 1; count++) {
    int u = minDistance(dist, sptSet);
    sptSet[u] = 1;

    for (int v = 0; v < V; v++)
      if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
        dist[v] = dist[u] + graph[u][v];
  }

  printSolution(dist);
}

int main() {
  int graph[V][V] = {
    { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
    { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
    { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
    { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
    { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
    { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
    { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
    { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
    { 0, 0, 2, 0, 0, 0, 6, 7, 0 }
  };

  dijkstra(graph, 0);

  return 0;
}
```

#### Output

```text
Vertex           Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14
```

#### Java

```java
// Dijkstra's algorithm

import java.util.*;
import java.lang.*;
import java.io.*;


class ShortestPath {
    static final int V = 9;

    int minDistance(int dist[], Boolean sptSet[]) {
        int min = Integer.MAX_VALUE, min_index = -1;

        for (int v = 0; v < V; v++)
            if (sptSet[v] == false && dist[v] <= min) {
                min = dist[v];
                min_index = v;
            }

        return min_index;
    }

    void printSolution(int dist[]) {
        System.out.println("Vertex \t\t Distance from Source");
        for (int i = 0; i < V; i++)
            System.out.println(i + " \t\t " + dist[i]);
    }

    void dijkstra(int graph[][], int src) {
        int dist[] = new int[V];

        Boolean sptSet[] = new Boolean[V];

        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
            sptSet[i] = false;
        }

        dist[src] = 0;

        for (int count = 0; count < V - 1; count++) {
            int u = minDistance(dist, sptSet);

            sptSet[u] = true;

            for (int v = 0; v < V; v++)

                if (!sptSet[v] && graph[u][v] != 0 &&
                        dist[u] != Integer.MAX_VALUE && dist[u] + graph[u][v] < dist[v])
                    dist[v] = dist[u] + graph[u][v];
        }

        printSolution(dist);
    }

    public static void main(String[] args) {
        int graph[][] = new int[][]{
                {0, 4, 0, 0, 0, 0, 0, 8, 0},
                {4, 0, 8, 0, 0, 0, 0, 11, 0},
                {0, 8, 0, 7, 0, 4, 0, 0, 2},
                {0, 0, 7, 0, 9, 14, 0, 0, 0},
                {0, 0, 0, 9, 0, 10, 0, 0, 0},
                {0, 0, 4, 14, 10, 0, 2, 0, 0},
                {0, 0, 0, 0, 0, 2, 0, 1, 6},
                {8, 11, 0, 0, 0, 0, 1, 0, 7},
                {0, 0, 2, 0, 0, 0, 6, 7, 0}
        };
        ShortestPath t = new ShortestPath();
        t.dijkstra(graph, 0);
    }
}
```

#### Output

```text
Vertex           Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14
```

### Floyd-Warshall Algorithm

Floyd–Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between all pairs of vertices, though it does not return details of the paths themselves.

#### C

```c
// Floyd-Warshall algorithm

#include <stdio.h>
#include <limits.h>

#define V 4

void printSolution(int dist[][V]) {
  printf("The following matrix shows the shortest distances between every pair of vertices \n");
  for (int i = 0; i < V; i++) {
    for (int j = 0; j < V; j++) {
      if (dist[i][j] == INT_MAX)
        printf("%7s", "INF");
      else
        printf("%7d", dist[i][j]);
    }
    printf(" \n");
    }
}

void floydWarshall(int graph[][V]) {
  int dist[V][V], i, j, k;

  for (i = 0; i < V; i++)
    for (j = 0; j < V; j++)
      dist[i][j] = graph[i][j];

  for (k = 0; k < V; k++) {
    for (i = 0; i < V; i++) {
      for (j = 0; j < V; j++) {
        if (dist[i][k] + dist[k][j] < dist[i][j])
          dist[i][j] = dist[i][k] + dist[k][j];
      }
    }
  }

  printSolution(dist);
}

int main() {
  int graph[V][V] = {
    { 0, 5, INF, 10 },
    { INF, 0, 3, INF },
    { INF, INF, 0, 1 },
    { INF, INF, INF, 0 }
  };

  floydWarshall(graph);
  return 0;
}
```

#### Output

```text
The following matrix shows the shortest distances between every pair of vertices
      0       5      8      9
    INF       0      3      4
    INF     INF      0      1
    INF     INF    INF      0
```

#### Java

```java
// Floyd-Warshall algorithm

import java.util.*;
import java.lang.*;

class FloydWarshall {
    final static int INF = 99999, V = 4;

    void floydWarshall(int graph[][]) {
        int dist[][] = new int[V][V];
        int i, j, k;

        for (i = 0; i < V; i++)
            for (j = 0; j < V; j++)
                dist[i][j] = graph[i][j];

        for (k = 0; k < V; k++) {
            for (i = 0; i < V; i++) {
                for (j = 0; j < V; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }

        printSolution(dist);
    }

    void printSolution(int dist[][]) {
        System.out.println("The following matrix shows the shortest " +
                "distances between every pair of vertices ");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][j] == INF)
                    System.out.print("INF ");
                else
                    System.out.print(dist[i][j] + "   ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int graph[][] = {
                {0, 5, INF, 10},
                {INF, 0, 3, INF},
                {INF, INF, 0, 1},
                {INF, INF, INF, 0}
        };
        FloydWarshall a = new FloydWarshall();

        a.floydWarshall(graph);
    }
}
```

#### Output

```text
The following matrix shows the shortest distances between every pair of vertices
0   5   8   9
INF 0   3   4
INF INF 0   1
INF INF INF 0
```

### Bellman-Ford Algorithm

The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

#### C

```c

// Bellman-Ford algorithm

#include <stdio.h>
#include <limits.h>

#define V 5
#define E 8

struct Edge {
  int src, dest, weight;
};

struct Graph {
  int V, E;
  struct Edge* edge;
};

struct Graph* createGraph(int V, int E) {
  struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
  graph->V = V;
  graph->E = E;
  graph->edge = (struct Edge*) malloc(graph->E * sizeof(struct Edge));
  return graph;
}

void printArr(int dist[], int n) {
  printf("Vertex   Distance from Source\n");
  for (int i = 0; i < V; ++i)
    printf("%d \t\t %d\n", i, dist[i]);
}

void BellmanFord(struct Graph* graph, int src) {
  int V = graph->V;
  int E = graph->E;
  int dist[V];

  for (int i = 0; i < V; i++)
    dist[i] = INT_MAX;
  dist[src] = 0;

  for (int i = 1; i <= V - 1; i++) {
    for (int j = 0; j < E; j++) {
      int u = graph->edge[j].src;
      int v = graph->edge[j].dest;
      int weight = graph->edge[j].weight;
      if (dist[u] != INT_MAX && dist[u] + weight < dist[v])
        dist[v] = dist[u] + weight;
    }
  }

  for (int i = 0; i < E; i++) {
    int u = graph->edge[i].src;
    int v = graph->edge[i].dest;
    int weight = graph->edge[i].weight;
    if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
      printf("Graph contains negative weight cycle");
      return;
    }
  }

  printArr(dist, V);

  return;
}

int main() {
  int V = 5;
  int E = 8;
  struct Graph* graph = createGraph(V, E);

  graph->edge[0].src = 0;
  graph->edge[0].dest = 1;
  graph->edge[0].weight = -1;

  graph->edge[1].src = 0;
  graph->edge[1].dest = 2;
  graph->edge[1].weight = 4;

  graph->edge[2].src = 1;
  graph->edge[2].dest = 2;
  graph->edge[2].weight = 3;

  graph->edge[3].src = 1;
  graph->edge[3].dest = 3;
  graph->edge[3].weight = 2;

  graph->edge[4].src = 1;
  graph->edge[4].dest = 4;
  graph->edge[4].weight = 2;

  graph->edge[5].src = 3;
  graph->edge[5].dest = 2;
  graph->edge[5].weight = 5;

  graph->edge[6].src = 3;
  graph->edge[6].dest = 1;
  graph->edge[6].weight = 1;

  graph->edge[7].src = 4;
  graph->edge[7].dest = 3;
  graph->edge[7].weight = -3;

  BellmanFord(graph, 0);

  return 0;
}
```

#### Output

```text
Vertex   Distance from Source
0                0
1                -1
2                2
3                -2
4                1
```

### Kruskal's Algorithm

Kruskal's algorithm is a minimum spanning tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest. It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning tree.

#### C

```c

// Kruskal's algorithm

#include <stdio.h>
#include <stdlib.h>

#define V 4

struct Edge {
  int src, dest, weight;
};

struct Graph {
  int V, E;
  struct Edge* edge;
};

struct Graph* createGraph(int V, int E) {
  struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
  graph->V = V;
  graph->E = E;
  graph->edge = (struct Edge*) malloc(graph->E * sizeof(struct Edge));
  return graph;
}

struct subset {
  int parent;
  int rank;
};

int find(struct subset subsets[], int i) {
  if (subsets[i].parent != i)
    subsets[i].parent = find(subsets, subsets[i].parent);
  return subsets[i].parent;
}

void Union(struct subset subsets[], int x, int y) {
  int xroot = find(subsets, x);
  int yroot = find(subsets, y);
  if (subsets[xroot].rank < subsets[yroot].rank)
    subsets[xroot].parent = yroot;
  else if (subsets[xroot].rank > subsets[yroot].rank)
    subsets[yroot].parent = xroot;
  else {
    subsets[yroot].parent = xroot;
    subsets[xroot].rank++;
  }
}

int myComp(const void* a, const void* b) {
  struct Edge* a1 = (struct Edge*) a;
  struct Edge* b1 = (struct Edge*) b;
  return a1->weight > b1->weight;
}

void KruskalMST(struct Graph* graph) {
  int V = graph->V;
  struct Edge result[V];
  int e = 0;
  int i = 0;
  qsort(graph->edge, graph->E, sizeof(graph->edge[0]), myComp);
  struct subset* subsets = (struct subset*) malloc(V * sizeof(struct subset));
  for (int v = 0; v < V; ++v) {
    subsets[v].parent = v;
    subsets[v].rank = 0;
  }
  while (e < V - 1) {
    struct Edge next_edge = graph->edge[i++];
    int x = find(subsets, next_edge.src);
    int y = find(subsets, next_edge.dest);
    if (x != y) {
      result[e++] = next_edge;
      Union(subsets, x, y);
    }
  }
  printf("Following are the edges in the constructed MST\n");
  for (i = 0; i < e; ++i)
    printf("%d -- %d == %d\n", result[i].src, result[i].dest, result[i].weight);
  return;
}

int main() {
  int V = 4;
  int E = 5;
  struct Graph* graph = createGraph(V, E);
  graph->edge[0].src = 0;
  graph->edge[0].dest = 1;
  graph->edge[0].weight = 10;
  graph->edge[1].src = 0;
  graph->edge[1].dest = 2;
  graph->edge[1].weight = 6;
  graph->edge[2].src = 0;
  graph->edge[2].dest = 3;
  graph->edge[2].weight = 5;
  graph->edge[3].src = 1;
  graph->edge[3].dest = 3;
  graph->edge[3].weight = 15;
  graph->edge[4].src = 2;
  graph->edge[4].dest = 3;
  graph->edge[4].weight = 4;
  KruskalMST(graph);
  return 0;
}
```

#### Output

```text

Following are the edges in the constructed MST

2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
```

#### Python

```python
# Kruskal's algorithm


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))



g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
```

#### Output

```text

Following are the edges in the constructed MST

2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
```

#### C++

```cpp
// Kruskal's algorithm


#include <bits/stdc++.h>
using namespace std;

class Graph {
  int V, E;
  vector<tuple<int, int, int>> edges;

    public:
    Graph(int V, int E) {
        this->V = V;
        this->E = E;
    }

    void addEdge(int u, int v, int w) {
        edges.push_back({w, u, v});
    }

    int kruskalMST();
};

struct DisjointSets {
    int *parent, *rnk;
    int n;

    DisjointSets(int n) {
        this->n = n;
        parent = new int[n + 1];
        rnk = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            rnk[i] = 0;
            parent[i] = i;
        }
    }

    int find(int u) {
        if (u != parent[u])
            parent[u] = find(parent[u]);
        return parent[u];
    }

    void merge(int x, int y) {
        x = find(x), y = find(y);

        if (rnk[x] > rnk[y])
            parent[y] = x;
        else
            parent[x] = y;

        if (rnk[x] == rnk[y])
            rnk[y]++;
    }
};

int Graph::kruskalMST() {
    int mst_wt = 0;
    sort(edges.begin(), edges.end());

    DisjointSets ds(V);

    vector<tuple<int, int, int>>::iterator it;
    for (it = edges.begin(); it != edges.end(); it++) {
        int u = get<1>(*it);
        int v = get<2>(*it);

        int set_u = ds.find(u);
        int set_v = ds.find(v);

        if (set_u != set_v) {
            cout << u << " - " << v << endl;
            mst_wt += get<0>(*it);
            ds.merge(set_u, set_v);
        }
    }

    return mst_wt;
}

int main() {
    int V = 9, E = 14;
    Graph g(V, E);

    g.addEdge(0, 1, 4);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 14);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(6, 7, 1);
    g.addEdge(6, 8, 6);
    g.addEdge(7, 8, 7);

    cout << "Edges of MST are \n";
    int mst_wt = g.kruskalMST();

    cout << "\nWeight of MST is " << mst_wt;

    return 0;

}
```

#### Output

```text

Edges of MST are
0 - 1
2 - 8
2 - 5
6 - 7
0 - 7
2 - 3
3 - 4
5 - 6

Weight of MST is 37
```

### Prim's Algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

#### Pseudocode

```text
Prim(G, w, r)
    for each u ∈ V[G]
        key[u] ← ∞
        π[u] ← NIL
    key[r] ← 0
    Q ← V[G]
    while Q ≠ ∅
        u ← EXTRACT-MIN(Q)
        for each v ∈ Adj[u]
            if v ∈ Q and w(u, v) < key[v]
                π[v] ← u
                key[v] ← w(u, v)
```

#### Python

```python
# Prim's algorithm


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min = float("inf")
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [float("inf")] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)


g = Graph(5)

g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

g.primMST()
```

#### Output

```text
Edge    Weight
0 - 1     2
1 - 2     3
0 - 3     6
1 - 4     5
```

#### C++

```cpp
// Prim's algorithm

#include <bits/stdc++.h>
using namespace std;

# define INF 0x3f3f3f3f

typedef pair<int, int> iPair;

class Graph {
    int V;
    list< pair<int, int> > *adj;

public:
    Graph(int V);
    void addEdge(int u, int v, int w);
    void primMST();
};

Graph::Graph(int V) {
    this->V = V;
    adj = new list<iPair> [V];
}

void Graph::addEdge(int u, int v, int w) {
    adj[u].push_back(make_pair(v, w));
    adj[v].push_back(make_pair(u, w));
}

void Graph::primMST() {
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
    int src = 0;
    vector<int> key(V, INF);
    vector<int> parent(V, -1);
    vector<bool> inMST(V, false);
    pq.push(make_pair(0, src));
    key[src] = 0;
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        inMST[u] = true;
        list< pair<int, int> >::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i) {
            int v = (*i).first;
            int weight = (*i).second;
            if (inMST[v] == false && key[v] > weight) {
                key[v] = weight;
                pq.push(make_pair(key[v], v));
                parent[v] = u;
            }
        }
    }
    for (int i = 1; i < V; ++i)
        cout << parent[i] << " - " << i << endl;
}

int main() {
    int V = 9;
    Graph g(V);
    g.addEdge(0, 1, 4);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 14);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(6, 7, 1);
    g.addEdge(6, 8, 6);
    g.addEdge(7, 8, 7);
    g.primMST();
    return 0;
}
```

#### Output

```text
0 - 1
1 - 2
2 - 3
2 - 5
5 - 6
6 - 7
2 - 8
```

### Dynamic Programming

Dynamic programming is a method for solving problems by breaking them down into smaller subproblems and storing the results of these subproblems to avoid computing them multiple times. It is mainly used for optimization problems, where multiple subproblems may have overlapping solutions. Dynamic programming algorithms are often used for problems that have optimal substructure, meaning that the optimal solution can be constructed from optimal solutions of its subproblems.

One common approach to solving problems using dynamic programming is to use a bottom-up approach, where the smaller subproblems are solved first and the solutions are stored in a table or array. Then, the solutions to larger subproblems can be found by combining the stored solutions in a specific way. Another approach is to use a top-down approach, where the larger subproblems are solved first and the solutions are passed down to the smaller subproblems as needed.

Dynamic programming can be applied to various types of problems, such as optimization, counting, and decision making. Some examples of problems that can be solved using dynamic programming include the Knapsack problem, the Longest Common Subsequence problem, and the Matrix Chain Multiplication problem.

#### Knapsack Problem

The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items.

##### Python

```python
# Knapsack problem

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]



val = [60, 100, 120]

wt = [10, 20, 30]

W = 50

n = len(val)

print(knapSack(W, wt, val, n))
```

##### Output

```text
220
```

##### C++

```cpp
// Knapsack problem

#include <bits/stdc++.h>
using namespace std;

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapSack(int W, int wt[], int val[], int n) {
    int i, w;
    int K[n + 1][W + 1];
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                K[i][w] = 0;
            else if (wt[i - 1] <= w)
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
            else
                K[i][w] = K[i - 1][w];
        }
    }
    return K[n][W];
}

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    cout << knapSack(W, wt, val, n);
    return 0;
}
```

##### Output

```text
220
```

##### Java

```java
// Knapsack problem

import java.util.*;

class Knapsack {
    static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    static int knapSack(int W, int wt[], int val[], int n) {
        int i, w;
        int K[][] = new int[n + 1][W + 1];
        for (i = 0; i <= n; i++) {
            for (w = 0; w <= W; w++) {
                if (i == 0 || w == 0)
                    K[i][w] = 0;
                else if (wt[i - 1] <= w)
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]);
                else
                    K[i][w] = K[i - 1][w];
            }
        }
        return K[n][W];
    }

    public static void main(String args[]) {
        int val[] = new int[]{60, 100, 120};
        int wt[] = new int[]{10, 20, 30};
        int W = 50;
        int n = val.length;
        System.out.println(knapSack(W, wt, val, n));
    }
}
```

##### Output

```text
220
```

#### Longest Common Subsequence

The longest common subsequence \(LCS\) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences. It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.

##### Python

```python
# Longest Common Subsequence

def lcs(X, Y, m, n):
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]




X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))
```

##### Output

```text
Length of LCS is  4
```

##### C++

```cpp
// Longest Common Subsequence

#include <bits/stdc++.h>
using namespace std;

int max(int a, int b) {
    return (a > b) ? a : b;
}

int lcs(char *X, char *Y, int m, int n) {
    int L[m + 1][n + 1];
    int i, j;
    for (i = 0; i <= m; i++) {
        for (j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i - 1] == Y[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;
            else
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }
    return L[m][n];
}

int main() {
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);
    cout << "Length of LCS is " << lcs(X, Y, m, n);
    return 0;
}
```

##### Output

```text
Length of LCS is 4
```

##### Java

```java
// Longest Common Subsequence

import java.util.*;

class LCS {
    static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    static int lcs(char[] X, char[] Y, int m, int n) {
        int L[][] = new int[m + 1][n + 1];
        int i, j;
        for (i = 0; i <= m; i++) {
            for (j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    L[i][j] = 0;
                else if (X[i - 1] == Y[j - 1])
                    L[i][j] = L[i - 1][j - 1] + 1;
                else
                    L[i][j] = max(L[i - 1][j], L[i][j - 1]);
            }
        }
        return L[m][n];
    }

    public static void main(String args[]) {
        String s1 = "AGGTAB";
        String s2 = "GXTXAYB";
        char[] X = s1.toCharArray();
        char[] Y = s2.toCharArray();
        int m = X.length;
        int n = Y.length;
        System.out.println("Length of LCS is " + lcs(X, Y, m, n));
    }
}
```

##### Output

```text
Length of LCS is 4
```

#### Longest Increasing Subsequence

The longest increasing subsequence \(LIS\) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

##### Python

```python
# Longest Increasing Subsequence

def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum


arr = [10, 22, 9, 33, 21, 50, 41, 60]

print("Length of lis is", lis(arr))
```

##### Output

```text
Length of lis is 5
```

##### C++

```cpp
// Longest Increasing Subsequence

#include <bits/stdc++.h>
using namespace std;

int lis(int arr[], int n) {
    int lis[n];
    lis[0] = 1;
    for (int i = 1; i < n; i++) {
        lis[i] = 1;
        for (int j = 0; j < i; j++)
            if (arr[i] > arr[j] && lis[i] < lis[j] + 1)
                lis[i] = lis[j] + 1;
    }
    return *max_element(lis, lis + n);
}

int main() {
    int arr[] = {10, 22, 9, 33, 21, 50, 41, 60};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Length of lis is " << lis(arr, n);
    return 0;
}
```

##### Output

```text
Length of lis is 5
```

##### Java

```java
// Longest Increasing Subsequence

import java.util.*;


class LIS {
    static int lis(int arr[], int n) {
        int lis[] = new int[n];
        lis[0] = 1;
        for (int i = 1; i < n; i++) {
            lis[i] = 1;
            for (int j = 0; j < i; j++)
                if (arr[i] > arr[j] && lis[i] < lis[j] + 1)
                    lis[i] = lis[j] + 1;
        }
        return Arrays.stream(lis).max().getAsInt();
    }

    public static void main(String args[]) {
        int arr[] = {10, 22, 9, 33, 21, 50, 41, 60};
        int n = arr.length;
        System.out.println("Length of lis is " + lis(arr, n));
    }
}
```

##### Output

```text
Length of lis is 5
```

#### Longest Palindromic Subsequence

Given a sequence, find the length of the longest palindromic subsequence in it. For example, if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest palindromic subsequence in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.

##### Python

```python
# Longest Palindromic Subsequence

def lps(str):
    n = len(str)
    L = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        L[i][i] = 1
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])
    return L[0][n - 1]








str = "BBABCBCAB"

print("The length of the LPS is " + str(lps(str)))
```

##### Output

```text
The length of the LPS is 7
```

##### C++

```cpp
// Longest Palindromic Subsequence

#include <bits/stdc++.h>
using namespace std;

int lps(string str) {
    int n = str.length();
    int i, j, cl;
    int L[n][n];
    for (i = 0; i < n; i++)
        L[i][i] = 1;
    for (cl = 2; cl <= n; cl++) {
        for (i = 0; i < n - cl + 1; i++) {
            j = i + cl - 1;
            if (str[i] == str[j] && cl == 2)
                L[i][j] = 2;
            else if (str[i] == str[j])
                L[i][j] = L[i + 1][j - 1] + 2;
            else
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);
        }
    }
    return L[0][n - 1];
}

int main() {
    string seq = "BBABCBCAB";
    int n = seq.length();
    cout << "The length of the LPS is " << lps(seq);
    return 0;
}
```

##### Output

```text
The length of the LPS is 7
```

##### Java

```java
// Longest Palindromic Subsequence

import java.util.*;

class LPS {
    static int lps(String str) {
        int n = str.length();
        int i, j, cl;
        int L[][] = new int[n][n];
        for (i = 0; i < n; i++)
            L[i][i] = 1;
        for (cl = 2; cl <= n; cl++) {
            for (i = 0; i < n - cl + 1; i++) {
                j = i + cl - 1;
                if (str.charAt(i) == str.charAt(j) && cl == 2)
                    L[i][j] = 2;
                else if (str.charAt(i) == str.charAt(j))
                    L[i][j] = L[i + 1][j - 1] + 2;
                else
                    L[i][j] = Math.max(L[i][j - 1], L[i + 1][j]);
            }
        }
        return L[0][n - 1];
    }

    public static void main(String args[]) {
        String seq = "BBABCBCAB";
        int n = seq.length();
        System.out.println("The length of the LPS is " + lps(seq));
    }
}
```

##### Output

```text
The length of the LPS is 7
```

#### Maxtrix Chain Multiplication

Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would have:

```text
(ABC)D = (AB)(CD) = A(BCD) = ....
```

However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product, or the efficiency.

For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,

```text
(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500
```

```text
A(BC) = (10×5×60) + (30×5×60) = 3000 + 9000 = 12000
```

##### Python

```python
# Matrix Chain Multiplication

def MatrixChainOrder(p, i, j):
    if i == j:
        return 0
    _min = 999999999
    for k in range(i, j):
        count = (MatrixChainOrder(p, i, k) +
                 MatrixChainOrder(p, k + 1, j) +
                 p[i - 1] * p[k] * p[j])
        if count < _min:
            _min = count
    return _min

arr = [1, 2, 3, 4, 3]
n = len(arr)
print("Minimum number of multiplications is " +
      str(MatrixChainOrder(arr, 1, n - 1)))
```

##### Output

```text
Minimum number of multiplications is 30
```

##### C++

```cpp
// Matrix Chain Multiplication

#include <bits/stdc++.h>
using namespace std;

int MatrixChainOrder(int p[], int i, int j) {
    if (i == j)
        return 0;
    int _min = 999999999;
    for (int k = i; k < j; k++) {
        int count = MatrixChainOrder(p, i, k) +
                    MatrixChainOrder(p, k + 1, j) +
                    p[i - 1] * p[k] * p[j];
        if (count < _min)
            _min = count;
    }
    return _min;
}

int main() {
    int arr[] = {1, 2, 3, 4, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Minimum number of multiplications is "
         << MatrixChainOrder(arr, 1, n - 1);
}
```

##### Output

```text
Minimum number of multiplications is 30
```

##### Java

```java
// Matrix Chain Multiplication

import java.util.*;

class MCM {
    static int MatrixChainOrder(int p[], int i, int j) {
        if (i == j)
            return 0;
        int _min = 999999999;
        for (int k = i; k < j; k++) {
            int count = MatrixChainOrder(p, i, k) +
                        MatrixChainOrder(p, k + 1, j) +
                        p[i - 1] * p[k] * p[j];
            if (count < _min)
                _min = count;
        }
        return _min;
    }

    public static void main(String args[]) {
        int arr[] = {1, 2, 3, 4, 3};
        int n = arr.length;
        System.out.println("Minimum number of multiplications is " +
                           MatrixChainOrder(arr, 1, n - 1));
    }
}
```

##### Output

```text
Minimum number of multiplications is 30
```

#### Rod Cutting

Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 \(by cutting in two pieces of lengths 2 and 6\)

```text
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
```

And if the prices are as following, then the maximum obtainable value is 24 \(by cutting in eight pieces of length 1\)

```text
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
```

##### Python

```python
# Rod Cutting

def cutRod(price, n):
    if n <= 0:
        return 0
    max_val = -999999999
    for i in range(0, n):
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1))
    return max_val

arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
```

##### Output

```text
Maximum Obtainable Value is 22
```

##### C++

```cpp
// Rod Cutting

#include <bits/stdc++.h>
using namespace std;

int cutRod(int price[], int n) {
    if (n <= 0)
        return 0;
    int max_val = -999999999;
    for (int i = 0; i < n; i++)
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1));
    return max_val;
}

int main() {
    int arr[] = {1, 5, 8, 9, 10, 17, 17, 20};
    int size = sizeof(arr) / sizeof(arr[0]);
    cout << "Maximum Obtainable Value is " << cutRod(arr, size);
}
```

##### Output

```text
Maximum Obtainable Value is 22
```

##### Java

```java
// Rod Cutting

import java.util.*;

class RodCutting {
    static int cutRod(int price[], int n) {
        if (n <= 0)
            return 0;
        int max_val = -999999999;
        for (int i = 0; i < n; i++)
            max_val = Math.max(max_val, price[i] + cutRod(price, n - i - 1));
        return max_val;
    }

    public static void main(String args[]) {
        int arr[] = {1, 5, 8, 9, 10, 17, 17, 20};
        int size = arr.length;
        System.out.println("Maximum Obtainable Value is " + cutRod(arr, size));
    }
}
```

##### Output

```text
Maximum Obtainable Value is 22
```

#### Subset Sum

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

##### Python

```python
# Subset Sum

def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n - 1] > sum:
        return isSubsetSum(set, n - 1, sum)
    return (isSubsetSum(set, n - 1, sum) or
            isSubsetSum(set, n - 1, sum - set[n - 1]))

set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubsetSum(set, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
```

##### Output

```text
Found a subset with given sum
```

##### C++

```cpp
// Subset Sum

#include <bits/stdc++.h>
using namespace std;

bool isSubsetSum(int set[], int n, int sum) {
    if (sum == 0)
        return true;
    if (n == 0 && sum != 0)
        return false;
    if (set[n - 1] > sum)
        return isSubsetSum(set, n - 1, sum);
    return isSubsetSum(set, n - 1, sum) ||
           isSubsetSum(set, n - 1, sum - set[n - 1]);
}

int main() {
    int set[] = {3, 34, 4, 12, 5, 2};
    int sum = 9;
    int n = sizeof(set) / sizeof(set[0]);
    if (isSubsetSum(set, n, sum) == true)
        cout << "Found a subset with given sum";
    else
        cout << "No subset with given sum";
}
```

##### Output

```text
Found a subset with given sum
```

##### Java

```java
// Subset Sum

import java.util.*;

class SubsetSum {
    static boolean isSubsetSum(int set[], int n, int sum) {
        if (sum == 0)
            return true;
        if (n == 0 && sum != 0)
            return false;
        if (set[n - 1] > sum)
            return isSubsetSum(set, n - 1, sum);
        return isSubsetSum(set, n - 1, sum) ||
               isSubsetSum(set, n - 1, sum - set[n - 1]);
    }

    public static void main(String args[]) {
        int set[] = {3, 34, 4, 12, 5, 2};
        int sum = 9;
        int n = set.length;
        if (isSubsetSum(set, n, sum) == true)
            System.out.println("Found a subset with given sum");
        else
            System.out.println("No subset with given sum");
    }
}
```

##### Output

```text
Found a subset with given sum
```
