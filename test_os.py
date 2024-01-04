import os
import csv
import win32gui


def get_window_name() -> str:
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).casefold()


def pick_snippet_csv_file() -> str:
    window_program_name = get_window_name()
    folderName = 'csv_snippets'
    file_path = ""
    mlist: list = os.listdir(folderName)
    csvFileName = ""
    for fileName in mlist:
        if fileName.split('.')[0] in window_program_name:
            csvFileName = fileName
            file_path = f'{folderName}/{csvFileName}'
    return file_path


def get_folder_path() -> str:
    window_program_name = get_window_name()
    parentFolderName = 'snippets'
    file_path = ""
    mlist: list = os.listdir(parentFolderName)
    for folderName in mlist:
        if folderName in window_program_name:   
            file_path = f'{parentFolderName}/{folderName}'
    return file_path
    
    
    
def get_snippets_from_csv()->dict:
    snippets:dict = {}
    listOfCsvFiles:list = []
    



def get_snippets_map(filePath: str, search_text: str) -> dict:
    snippets: dict = {}
    with open(filePath, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if search_text in row[0]:
                snippets[row[0]] = row[1].replace(
                    "\\n", "\n").replace("\\t", "\t")
    print(f'найдено совпадения {snippets}')
    return snippets
