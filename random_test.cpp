// C++ program to demonstrate
// the use of rand()
#include <cstdlib>
#include <iostream>
#include <time.h>
using namespace std;

int main()
{
    srand(time(0));
    // This program will create some sequence of
    // random numbers on every program run
    for (int i = 0; i < 5; i++)
        cout << rand() << " ";

    return 0;
}
