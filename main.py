from tkinter import *
import time
import threading

#variables
secs_t = 2
secs_d = 3
secs_d_l = 4

mins_t,sec_t = divmod(secs_t,60)
hours_t,mins_t = divmod(mins_t,60)

mins_d,sec_d = divmod(secs_d,60)
hours_d,mins_d = divmod(mins_d,60)

stop_loop = False
iteraciones_cortas = 2
iteraciones_largas = 2

#FUNCTIONS 
def contador(secs,t,stop_loop):
    if t=="t":total_secs = secs_t
    if t=="d":total_secs = secs_d
    if t=="d_l":total_secs = secs_d_l
    while total_secs >=0 and not stop_loop:
        mins,sec = divmod(total_secs,60)
        hours,mins = divmod(mins,60)
        
        str_time = f"{hours:02d}:{mins:02d}:{sec:02d}"
        time.sleep(1)
        total_secs -= 1
        if t=="t": label_trabajo.config(text=str_time) 
        if t in "dd_l": label_descanso.config(text=str_time)
        root.update()    
 
def start_iteracion():
    thr = threading.Thread(target=iteracion)
    thr.start()
 
def iteracion():    
    global stop_loop
    stop_loop = False
    iter_completa = 0
    while iter_completa < iteraciones_largas and not stop_loop:
        if label_trabajo["text"] != "00:00:00" and int(label_iter["text"]) < iteraciones_cortas:
            contador(secs_t,"t",stop_loop)        
        elif label_descanso["text"] != "00:00:00" and int(label_iter["text"]) < iteraciones_cortas:
            contador(secs_d,"d",stop_loop)
            label_iter["text"] = (int(label_iter["text"]) + 1)
            label_trabajo["text"] = f"{hours_t:02d}:{mins_t:02d}:{sec_t:02d}"
            label_descanso["text"] = f"{hours_d:02d}:{mins_d:02d}:{sec_d:02d}"
            
        elif int(label_iter["text"]) >= iteraciones_cortas and iter_completa < iteraciones_largas:
            label_trabajo["text"] = "00:00:00"
            title_descanso["text"] = "Tiempo de\ndescanso largo: "
            contador(secs_d_l,"d_l",stop_loop)
            title_descanso["text"] = "Tiempo de\ndescanso: "
            iter_completa += 1
            label_iter_completa["text"] = "Iteraciones completas: "+ str(iter_completa)
            label_iter["text"] = 0
            label_trabajo["text"] = f"{hours_t:02d}:{mins_t:02d}:{sec_t:02d}"
            label_descanso["text"] = f"{hours_d:02d}:{mins_d:02d}:{sec_d:02d}"
               
    label_iter["text"] = 0
    label_trabajo["text"] = f"{hours_t:02d}:{mins_t:02d}:{sec_t:02d}"
    label_descanso["text"] = f"{hours_d:02d}:{mins_d:02d}:{sec_d:02d}"
    label_iter_completa["text"] = "Iteraciones completas: 0"
    
def stop():
    global stop_loop
    stop_loop = True
    
