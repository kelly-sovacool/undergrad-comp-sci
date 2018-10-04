//
//  main.cpp
//  PA03_draft1
//
//  Created by Kelly Sovacool on 11/7/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#include <iostream>
#include <string>
#include "GameList.hpp"
#include "Game.hpp"
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

string get_name() {
    /***
    Purpose: get game name from the user
    Description: ignore any previous newlines, 
     get entire line from the user, 
     return the line as a string
    Input: None (gets input from keyboard)
    Output: string
    ***/
    cin.ignore(256, '\n');
    string name;
    cout << "Please enter the name of the game: ";
    getline(cin, name);
    return name;
}

int get_count() {
    /***
    Purpose: get valid count from the user
    Description: continuously get input from the user 
     until user inputs an int greater than or equal to zero
    Input: None (gets input from keyboard)
    Output: int
    ***/
    int count;
    bool isValidCount = false;
    while (!isValidCount) { // get count until it's valid
        cout << "Copies: ";
        cin >> count;
        if (cin.fail()) { // if user enters a string
            cin.clear();
            string non_int;
            cin >> non_int;
            cout << "Invalid input: must be an integer." << endl;
        }
        else if (count < 0) // if input out of range
            cout << "Invalid input: must be an integer greater or equal to zero." << endl;
        else
            isValidCount = true; // exit input validation loop
    }
    return count;
}

float get_price() {
    /***
    Purpose: get valid price from the user
    Description: coninuously get input from the user
     until user inputs a float greater than zero
    Input: None (gets input from keyboard)
    Output: float greater than zero
    ***/
    float price; bool isValidPrice = false;
    while (!isValidPrice) { // get price until it's valid
        cout << "Price: $";
        cin >> price;
        if (cin.fail()) { // if user enters a string
            cin.clear();
            string non_int;
            cin >> non_int;
            cout << "Invalid price: must be a floating-point number." << endl;
        }
        else if (price <= 0) // if input out of range
            cout << "Invalid price: must be a float greater than zero." << endl;
        else
            isValidPrice = true; // exit input validation loop
    }
    return price;
}

float get_score() {
    /***
    Purpose: get valid score from the user
    Description: continuously get input from the user
     until it's a score in the range [0.0, 10.0]
    Input: None (gets input from the keyboard)
    Output: float in range [0.0, 10.0]
    ***/
    float score; bool isValidScore = false;
    while (!isValidScore) { // get score until it's valid
        cout << "Score: ";
        cin >> score;
        if (cin.fail()) { // if user enters a string
            cin.clear();
            string non_int;
            cin >> non_int;
            cout << "Invalid score: must be a floating-point number." << endl;
        }
        else if (score < 0 || score > 10) // if score out of range
            cout << "Invalid score: must be a float in the range [0.0, 10.0]." << endl;
        else
            isValidScore = true; // exit input validation loop
    }
    return score;
}

int main() {
    cout << "This application stores a list	of board games in stock	for	Wildcats Store" << endl;
    GameList stock;
    bool wantsInput = true;
    while (wantsInput) { // only ends when user quits
        bool isValid = false;
        int input;
        while (!isValid) { // get valid menu choice from the user
            cout << "Select from:" << endl;
            cout << "1. Insert a game record"  << endl;
            cout << "2. Delete a game record" << endl;
            cout << "3. Print the game list" << endl;
            cout << "4. Search the game list" << endl;
            cout << "5. Quit" << endl;
            cin >> input;
            if (cin.fail()) { // if user enters a string
                cin.clear();
                string non_int;
                cin >> non_int;
                cout << "Invalid input: must be an integer." << endl;
            }
            else if (input < 1 || input > 5) // if input out of range
                cout << "Invalid input: must be an integer in range 1 to 5." << endl;
            else
                isValid = true; // exit input validation loop
        }
        if (input == 1) { // insert
            string name = get_name();
            int count = get_count();
            float price = get_price();
            float score = get_score();
            stock.Insert(name, count, price, score);
        }
        else if (input == 2) // delete
            stock.Delete(get_name());
        else if (input == 3) // print
            stock.Print();
        else if (input == 4) { // search
            string key;
            cout << "Please enter the key from the game name you want to search for: ";
            cin >> key;
            stock.Search(key);
        }
        else if (input == 5) {
            cout << "Thank you for using this program." << endl;
            pause_215(true);
            wantsInput = false; // exit outer while loop
        }
    }
    return 0;
}
