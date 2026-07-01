import csv # let's python read and write csv files 
from datetime import date # I t gives us the current date 


print("Welcome to your running tracker ! ") 
print("Let's log todays run ! ") 

distance = float(input("How many km did you run today ? : "))

hours = int(input("How many hours did you run ? : "))

minutes = int(input("How many minutes did you run? : "))

seconds = int(input("How many seconds did you run ? : "))

print("You ran ", distance,"km", hours,"h", minutes,"m", seconds,"s" )

today = date.today() # it gives us the current date 
print("Todays date is :" , today) 

with open("runs.csv" , "a", newline="" ) as file: # it opens the file in append mode
    writer = csv.writer(file) # it creates a place to write in the file
    writer.writerow( [today, distance, hours, minutes, seconds]) # this write the data in the file that we opened which is runs.csv
    print("Your run has been saved !") # this confirms that the data has been saved in csv file 
