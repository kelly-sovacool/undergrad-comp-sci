/**
Class: CS215-004
Project: Pgm 4
Date: 02 Dec. 2015
Author: Kelly Sovacool
**/
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "Shape.h"
#include "Circle.h"
#include "Rectangle.h"
#include "Cuboid.h"
#include "Sphere.h"
#include "Cylinder.h"
using namespace std;

void pause_215(bool have_newline)
{
    if (have_newline) {
        // Ignore the newline after the user's previous input.
        cin.ignore(256, '\n');
    }// Prompt for the user to press ENTER, then wait for a newline.
    cout << endl << "Press ENTER to continue." << endl;
    cin.ignore(256, '\n');
}
void maxSurfaceArea(vector<Shape*> vect) {
	// hold shape with maximum surface area
    Shape* maxSA_shape = vect[0];
    // compare each shape in vector to current max
    for (int i=0; i<vect.size(); i++) {
    	// if shape is greater than max, it becomes the new max
        if ( (vect[i]->computeArea()) > (maxSA_shape->computeArea()) )
            maxSA_shape = vect[i];
    }
    cout << "The shape with the largest surface area is:" << endl;
    maxSA_shape->display();
}
void expandAll(vector<Shape*> vect, int factor) {
	// if factor is greater than zero
    if (factor > 0) {
    	// expand all shapes by the factor
        for (int i=0; i<vect.size(); i++)
            vect[i]->expand(factor);
    }
    // otherwise, output error message
    else
        cout << "Invalid factor; must be integer greater than zero." << endl;
}
void displayAll(vector<Shape*> vect) {
	// call display function for each shape in vector
    for (int i=0; i< vect.size(); i++)
        vect[i]->display();
}
int main() {
    vector<Shape*> shapes;
    string filename;
    ifstream infile;
    bool open_failed = true;
    int numtries = 1;
    // give the user 3 tries to enter valid filename
    while (open_failed && numtries < 4)
    {
        cout << "Type the filename: ";
		cin >> filename;
        infile.open(filename.c_str());
        open_failed = (infile.fail());
        if (open_failed)
        { // output error message if open failed
            cout << "Open " << filename << " failed." << endl;
            cout << "(Try # " << numtries << " of 3)" << endl;
            pause_215(true);
        }
        numtries++;
    }
    // get shapes until end of file reached
    while (!infile.eof())
    {
        string name;
        cin >> name;
        if (name == "Rectangle") { // add Rectangle ptr to vector
            double len;
            double wid;
            cin >> len >> wid;
            shapes.push_back(new Rectangle(len, wid));
        }
        else if (name == "Cuboid") { // add Cuboid ptr to vector
            double len;
            double wid;
            double hei;
            cin >> len >> wid >> hei;
            shapes.push_back(new Cuboid(len, wid, hei));
        }
        else if (name == "Circle") { // add Circle ptr to vector
            double rad;
            cin >> rad;
            shapes.push_back(new Circle(rad));
        }
        else if (name == "Sphere") { // add Sphere ptr to vector
            double rad;
            cin >> rad;
            shapes.push_back(new Sphere(rad));
        }
        else if (name == "Cylinder") { // add Cylinder ptr to vector
            double rad;
            double hei;
            cin >> rad >> hei;
            shapes.push_back(new Cylinder(rad, hei));
        }
    }
    infile.close();
    
    displayAll(shapes); // derived-class display fcns call compute_area/volume fcns
    maxSurfaceArea(shapes);
    int factor;
    cout << "Enter a factor (positive integer) to expand all shapes by: " << endl;
    cin >> factor;
    expandAll(shapes, factor);
    displayAll(shapes);
    maxSurfaceArea(shapes);
    
    // deallocate memory
    for (int k=0; k<shapes.size(); k++)
        delete shapes[k];
    return 0;
}
