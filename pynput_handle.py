from pynput.keyboard import Key, Controller

keyboard_controller = Controller()


def pynput_key_press(key):
    keyboard_controller.press(key)
    keyboard_controller.release(key)

def pynput_shortcut(key1, key2):
    keyboard_controller.press(key1)
    keyboard_controller.press(key2)
    keyboard_controller.release(key1)
    keyboard_controller.release(key2)