import os
import csv
import win32gui

def get_window_name()->str:
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd)
    

def pick_snippet_csv_file()->str:
    window_program_name = get_window_name()
    folderName = 'csv_snippets'
    file_path = ""
    mlist:list = os.listdir(folderName) 
    csvFileName = ""
    for fileName in mlist:
        if fileName.split('.')[0] in window_program_name.casefold():
            csvFileName = fileName
            file_path = f'{folderName}/{csvFileName}'
    return file_path

def get_snippets_map(filePath:str, search_text:str)->None:
    snippets:dict = {}
    with open(filePath, newline = '', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if search_text in row[0]:
                snippets[row[0]] = row[1].replace("\\n", "\n").replace("\\t", "\t")
    print(f'найдено совпадения {snippets}')
    return snippets        


