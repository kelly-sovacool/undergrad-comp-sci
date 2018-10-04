
#include "Sphere.h"
#include <cmath>
#include <iostream>
using namespace std;
Sphere::Sphere(double r) : Circle(r) {}
double Sphere::computeArea() {
	// area = 4 * pi * radius squared
	double area = 4 * PI * pow(get_rad(), 2);
	return area;
}
double Sphere::computeVolume() {
	// volume = 4/3 * pi * radius cubed
	double volume = 4 / 3 * PI * pow(get_rad(), 3);
	return volume;
}
void Sphere::expand(int factor) {
	// use circle expand function because have same data members
	Circle::expand(factor);
}
void Sphere::display() {
	// display current radius, area, and volume
	cout << "Sphere: (radius = " << get_rad() << ")" << endl;
	cout << "Area: " << computeArea() << endl;
	cout << "Volume: " << computeVolume() << endl;
	cout << endl;
}