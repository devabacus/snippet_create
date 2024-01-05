python -m venv env
.\env\Scripts\Activate.ps1

pip install pyautogui
pip install pynput
pip install keyboard
pip install pywin32
pip install pyperclip

python -m pip freeze > requirements.txt
pip install -r requirements.txt
python.exe -m pip install --upgrade pip