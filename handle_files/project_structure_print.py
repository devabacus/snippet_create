import os

def generate_project_structure(folder_path, exclude_folders=[], indent=''):
    project_structure = ''
    items = os.listdir(folder_path)
    
    for item in sorted(items):
        item_path = os.path.join(folder_path, item)
        
        # Проверяем, является ли элемент одной из папок, которые нужно исключить
        if os.path.isdir(item_path) and item in exclude_folders:
            continue
        
        if os.path.isdir(item_path):
            project_structure += f'{indent}📁 {item}\n'
            project_structure += generate_project_structure(item_path, exclude_folders, indent + '    ')
        else:
            project_structure += f'{indent}📄 {item}\n'
    
    return project_structure

# Укажите путь к папке проекта (родительской папке для папки скрипта)
project_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Получите путь к папке, в которой находится данный скрипт
script_folder_path = os.path.dirname(os.path.abspath(__file__))

# Создайте путь к папке "handle_files" внутри папки проекта
output_folder_path = os.path.join(project_folder_path, 'handle_files')
project_name = os.path.basename(project_folder_path)

# Укажите список папок, которые нужно исключить из структуры проекта
exclude_folders = [
    project_name,
    'env', 
    '__pycache__', 
    '.pytest_cache', 
    '.git', 
    '.vscode'
    # Добавьте другие папки, которые нужно исключить
]

project_structure = generate_project_structure(project_folder_path, exclude_folders)

# Добавьте уровень выше к структуре проекта
project_structure = f'📁 {os.path.basename(project_folder_path)}\n{project_structure}'

# Укажите имя файла, в который будет записана структура проекта
output_file = os.path.join(output_folder_path, 'структура_проекта.txt')

os.makedirs(output_folder_path, exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(project_structure)

print(f'Структура проекта сохранена в файл: {output_file}')
