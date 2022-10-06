import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, RIGHT, TOP, LEFT, BOTTOM, BOTH, X, Y

import search_xpath
import re

times_of_pressure = 0


def screen():
    global root

    list_entry = []
    list_name_button = []
    list_of_links = []
    root= tk.Tk()
    my_name = ""
    root.geometry("400x300")
    root.title("Breccia's sorter")



    def addLink():
        nextRow = len(list_entry)
        name_button = f"Registra {nextRow+1}° Ordine"
        list_name_button.append(name_button)

        button = tk.Button(root, text=name_button, command=lambda: saveLink(name_button))
        button.grid(row = nextRow+1, column = 0, sticky = tk.W, pady = 2)

        entry = tk.Entry(root, width=70)
        entry.grid(row = nextRow+1, column = 1, sticky = tk.W, pady = 2)

        list_entry.append(entry)

        w = 400
        h = 300+len(list_entry)*30
        root.geometry(f"{w}x{h}")

    def saveLink(name_button):
        number_in_list = [int(s) for s in re.findall(r'\b\d+\b', name_button)]
        x = list_entry[number_in_list[0]-1].get()
        if x == "":
            messagebox.showerror("showerror", "Inserire un link!")
        elif not x.startswith("https://www.cardmarket.com/"):
            messagebox.showerror("showerror", "Inserire un link valido di mkm")
        elif x not in list_of_links:
            list_of_links.append(x)
        else:
            messagebox.showerror("showerror", "Link già registrato!")

        #root.quit()

    def start():
        search_xpath.startMultiProcess(list_of_links)

    button_add = tk.Button(root, text='Aggiungi Link', command=addLink)
    button_add.grid(row = 0, column = 0, sticky = tk.W, pady = 2)

    button_start = tk.Button(root, text='Start', command=start)
    button_start.grid(row = 0, column = 1, sticky = tk.W, pady = 2)


    #search_xpath.search(driver)
    print("mainloop")
    root.mainloop()

if __name__ == "__main__":
    screen()
