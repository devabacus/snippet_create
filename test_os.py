import os
import csv
import win32gui

def get_window_name() -> str:
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).casefold()

def get_folder_path(parentFolderName:str) -> str:
    window_program_name = get_window_name()
    file_path = ""
    mlist: list = os.listdir(parentFolderName)
    for folderName in mlist:
        if folderName in window_program_name:
            file_path = f'{parentFolderName}/{folderName}'
    return file_path

def get_snippets_from_csv_files(search_text: str) -> dict:
    snippets: dict = {}
    program_folder = get_folder_path('snippets')
    listOfCsvFiles: list = os.listdir(program_folder)
    for csvFile in listOfCsvFiles:
        new_item_snippet = get_snippets_map(
            f'{program_folder}/{csvFile}', search_text)
        snippets.update(new_item_snippet)
    return snippets

def get_snippets_map(filePath: str, search_text: str) -> dict:
    snippets: dict = {}
    with open(filePath, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile,delimiter='|')
        for row in reader:
            if search_text in row[0]:
                snippets[row[0]] = row[1].replace(
                    "\\n", "\n").replace("\\t", "\t")
    return snippets
