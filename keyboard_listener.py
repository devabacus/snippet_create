from pynput.keyboard import Listener, Key, KeyCode
import snippet_manager
from ui_components import show_popup
from utils import *
from shortcut_handle import *

from utils import get_window_name


typed_keys = ''
ctrl_pressed = False
commented = False


def on_press(key, root):
    global typed_keys, ctrl_pressed
    print(key)
    if "visual basic" in get_window_name():
        try:
            if key == Key.ctrl_l and ctrl_pressed == False:
                ctrl_pressed = True
            elif ctrl_pressed and hasattr(key, 'vk') and key.vk == 191:
                keyboard_controller.release(Key.ctrl_l)
                toggle_comment()
            elif hasattr(key, 'char') and key.char == '\x04':
                keyboard_controller.release(Key.ctrl_l)
                keyboard_controller.release(Key.ctrl_r)
                raw_duplicate()
            elif key == Key.space and ctrl_pressed:
                snippets = snippet_manager.get_snippets(typed_keys)
                show_popup(typed_keys, snippets, root)
                ctrl_pressed = False
                typed_keys = ''
            elif hasattr(key, 'char') and key.char:
                if key.char and key.char.isalnum():
                    typed_keys += key.char
            else:
                typed_keys = ''
        except AttributeError:
            typed_keys = ''


def on_release(key):
    global ctrl_pressed
    if key == Key.ctrl_l:
        ctrl_pressed = False


def start_keyboard_listener(root):
    listener = Listener(on_press=lambda key: on_press(
        key, root), on_release=on_release)
    listener.start()
