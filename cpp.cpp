// Stacks

// Create a stack that will have a list of strings strored onto it

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    stack<string> s;
    s.push("Hello");
    s.push("World");
    s.push("!");
    //print all the elements in the stack

    // cout << stack << endl;


    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();



    // write a program that will print the memory that data types take up

    cout << "Size of int: " << sizeof(int) << endl;
    cout << "Size of float: " << sizeof(float) << endl;
    cout << "Size of double: " << sizeof(double) << endl;
    cout << "Size of char: " << sizeof(char) << endl;
    cout << "Size of bool: " << sizeof(bool) << endl;





    return 0;
}