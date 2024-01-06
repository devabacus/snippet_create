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

def convert_to_snippet()->None:
    print("copy snippet for generate")
    # original_clipboard = pyperclip.paste()
    pynput_shortcut(Key.ctrl_l, 'c')
    data_for_snippet = pyperclip.paste()
    print(repr(data_for_snippet))
    # data_for_snippet = data_for_snippet.replace('\r\n', '\n').replace('    ', '\t
    # data_for_snippet = data_for_snippet.replace('\n', '\\n').replace('\t', '\\t')
    data_for_snippet = data_for_snippet.replace('\r\n', '\n')
    data_for_snippet = data_for_snippet.replace('\n', '\\n')
    data_for_snippet = f'|{data_for_snippet}'
    print(repr(data_for_snippet))
    pyperclip.copy(data_for_snippet)
    