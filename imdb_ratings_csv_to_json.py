# Importing the necessary libraries
import csv
import json
import sys


# The main function that will convert csv to json
def csv_to_json(csvFilePath):
    # create a dictionary
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding="utf-8") as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # create a new dict to store the selected key-value pairs
            title_rating_dict = {}
            title_rating_dict["title"] = row["Title"]
            title_rating_dict["rating"] = row["Your Rating"]

            # add this python dict to json array
            jsonArray.append(title_rating_dict)

    # convert python jsonArray to JSON String and write to file
    with open("movies.json", "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# Checking if the filename is given as a command line argument
if len(sys.argv) != 2:
    print("Please provide a filename as a command line argument.")
    sys.exit()

# Getting the filename from the command line argument
filename = sys.argv[1]

# Calling the function with the csv file path
csv_to_json(filename)
