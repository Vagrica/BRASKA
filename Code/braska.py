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
slova_y = 120 #Y sa bude updatovat aby sa slova posuvali od seba na y-osi
slovnik = {}
def input_output(): #Funkcia pre vytvorenie novych slov pre slovnik
    global inp_otvorene
    if(not inp_otvorene): #Umozni okno otvorit len raz
        inp_otvorene = True
        inp_window = Toplevel(window) #Vytvorenie dalsieho okna po stlaceni tlacitka nove slovo
        inp_window.title("Braska Input")
        inp_window.geometry("400x400")

        #Canvas pre nove slovo
        inp_canvas = Canvas(inp_window,width=400,height=400,background="black")
        inp_canvas.pack()

        #nove slovo Grafika
        inp_canvas.create_text(200,30,text="Pridaj Nové Slovo",font=("Helvetica 24 bold"),fill="white")
        #nove slovo input
        #SK Input
        inp_canvas.create_text(40,90,text="SK",font=("Helvetica 18 bold"),fill="white")
        Sk_input_txt = Entry(inp_canvas,width=16,font=("Helvetica 22 bold"))
        inp_canvas.create_window(200,90,window=Sk_input_txt)

        #BR Input
        inp_canvas.create_text(40,180,text="BR",font=("Helvetica 18 bold"),fill="white")
        Br_input_txt = Entry(inp_canvas,width=16,font=("Helvetica 22 bold"))
        inp_canvas.create_window(200,180,window=Br_input_txt)

        #VYSLOVNOST
        inp_canvas.create_text(40,270,text="VYS",font=("Helvetica 18 bold"),fill="white")
        Vys_input_txt = Entry(inp_canvas,width=16,font=("Helvetica 22 bold"))
        inp_canvas.create_window(200,270,window=Vys_input_txt)

        #Odoslat
        def odos_slovo():
            global slova_y
            Sk_input = Sk_input_txt.get()
            Br_input = Br_input_txt.get()
            Vys_input = Vys_input_txt.get()
            slova_y += 40

            slovnik[Sk_input]  = { #Sk_input ma v sebe brazilsku verziu a vyslovnost napr mlieko ma v sebe mel a mel, voda ma aqua a akvua
                "BR" : Br_input,
                "VYS" : Vys_input
            }

            canvas.create_text(240,slova_y,text=Sk_input,font=("Helvetica 18 bold"),fill="white")
            canvas.create_text(360,slova_y,text=Br_input,font=("Helvetica 18 bold"),fill="white")
            canvas.create_text(480,slova_y,text=Vys_input,font=("Helvetica 18 bold"),fill="white")
                
        Odos_input = Button(inp_canvas,text="Odoslať",width=10,height=2,font=("Helvetica 10 bold"),command=odos_slovo)
        inp_canvas.create_window(200,350,window=Odos_input)
        

        def input_zatvoreni(): #Pri stlaceni x na okne funkcia pre zatvorenie
            global inp_otvorene
            inp_otvorene = False
            inp_window.destroy()
        inp_window.protocol("WM_DELETE_WINDOW",input_zatvoreni)
#KONIEC FUNKCIE INPUT OUTPUT



#Tlacitka
f_index = Button(canvas, text = "Full\nIndex", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie celeho Indexu,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"))
canvas.create_window(45,20,anchor='nw',window=f_index)

settings = Button(canvas, text = "Nastavenia", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie nastaveni,momentalne nefunkcne
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"))
canvas.create_window(45,110,anchor='nw',window=settings)

wordInput = Button(canvas, text = "nove\nslovo", width= 8, height= 3,bg="#d3d3d3", #Zobrazenie okna nove slovo
                 fg="black",activebackground="#828283",activeforeground="white",borderwidth=0,font=("Helvetica 8 bold"),command=input_output)
canvas.create_window(45,200,anchor='nw',window=wordInput)

vyhladavanie = Entry(canvas, text="Vyhladavanie",width=20,font=("Helvetica 24 bold")) #VYHLADAVANIE,POZRI SA DO FUNKCIE INPUT OUTPUT TAM MAS MOJ SLOVNIK
canvas.create_window(380,60,anchor='center',window=vyhladavanie)

window.mainloop()