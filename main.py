# imports
import csv

# open the file

with open("example.csv") as file:
	reader = csv.reader(file)
	# prep to store names of columns
	titleRow = reader.next()
   	#rest = [row for row in reader]
   	columnList = {}
	for row in reader:
		iterator = 0
		cellList = []
		for cell in row:
			if cell == "":
				cellList.append(titleRow[iterator])
				#print("Within " + row[0] + ", " + titleRow[iterator] + " has an empty")
			iterator += 1 
		#print cellList
		columnList[row[0]] = cellList

for item in sorted(columnList):
	itemString = (str(columnList[item]))
	if itemString != "[]":
		print(item + ":" + str(columnList[item]))




