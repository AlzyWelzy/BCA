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
