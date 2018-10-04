
#ifndef Cylinder_h
#define Cylinder_h
#include "Circle.h"
class Cylinder : public Circle
{
public:
    Cylinder(double r, double hei);
    double computeArea();
    void expand(int factor);
    void display();
    ~Cylinder();
    double computeVolume();
private:
    double height;
};
#endif /* Cylinder_hpp */
