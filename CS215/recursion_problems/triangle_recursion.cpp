//
//  main.cpp
//  exploring_in_class
//
//  Created by Kelly Sovacool on 11/19/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include <iostream>
using namespace std;

void print_triangle(int num) {
    for (int i=0; i<num; i++)
        cout << "*";
    cout << endl;
    if (num > 1)
        print_triangle(num - 1);
}

int main() {
    cout << "Enter max num of stars: ";
    int num;
    cin >> num;
    print_triangle(num);
    return 0;
}
