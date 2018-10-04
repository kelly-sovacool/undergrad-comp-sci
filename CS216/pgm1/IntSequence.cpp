#include "IntSequence.h"
#include <iostream>
#include <cstdlib>
using namespace std;

IntSequence::IntSequence() {
	capacity = INITIAL_CAPACITY;
	count = 0;
	seq = new int[INITIAL_CAPACITY];
}
IntSequence::IntSequence(int in_capacity) {
	capacity = in_capacity;
	count = 0;
	seq = new int(in_capacity);
}
void IntSequence::insert(int item) {
	if (count == capacity) { // allocate more memory if cap reached
		capacity *= 2;
		int* copy = new int[capacity];
		for (int i=0; i<count; i++)
			copy[i] = seq[i];
		delete[] seq;
		seq = copy;
	}
	seq[count] = item;
	count++;
}
void IntSequence::print() {
	if (count > 0) {
		cout << "\t";
		for (int i=0; i<count; i++)
			cout << seq[i] << " ";
	}
	else
		cout << "Array is empty.";
	cout << endl;
}
void IntSequence::selection_sort() {
	cout << "Sequence:"; print();
	int min_indx;
	for (int i=0; i < (count-1); i++) {
		min_indx = i;
		for (int j=(i+1); j<count; j++) {
			if (seq[j] < seq[min_indx])
				min_indx = j;
		}
		if (min_indx != i) {
			cout << "Min " << seq[min_indx];
			cout << ", swap with " << seq[i] << ": "; print();
			int tmp = seq[i];
			seq[i] = seq[min_indx];
			seq[min_indx] = tmp;
		}
	}
	cout << "Sequence:"; print();
}
void IntSequence::insertion_sort() {
	cout << endl;
	for (int i=0; i < count; i++) {
		int pos = i;
		while (pos > 0 && seq[pos] < seq[pos-1] ) {
			cout << "Insert: " << seq[pos];
			print();
			int tmp = seq[pos];
			seq[pos] = seq[pos-1];
			seq[pos-1] = tmp;
			pos--;
		}
	}
	cout << "Sequence:"; print();
}
void IntSequence::bubble_sort() {
	cout << endl << "Sequence:"; print();
	for (int i=1; i<count; i++) {
		cout << "Iteration " << i << ":";
		for (int j=0; j< (count-1); j++) {
			if (seq[j] > seq[j+1]) {
				int tmp = seq[j];
				seq[j] = seq[j+1];
				seq[j+1] = tmp;
			}
		}
		print();
	}
	cout << "Sequence:"; print();
}
void IntSequence::shuffle() {
	for (int i=(count-1); i>=1; i--) {
		int r = rand() % (i+1);
		int tmp = seq[r];
		seq[r] = seq[i];
		seq[i] = tmp;
	}
}
int IntSequence::sequential_search(int key) {
	int retval;
	bool keyFound = false;
	int i = 0;
	while (!keyFound && i<count) {
		if (seq[i] == key)
			keyFound = true;
		else
			i++;
	}
	if (keyFound)
		retval = i;
	else
		retval = -1;
	cout << i << " comparisons made." << endl;
	return retval;
}
int IntSequence::binary_search(int key) {
	int comps;
	int retval = bin_search_helper(key, 0, count-1, comps);
	cout << comps << " comparisons made." << endl;
	return retval;
}
IntSequence::~IntSequence() { 
	delete[] seq; 
}
int IntSequence::bin_search_helper(int key, int left, int right, int &comps) {
	comps++;
	int retval;
	if (left > right)
		retval = -1;
	else {
		int middle = (left + right) /2;
		if (seq[middle] > key)
			retval = bin_search_helper(key, left, middle-1, comps);
		else if (seq[middle] < key)
			retval = bin_search_helper(key, middle+1, right, comps);
		else
			retval = middle;
	}
	return retval;
}
