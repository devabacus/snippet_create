import pyperclip
from utils import *


def toggle_comment() -> None:
    global commented
    # сохраняем содержимое буфера
    original_clipboard = pyperclip.paste()
    # выделяем и копируем первый символ в строке
    pynput_key_press(Key.end)
    pynput_key_press(Key.home)
    pynput_shortcut(Key.shift, Key.right)
    pynput_shortcut(Key.ctrl_l, 'c')
    time.sleep(0.1)
    first_char = pyperclip.paste()
    print(first_char)
    pyperclip.copy(original_clipboard)
    if first_char != "'":
        pynput_key_press(Key.left)
        time.sleep(0.1)
        pynput_key_press("'")
        pynput_key_press(Key.down)
    else:
        pynput_key_press(Key.backspace)
        pynput_key_press(Key.down)


def raw_duplicate() -> None:
    # original_clipboard = pyperclip.paste()
    pynput_key_press(Key.home)
    pynput_shortcut(Key.shift, Key.end)
    pynput_shortcut(Key.ctrl_l, 'c')
    pynput_key_press(Key.end)
    pynput_key_press(Key.enter)
    pynput_shortcut(Key.ctrl_l, 'v')
    # pyperclip.copy(original_clipboard)