def edit():
    edit_win = Toplevel()
    edit_win.title("Edicion de parametros")
    edit_win.config(bg="#AFF7F0")
    
    frm_trabajo = LabelFrame(edit_win,text="Periodo de trabajo",bg="#AFF7F0")
    frm_trabajo.grid(row=0,column=0,columnspan=2,rowspan=2,ipady=3,ipadx=3)
    Label(frm_trabajo,text=f"Total de segundos\npor periodo de trabajo: ",font=("Helvetica",10),bg="#AFF7F0").grid(row=0,column=0)
    Label(frm_trabajo,text=f"Total a introducir (en segundos): ",font=("Helvetica",10),bg="#AFF7F0").grid(row=1,column=0)
    segundos_trab=StringVar()
    Entry(frm_trabajo,textvariable=segundos_trab,font=("Helvetica",10),state="disabled").grid(row=0,column=1)
    segundos_trab.set(f"{secs_t} segundos ")
    entry_trabajo = Entry(frm_trabajo,font=("Helvetica",10))
    entry_trabajo.grid(row=1,column=1)
    
    frm_descanso = LabelFrame(edit_win,text="Periodo de descanso corto",bg="#AFF7F0")
    frm_descanso.grid(row=2,column=0,columnspan=2,rowspan=2,ipady=3,ipadx=3)
    Label(frm_descanso,text=f"Total de segundos\npor periodo de descanso corto: ",font=("Helvetica",10),bg="#AFF7F0").grid(row=2,column=0)
    Label(frm_descanso,text=f"Total a introducir (en segundos): ",font=("Helvetica",10),bg="#AFF7F0").grid(row=3,column=0)
    segundos_d_c=StringVar()
    Entry(frm_descanso,textvariable=segundos_d_c,font=("Helvetica",10),state="disabled").grid(row=2,column=1)
    segundos_d_c.set(f"{secs_d} segundos ")
    entry_descanso = Entry(frm_descanso,font=("Helvetica",10))
    entry_descanso.grid(row=3,column=1)
    
    frm_descanso_l = LabelFrame(edit_win,text="Periodo de descanso largo",bg="#AFF7F0")
    frm_descanso_l.grid(row=4,column=0,columnspan=2,rowspan=2,ipady=3,ipadx=3)
    Label(frm_descanso_l,text=f"Total de segundos\npor periodo de descanso largo: ",font=("Helvetica",10),bg="#AFF7F0").grid(row=4,column=0)
    Label(frm_descanso_l,text=f"Total a introducir (en segundos): ",font=("Helvetica",10),bg="#AFF7F0").grid(row=5,column=0)
    segundos_d_l=StringVar()
    Entry(frm_descanso_l,textvariable=segundos_d_l,font=("Helvetica",10),state="disabled").grid(row=4,column=1)
    segundos_d_l.set(f"{secs_d_l} segundos ")
    entry_descanso_l = Entry(frm_descanso_l,font=("Helvetica",10))
    entry_descanso_l.grid(row=5,column=1)
    
    frm_iter_cort = LabelFrame(edit_win,text="Iteraciones cortas",bg="#AFF7F0")
    frm_iter_cort.grid(row=6,column=0,columnspan=2,rowspan=2,ipady=3,ipadx=3)    
    Label(frm_iter_cort,text=f"Cantidad anterior\ntotal de iteraciones cortas: ",font=("Helvetica",10),bg="#AFF7F0",width=24).grid(row=6,column=0)
    Label(frm_iter_cort,text=f"Cantidad a introducir: ",font=("Helvetica",10),width=24,bg="#AFF7F0").grid(row=7,column=0)
    iter_c=StringVar()
    Entry(frm_iter_cort,textvariable=iter_c,font=("Helvetica",10),state="disabled").grid(row=6,column=1)
    iter_c.set(str(iteraciones_cortas) + " iteraciones cortas")
    entry_iter_cort = Entry(frm_iter_cort,font=("Helvetica",10))
    entry_iter_cort.grid(row=7,column=1)
    
    frm_iter_largas = LabelFrame(edit_win,text="Iteraciones largas",bg="#AFF7F0")
    frm_iter_largas.grid(row=8,column=0,columnspan=2,rowspan=2,ipady=3,ipadx=3)
    Label(frm_iter_largas,text=f"Cantidad anterior de\niteraciones completas: ",font=("Helvetica",10),bg="#AFF7F0",width=24).grid(row=8,column=0)
    Label(frm_iter_largas,text=f"Cantidad a introducir: ",font=("Helvetica",10),width=24,bg="#AFF7F0").grid(row=9,column=0)
    iter_l=StringVar()
    Entry(frm_iter_largas,textvariable=iter_l,font=("Helvetica",10),state="disabled").grid(row=8,column=1)
    iter_l.set(str(iteraciones_largas) + " iteraciones largas")
    entry_iter_l = Entry(frm_iter_largas,font=("Helvetica",10))
    entry_iter_l.grid(row=9,column=1)    
    
    label_save = Label(edit_win,text="",font=("Helvetica",10,"bold"),bg="#AFF7F0")
    label_save.grid(row=10,column=0,columnspan=2)
    
    Button(edit_win,text="Guardar cambios",font=("Helvetica",10),bg="#7FFFAA",command=lambda:\
           guardar(entry_trabajo,entry_descanso,entry_descanso_l,entry_iter_cort,entry_iter_l,label_save,edit_win)).grid(row=11,column=0,columnspan=2)

