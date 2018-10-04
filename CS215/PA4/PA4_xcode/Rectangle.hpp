//
//  Rectangle.hpp
//  PA04_xcode
//
//  Created by Kelly Sovacool on 11/30/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//
#include "Shape.hpp"
#ifndef Rectangle_hpp
#define Rectangle_hpp

class Rectangle : public Shape
{
public:
    Rectangle(double len, double wid);
    double computeArea();
    void expand(int factor);
    void display();
    ~Rectangle();
    double get_len() const;
    double get_wid() const;
private:
    double length, width;
};

#endif /* Rectangle_hpp */
