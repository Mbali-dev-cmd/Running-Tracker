import json # we let python read and write json files 
import csv # we let python read and write csv files

total_distance = 0.0 # it is a variable that will store the total distance run by the user
total_pace = 0.0 # it is a variable that will store the total pace of the user / keeps adding each run's pace 
run_count = 0 # it is a variable that will store the total number of runs / count how many runs you've done 
longest_run = 0.0 # it is a variable that will store the longest run of the user 

run_history = [] # this is an empty box that we will fill with one entry per run 

with open("runs.csv", "r", newline="") as file : # it opens the file in read mode only the "r" stand for read mode 
    reader = csv.reader(file) # it creates a place to read the file
    for row in reader: # it reads the file line by line
        print(row) # it prints the data in the file that we opened which is runs.csv
        total_distance = total_distance + float(row[1]) # it adds the distance run by the user to total_distance variable 
    
        run_minutes = (int(row[2]) * 60) + int(row[3]) + (int(row[4]) / 60.0 )
        pace = run_minutes / float(row[1]) # it calculate the pace of the user by dividing the total time by the distance run
        total_pace = total_pace + pace # it adds the pace of the user to total_pace vairable
        run_count = run_count + 1 # it adds 1 to the run_count variable to keep track of how many runs you've done 

        run_history.append({
                           "date": row[0],
                           "distance": float(row[1]),
                           "hours": int(row[2]),
                           "minutes": int(row[3]),
                           "seconds": int(row[4]),
                           "pace": round(pace, 2)
                           })

        if float(row[1]) > longest_run : # it checks if the distance run by the user is greater than the longest run
            longest_run = float(row[1]) # it updates the longest run variable with the new longest run

print("Total distance run is ", total_distance, "km") # it prints the total distance

print("The longest run is ", longest_run, "km") # it prints the longest run of the user 

average_pace = total_pace / run_count # it calculate the average pace of the user 
print( "Your average pace is ", average_pace, "min/km") # it prints the average pace of the user 

total_distance = round(total_distance, 2) # it rounds the total distance to 2 decimal places 
average_pace =round(average_pace, 2) 
longest_run = round(longest_run, 2) 

run_stats = { #  it creates a dictionary to store the run stats 
            "total_distance" : total_distance,
            "average_pace" : average_pace,
            "longest_run" : longest_run,
            "total_runs" : run_count,
            "run_history" : run_history 
} 

print(run_stats) # it prints the run stats dictionary 

with open("run_stats.json", "w") as json_file: # it opens the file in write mode only the "w" stand for write mode 
    json.dump(run_stats, json_file, indent=4) # it writes the run stats dictionary to the json file