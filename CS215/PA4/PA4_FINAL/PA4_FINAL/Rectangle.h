
#include "Shape.h"
#ifndef Rectangle_h
#define Rectangle_h

class Rectangle : public Shape
{
public:
	Rectangle(double len, double wid);
	double computeArea();
	void expand(int factor);
	void display();
	~Rectangle() {}
	double get_len() const;
	double get_wid() const;
private:
	double length, width;
};

#endif /* Rectangle_hpp */
