from tkinter import * #Appka bude robena v tkinteri

#Vlastnosti zakladneho okna a canvasu
window = Tk()
window.title("Braska")
window.geometry("600x850")

#Canvas
canvas = Canvas(window,width=600,height=850,background="black")
canvas.pack()

#Grafika
canvas.create_rectangle(0,0,150,850,fill="white") #Lavy bocny panel
canvas.create_rectangle(150,0,600,150,fill="grey") #Horny sivy panel

#Funkcie
inp_otvorene = False
def input_output(): #Funkcia pre vytvorenie novych slov pre slovnik
    global inp_otvorene
    if(not inp_otvorene): #Umozni okno otvorit len raz
        inp_otvorene = True
        inp_window = Toplevel(window) #Vytvorenie dalsieho okna po stlaceni tlacitka nove slovo
        inp_window.title = ("Braska Input")
        inp_window.geometry("400x400")

        #Canvas pre nove slovo
        inp_canvas = Canvas(inp_window,width=400,height=400,background="black")
        inp_canvas.pack()

        #nove slovo Grafika
        inp_canvas.create_text(200,30,text="Pridaj Nové Slovo",font=("Helvetica 18 bold"),fill="white")

        def input_zatvoreni(): #Pri stlaceni x na okne
            global inp_otvorene,Inp_window
            inp_otvorene = False
            inp_window.destroy()
        inp_window.protocol("WM_DELETE_WINDOW",input_zatvoreni)


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

wordInput = Button(canvas, text = "nove\nslovo", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie okna nove slovo,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"),command=input_output)
canvas.create_window(45,290,anchor='nw',window=wordInput)

vyhladavanie = Entry(canvas, text="Vyhladavanie",width=20,font=("Helvetica 24 bold"))
canvas.create_window(380,60,anchor='center',window=vyhladavanie)

window.mainloop()