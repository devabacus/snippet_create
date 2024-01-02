import os
import csv

mlist:list = os.listdir('csv_snippets') 

def pick_snippet_csv_file(window_program_name:str)->str:
    csvFileName = ""
    for fileName in mlist:
        if fileName.split('.')[0] in window_program_name.casefold():
            csvFileName = fileName
    return csvFileName

csvFileName = pick_snippet_csv_file("visual basic bla bla bla 123412lkj")

file_path = f'csv_snippets/{csvFileName}'
search_text = "si"

if len(csvFileName) != 0:
    #check first csv column for coincidence with keyword
    with open(file_path, newline = '', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        snippets:dict = {}
        for row in reader:
            if search_text in row[0]:
                snippets[row[0]] = row[1]
                
        print(f'найдено совпадения {snippets}')


