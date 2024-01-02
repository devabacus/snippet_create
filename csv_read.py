import csv

with open('visual basic.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(reader.line_num, row)

    

    
    