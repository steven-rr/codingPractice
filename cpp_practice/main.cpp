#include <iostream>
#include "linkedlist.h"
#include "hashtable.h"
using namespace std;


double addFx(double x, double y)
{
    return x + y;
};

int main()
{
    LinkedList link1;
    double result;
    result = link1.doSomething(1.0,2.0);
    
    HashTable hashtable1;
    double result2;
    result2 = hashtable1.doSomethingAgain(2.0, 2.0);
    
    double x = 1.0;
    std::cout << "hello world"<< std::endl;
    double z = addFx(1.0, 2.0);
    return 0;

};


