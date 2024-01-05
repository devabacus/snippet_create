from pynput.keyboard import Listener, Key
import snippet_manager
from ui_components import show_popup

typed_keys = ''
ctrl_pressed = False

def on_press(key, root):
    global typed_keys, ctrl_pressed
    try:
        if key == Key.ctrl_l:
            ctrl_pressed = True
        elif key == Key.space and ctrl_pressed:
            snippets = snippet_manager.get_snippets(typed_keys)
            show_popup(snippets, root)
            ctrl_pressed = False
            typed_keys = ''
        elif hasattr(key, 'char') and key.char:
            if key.char.isalnum():
                typed_keys += key.char
        else:
            typed_keys = ''
    except AttributeError:
        typed_keys = ''

def start_keyboard_listener(root):
    listener = Listener(on_press=lambda key: on_press(key, root))
    listener.start()
