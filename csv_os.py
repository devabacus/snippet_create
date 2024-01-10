import os
import csv
from utils import get_window_name


def get_folder_path(parent_folder_name: str) -> str:
    window_program_name = get_window_name()
    for folder_name in os.listdir(parent_folder_name):
        if folder_name in window_program_name:
            return os.path.join(parent_folder_name, folder_name)
    return ""


def get_snippets_from_csv_files(search_text: str) -> dict:
    snippets = {}
    program_folder = get_folder_path('snippets')
    try:
        for csv_file in os.listdir(program_folder):
            file_path = os.path.join(program_folder, csv_file)
            new_item_snippet = get_snippets_map(file_path, search_text)
            sorted_snippet = sort_snippet(new_item_snippet, search_text)
            snippets.update(sorted_snippet)
    except FileNotFoundError:
        print("Directory not found:", program_folder)
    except Exception as e:
        print("An error occurred:", e)
    return snippets

def custom_sort_key(item):
    # Сортировка сначала по длине ключа, затем по алфавиту
    return (len(item), item)

def sort_snippet(snippets:dict, search_text:str)->dict:
    sorted_dict = dict(sorted(snippets.items(), key=custom_sort_key))
    return sorted_dict

def get_snippets_map(file_path: str, search_text: str) -> dict:
    snippets = {}
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                if search_text in row[0]:
                    snippets[row[0]] = row[1].replace(
                        "\\n", "\n").replace("\\t", "\t")
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred while reading the file:", e)
    return snippets
