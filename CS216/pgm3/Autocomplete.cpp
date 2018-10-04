// CS216-002
// Pgm 3
// Kelly Sovacool

#include "Autocomplete.h"
#include <vector>
#include <string>
#include "Term.h"

Autocomplete::Autocomplete(){}

void Autocomplete::insert(Term newterm) {
	// add new term to end of terms vector
	terms.push_back(newterm);
}
void Autocomplete::term_sort(string order) {
	// sort terms vector by lexicographic or weight order
	// via bubble sort algorithm
	if (order == "lex") { // lexicographic order specified
		bool must_swap = true;
		while(must_swap) {
			must_swap = false;
			for (int i = 0; i < terms.size()-1; i++) {
				if (terms[i].compareTo(terms[i+1])==-1) {
					Term temp_term = Term(terms[i].query, terms[i].weight);
					terms[i] = terms[i+1];
					terms[i+1] = temp_term;
					must_swap = true;
				}
			}
		}
	}
	else if (order == "weight") { // weight order specified
		bool must_swap = true;
		while(must_swap) {
			must_swap = false;
			for (int i = 0; i < terms.size()-1; i++) {
				if (terms[i].byReverseWeightOrder(terms[i+1])==-1) {
					Term temp_term = Term(terms[i].query, terms[i].weight);
					terms[i] = terms[i+1];
					terms[i+1] = temp_term;
					must_swap = true;
				}
			}
		}
	}
}
vector<Term> Autocomplete::allMatches(string prefix) {
	// given prefix, return vector of terms starting with prefix
	// sorted by descending order of weight
	term_sort("lex"); // must begin with vector in lexicographic order
	int first = 0;
	int last = terms.size()-1;
	// Search finds first and last indices of matching terms in master vector
	// and modifies first/last via call by reference
	Search(prefix, first, last);
	vector<Term> matches;
	// add matching terms to the return vector
	for (int i=first; i<=last+1; i++)
		matches.push_back(terms[i]);
	// sort matching terms by weight
	term_sort("weight");
	return matches;
}
void Autocomplete::Search(string key, int& first, int& last) {
	// find a match
	int match = BS_helper(key, first, last);
	// find first match
	bool first_found = false;
	int j = match;
	while (!first_found && j >= 0) {
		// iterate over left half of terms vector until first match found
		if (terms[j].query.substr(0,key.length()) != key) {
			// set first to index of first match
			first = j+1; // assumes binary search returned correct match
			first_found = true;
		}
		j++;
	}
	// find last match
	bool last_found = false;
	int k = match;
	while (!last_found && k < terms.size()) {
		if (terms[k].query.substr(0,key.length()) != key) {
			last = k-1; // set last to index of last match
			last_found = true;
		}
		k++;
	}
}
int Autocomplete::BS_helper(string key, int left, int right) {
	int indx;
	if (left > right) // key not in terms
		indx = -1;
	else {
		int middle = (left + right) / 2;
		// continue search in left half
		if (terms[middle].query.substr(0,key.length()) > key)
			indx = BS_helper(key, left, middle-1);
		// continue search in right half
		else if (terms[middle].query.substr(0,key.length()) < key)
			indx = BS_helper(key, middle+1, right);
		// found it
		else
			indx = middle;
	}
	return indx;
}
void Autocomplete::print() {
	for (int i = 0; i < terms.size(); i++)
		terms[i].print();
}
