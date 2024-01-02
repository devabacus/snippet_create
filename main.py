from pynput.keyboard import Listener
import tkinter as tk
import pyautogui

typed_keys = ''
snippets = {
    "Snippet 1": "def function_name():\n    pass",
    "Snippet 2": "class ClassName:\n    def __init__(self):\n        pass",
}

content_window = None

def on_press(key):
    global typed_keys
    try:
        typed_keys += key.char
        if typed_keys.endswith('trig'):
            show_popup()
    except AttributeError:
        typed_keys = ''

def update_snippet_content(snippet_key):
    global content_window
    if content_window:
        content_window.destroy()
    content_window = tk.Toplevel(root)
    content = tk.Text(content_window, height=10, width=40)
    content.insert(tk.END, snippets[snippet_key])
    content.pack()
    x = popup.winfo_x() + popup.winfo_width()
    y = popup.winfo_y()
    content_window.geometry(f"+{x}+{y}")

def on_select(event):
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        update_snippet_content(selected_snippet)

def insert_snippet():
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        pyautogui.hotkey('alt', 'tab')
        pyautogui.press('backspace', presses=4)
        pyautogui.write(snippets[selected_snippet],0.01)
        popup.destroy()
        if content_window:
            content_window.destroy()

def show_popup():
    global popup, listbox
    x, y = pyautogui.position()
    popup = tk.Toplevel(root)
    # popup.overrideredirect(True)
    popup.geometry(f"200x100+{x}+{y}")
    listbox = tk.Listbox(popup)
    for key in snippets.keys():
        listbox.insert(tk.END, key)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox.pack()
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