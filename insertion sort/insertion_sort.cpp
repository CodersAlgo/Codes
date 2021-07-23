#include <iostream>

using namespace std;

template <class T>

void Print(T& vec, int n, string s){

    cout << s << ": [" << flush;

    for (int i=0; i<n; i++){
        cout << vec[i] << flush;
        if (i < n-1){
            cout << ", " << flush;
        }
    }

    cout << "]" << endl;
}

void InsertionSort(int A[], int n){

    for (int i=1; i<n; i++){
        int j = i-1;
        int x = A[i];

        while (j>-1 && A[j] > x){
            A[j+1] = A[j];
            j--;
        }
        
        A[j+1] = x;
    }
}

int main() {

    int A[] = {1,-1,9,0,-3,6,10,20,67,-9,8,8};

    InsertionSort(A, sizeof(A)/sizeof(A[0]));
    Print(A, sizeof(A)/sizeof(A[0]), "Array after sorting with insertion sort algorithm :- ");

    return 0;
}
