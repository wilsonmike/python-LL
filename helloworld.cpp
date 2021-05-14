#include <iostream>
using namespace std;

int main()
{
    string name;
    string favFood;

    cout << "Please enter your name: " << endl;
    cin >> name;
    cout << "Hello, " << name << ", nice to see you, what is your favorite food? \n";
    cin >> favFood;
    cout << "Great! " << favFood << ", very tasty! \n";
}