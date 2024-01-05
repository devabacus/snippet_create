from pynput.keyboard import Listener, Key, KeyCode
import snippet_manager
from ui_components import show_popup
from utils import *

typed_keys = ''
ctrl_pressed = False

def on_press(key, root):
    global typed_keys, ctrl_pressed
    try:
        if key == Key.ctrl_l and ctrl_pressed == False         :
            ctrl_pressed = True
        elif ctrl_pressed and hasattr(key, 'vk') and key.vk == 191:
            keyboard_controller.release(Key.ctrl_l)
            pynput_key_press(Key.home) 
            pynput_key_press("'")           # Нажимаем '
            pynput_key_press(Key.down)
        elif key == Key.space and ctrl_pressed:
            snippets = snippet_manager.get_snippets(typed_keys)
            show_popup(snippets, root)
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
        # print("ctrl_releas = False")

def start_keyboard_listener(root):
    listener = Listener(on_press=lambda key: on_press(key, root), on_release=on_release)
    listener.start()