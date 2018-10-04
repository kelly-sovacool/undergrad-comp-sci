
#include "Shape.h"
#ifndef Circle_h
#define Circle_h
class Circle : public Shape
{
public:
    Circle(double r);
    double computeArea();
    void expand(int factor);
    void display();
    ~Circle() {}
    double get_rad() const;
private:
    double radius;
};

#endif /* Circle_hpp */
