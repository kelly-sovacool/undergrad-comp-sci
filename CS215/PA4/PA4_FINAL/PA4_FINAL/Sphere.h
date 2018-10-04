
#ifndef Sphere_h
#define Sphere_h
#include "Circle.h"

class Sphere : public Circle
{
public:
	Sphere(double r);
	double computeArea();
	void expand(int factor);
	void display();
	~Sphere() {}
	double computeVolume();
private:
};
#endif /* Sphere_hpp */
