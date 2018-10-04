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
		void term_sort();
		// compare terms in descending order by weight
		int byReverseWeightOrder(Term that);
		
		// compare terms by lexicographic order
		int compareTo(Term that);

		// compare terms in lexicographic order using only
		// the first r characters of each query
		int byPrefixOrder(Term that, int r);
		
		// displays term in format:
		// weight '\t' query
		void print();
		
		long get_weight(); // return weight

		string get_query(); // return query

		friend class Autocomplete;
	
	private:
		string query;
		long weight;

};

#endif
