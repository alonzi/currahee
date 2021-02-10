"""
github.com/alonzi (datascientist@virginia.edu)
vizualization subroutines for currahee game
2021-02-03
github.com/alonzi/currahee
gotta have sick viz
"""

import tkinter as tk
import chess

class cl_viz:

    def clearPane(self):    
        for x in self.pane.grid_slaves(): x.destroy() # send email to make them change the term

    def showMap(self,message):
        self.clearPane()

        canvas = tk.Canvas(self.pane, width = 370, height = 470)

        img = tk.PhotoImage(file="tmp.png")
        canvas.create_image(20,20,anchor=tk.NW,image=img)

  #      img = tk.PhotoImage(file='wpawn.png')
  #      canvas.create_image(400,100,image=img)

  #      img = tk.PhotoImage(file='rook.png')
  #      canvas.create_image(400,200,image=img)

  #      img = tk.PhotoImage(file='bpawn.png')
  #      canvas.create_image(400,300,image=img)

        canvas.grid(row=0)


        msg = tk.Message(self.pane, text = message)
        msg.grid(row=0,column=1)
        msg.config(bg='olive drab', font=('courier', 14, 'bold'),bd=2,width=700)

        tk.Button(self.pane, 
                text='Next', 
                command=self.pane.quit).grid(row=1, 
                                                column=1, 
                                                pady=4,
                                                padx=4)

        tk.mainloop()
        return True

    def request(self,prompt,var2set):
        ''' give a prompt and a variable to set with answer '''
        msg = tk.Message(self.pane, text = prompt)
        msg.grid(row=0,column=0,columnspan=2)
        msg.config(bg='olive drab', font=('courier', 14, 'bold'),bd=2,width=300)
        tk.Label(self.pane,text=var2set).grid(row=1,column=0)
        e1 = tk.Entry(self.pane)
        e1.grid(row=1,column=1)
        tk.Button(self.pane, 
                text='Enter', 
                command=self.pane.quit).grid(row=2, 
                                                column=0,
                                                columnspan=1, 
                                                pady=4,
                                                padx=4)

        tk.mainloop() # halts the python progression
        return e1.get()

    def __init__(self):
        self.pane=tk.Tk()
        self.pane.title("Currahee!")