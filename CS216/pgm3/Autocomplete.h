// CS216-002
// Pgm 3
// Kelly Sovacool

#include <vector>
#include <string>
#include "Term.h"
using namespace std;
#ifndef AUTOCOMPLETE_H
#define AUTOCOMPLETE_H

class Autocomplete
{
	public:
		Autocomplete(); // default constructor
		
		// insert new term to sequence
		void insert(Term newterm);

		// sort terms by lexicographic or weight order
		void term_sort(string order);

		// return all terms starting with prefix
		// in descending order of weight
		vector<Term> allMatches(string prefix);

		// first; index of 1st query that equals search key
		// 	or -1 if no matching key
		// last: index of last query that equals search key
		// 	or -1 if no matching key
		void Search(string key, int& first, int& last);
		
		// return index of search key with binary search algorithm
		int BS_helper(string key, int left, int right);

		// display all terms
		void print();

			
	private:
		// dynamic array = sequence of Term objects
		vector<Term> terms;

};

#endif
