from pynput import keyboard

ctrl_pressed = False

def on_press(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = True
    elif ctrl_pressed and hasattr(key, 'vk') and key.vk == 191:
        print("Ctrl + '/' pressed")

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False
    if key == keyboard.Key.esc:
        return False  # Останавливаем прослушивание

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()