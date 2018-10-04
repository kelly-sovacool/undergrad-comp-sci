//
//  Sphere.cpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include "Sphere.hpp"
#include <cmath>
#include <iostream>
using namespace std;
Sphere::Sphere(double r) : Circle(r) {}
double Sphere::computeArea() {
    double area = 4 * PI * pow(get_rad(), 2);
    return area;
}
double Sphere::computeVolume() {
    double volume = 4/3 * PI * pow(get_rad(), 3);
    return volume;
}
void Sphere::expand(int factor) {
    Circle::expand(factor);
}
void Sphere::display() {
    cout << "Sphere: (radius = " << get_rad() << ")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << "Volume: " << computeVolume() << endl;
    cout << endl;
}