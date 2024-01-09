from pynput.keyboard import Key, Controller
import time
import win32gui
import pyperclip


keyboard_controller = Controller()

def pynput_key_press(key):

    keyboard_controller.press(key)
    keyboard_controller.release(key)

def pynput_shortcut(key1, key2):
    keyboard_controller.press(key1)
    keyboard_controller.press(key2)
    keyboard_controller.release(key2)
    keyboard_controller.release(key1)

# sometimes vba editor autocompleted the typed
def get_ln_remove_chars(typed_keys:str)->int:
    original_clipboard = pyperclip.paste()
    pynput_key_press(Key.end)
    time.sleep(0.1)
    pynput_shortcut(Key.shift, Key.home)
    time.sleep(0.1)
    pynput_shortcut(Key.ctrl_l, 'c')
    time.sleep(0.1)
    new_typed_keys = pyperclip.paste()
    pyperclip.copy(original_clipboard)

    
    
    new_typed_keys_ln = len(new_typed_keys)
    typed_keys_pos = new_typed_keys.casefold().find(typed_keys.casefold())
    print(f'new_typed_keys_ln {new_typed_keys_ln}')
    print(f'typed_keys_pos {typed_keys_pos}')
    return new_typed_keys_ln - typed_keys_pos
    


def insert_snippet(typed_keys, listbox, snippets, popup, comment_sym = ''):
    
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        snippet_text = snippets[selected_snippet]

        pynput_shortcut(Key.alt, Key.tab)
        remove_num = get_ln_remove_chars(typed_keys)
        print(f'delete need chars: {remove_num}')
        pynput_key_press(Key.right) # deselect text
        for _ in range(remove_num):
            time.sleep(0.1)
            pynput_key_press(Key.backspace)
        comment_chars = False
        first_raw_comment = False
        
        
        original_clipboard = pyperclip.paste()
        print(snippet_text)
        time.sleep(0.1)
        pyperclip.copy(snippet_text)
        time.sleep(0.1)
        pynput_shortcut(Key.ctrl_l, 'v')
        time.sleep(0.1)
        pyperclip.copy(original_clipboard)
        
        
        
        # for char in snippet_text:
        #     if char == "\n":
        #         if comment_chars == True:
        #             comment_chars = False
        #         if first_raw_comment:
        #             first_raw_comment = False
        #         else: 
        #             pynput_key_press(Key.enter)
        #         time.sleep(0.1)
        #     elif comment_sym and char == comment_sym and snippet_text[0] == comment_sym:
        #         comment_chars = True
        #         first_raw_comment = True
        #     elif comment_chars == False:
        #         pynput_key_press(char)

            

        popup.destroy()


def get_window_name() -> str:
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).casefold()