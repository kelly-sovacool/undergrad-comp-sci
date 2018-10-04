
#include "Circle.h"
#include <cmath>
#include <iostream>
using namespace std;

Circle::Circle(double r) {
    double radius = r;
}
double Circle::computeArea() {
	// area = pi * radius squared
    double area = PI * pow(radius, 2);
    return area;
}
void Circle::expand(int factor) {
	// only expand if factor greater than zero
    if (factor > 0)
        radius *= factor;
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Circle::display() {
	// display current radius and area
    cout << "Circle: (radius = " << radius << ")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << endl;
}
double Circle::get_rad() const {
	// allow child classes to access radius
    return radius;
}