//
//  Sphere.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#ifndef Sphere_hpp
#define Sphere_hpp
#include "Circle.hpp"

class Sphere : public Circle
{
public:
    Sphere(double r);
    double computeArea();
    void expand(int factor);
    void display();
    ~Sphere();
    double computeVolume();
private:
};
#endif /* Sphere_hpp */
