#include <iostream>
using namespace std;

int main(){

    int len,num,*ptr;

    cout << "Type the len of your list: ";
    cin >> len;

    int numbers[len];

    cout << "Type the numbers that you want on your list: " << endl;

    for (int i = 0; i < len; i++)
    {
        cin >> num;
        numbers[i] = num;    
    }
    
    /*
    Testing the array
    for (int i = 0; i < len; i++)
    {
        cout << numbers[i];    
    }
    */

   for (int i = 0; i < len; i++)
   {
       if (*ptr < numbers[i])
       {
           ptr = &numbers[i];
       }
   }

   cout << "Max number " << *ptr;
   

    return 0;
}