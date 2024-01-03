import time
from pynput.keyboard import Listener
from pynput.keyboard import Key, Controller
import tkinter as tk
import pyautogui
import win32gui
import test_os

typed_keys = ''
typed_keys_ln = 0
snippets:dict = {}
ctrl_pressed = False
keyboard_controller = Controller()

def on_press(key):
    global typed_keys, ctrl_pressed, snippets, typed_keys_ln
    try:
        if key == Key.ctrl_l:
            ctrl_pressed = True
        elif key == Key.space and ctrl_pressed:
            
            filePath = test_os.pick_snippet_csv_file()
            test_os.pick_snippet_csv_files()
            if len(filePath) != 0:
                if test_os.get_snippets_map(filePath, typed_keys):
                    snippets = test_os.get_snippets_map(filePath, typed_keys)
                    show_popup()
            ctrl_pressed =False
        elif hasattr(key, 'char') and key.char:
            if key.char.isalnum():
                typed_keys += key.char
                typed_keys_ln = len(typed_keys)
                
        else:
            typed_keys = ''
        # if typed_keys.endswith('trig'):
        #     show_popup()
    except AttributeError:
        typed_keys = ''

def update_snippet_content(snippet_key):
    content.delete('1.0', tk.END)
    content.insert(tk.END, snippets[snippet_key])

def on_select(event):
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        update_snippet_content(selected_snippet)

def insert_snippet1():
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        pyautogui.hotkey('alt', 'tab')
        pyautogui.press('backspace', presses=4)
        pyautogui.write(snippets[selected_snippet])
        popup.destroy()
        
def pynput_key_press(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)
        
def pynput_shortcut(key1, key2):
    keyboard_controller.press(key1)
    keyboard_controller.press(key2)
    keyboard_controller.release(key1)
    keyboard_controller.release(key2)
        
def insert_snippet():
    global typed_keys_ln
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        snippet_text = snippets[selected_snippet]

        # Имитация Alt+Tab для смены фокуса на окно редактора
        pynput_shortcut(Key.alt, Key.tab)

        # Удаление триггера 'trig'
        for _ in range(typed_keys_ln+1):
            pynput_key_press(Key.backspace)
        
        typed_keys_ln = 0
        # Ввод сниппета
        for char in snippet_text:
            if char == "\n":
                pynput_key_press(Key.enter)
                time.sleep(0.1)
            else:
                pynput_key_press(char)
                # pyautogui.write(char,interval=0)
        
        popup.destroy()

def show_popup():
    global popup, listbox, content
    x, y = pyautogui.position()
    popup = tk.Toplevel(root)
    popup.geometry(f"400x200+{x}+{y}")
    listbox = tk.Listbox(popup)
    for key in snippets.keys():
        listbox.insert(tk.END, key)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox.pack(side=tk.LEFT, fill=tk.Y)
    content = tk.Text(popup, height=10, width=40)
    content.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.select_set(0)
    on_select(None)
    popup.bind('<Return>', lambda e: insert_snippet())
    popup.bind('<Escape>', lambda e: popup.destroy())
    popup.focus_force()  # Фокус на popup
    listbox.focus_set()  # Фокусируемся на listbox

root = tk.Tk()
root.withdraw()
listener = Listener(on_press=on_press)
listener.start()
root.mainloop()
