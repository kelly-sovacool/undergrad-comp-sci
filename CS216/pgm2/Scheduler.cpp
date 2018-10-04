// CS216-00s
// Pgm 2
// Kelly Sovacool
#include <cmath>
#include <iostream>
#include "Scheduler.h"
#include <vector>
using namespace std;

Scheduler::Scheduler() {
	teams = 0;
	Arrange = new int*[teams];
}
Scheduler::Scheduler(int ini_teams) {
	teams = ini_teams;
	Arrange = new int*[teams];
	for (int i=0; i< teams; i++) {
		Arrange[i] = new int[teams]; // allocate necessary memory 
		Arrange[0][i] = i+1; // set first row of teams
	}
}
Scheduler::~Scheduler() { 
	for (int i=0; i < teams; i++)
		delete[] Arrange[i];
	delete[] Arrange; 
}
void Scheduler::generateSchedule() {
	int iteration = 1;
	helper(teams, iteration);
}
void Scheduler::helper(int blocksize,int iter) {
	// reverse order of teams in each block
	for (int i=0; i<=(teams-blocksize); i += blocksize) {
		vector<int> rev(blocksize);
		// create reversed block
		for (int k=(i+blocksize-1); k>=i; k--)
			rev.push_back(Arrange[iter-1][k]);
		// new block in Arrange with reversed block
		for (int m=i; m<(i+blocksize); m++)
			Arrange[iter][m] = rev[m-i];
	}	
	cout << "reversed blocks for iter=" << iter << endl;
	// if it's possible to swap more teams...
	if (blocksize > 2) {
		int new_iter = iter + 1;
		cout << "calling helper in iter=" << new_iter << endl;
		helper(sqrt(blocksize), new_iter); // do it again
	}
}	
void Scheduler::print() {
	cout << "The schedule for " << teams << " teams is:" << endl;
	for (int j=0; j<teams; j++) {
		for (int k=0; k<teams; k++)
			cout << Arrange[j][k];
	}
}

