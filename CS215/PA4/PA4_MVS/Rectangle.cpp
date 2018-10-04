
#include "Rectangle.h"
#include <iostream>
using namespace std;

Rectangle::Rectangle(double len, double wid)
{
    double length = len;
    double width  = wid;
}
double Rectangle::computeArea() {
	// area is length times width
    double area = length * width;
    return area;
}
void Rectangle::expand(int factor) {
	// only expand if factor is greater than zero
    if (factor > 0) {
        length *= factor;
        width *= factor;
    }
    else
        cout << "Invalid factor: must be integer greater than zero." << endl;
}
void Rectangle::display() {
	// display current length, width, and area
    cout << "Rectangle: (length = "<< length <<", width = " << width << ")" << endl;
    cout << "Area: " << computeArea() << endl;
    cout << endl;
}
double Rectangle::get_len() const {
	// allow child classes to access length
    return length;
}
double Rectangle::get_wid() const {
	// allow child classes to access width
    return width;
}