# imports
import csv

# open the file
with open("example.csv") as file:
	reader = csv.reader(file)
	# prep to store names of columns
	titleRow = reader.next()
   	#rest = [row for row in reader]

	for row in reader:
		iterator = 0
		for cell in row:
			if cell == "":
				print(titleRow[iterator],row[0])
			iterator += 1 