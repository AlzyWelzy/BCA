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

    cout << stack << endl;


    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    return 0;
}