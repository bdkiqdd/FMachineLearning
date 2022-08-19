#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wsign-compare"

#include <iostream>
#include <chrono> // Lib to do some benchmarking on the C++ app 
#include <numeric>
#include <fstream> // To use archives
#include <vector> 
#include <string>
// Funcs to make easy do a Naive Bayes
#include <algorithm>
#include <math.h>
#include <cmath>

using namespace std;
using namespace std::chrono;

const int startTest = 900;

const int numOfInteractions = 5;

ifstream openFile(string fileName){

    ifstream inputFile(fileName);

   if(!inputFile.is_open()){
        cout << "Error to open the file. " << endl;
   }else{
        cout << "Successfully opened!" << endl;
   }

    return inputFile;
}

int main()
{

    //ifstream inputData("dados/dataset.csv");

    // string line;
    
    /*
    while (getline (inputData,line)){
        cout << line << endl;
    }
    inputData.close();
    */
   
    double idVal;
    double tipo_docVal;
    double classeVal;
    double cerificado_validoVal;
    double uso_diasVal;

    vector<double> id;
    vector<double> tipo_doc;
    vector<double> classe;
    vector<double> cerificado_valido;
    vector<double> uso_dias;

    string header,cell;

    getline(openFile("dados/dataset.csv"),header);
}