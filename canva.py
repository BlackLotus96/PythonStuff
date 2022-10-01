import tkinter as tk
from tkinter import ttk, RIGHT, TOP, LEFT, BOTTOM, BOTH, X, Y
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
    list_name_button = []
    root= tk.Tk()
    my_name = ""
    root.geometry("400x300")
    root.title("Breccia's sorter")



    def addLink():
        nextRow = len(list_entry)
        name_button = f"Registra {nextRow+1}° Ordine"
        list_name_button.append(name_button)

        button = tk.Button(root, text=name_button, command=lambda: getLink(nextRow))
        button.grid(row = nextRow+1, column = 0, sticky = tk.W, pady = 2)

        entry = tk.Entry(root, width=70)
        entry.grid(row = nextRow+1, column = 1, sticky = tk.W, pady = 2)

        list_entry.append(entry)

        w = 400
        h = 300+len(list_entry)*30
        root.geometry(f"{w}x{h}")

    def getLink(n_button):
        x = list_entry[n_button].get()
        driver.get(x)
        root.quit()


    button_add = tk.Button(root, text='Aggiungi Link', command=addLink)
    button_add.grid(row = 0, column = 0, sticky = tk.W, pady = 2)

    #canvas.create_window(200, 180, window=button)

    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')

    path = find(driver_name, driver_path).replace('\\', '/')
    driver = webdriver.Chrome(path, chrome_options=options)
    root.mainloop()
    return driver