def guardar(entry_trabajo,entry_descanso,entry_descanso_l,entry_iter_cort,entry_iter_l,label_save,edit_win):
    global secs_t,secs_d,secs_d_l,iteraciones_cortas,iteraciones_largas
    entries = [entry_trabajo,entry_descanso,entry_descanso_l,entry_iter_cort,entry_iter_l]
    
    data = [secs_t,secs_d,secs_d_l,iteraciones_cortas,iteraciones_largas]
    
    contador = 0
    if entry_trabajo.get()!= "": secs_t = int(entry_trabajo.get())
    if entry_descanso.get()!= "": secs_d = int(entry_descanso.get())
    if entry_descanso_l.get()!= "": secs_d_l =int(entry_descanso_l.get())
    if entry_iter_cort.get()!= "": iteraciones_cortas = int(entry_iter_cort.get())
    if entry_iter_l.get()!= "": iteraciones_largas = int(entry_iter_l.get())
        
    label_save["text"]="Datos modificados correctamente"
    root.update()

#INTERFACE
root = Tk()
frm = Frame(root,width=400,height=350,bg="#3090f8")
frm.grid(rowspan=7,columnspan=3)

#Labels
Label(root,text="POMODORO APP",font=("Helvetica",17,"bold"),bg="#3090f8").grid(row=0,column=1)
Label(root,text="Tiempo de \ntrabajo: ",font=("Helvetica",12),bg="#3090f8").grid(row=1,column=0,padx="15 0")
title_descanso = Label(root,text="Tiempo de \ndescanso: ",font=("Helvetica",12),bg="#3090f8")
title_descanso.grid(row=1,column=1,padx="0 0")
Label(root,text="Iteracion: ",font=("Helvetica",12),bg="#3090f8").grid(row=1,column=2,padx="0 10")

label_trabajo = Label(root,text=f"{hours_t:02d}:{mins_t:02d}:{sec_t:02d}",font=("Helvetica",11),bg="#FFFFAA",width=7)
label_trabajo.grid(row=2,column=0,sticky=N,padx="25 0")
label_descanso = Label(root,text=f"{hours_d:02d}:{mins_d:02d}:{sec_d:02d}",font=("Helvetica",11),bg="#FFFFAA",width=7)
label_descanso.grid(row=2,column=1,sticky=N,padx="0 0")
label_iter = Label(root,text=0,font=("Helvetica",11),bg="#FFFFAA",width=7)
label_iter.grid(row=2,column=2,sticky=N,padx="0 15")
label_iter_completa = Label(root,text="Iteraciones completas: 0",font=("Helvetica",12),bg="#3090f8")
label_iter_completa.grid(row=3,column=1)

#Buttons
Button(root,text="Iniciar sesion de \npomodoros",font=('Helvetica', 11),anchor="center",width=15,bg="#7FFFAA",fg="black",command=start_iteracion)\
                          .grid(row=4,column=1,padx=10)
Button(root,text="Editar",font=('Helvetica', 11),anchor="center",width=15,bg="#FFAA00",fg="black",command=edit)\
                          .grid(row=5,column=1,padx=10)
Button(root,text="Detener",font=('Helvetica', 11),anchor="center",width=15,bg="#FF2A55",fg="black",command=stop)\
                          .grid(row=6,column=1,padx=10)

root.title("Pomodoro App")
root.geometry("400x350+400+100")

root.mainloop()