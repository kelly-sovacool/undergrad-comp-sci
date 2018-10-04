
#include "Cylinder.h"
#include <iostream>
using namespace std;
Cylinder::Cylinder(double r, double hei)
: Circle(r)
{
    double height = hei;
}
double Cylinder::computeArea() {
	// area = 2 * pi * radius * height + 2 * area of the circles
    double area = 2 * PI * get_rad() * height + 2 * Circle::computeArea();
    return area;
}
double Cylinder::computeVolume() {
	// volume = height * area of the circles
    double volume = height * Circle::computeArea();
    return volume;
}
void Cylinder::expand(int factor) {
	// only expand if factor is greater than zero
    if (factor > 0) {
        Circle::expand(factor);
        height *= factor;
    }
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Cylinder::display() {
	// display current radius, height, area, and volume
    cout << "Cylinder: (radius = " << get_rad() << ", height = "<< height <<")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << "Volume: " << computeVolume() << endl;
    cout << endl;
}