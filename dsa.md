# Data Structures and Algorithms Cheatsheet with Explanation and Code Snippets in Python, Java, C/C++, and JavaScript

## Table of Contents

- [Data Structures and Algorithms Cheatsheet with Explanation and Code Snippets in Python, Java, C/C++, and JavaScript](#data-structures-and-algorithms-cheatsheet-with-explanation-and-code-snippets-in-python-java-cc-and-javascript)
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

In Python:

```python
array.insert(0, 0)
```

In Java:

```java
int[] newArray = new int[array.length + 1];
newArray[0] = 0;
System.arraycopy(array, 0, newArray, 1, array.length);
array = newArray;
```

In C/C++:

```c
int newArray[sizeof(array) / sizeof(array[0]) + 1];
newArray[0] = 0;
for (int i = 1; i < sizeof(newArray) / sizeof(newArray[0]); i++) {
  newArray[i] = array[i - 1];
}
array = newArray;
```

In JavaScript:

```javascript
array.unshift(0);
```

#### Array Deletion

In Python:

```python
array.pop(0)
```

In Java:

```java
int[] newArray = new int[array.length - 1];
System.arraycopy(array, 1, newArray, 0, array.length - 1);
array = newArray;
```

In C/C++:

```c
int newArray[sizeof(array) / sizeof(array[0]) - 1];
for (int i = 0; i < sizeof(newArray) / sizeof(newArray[0]); i++) {
  newArray[i] = array[i + 1];
}
array = newArray;
```

In JavaScript:

```javascript
array.shift();
```

### Linked Lists

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers. Each element in a linked list is called a node. Each node contains two items: the data stored and a link to the next node. The data can be any valid data type. The last node has a link to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty, then the head is a null reference. A single node is not a linked list because it does not contain any link to the next node. A linked list is represented by a pointer to the first node of the linked list. The last node points to null. It should be noted that we can traverse the linked list in only forward direction. We cannot move backwards.

#### Linked List Declaration

In Python:

````python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
        self.head = node
        else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    ```
````

In Java:

```java
class Node {
  int data;
  Node next;

  Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  Node head;

  LinkedList() {
    this.head = null;
  }

  void insert(int data) {
    Node node = new Node(data);
    if (head == null) {
      head = node;
    } else {
      Node current = head;
      while (current.next != null) {
        current = current.next;
      }
      current.next = node;
    }
  }
}
```

In C/C++:

```c
struct Node {
  int data;
  struct Node *next;
};

struct LinkedList {
  struct Node *head;
};

void insert(struct LinkedList *list, int data) {
  struct Node *node = (struct Node *)malloc(sizeof(struct Node));
  node->data = data;
  node->next = NULL;
  if (list->head == NULL) {
    list->head = node;
  } else {
    struct Node *current = list->head;
    while (current->next != NULL) {
      current = current->next;
    }
    current->next = node;
  }
}
```

In JavaScript:

```javascript
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

  insert(data) {
    const node = new Node(data);
    if (this.head === null) {
      this.head = node;
    } else {
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = node;
    }
  }
}
```

#### Linked List Traversal

In Python:

```python
current = linked_list.head
while current is not None:
  print(current.data)
  current = current.next
```

In Java:

```java
Node current = linked_list.head;
while (current != null) {
  System.out.println(current.data);
  current = current.next;
}
```

In C/C++:

```c
struct Node *current = linked_list->head;
```

In JavaScript:

```javascript
let current = linked_list.head;
while (current !== null) {
  console.log(current.data);
  current = current.next;
}
```

#### Linked List Insertion

In Python:

```python
node = Node(data)
node.next = linked_list.head
linked_list.head = node
```

In Java:

```java
Node node = new Node(data);
node.next = linked_list.head;
linked_list.head = node;
```

In C/C++:

```c
struct Node *node = (struct Node *)malloc(sizeof(struct Node));
node->data = data;
node->next = linked_list->head;
linked_list->head = node;
```

In JavaScript:

```javascript
const node = new Node(data);
node.next = linked_list.head;
linked_list.head = node;
```

#### Linked List Deletion

In Python:

```python
linked_list.head = linked_list.head.next
```

In Java:

```java
linked_list.head = linked_list.head.next;
```

In C/C++:

```c
linked_list->head = linked_list->head->next;
```

In JavaScript:

```javascript
linked_list.head = linked_list.head.next;
```

### Stacks

A stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). Mainly the following three basic operations are performed in the stack:

- Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.

- Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.

- Peek or Top: Returns top element of stack.

- isEmpty: Returns true if stack is empty, else false
