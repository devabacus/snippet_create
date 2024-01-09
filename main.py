import tkinter as tk
from keyboard_listener import start_keyboard_listener

def main():
    root = tk.Tk()
    root.withdraw()
    start_keyboard_listener(root)
    root.mainloop()

if __name__ == "__main__":
    main()
     