//
//  Class: CS215
//  Project: Program Assignemnt 1
//  Date: 10 Sept. 2015
//  Purpose: Convert integers between 1 and 3,999 to Roman Numerals until the user enters -1
//  Author: Kelly Sovacool
//

#include <iostream>
#include <string>
using namespace std;

int main() {

    bool wantsInput = true; // sentinel to control loop: set to false when user enters -1
    while (wantsInput) { // continue getting integers and converting until user enters -1
        cout << "Integer-Roman Number Conversion Tool:" << endl;
        cout << "Enter -1 to quit the program." << endl;
        cout << "Please enter a positive integer less than 4,000 to convert: ";
        int pos_int; // the positive integer that the user inputs
        cin >> pos_int;
        string ones_digit; // roman numeral for ones digit
        string tens_digit; // roman numeral for tens digit
        string hund_digit; // roman numeral for hundreds digit
        string thou_digit; // roman numeral for thousands digit
        
        // if user didn't enter an integer
        if (cin.fail())
        {
            cout << "Invalid input. You must enter a positive integer." << endl;
            cin.clear(); // try again
            string dummy;
            cin >> dummy;
        }
        // check for integer between 1 and 3,999 (inclusive)
        else if (pos_int <-1 || pos_int == 0 || pos_int >= 4000)
        {
            cout << "Invalid input. Your number must be greater than 0 and less than 4,000." << endl;
        }
        // else if user enters negative one
        else if (pos_int == -1)
        {
            wantsInput = false; // set boolean sentinel to false to end while loop
        }
        else // only does conversion if input is valid
        {

            int iteration = 0; // keep track of which digit is being examined
            for (pos_int = pos_int; pos_int > 0; (pos_int = pos_int / 10)) // iterate over digits in integer
            {
                int curr_digit = pos_int % 10; // get the current digit
                if (curr_digit >= 1 and curr_digit <= 3)
                {
                    for (int i = 1; i <= curr_digit; i++)
                    {
                        if (iteration == 0) { // 1 to 3
                            ones_digit += "I";
                        }
                        else if (iteration == 1) { // 10s to 30s
                            tens_digit += "X";
                        }
                        else if (iteration == 2) { // 100s to 300s
                            hund_digit += "C";
                        }
                        else if (iteration == 3) { // 1000s to 3000s
                            thou_digit += "M";
                        }
                    }
                }
                else if (curr_digit == 4)
                {
                    if (iteration == 0) { // 4
                        ones_digit = "IV";
                    }
                    else if (iteration == 1) { // 40s
                        tens_digit = "XL";
                    }
                    else if (iteration == 2) { // 400s
                        hund_digit = "CD";
                    }
                }
                else if (curr_digit >= 5 and curr_digit <= 8)
                {
                    if (iteration == 0) { // 5 to 8
                        ones_digit = "V";
                        for (int i = 1; (i <= curr_digit % 5); i++) {
                            ones_digit += "I";
                        }
                    }
                    else if (iteration == 1) { // 50s to 80s
                        tens_digit = "L";
                        for (int i = 1; (i <= curr_digit % 5); i++) {
                            tens_digit += "X";
                        }
                    }
                    else if (iteration == 2) { // 500s to 800s
                        hund_digit = "D";
                        for (int i = 1; (i <= curr_digit % 5); i++) {
                            hund_digit += "C";
                        }
                    }
                }
                else if (curr_digit == 9)
                {
                    if (iteration == 0) { // 9
                        ones_digit = "IX";
                    }
                    else if (iteration == 1) { // 90s
                        tens_digit = "XC";
                    }
                    else if (iteration == 2) { // 900s
                        hund_digit = "CM";
                    }
                }
                
                iteration++; // increase counter keeping track of digit position
            }
            // concatenate digit variables to get full roman numeral
            string rom_num = thou_digit + hund_digit + tens_digit + ones_digit;
            cout << "The Roman Numeral is " << rom_num << endl;
        }
        
    } // end of outermost while loop (when user enters -1)
    cout << "Thank you for using Integer-Roman Number Conversion Tool." << endl;
    return 0;
            
}
