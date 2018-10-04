//
//  Cylinder.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#ifndef Cylinder_hpp
#define Cylinder_hpp
#include "Circle.hpp"
#include <stdio.h>
class Cylinder : public Circle
{
public:
    Cylinder(double r, double hei);
    double computeArea();
    void expand(int factor);
    void display();
    //~Cylinder();
    double computeVolume();
private:
    double height;
};
#endif /* Cylinder_hpp */
