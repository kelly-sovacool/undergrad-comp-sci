// CS216-002
// Pgm 3
// Kelly Sovacool

#include "Term.h"
#include <string>
#include <iostream>
using namespace std;

Term::Term() {}
Term::Term(string query, long weight) {
	query = query;
	weight = weight;
	left = NULL;
	right = NULL;
}
// compare by descending order of weight
int Term::byReverseWeightOrder(Term that) {
	int retval;
	if (weight > that.get_weight())
		retval = 1;
	if (weight < that.get_weight())
		retval = -1;
	else
		retval = 0;
	return retval;
}
// compare queries by lexicographic order
int Term::compareTo(Term that) {
	int retval;
	if (query > that.get_query())
		retval = 1;
	if (query < that.get_query())
		retval = -1;
	else
		retval = 0;
	return retval;
}
// compare prefixes of queries by lexicographic order
int Term::byPrefixOrder(Term that, int r) {
	int retval;
	string query_sub = query.substr(0,r);
	string that_sub = that.get_query().substr(0,r);
	if (query_sub > that_sub)
		retval = 1;
	if (query_sub < that_sub)
		retval = -1;
	else
		retval = 0;
	return retval;
}
// output term information in specifed format
void Term::print() {
	cout << weight << '\t' << query << endl;
}
long Term::get_weight() {
	return weight;
}
string Term::get_query() {
	return query;
}
