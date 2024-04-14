from PyPDF2 import PdfReader , PdfWriter 
from typing import Annotated
import os
import tkinter as tk
from tkinter import ttk
import threading
from tkinter import messagebox
from tkinter import filedialog



def write_pdf_file(file:Annotated[str , "veuillez entrez le chemin du fichier "],
                   nombre_page : Annotated[int , "nombre de maximun de page pour un division "] = 0 ,
                   name:str = "doc") ->any:
    

    INIT_VALUE = 0
    
    print("ici")
    if os.path.exists(file): 
        
        
        print("ici 2")
        reader = PdfReader(stream=file)
          
        nb_page = len(reader.pages)
        progressbar["maximum"] = nb_page
        compteur =  INIT_VALUE
        compteur_max = INIT_VALUE
        nb_fichier = []
        
        print("ici 3")
        while nb_page > 0 :
            
            if nb_page > nombre_page :
                nb_fichier.append(int(nombre_page))
            else:
                nb_fichier.append(nb_page) 
                
            nb_page = nb_page - nombre_page        
            
            
        print(nb_fichier)
        
        for nombre in nb_fichier:

                
            writer = PdfWriter()
            
            compteur = compteur_max    
            compteur_max +=nombre
            
            for n in range(compteur,compteur_max): 
                
                
                progressbar["value"] = n
                writer.add_page(reader.pages[n])
                root.update()

                
            
            writer.write(f'{name}/{name.split("/")[-1]}  {compteur }-{compteur_max}.pdf')
            writer.close()
            var.set(f'{name} {compteur }-{compteur_max}.pdf')
            root.update()
                
        messagebox.showinfo("PROCESS" , " PROCESS DONE ")    
        progressbar.stop()
        btn_v["state"]= "normal"
        btn_v["text"]= "Start"
        entry.delete(0,tk.END)
        entry.insert(0,0)
        
        entry1.delete(0,tk.END)
        entry1.insert(0,"")
        
        entry2.delete(0,tk.END)
        entry2.insert(0,"")
        
        var.set("")
           
                # print(page.extract_text())

def start_task():
    # Start the long-running task in a separate thread
    threading.Thread(target=func).start()                
                
def func():                
    
    if btn_v["text"] == "Start" :
        
        btn_v["text"] = "Loading.."    
        btn_v["disabledforeground"] = "white"    
        btn_v["state"] = "disabled" 
        progressbar.pack(side=tk.BOTTOM , pady=25,padx=30)   
        write_pdf_file(entry1.get(),int(entry.get()),entry2.get())
        
def get_file():
    entry1.delete(0,tk.END)
    entry1.insert(0,filedialog.askopenfile().name)
    
def get_directory():
    entry2.delete(0,tk.END)
    entry2.insert(0,filedialog.askdirectory())

def up():
    global value
    value+=1
    entry.delete(0,tk.END)
    entry.insert(0,value)  
          
def down():
    global value
    if value>0:
        value-=1
        entry.delete(0,tk.END)
        entry.insert(0,value)        
    
    
     
PATH = ""
NAME = "pdf_cut"
value = 0

if __name__ == "__main__":
    
    # write_pdf_file(PATH,PAGES,NAME)
        

    root = tk.Tk() 
    fond = tk.PhotoImage(file ="c:/Users/CoderSpirit/Documents/Archive[2022, 2024]/PDF_FILE_CUT/Assets./pdf_bg_2.png") 
    root.geometry("600x350")   
    root.resizable(False,False)
    var = tk.StringVar()
    var.set("")
    
    lb_fond = tk.Label(root , image= fond)
    lb_fond.place(x=0,y=0,relheight=1,relwidth=1)
    
    conteneur = tk.Frame(root, bg="#FE5252")
    conteneur.pack(side=tk.TOP , fill=tk.X , padx=50, pady=20)
    
    titre = tk.Label(conteneur, text="PDF FILE CUT" , bg ="#FE5252",font=("ARIAL",20,"bold"), fg="white")
    titre.pack()
    
    conteneur_1 = tk.Frame(root , bg= "#FE5252")
    conteneur_1.pack(pady=20)

    
    conteneur_2 = tk.Frame(root, bg= "#FE5252")
    conteneur_2.pack(pady=20)
    
    conteneur_3 = tk.Frame(root, bg= "#FE5252")
    conteneur_3.pack(pady=20)
    
    lb_entry1= tk.Label(conteneur_1, text ="select pdf file",width=18, bg= "#FE5252")
    lb_entry1.pack(side=tk.LEFT)
    
    entry1 = tk.Entry(conteneur_1,width=30)
    entry1.pack(side=tk.LEFT)
    
    btn_parcourir = tk.Button(conteneur_1 , text= "▼",command=get_file)
    btn_parcourir.pack(side=tk.LEFT)
    
    lb_page= tk.Label(root, text ="set files number ", bg= "#FE5252")
    lb_page.place(relx=0.30,rely=0.40 ,anchor=tk.CENTER)
    
    entry = tk.Entry(root,width=10 ,font=("AREAL",15) )
    entry.place(relx=0.60,rely=0.40 ,anchor=tk.CENTER)
    entry.insert(0 ,value)
    
    
    btn_up= tk.Button(root , text= "▲",command=up)
    btn_up.place(relx=0.72,rely=0.40 ,anchor=tk.CENTER )
    
    btn_down= tk.Button(root , text= "▼",command=down)
    btn_down.place(relx=0.76,rely=0.40 ,anchor=tk.CENTER)
    
    
    lb_entry2= tk.Label(conteneur_2, text ="select the output folder", bg= "#FE5252")
    lb_entry2.pack(side=tk.LEFT)
    
    entry2 = tk.Entry(conteneur_2,width=30)
    entry2.pack(side=tk.LEFT)
    
    btn_parcourir2 = tk.Button(conteneur_2 , text= "▼",command=get_directory)
    btn_parcourir2.pack(side=tk.LEFT)
    
    
    
    label = tk.Label(root , textvariable= var, bg= "#DA1B1B")
    label.place(relx=0.5, rely=0.8 ,anchor=tk.CENTER)
    
    btn_v = tk.Button(conteneur_3 , text="Start" , command= start_task,
                      font=('COLLIBRI',12,"bold"), bg="green", width=20,
                      fg="white"
                      )
    btn_v.pack()
    
 
    
    progressbar = ttk.Progressbar(root,value=0 , length=500)

    copyright_ = tk.Label(root , text="by ©sam15olala@gmail.com", bg= "#D71112")
    copyright_.place(relx=1, rely=1 ,anchor=tk.SE)
    
    messagebox.showinfo("UTILISATION",
                        "ATTENTION CE PROGRAMME NE GEREE PAS D ERREUR DONC VEUILLEZ INSERER LES CHAMPS EN RESPECTANT LES TYPES  ")
    root.mainloop() 
