//
//  Cylinder.cpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include "Cylinder.hpp"
#include <iostream>
using namespace std;
Cylinder::Cylinder(double r, double hei)
: Circle(r)
{
    double height = hei;
}
double Cylinder::computeArea() {
    double area = 2 * PI * get_rad() * height + 2 * Circle::computeArea();
    return area;
}
double Cylinder::computeVolume() {
    double volume = height * Circle::computeArea();
    return volume;
}
void Cylinder::expand(int factor) {
    if (factor > 0) {
        Circle::expand(factor);
        height *= factor;
    }
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Cylinder::display() {
    cout << "Cylinder: (radius = " << get_rad() << ", height = "<< height <<")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << "Volume: " << computeVolume() << endl;
    cout << endl;
}