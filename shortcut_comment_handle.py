import pyperclip
from utils import *


def comment_additional_raw(raw_num: int) -> None:
    for _ in range(1, raw_num):
        pynput_key_press(Key.left)
        pynput_key_press("'")
        pynput_key_press(Key.down)

def uncomment_additional_raw(raw_num: int) -> None:
    for _ in range(1, raw_num):
        pynput_key_press(Key.delete)
        pynput_key_press(Key.down)


def toggle_multi_raw_comment(raw_num: int) -> None:
    commented = toggle_one_raw_comment(one_raw=False)
    if commented:
        pynput_key_press(Key.left)
        for _ in range(1, raw_num):
            pynput_key_press(Key.down)
        for _ in range(1, raw_num):
            pynput_key_press(Key.delete)
            pynput_key_press(Key.up)
        pynput_key_press(Key.delete)
            
    else:
        comment_additional_raw(raw_num)
        

# either block of raws or one raw need to comment
def define_type_of_comment() -> None:
    original_clipboard = pyperclip.paste()
    pyperclip.copy('')
    pynput_shortcut(Key.ctrl_l, 'c')
    time.sleep(0.05)
    data_for_comment = pyperclip.paste()
    raw_num = data_for_comment.count("\n")
    if data_for_comment[-1:] != '\n':
        raw_num += 1
    if len(data_for_comment) == 0 or raw_num == 0:
        pyperclip.copy(original_clipboard)
        toggle_one_raw_comment(one_raw=True)
    else:
        toggle_multi_raw_comment(raw_num)

def toggle_one_raw_comment(one_raw:bool) -> bool:
    # сохраняем содержимое буфера
    original_clipboard = pyperclip.paste()
    # выделяем и копируем первый символ в строке
    pynput_key_press(Key.home)
    pynput_key_press(Key.home)
    pynput_shortcut(Key.shift, Key.right)
    pynput_shortcut(Key.ctrl_l, 'c')
    time.sleep(0.1)
    first_char = pyperclip.paste()
    pyperclip.copy(original_clipboard)
    commented = False
    if first_char != "'":
        pynput_key_press(Key.left)
        time.sleep(0.1)
        pynput_key_press("'")
        pynput_key_press(Key.down)
    else:
        if(one_raw):
            pynput_key_press(Key.backspace)
            pynput_key_press(Key.down)
        commented = True
    return commented
