// CS216-002
// Pgm 3
// Kelly Sovacool

#include <string>
using namespace std;

#ifndef TERM_H
#define TERM_H

class Term
{
	public:
		Term(); // default constructor
		Term(string query, long weight); // construct with query string & weight
		void print();
		
		long get_weight(); // return weight

		string get_query(); // return query

		friend class Autocomplete;
	
	private:
		string query;
		long weight;
		Term* left; // pointer to left branch, NULL if empty
		Term* right; // likewise for right branch
};

#endif
