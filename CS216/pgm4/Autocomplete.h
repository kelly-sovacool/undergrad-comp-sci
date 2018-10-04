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
		
		// insert new term to binary tree
		// maintains lexicographic order
		void insert(Term newterm);

		// check whether tree is balanced
		bool isBalanced();

		// balance the tree
		void balance();

		// help balance function rearrange nodes
		void rearrange(Term node);

		// return k terms that match the search key
		// in descending order of weight
		Terms* allMatches(string prefix);

	private:
		Term* root; // pointer to root of tree of Terms
		int count_total; // total number of terms in tree
		int count_left; // number of terms in root's left branch
};

#endif
