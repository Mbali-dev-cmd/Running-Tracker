#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {

	double distance, totalMinutes, pace;
	int hours, minutes, seconds;

	cout << "How many km did you run today?" << endl;
	cin >> distance;

	cout << "How many hours did it take you to run that distance?" << endl; // we ask the user separate questions to make it easier for them to input the time in hours, minutes, and seconds.
	cin >> hours;

	cout << "How many minutes did it take you to run that distance?" << endl;
	cin >> minutes;

	cout << "How many seconds did it take you to run that distance?" << endl;
	cin >> seconds;

	totalMinutes = (hours * 60) + minutes + (seconds / 60.0);

	cout << "You ran " << distance << "km in " << totalMinutes << " minutes" << endl;

	pace = totalMinutes / distance;
 
	int paceMinutes = static_cast<int>(pace); // Get the whole number of minutes only 
	double paceSeconds = (pace - paceMinutes) * 60;

	cout << "Your pace was " << paceMinutes << ":" << setw(2) << setfill('0') << (int)paceSeconds << " min/km" << endl; // we use the setw and setfill to format the seconds to always show two digits



	return 0;


}
