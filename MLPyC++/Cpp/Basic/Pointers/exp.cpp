#include <iostream>

int main(){

    int x =5;

    // Print the variable value
    std::cout << x << "\n";

    // Print the local on memory that this variable is
    std::cout << &x << "\n";

    // Print with the addres of variable your own value
    std::cout << *(&x) <<"\n"; 

    return 0;
}