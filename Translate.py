from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type",scr="auto",des="kn"):
    txt=text
    Scr=scr
    Des=des
    trans=Translator()
    transl1 = trans.translate(txt, src=Scr, dest=Des)
    return transl1.text


def data():
    s=comb_lang.get()
    d=comb_Resu.get()
    mess=sur_txt.get(1.0,END)
    textget=change(text=mess,scr=s,des=d)
    dest_Txt.delete(1.0,END)
    dest_Txt.insert(END,textget)

root=Tk()
root.title("Translator App")
root.geometry("500x600")
root.config(bg="gray")
lab_text = Label(root, text="Translator",  font=("Arial", 30, "bold"),fg="#2c3e50",bg="gray", bd=1,relief="solid")
lab_text.place(x=100, y=40, height=50, width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_text = Label(root, text="Source Text",  font=("Arial", 12, "bold"),fg="black",bg="gray") 
lab_text.place(x=1, y=115, height=25, width=110) 

sur_txt=Text(frame, font=("Arial", 12), height=8, wrap=WORD, padx=5, pady=5)
sur_txt.place(x=10, y=140, height=120, width=480)

list_Lang=list(LANGUAGES.values())
comb_lang=ttk.Combobox(frame,value=list_Lang)
comb_lang.place(x=10,y=270,height=30,width=150)
comb_lang.set("English") 

Button_change=Button(frame,text="Translate",relief=RAISED,command=data)
Button_change.place(x=175,y=270,height=30,width=150)

comb_Resu=ttk.Combobox(frame,value=list_Lang)
comb_Resu.place(x=339,y=270,height=30,width=150)
comb_Resu.set("kannada") 

lab_text = Label(root, text="Translated Text",  font=("Arial", 12, "bold"),fg="black",bg="gray") 
lab_text.place(x=1, y=320, height=25, width=140)

dest_Txt=Text(frame, font=("Arial", 12), height=8, wrap=WORD, padx=5, pady=5)
dest_Txt.place(x=10, y=350, height=90, width=480)

root.mainloop()

