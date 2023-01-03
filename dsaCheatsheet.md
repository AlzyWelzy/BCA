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
  - [Algorithms](#algorithms)
    - [Sorting](#sorting)
      - [Bubble Sort](#bubble-sort)
        - [C++](#c-1)
        - [JavaScript (ES6)](#javascript-es6-1)
        - [Java](#java-9)
        - [Python](#python-10)
      - [Selection Sort](#selection-sort)
        - [C++](#c-2)
        - [JavaScript (ES6)](#javascript-es6-2)
        - [Java](#java-10)
        - [Python](#python-11)
      - [Insertion Sort](#insertion-sort)
        - [C++](#c-3)
        - [JavaScript (ES6)](#javascript-es6-3)
        - [Java](#java-11)
        - [Python](#python-12)
      - [Merge Sort](#merge-sort)
        - [C++](#c-4)
        - [JavaScript (ES6)](#javascript-es6-4)
        - [Java](#java-12)
        - [Python](#python-13)
        - [C++](#c-5)
      - [Quick Sort](#quick-sort)
        - [Java](#java-13)
        - [Python](#python-14)
        - [C++](#c-6)
        - [JavaScript](#javascript-8)
      - [Heap Sort](#heap-sort)
        - [Java](#java-14)
        - [Python](#python-15)
        - [C++](#c-7)
        - [JavaScript](#javascript-9)
    - [Searching](#searching)
      - [Linear Search](#linear-search)
        - [Pseudocode](#pseudocode)
        - [C](#c-8)
        - [Python](#python-16)
        - [C++](#c-9)
        - [JavaScript](#javascript-10)
        - [Java](#java-15)
      - [Binary Search](#binary-search)
        - [Pseudocode](#pseudocode-1)
        - [C](#c-10)
        - [Python](#python-17)
        - [C++](#c-11)
        - [JavaScript](#javascript-11)
        - [Java](#java-16)
      - [Jump Search](#jump-search)
        - [Pseudocode](#pseudocode-2)
        - [C](#c-12)
        - [Python](#python-18)
        - [C++](#c-13)
        - [JavaScript](#javascript-12)
        - [Java](#java-17)
      - [Interpolation search](#interpolation-search)

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
