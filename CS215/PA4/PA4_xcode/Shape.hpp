//
//  Shape.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#ifndef Shape_hpp
#define Shape_hpp
const double PI = 3.14159265359;
#include <stdio.h>

class Shape
{
public:
    Shape() {}
    virtual double computeArea()=0;
    virtual void expand(int factor)=0;
    virtual void display()=0;
    virtual ~Shape() {}
    //other member functions if you want to add;
};
#endif /* Shape_hpp */
