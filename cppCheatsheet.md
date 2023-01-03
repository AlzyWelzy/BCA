# C++ Deep Cheatsheet

Welcome to the C++ Deep Cheatsheet repository. This repository contains an in-depth reference for the C++ programming language.

## Table of Contents

1. Basics
   - Data types
   - Variables
   - Operators
   - Control structures
   - Functions
2. Classes and Objects
   - Defining classes
   - Encapsulation
   - Inheritance
   - Polymorphism
3. Templates and Generic Programming
4. The Standard Template Library (STL)
   - Containers
   - Iterators
   - Algorithms
5. Exception Handling
6. Input/Output (I/O)
7. Namespaces
8. Preprocessor Directives

## Basics

### Data types

- `bool`: Represents a boolean value (`true` or `false`).
- `char`: Represents a single character.
- `int`: Represents an integer value.
- `float`: Represents a floating-point value.
- `double`: Represents a double-precision floating-point value.

### Variables

To declare a variable in C++, you must specify its data type and name. For example:

```c++
int age;
float price;
```

You can also initialize a variable at the time of declaration by assigning it a value:

```c++
int age = 21;
float price = 9.99;
```

### Operators

C++ supports a variety of operators for performing operations on variables. The following table lists some of the most commonly used operators:

| Operator | Description              |
| -------- | ------------------------ |
| `+`      | Addition                 |
| `-`      | Subtraction              |
| `*`      | Multiplication           |
| `/`      | Division                 |
| `%`      | Modulus                  |
| `++`     | Increment                |
| `--`     | Decrement                |
| `=`      | Assignment               |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `&&`     | Logical AND              |
| `!`      | Logical NOT              |
| `\|\|`   | Logical OR               |

### Control structures

C++ supports a variety of control structures for controlling the flow of execution of a program. The following table lists some of the most commonly used control structures:

| Control structure | Description                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| `if`              | Executes a block of code if a condition is true                                                     |
| `if...else`       | Executes a block of code if a condition is true, or another block of code if the condition is false |
| `switch`          | Executes a block of code based on the value of a variable                                           |
| `while`           | Executes a block of code repeatedly while a condition is true                                       |
| `do...while`      | Executes a block of code repeatedly while a condition is true, and executes the block at least once |
| `for`             | Executes a block of code repeatedly for a specified number of times                                 |
| `break`           | Terminates a loop or switch statement                                                               |
| `continue`        | Skips the current iteration of a loop                                                               |

### Functions

A function is a block of code that performs a specific task. Functions are useful for breaking down a program into smaller, more manageable pieces. Functions can also be reused in other parts of a program.

To define a function in C++, you must specify its return type, name, and parameters. For example:

```c++
int add(int a, int b) {
    return a + b;
}
```

## Classes and Objects

### Defining classes

A class is a user-defined data type that can be used to create objects. A class definition consists of a class header and a class body. The class header specifies the name of the class and the access specifier. The class body contains the data members and member functions of the class.

```c++
class Person {
    public:
        string name;
        int age;
        void sayHello() {
            cout << "Hello, my name is " << name << endl;
        }
};
```

### Encapsulation

Encapsulation is the process of combining data and functions that operate on that data into a single unit. Encapsulation is used to hide the implementation details of a class from other objects.

```c++
class Person {
    private:
        string name;
        int age;
    public:
        void setName(string name) {
            this->name = name;
        }
        void setAge(int age) {
            this->age = age;
        }
        string getName() {
            return name;
        }
        int getAge() {
            return age;
        }
};
```

### Inheritance

Inheritance is the process of deriving a new class from an existing class. The new class is called a derived class, and the existing class is called a base class. The derived class inherits all the data members and member functions of the base class.

```c++
class Student : public Person {
    private:
        int studentId;
    public:
        void setStudentId(int studentId) {
            this->studentId = studentId;
        }
        int getStudentId() {
            return studentId;
        }
};
```

### Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in C++ occurs when a parent class reference is used to refer to a child class object.

