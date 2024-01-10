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
    return new_typed_keys_ln - typed_keys_pos

def insert_snippet(typed_keys, listbox, snippets, popup, comment = ''):
    
    index = listbox.curselection()
    if index:
        selected_snippet = listbox.get(index)
        snippet_text = snippets[selected_snippet]

        pynput_shortcut(Key.alt, Key.tab)
        remove_num = get_ln_remove_chars(typed_keys)
        pynput_key_press(Key.right) # deselect text
        for _ in range(remove_num):
            pynput_key_press(Key.backspace)
        
        original_clipboard = pyperclip.paste()
        clean_snippet_text = ''
        if comment == '':
            clean_snippet_text = snippet_text
            print(snippet_text)
        else:
            start_del_ind = snippet_text.find(comment)
            end_del_ind = snippet_text.find('\n', start_del_ind)
            if end_del_ind == -1:
                end_del_ind = len(snippet_text)
                # one row snippet with comment need to handle
                
            str_for_del = snippet_text[start_del_ind:end_del_ind]
            clean_snippet_text = snippet_text.replace(str_for_del, '')
            if comment and snippet_text.find(comment) == 0:
                pynput_key_press(Key.delete)
            
        time.sleep(0.1)
        pyperclip.copy(clean_snippet_text)
        time.sleep(0.1)
        pynput_shortcut(Key.ctrl_l, 'v')
        time.sleep(0.1)
        pyperclip.copy(original_clipboard)
        popup.destroy()


def get_window_name() -> str:
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).casefold()