//
//  Circle.cpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include "Circle.hpp"
#include <cmath>
#include <iostream>
using namespace std;

Circle::Circle(double r) {
    double radius = r;
}
double Circle::computeArea() {
    double area = PI * pow(radius, 2);
    return area;
}
void Circle::expand(int factor) {
    if (factor > 0)
        radius *= factor;
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Circle::display() {
    cout << "Circle: (radius = " << radius << ")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << endl;
}
double Circle::get_rad() const {
    return radius;
}