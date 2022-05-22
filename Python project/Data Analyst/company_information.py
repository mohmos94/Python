import csv

filename = "file/test.csv"

rows = []
count = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for element in header:
        print(element, end=" ")
    for row in reader:
        count += 1
        rows.append(row)
        for element in row:
            print(element, end=" ")
        print()
print("number of row under are: {}".format(count))





