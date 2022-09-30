import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def screen(driver_name, driver_path):
    global root
    list_entry = []
    root= tk.Tk()
    root.geometry("400x300")
    root.title("Breccia's sorter")

    def addLink():

        entry = tk.Entry(root, width=70)
        entry.pack(pady=25)
        list_entry.append(entry)
        w = 400
        h = 300+len(list_entry)*30
        root.geometry(f"{w}x{h}")


    button_add = tk.Button(root, text='Add Link', command=addLink)
    button_add.pack()

    # Entry box
    entry = tk.Entry(root, width=70)
    entry.pack()
    list_entry.append(entry)



    # Button
    def getLink():
        x = entry.get()
        driver.get(x)
        root.destroy()

    button = tk.Button(root, text='Go to Link', command=getLink)
    button.pack()


    #canvas.create_window(200, 180, window=button)

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    path = find(driver_name, driver_path).replace('\\', '/')
    driver = webdriver.Chrome(path, chrome_options=options)

    root.mainloop()
    return driver
