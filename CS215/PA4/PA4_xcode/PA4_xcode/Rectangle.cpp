//
//  Rectangle.cpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include "Rectangle.hpp"
#include <iostream>
using namespace std;

Rectangle::Rectangle(double len, double wid)
{
    double length = len;
    double width  = wid;
}
double Rectangle::computeArea() {
    double area = length * width;
    return area;
}
void Rectangle::expand(int factor) {
    if (factor > 0) {
        length *= factor;
        width *= factor;
    }
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Rectangle::display() {
    cout << "Rectangle: (length = "<< length <<", width = " << width << ")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << endl;
}
double Rectangle::get_len() const {
    return length;
}
double Rectangle::get_wid() const {
    return width;
}