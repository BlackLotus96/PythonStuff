import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, RIGHT, TOP, LEFT, BOTTOM, BOTH, X, Y
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import search_xpath
import re

times_of_pressure = 0
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def screen(driver):
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

        button = tk.Button(root, text=name_button, command=lambda: getLink(name_button))
        button.grid(row = nextRow+1, column = 0, sticky = tk.W, pady = 2)

        entry = tk.Entry(root, width=70)
        entry.grid(row = nextRow+1, column = 1, sticky = tk.W, pady = 2)

        list_entry.append(entry)

        w = 400
        h = 300+len(list_entry)*30
        root.geometry(f"{w}x{h}")

    def getLink(name_button):
        global times_of_pressure
        number_in_list = [int(s) for s in re.findall(r'\b\d+\b', name_button)]
        x = list_entry[number_in_list[0]-1].get()
        if x == "":
            messagebox.showerror("showerror", "Inserire un link!")
        elif not x.startswith("https://www.cardmarket.com/"):
            messagebox.showerror("showerror", "Inserire un link valido di mkm")
        else:
            driver.get(x)
            times_of_pressure+=1
            search_xpath.search(driver, times_of_pressure)
        #root.quit()


    button_add = tk.Button(root, text='Aggiungi Link', command=addLink)
    button_add.grid(row = 0, column = 0, sticky = tk.W, pady = 2)


    #search_xpath.search(driver)
    print("mainloop")
    root.mainloop()

if __name__ == "__main__":

    driver_name = 'chromedriver.exe'
    driver_path = r"C:\Users\simone.meddi\Desktop\Simone\Python\PythonDrivers"
    path = find(driver_name, driver_path).replace('\\', '/')
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(path, chrome_options=options)
    print("prima di screen")
    screen(driver)
    print("dopo di screen")
