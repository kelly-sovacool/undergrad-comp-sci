
#ifndef Shape_h
#define Shape_h
const double PI = 3.14159265359;
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
