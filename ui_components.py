import tkinter as tk
import pyautogui
from utils import insert_snippet

def update_snippet_content(snippet_key, content, snippets):
    content.delete('1.0', tk.END)
    content.insert(tk.END, snippets[snippet_key])

def on_select(event, listbox, content, snippets):
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        update_snippet_content(selected_snippet, content, snippets)

def show_popup(typed_keys, snippets, root):
    if len(snippets) == 0: return 
    popup = tk.Toplevel(root)
    x, y = pyautogui.position()
    popup.geometry(f"400x200+{x}+{y}")

    listbox = tk.Listbox(popup)
    content = tk.Text(popup, height=10, width=40)
    
    for key in snippets.keys():
        listbox.insert(tk.END, key)
    listbox.bind('<<ListboxSelect>>', lambda e: on_select(e, listbox, content, snippets))
    
    listbox.pack(side=tk.LEFT, fill=tk.Y)
    content.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.select_set(0)
    on_select(None, listbox, content, snippets)

    popup.bind('<Return>', lambda e: insert_snippet(typed_keys, listbox, snippets, popup))
    popup.bind('<Escape>', lambda e: popup.destroy())

    popup.focus_force()
    listbox.focus_set()
