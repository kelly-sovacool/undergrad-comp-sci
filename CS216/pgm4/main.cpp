// CS216-002
// Pgm 3
// Kelly Sovacool

#include "Term.h"
#include "Autocomplete.h"
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main(int argc, char *argv[]) {
	if (argc != 3) // display correct usage if number of args incorrect
		cout << "usage: " << argv[0] << " <filename> <int>" << endl;
	else {
		ifstream infile;
		string filename = argv[1];	
		infile.open(filename.c_str());
		istringstream iss(argv[2]);
		int k; // convert arg (number of terms to display) to int k
		if (infile.fail()) // quit if open failed
			cout << "Open" << filename << " failed." << endl;
		else if (iss >> k) { // only proceed if int conversion successful
			Autocomplete terms;
			// get terms until end of file reached
			cout << "Getting input from " << filename << endl;
			while (!infile.eof()) {
				string q;
				long w;
				cin >> w >> q;
				terms.insert(Term(q,w));
				cout << "inserted Term weight = " << w << "; query = " << q << endl;
			}	
			infile.close();
			
			// read queries until user quits
			bool wantsInput = true;
			while (wantsInput) {
				string key;
				cout << "Please input the search query (type exit to quit):" << endl;
				cin >> key;
				if (key == "exit") {
					cout << "Goodbye!" << endl;
					wantsInput = false;
				}
				else {
					vector<Term> matches = terms.allMatches(key);
					int stop;
					// print number of matches specified by user
					if (matches.size() >= k)
						stop = k;
					// print all matches
					else
						stop = matches.size();
					for (int i = 0; i < stop; i++)
						matches[i].print();
					cout << "__________" << endl; // formatting
				}
			}
		}
	}
	return 0;
}
