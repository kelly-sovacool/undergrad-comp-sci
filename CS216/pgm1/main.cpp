/*/
 * CS216
 * Program 1
 * 07 Feb. 2016
 * Kelly Sovacool
 */

#include <iostream>
#include "IntSequence.h"
using namespace std;

int main() {
	IntSequence seqarray;
	bool wantsInput = true;
	while (wantsInput) {
		// print main menu
		cout << "1. Read" << endl;
		cout << "2. Print" << endl;
		cout << "3. Sort" << endl;
		cout << "4. Shuffle" << endl;
		cout << "5. Search" << endl;
		cout << "6. Quit" << endl;
		cout << "Option: ";
		int input;
		cin >> input;
		if (input==1) {
			bool wantsRead = true;
			while (wantsRead) {
				cout << "Enter the next element ('q' to quit): ";
				int num;
				cin >> num;
				if (cin.fail()) { // if string entered
					cin.clear();
					string non_int;
					cin >> non_int;
					if (non_int == "q")
						wantsRead = false;
					else
						cout << "Invalid input." << endl;
				}
				else
					seqarray.insert(num);
			}
		}
		else if (input==2) {
			cout << "Sequence:"; 
			seqarray.print();
		}
		else if (input==3) {
			// print sort submenu
			cout << "1. Insertion Sort" << endl;
			cout << "2. Selection Sort" << endl;
			cout << "3. Bubble Sort" << endl;
			cout << "4. Quit" << endl;
			int sort_input;
			cout << "Option: ";
			cin >> sort_input;
			if (sort_input==1) {
				cout << "===Insertion Sort==============================================";
				seqarray.insertion_sort();
			}
			else if (sort_input==2) {
				cout << "===Selection Sort==============================================";
				seqarray.selection_sort();
			}
			else if (sort_input==3) {
				cout << "===Bubble Sort==============================================";
				seqarray.bubble_sort();
			}
			else if (sort_input != 4) {
				if (cin.fail()) { // clear the pipe if string entered
					cin.clear();
					string non_int;
					cin >> non_int;
				}
				cout << "Invalid option!" << endl;
			}
		}
		else if (input==4) { // shuffle
			seqarray.shuffle();
		}
		else if (input==5) { // search
			// print search submenu
			cout << "1. Sequential Search" << endl;
			cout << "2. Binary Search" << endl;
			cout << "3. Quit" << endl;
			int srch_input;
			cout << "Option: ";
			cin >> srch_input;
			cout << "Enter the key to find: ";
			int key;
			cin >> key;
			cout << "Sequence:";
			seqarray.print();
			if (srch_input==1) {
				int pos = seqarray.sequential_search(key);
				if (pos > -1)
					cout << "Key found at index " << pos << endl;
				else
					cout << "Key not found." << endl;
			}
			else if (srch_input==2) {
				int pos = seqarray.binary_search(key);
				if (pos > -1)
					cout << "Key found at index " << pos << endl;
				else
					cout << "Key not found." << endl;
			}
			else if (srch_input!=3) {
				if (cin.fail()) { // clear pipe if string entered
					cin.clear();
					string non_int;
					cin >> non_int;
				}
				cout << "Invalid Option!" << endl;
			}
		}
		else if (input==6) { // quit
			cout << "Thank you for using the program." << endl;
			wantsInput = false;
		}
		else {// invalid input
			if (cin.fail()) { // if string entered
				cin.clear(); // clear the pipe
				string non_int; 
				cin >> non_int;
			}
			cout << "Invalid option!" << endl;
		}
		cout << "=================================================" << endl;
	}
}
