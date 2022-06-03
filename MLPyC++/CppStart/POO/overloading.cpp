#include <iostream>
using namespace std;

class Pessoa{

    public:
        void print(string name){
            cout << "Name -> " << name;
        };

        void print(string name,string surname){
            cout << "Concat name -> " << name << " " << surname;
        };
};

int main(void){

    Pessoa pessoa;

    pessoa.print("Kaique");

    cout << endl;

    pessoa.print("Kaique","Gomes");
    return 0;
}