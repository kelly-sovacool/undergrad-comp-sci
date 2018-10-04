// CS216
// Program 2
// 29 Feb. 2016
// Kelly Sovacool

#include <iostream>
#include <vector>
#include <cmath>
#include "Scheduler.h"
using namespace std;

bool isPower2(int num) { // check if number is a power of 2
	bool ret_val;
	if (num == 1) // special case of 1
		ret_val = true;
	else if (num == 2) // number is 2
		ret_val = true;
	else if (num % 2 != 0) // odd number
		ret_val = false;
	else { // not sure yet
		int sqrt_num = sqrt(num);
		ret_val = isPower2(sqrt_num);
	}
	return ret_val;
}

int main() {
	
	bool wantsInput = true;
	while (wantsInput) {
		int num_teams;
		cout << "Please input the number of teams to be scheduled (q to quit): ";
		cin >> num_teams;
		if (cin.fail()) { // if string entered
			cin.clear();
			string str;
			cin >> str;
			if (str == "q" || str == "Q") {
				cout << "Goodbye" << endl;
				wantsInput = false;
			}
			else
				cout << "Invalid input!" << endl;
		}
		else if (!isPower2(num_teams))
			cout << "The number of teams must be a power of 2." << endl;
		else if (num_teams > 512) 
			cout << "The maximum number of teams is 512." << endl;
		else {
			Scheduler schedule(num_teams);
			schedule.generateSchedule();
			schedule.print();
			schedule.~Scheduler();
		}
	}
	return 0;
}
