//
//  Circle.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//
#include "Shape.hpp"
#ifndef Circle_hpp
#define Circle_hpp
class Circle : public Shape
{
public:
    Circle(double r);
    double computeArea();
    void expand(int factor);
    void display();
    //~Circle() {}
    double get_rad() const;
private:
    double radius;
};

#endif /* Circle_hpp */
