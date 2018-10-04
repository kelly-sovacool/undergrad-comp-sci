//
//  Cuboid.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//
#include "Rectangle.hpp"
#ifndef Cuboid_hpp
#define Cuboid_hpp

class Cuboid : public Rectangle
{
public:
    Cuboid(double len, double wid, double hei);
    double computeArea();
    void expand(int factor);
    void display();
    //~Cuboid();
    double computeVolume();
private:
    double height;
};

#endif /* Cuboid_hpp */
