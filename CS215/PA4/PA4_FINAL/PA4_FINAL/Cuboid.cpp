
#include "Cuboid.h"
#include <iostream>
using namespace std;
Cuboid::Cuboid(double len, double wid, double hei)
	: Rectangle(len, wid)
{
	double height = hei;
}
double Cuboid::computeArea() {
	// surface area is the sum of the area of each of its faces
	double face1 = get_len() * get_wid();
	double face2 = get_wid() * height;
	double face3 = get_len() * height;
	double surf_area = 2 * face1 + 2 * face2 + 2 * face3;
	return surf_area;
}
void Cuboid::expand(int factor) {
	// only expand if the factor is greater than zero
	if (factor > 0) {
		Rectangle::expand(factor);
		height *= factor;
	}
	else
		cout << "Invalid factor: must be integer greater than zero." << endl;
}
double Cuboid::computeVolume() {
	// volume is length times width times height
	double volume = get_len() * get_wid() * height;
	return volume;
}
void Cuboid::display() {
	// display current length, width, height, area, and volume
	cout << "Cuboid: (length = " << get_len() << ", width = " << get_wid() << ", height = " << height << ")" << endl;
	cout << "Area: " << computeArea() << endl;
	cout << "Volume: " << computeVolume() << endl;
	cout << endl;
}