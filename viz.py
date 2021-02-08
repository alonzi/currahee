"""
github.com/alonzi (datascientist@virginia.edu)
vizualization subroutines for currahee game
2021-02-03
github.com/alonzi/currahee
gotta have sick viz
"""

import tkinter as tk

def request(prompt,var2set):
    ''' give a prompt and a variable to set with answer '''

    master = tk.Tk()
    msg = tk.Message(master, text = prompt)
    msg.grid(row=0,column=0,columnspan=2)
    msg.config(bg='olive drab', font=('courier', 14, 'bold'),bd=0,width=300)
    tk.Label(master,text=var2set).grid(row=1,column=0)
    e1 = tk.Entry(master)
    e1.grid(row=1,column=1)
    tk.Button(master, 
            text='Enter', 
            command=master.quit).grid(row=2, 
                                        column=0,
                                        columnspan=1, 
                                        pady=4,
                                        padx=4)
    tk.Button(master, 
            text='Close', 
            command=master.destroy).grid(row=2, 
                                         column=1,
                                         columnspan=1, 
                                         pady=4,
                                         padx=4)

    tk.mainloop() # halts the python progression
    return e1.get()
