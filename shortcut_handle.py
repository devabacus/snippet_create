import pyperclip
from utils import *

def raw_duplicate() -> None:
    # original_clipboard = pyperclip.paste()
    pynput_key_press(Key.home)
    pynput_shortcut(Key.shift, Key.end)
    pynput_shortcut(Key.ctrl_l, 'c')
    pynput_key_press(Key.end)
    pynput_key_press(Key.enter)
    pynput_shortcut(Key.ctrl_l, 'v')
    # pyperclip.copy(original_clipboard)


def convert_to_snippet() -> None:
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
