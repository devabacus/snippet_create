from pynput.keyboard import Key, Controller
import time

keyboard_controller = Controller()

def pynput_key_press(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)

def pynput_shortcut(key1, key2):
    keyboard_controller.press(key1)
    keyboard_controller.press(key2)
    keyboard_controller.release(key2)
    keyboard_controller.release(key1)

def insert_snippet(listbox, snippets, popup):
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        snippet_text = snippets[selected_snippet]

        pynput_shortcut(Key.alt, Key.tab)

        for _ in range(len(snippet_text)+1):
            pynput_key_press(Key.backspace)

        for char in snippet_text:
            if char == "\n":
                pynput_key_press(Key.enter)
                time.sleep(0.1)
            else:
                pynput_key_press(char)

        popup.destroy()
