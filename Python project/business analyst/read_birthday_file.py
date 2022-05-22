import csv

filename = "business analyst/file/birthday.txt"

count = 0

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if count == 0:
            print(f'{" ".join(row)} ')
            count += 1
        else:
            print(f"{row[0]} work as {row[1]} and has a birthday {row[2]}")
            count += 1
print(f'number of line are: {count}')
