
#include "Rectangle.h"
#ifndef Cuboid_h
#define Cuboid_h

class Cuboid : public Rectangle
{
public:
    Cuboid(double len, double wid, double hei);
    double computeArea();
    void expand(int factor);
    void display();
    ~Cuboid();
    double computeVolume();
private:
    double height;
};

#endif /* Cuboid_hpp */
