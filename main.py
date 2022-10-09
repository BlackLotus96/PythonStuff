import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, RIGHT, TOP, LEFT, BOTTOM, BOTH, X, Y

import search_xpath
import re

global root
w = 800
h = 600


def screen():

    list_name_button = []
    list_of_links = []
    list_of_triples = []
    list_of_number_links = []
    root= tk.Tk()
    my_name = ""
    root.geometry(f"{w}x{h}")
    root.title("Breccia's sorter")



    def addLink():
        global h
        global w
        nextRow = len(list_of_triples)
        name_button = f"Registra {nextRow+1}° Ordine"
        number_in_list = [int(s) for s in re.findall(r'\b\d+\b', name_button)]

        button = tk.Button(root, text=name_button, command=lambda: saveLink(number_in_list[0]))
        button.grid(row = nextRow+1, column = 0, sticky = tk.W, pady = 2)

        button_cancel = tk.Button(root, text="Cancella", command=lambda: cancelLink(number_in_list[0]))
        button_cancel.grid(row = nextRow+1, column = 1, sticky = tk.W, pady = 2)

        entry = tk.Entry(root, width=140)
        entry.grid(row = nextRow+1, column = 2, sticky = tk.W, pady = 2)

        list_of_triples.append([button, button_cancel, entry])

        h = 600+len(list_of_triples)*30
        root.geometry(f"{w}x{h}")

    def cancelLink(number):
        butt_1_widg = list_of_triples[number-1][0]
        butt_2_widg = list_of_triples[number-1][1]
        entry_widg = list_of_triples[number-1][2]
        butt_1_widg.destroy()
        butt_2_widg.destroy()
        entry_widg.destroy()
        if len(list_of_links) != 0:
            index = list_of_number_links.index(number-1)
            del list_of_links[index]
            list_of_number_links.pop(number-1)

    def saveLink(number):
        x = list_of_triples[number-1][2].get()
        if x == "":
            messagebox.showerror("showerror", "Inserire un link!")
        elif not x.startswith("https://www.cardmarket.com/"):
            messagebox.showerror("showerror", "Inserire un link valido di mkm")
        elif x not in list_of_links:
            list_of_links.append(x)
            list_of_number_links.append(number-1)
        else:
            messagebox.showerror("showerror", "Link già registrato!")
        print(list_of_links)
        print(list_of_number_links)
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
