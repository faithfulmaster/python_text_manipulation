import csv
import pandas as pd

# function to write data to csv file
def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter= ',')
        for line in data:
            writer.writerow(line)

# main function
if __name__ == "__main__":

    # Input column data into csv file
    data = ["Name".split(","),
            "Sam".split(","),
            "Raju".split(",")]
    path = "output.csv"
    csv_writer(data, path)

    # Read csv file
    word = pd.read_csv(path)
    print word

    # Copy the existing column and append it to the csv file under a new column name
    word.insert(1, "Copied name", word)
    word.to_csv(path)

    # Read and print the updated csv file
    word = pd.read_csv(path)
    print word
