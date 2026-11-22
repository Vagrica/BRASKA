from tkinter import * #Appka bude robena v tkinteri

#Vlastnosti okna a canvasu
window = Tk()
window.title("Braska")
window.geometry("600x850")
window.config(background="black")

#Canvas
canvas = Canvas(window,width=600,height=850,background="black")
canvas.pack()

#Grafika
canvas.create_rectangle(0,0,150,850,fill="white") #Lavy bocny panel
canvas.create_rectangle(150,0,600,150,fill="grey") #Horny sivy panel

#Tlacitka
f_index = Button(canvas, text = "Full\nIndex", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie celeho Indexu,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"))
canvas.create_window(45,20,anchor='nw',window=f_index)

settings = Button(canvas, text = "Nastavenia", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie nastaveni,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"))
canvas.create_window(45,110,anchor='nw',window=settings)

prepojenia = Button(canvas, text = "Prepojenia", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie prepojeni,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"))
canvas.create_window(45,200,anchor='nw',window=prepojenia)

vyhladavanie = Entry(canvas, text="Vyhladavanie",width=20,font=("Helvetica 24 bold"))
canvas.create_window(380,60,anchor='center',window=vyhladavanie)

window.mainloop()