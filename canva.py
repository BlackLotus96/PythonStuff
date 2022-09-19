import tkinter as tk
from selenium import webdriver
import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def screen(driver_name, driver_path):
    root= tk.Tk()

    canvas = tk.Canvas(root, width = 400, height = 300)
    canvas.pack()

    entry = tk.Entry(root)
    canvas.create_window(200, 140, window=entry)

    path = find(driver_name, driver_path).replace('\\', '/')
    driver = webdriver.Chrome(path)

    def getLink ():
        x = entry.get()
        driver.get(x)

    button = tk.Button(text='Go to Link', command=getLink)
    canvas.create_window(200, 180, window=button)

    root.mainloop()
    return driver