```c++
class Person {
    public:
        virtual void sayHello() {
            cout << "Hello" << endl;
        }
};

class Student : public Person {
    public:
        void sayHello() {
            cout << "Hello, I am a student" << endl;
        }
};

int main() {
    Person *person = new Student();
    person->sayHello();
    return 0;
}
```

## Templates and Generic Programming

Templates are a powerful feature of C++ that allow you to write generic functions and classes. Generic functions and classes can work with any data type.

```c++
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << add(1, 2) << endl;
    cout << add(1.1, 2.2) << endl;
    cout << add("Hello, ", "World!") << endl;
    return 0;
}
```

## The Standard Template Library (STL)

The Standard Template Library (STL) is a powerful library of generic data structures and algorithms. The STL is part of the C++ standard library, and is included automatically when you include the `<iostream>` header.

### Containers

Containers are objects that store other objects. The STL provides a variety of containers for storing data. The following table lists some of the most commonly used containers:

| Container | Description              |
| --------- | ------------------------ |
| `vector`  | A dynamic array          |
| `list`    | A doubly-linked list     |
| `deque`   | A double-ended queue     |
| `set`     | A set of unique elements |
| `map`     | A set of key-value pairs |

### Iterators

Iterators are objects that point to elements in a container. The STL provides a variety of iterators for accessing elements in a container. The following table lists some of the most commonly used iterators:

| Iterator           | Description                |
| ------------------ | -------------------------- |
| `vector::iterator` | An iterator for a `vector` |
| `list::iterator`   | An iterator for a `list`   |
| `deque::iterator`  | An iterator for a `deque`  |
| `set::iterator`    | An iterator for a `set`    |
| `map::iterator`    | An iterator for a `map`    |

### Algorithms

Algorithms are functions that perform operations on containers. The STL provides a variety of algorithms for manipulating containers. The following table lists some of the most commonly used algorithms:

| Algorithm | Description                                                           |
| --------- | --------------------------------------------------------------------- |
| `sort`    | Sorts the elements in a container                                     |
| `reverse` | Reverses the order of the elements in a container                     |
| `find`    | Finds an element in a container                                       |
| `count`   | Counts the number of elements in a container that match a given value |
| `copy`    | Copies the elements from one container to another                     |

## Input and Output

### Reading input

The `cin` object is used to read input from the standard input stream. The `>>` operator is used to read data from the `cin` object.

```c++
int main() {
    int a;
    cin >> a;
    cout << a << endl;
    return 0;
}
```

### Writing output

The `cout` object is used to write output to the standard output stream. The `<<` operator is used to write data to the `cout` object.

```c++
int main() {
    int a = 1;
    cout << a << endl;
    return 0;
}
```

### Formatting output

The `iomanip` header provides functions for formatting output. The `setw` function is used to set the width of a field. The `setfill` function is used to set the fill character of a field.

```c++
int main() {
    int a = 1;
    cout << setw(10) << setfill('0') << a << endl;
    return 0;
}
```

### Reading and writing files

The `fstream` header provides functions for reading and writing files. The `ifstream` class is used to read from a file. The `ofstream` class is used to write to a file.

```c++
int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int a;
    fin >> a;
    fout << a << endl;
    return 0;
}
```

## Exception Handling

Exception handling is a mechanism for handling errors in a program. Exceptions are thrown when an error occurs, and are caught when they are handled.

```c++
int main() {
    try {
        throw 1;
    } catch (int e) {
        cout << "Caught exception with value " << e << endl;
    }
    return 0;
}
```

<!-- ## References

- [C++ Tutorial](https://www.tutorialspoint.com/cplusplus/index.htm)
- [C++ Reference](http://www.cplusplus.com/reference/) -->

## Exercises

1. Write a program that reads a list of integers from the standard input stream, and prints the sum of the integers to the standard output stream.

2. Write a program that reads a list of integers from the standard input stream, and prints the sum of the integers to the standard output stream. The program should handle the case where the user enters a non-integer value.

3. Write a program that reads a list of integers from the standard input stream, and prints the sum of the integers to the standard output stream. The program should handle the case where the user enters a non-integer value, and should continue to read input until the user enters a valid value.
