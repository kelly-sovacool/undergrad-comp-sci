// CS216-002
// Pgm 2
// Kelly Sovacool
#ifndef SCHEDULER_H
#define SCHEDULER_H

class Scheduler
{
	public:
		Scheduler(); // default constructor
		Scheduler(int ini_teams); // constructor
		// generate schedule for n teams
		void generateSchedule();
		// display table content of schedule
		void print();
		// destructor
		~Scheduler();
		// recursive helper function for generateSchedule
		void helper(int blocksize, int iter);
	private:
		int teams; // number of teams
		int** Arrange; // 2D vector

};

#endif
