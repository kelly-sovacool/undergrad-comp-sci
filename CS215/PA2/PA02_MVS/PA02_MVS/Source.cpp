/*/
CS215-004
Program Assignment 02
Purpose: Simulate a game called Nim, in which two players (the user and the computer)
remove marbles from a pile until there are none left. The player to remove the last marble loses. 
Date: 11 Oct. 2015
Author: Kelly Sovacool
/*/
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

void pause_215(bool have_newline) {
	// Purpose: pause the program until the user enters a newline character
	// Description: if a newline from the user's previous input is still in the pipe, ignore it.
		// Otherwise, prompt the user to press the return key.
	// Input: boolean (true if user entered newline char, false otherwise)
	// Output: void
	if (have_newline) {
		// Ignore the newline after the user's previous input.
		cin.ignore(256, '\n');
	}
	// Prompt for the user to press ENTER, then wait for a newline.
	cout << endl << "Press ENTER to continue." << endl;
	cin.ignore(256, '\n');
}

bool isPower2(int num) {
	// Purpose: check if a number is a power of two.
	// Description: Divide the input by two until an odd number or 2 is reached.
		// If odd number, return false. If 2, return true.
	// Input: size of the pile (integer)
	// Output: boolean (true if input is a power of two, else false)
	bool return_val;
	if (num % 2 != 0) { // if number is odd
		return_val = false; // not a power of two
	}
	else if (num / 2 == 1) { // if number is two
		return_val = true; // is a power of two
	}
	else { // otherwise:
		int half_num = num / 2; // divide by two
		return_val = isPower2(half_num); // and check if half the number is a power of two
	}
	return return_val;
}

void comp_turn(int& pile) {
	// Purpose: determine how many marbles the computer will take and update the pile
	// Description: If the pile size is a power of 2 minus 1, take a random amount between
		// 1 and half the pile size. Otherwise, take enough marbles to make the pile size
		// a power of 2 minus 1. This ensures that if the computer is the first player,
		// it will always win.
	// Input: size of the pile (integer)
	// Output: void (updates pile size via call by reference)
	int take_amt;
	// check if pile size is a power of two minus one
	bool isPowerLess1 = isPower2(pile + 1);
	if (isPowerLess1) {
		if (pile != 3) {
			// take at least one but less than half the pile
			int half_pile = pile / 2;
			// generate random number between one and half the pile
			srand(time(0));
			take_amt = rand() % (half_pile - 1) + 1;
		}
		else { // pile size of 3 is special case that messses up rand expression above
			take_amt = 1; // means computer will lose
		}
		pile = pile - take_amt;
	}
	else {
		// remove enough to make the pile a power of two minus 1
		int pile_copy = pile;
		while (!isPower2(pile_copy + 1)) {
			pile_copy--;
		}
		take_amt = pile - pile_copy;
		pile = pile_copy;
	}
	cout << "The computer removes " << take_amt << endl;
}

void human_turn(int& pile) {
	// Purpose: determine how many marbles the player will take and update the pile
	// Description: Get the amount of marbles the player will take from standard input.
		// Continuously ask for input until it's a positive integer less than half the pile size.
	// Input: size of the pile (integer)
	// Output: void (updates the pile size via call by reference)
	bool isValidAmt = false;
	int marble_amt = 0;
	while (!isValidAmt) { // input validation for human player's move
		cout << "How many marbles would you like to remove? ";
		cin >> marble_amt;
		if (cin.fail()) { // if non-integer entered
			cin.clear();
			string non_int;
			cin >> non_int;
			cout << "Invalid amount. Must be an integer." << endl;
		}
		else if (marble_amt > pile / 2) { // if number greater than half the pile entered
			cout << "Invalid amount. Must be no more than half the remaining marbles." << endl;
		}
		else if (marble_amt < 1) { // if number less than 1 entered
			cout << "Invalid amount. Must be no less than 1 marble." << endl;
		}
		else
			isValidAmt = true;
	}
	pile = pile - marble_amt; // update the pile
}

int main() {
	int max_pile_size = 0;
	bool isValidSize = false;
	while (!isValidSize) { // input validation for max pile size
		cout << "Welcome to the game of Nim." << endl;
		cout << "To start, please enter a number greater than 10 to serve as the max range of the pile size." << endl;
		cin >> max_pile_size;
		if (cin.fail()) {
			cin.clear();
			string non_int;
			cin >> non_int;
			cout << "Invalid max pile size: Must be an integer." << endl;
		}
		else if (max_pile_size < 10) {
			cout << "Invalid max pile size: Too small." << endl;
		}
		else {
			isValidSize = true;
		}
	}

	// generate random int for pile size
	srand(time(0));
	int pile_size = rand() % (max_pile_size - 9) + 10;
	// randomly select which player goes first
	int player = rand() % 2;
	while (pile_size > 1) { // take marbles until 1 left
		cout << "The size of the pile is " << pile_size << endl;
		if (player == 0) {
			comp_turn(pile_size); // computer's turn
			player++; // player's turn is next
		}
		else {
			human_turn(pile_size); // player's turn
			player--; // computer's turn isnext
		}
	}

	// end of game
	if (player == 0) { // if player took the second to last marble
		cout << "The computer removes the last marble." << endl;
		cout << "You win!" << endl; // player wins
	}
	else { // if computer took the second to last marble
		cout << "You remove the last marble." << endl;
		cout << "You lose!" << endl; // computer wins
	}
	cout << "Thank you for playing this game." << endl;
	pause_215(true);
	return 0;
}
