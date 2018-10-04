//
//  main.cpp
//  PA02_perfect_players
//
//  Created by Kelly Sovacool on 9/29/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void pause_215(bool have_newline) {
    // Purpose: pause the program until the user enters a newline character
    // Description:
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
    // Description:
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
    // Description:
    // Input: size of the pile (integer)
    // Output: void (updates pile size via call by reference)
    int take_amt;
    // check if pile size is a power of two minus one
    bool isPowerLess1 = isPower2(pile+1);

    if (isPowerLess1) {
        // take at least one but less than half the pile
        if (pile == 3) { // special case that messes up rand fcn
            take_amt = 1; // have to take 1, no other option
        }
        else {
            int half_pile = pile / 2;
            // generate random number between one and half the pile
            srand(time(0));
            take_amt = rand()%(half_pile-1) + 1;
        }
        pile = pile - take_amt;
    }
    else {
        // remove enough to make the pile a power of two minus 1
        int pile_copy = pile;
        while (not isPower2(pile_copy+1)) {
            pile_copy--;
        }
        take_amt = pile - pile_copy;
        pile = pile_copy;
    }
    cout << "The computer removes " << take_amt << endl;
}

int main() {
    int max_pile_size = 0;
    bool isValidSize = false;
    while (not isValidSize) { // input validation for max pile size
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
    int pile_size = rand()%(max_pile_size-9)+10;
    // randomly select which player goes first
    srand(time(0));
    int player = rand()%2;
    while (pile_size > 1) { // take marbles until 1 left
        cout << "The size of the pile is " << pile_size << endl;
        if (player == 0) {
            cout << "Comp. A:" << endl;
            comp_turn(pile_size); // computer's turn
            player++; // player's turn is next
        }
        else {
            cout << "Comp. B:" << endl;
            comp_turn(pile_size); // player's turn
            player--; // computer's turn isnext
        }
    }
    
    // end of game
    if (player == 0) { // if player took the second to last marble
        cout << "Comp. A removes the last marble." << endl;
        cout << "Comp. B wins!" << endl; // player wins
    }
    else { // if computer took the second to last marble
        cout << "Comp. B removes the last marble." << endl;
        cout << "Comp. A wins!" << endl; // computer wins
    }
    cout << "Thank you for playing this game." << endl;
    //pause_215(true);
    return 0;
}
