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

    def setScoreBoard(self,l,s,p):
        self.LT=l
        self.SGT=s
        self.PVT=p
        return True

    def clearPane(self):    
        for x in self.pane.grid_slaves(): x.destroy() # send email to make them change the term

    def showMap(self,message):
        self.clearPane()
        self.x=True

        def left():
            self.x='left'
            self.pane.quit()

        def center(): 
            self.x='center'
            self.pane.quit()

        def right():  
            self.x='right'
            self.pane.quit()

        msgl = tk.Message(self.pane, text = " LT: {}  ".format(self.LT))
        msgl.config(bg='lightgreen', font=('times', 24, 'bold'),anchor=tk.N)
        msgl.grid(row=0,column=3)
        msgs = tk.Message(self.pane, text = " SGT: {}  ".format(self.SGT))
        msgs.config(bg='lightgreen', font=('times', 24, 'bold'),anchor=tk.N)
        msgs.grid(row=0,column=4)
        msgp = tk.Message(self.pane, text = " PVT: {}  ".format(self.PVT))
        msgp.config(bg='lightgreen', font=('times', 24, 'bold'),anchor=tk.N)
        msgp.grid(row=0,column=5)

        canvas = tk.Canvas(self.pane, width = 370, height = 370)
        img = tk.PhotoImage(file="tmp.png")
        canvas.create_image(20,20,anchor=tk.NW,image=img)
        canvas.grid(row=0,rowspan=2,column=0,columnspan=3)


        msg = tk.Message(self.pane, text = message)
        msg.grid(row=1,column=3,columnspan=3)
        msg.config(bg='olive drab', font=('courier', 14, 'bold'),bd=2,width=700)

        tk.Button(self.pane, 
                text='Next', 
                command=self.pane.quit).grid(row=2, 
                                                column=3,
                                                columnspan=3, 
                                                pady=4,
                                                padx=4)


        tk.Button(self.pane, 
                text='Left', 
                command=left).grid(row=2, 
                                                column=0,
                                                columnspan=1, 
                                                pady=4,
                                                padx=4)
        tk.Button(self.pane, 
                text='Center', 
                command=center).grid(row=2, 
                                                column=1,
                                                columnspan=1, 
                                                pady=4,
                                                padx=4)
        tk.Button(self.pane, 
                text='Right', 
                command=right).grid(row=2, 
                                                column=2,
                                                columnspan=1, 
                                                pady=4,
                                                padx=4)

        tk.mainloop()
        return self.x

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
        self.LT = 0
        self.SGT = 0
        self.PVT = 0
        self.x = True