import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk


def Gen():
    txt.configure(state='normal')
    j = int(np.random.randint(0,len(lastname),1).astype(int))
    k = int(np.random.randint(0,len(firstname),1).astype(int))
    if (n1.get()!="") & (n2.get()!=""):
        n1_get = n1.get().strip('\n').replace('\n','')
        n2_get = n2.get().strip('\n').replace('\n','')
        txt.insert(INSERT, n1_get+n2_get+'\n')
    elif n1.get()!="":
        n1_get = n1.get().strip('\n').replace('\n','')
        nn1 = firstname[k]
        txt.insert(INSERT, n1_get+nn1+'\n')
    elif n2.get()!="":
        n2_get = n2.get().strip('\n').replace('\n','')
        nn2 = lastname[j]
        txt.insert(INSERT, nn2+n2_get+'\n')
    else:
        nnn = lastname[j] + firstname[k]
        txt.insert(INSERT, nnn+'\n')
    txt.configure(state='disabled')
        #txt.insert(INSERT, str(lastname.iloc[num_r1,0].values+firstname.iloc[num_r2,0].values)+'\n')
        

def RandomGen():
    txt.configure(state='normal')
    e1.delete(0,"end")
    e2.delete(0,"end")
    j = int(np.random.randint(0,len(lastname),1).astype(int))
    k = int(np.random.randint(0,len(firstname),1).astype(int))
    nnn = lastname[j] + firstname[k]
    txt.insert(INSERT, nnn+'\n')
    txt.configure(state='disabled')

def Gen_more_10():
    txt.configure(state='normal')
    i = 0
    while i < 10:
        j = int(np.random.randint(0,len(lastname),1).astype(int))
        k = int(np.random.randint(0,len(firstname),1).astype(int))
        if (n1.get()!="") & (n2.get()!=""):
            n1_get = n1.get().strip('\n').replace('\n','')
            n2_get = n2.get().strip('\n').replace('\n','')
            txt.insert(INSERT, n1_get+n2_get+'\n')
        elif n1.get()!="":
            n1_get = n1.get().strip('\n').replace('\n','')
            nn1 = firstname[k]
            txt.insert(INSERT, n1_get+nn1+'\n')
        elif n2.get()!="":
            n2_get = n2.get().strip('\n').replace('\n','')
            nn2 = lastname[j]
            txt.insert(INSERT, nn2+n2_get+'\n')
        else:
            nnn = lastname[j] + firstname[k]
            txt.insert(INSERT, nnn+'\n')
        i += 1
        if i >= 10:
            break
    txt.configure(state='disabled')

def Gen_more_50():
    txt.configure(state='normal')
    i = 0
    while i < 50:
        j = int(np.random.randint(0,len(lastname),1).astype(int))
        k = int(np.random.randint(0,len(firstname),1).astype(int))
        if (n1.get()!="") & (n2.get()!=""):
            n1_get = n1.get().strip('\n').replace('\n','')
            n2_get = n2.get().strip('\n').replace('\n','')
            txt.insert(INSERT, n1_get+n2_get+'\n')
        elif n1.get()!="":
            n1_get = n1.get().strip('\n').replace('\n','')
            nn1 = firstname[k]
            txt.insert(INSERT, n1_get+nn1+'\n')
        elif n2.get()!="":
            n2_get = n2.get().strip('\n').replace('\n','')
            nn2 = lastname[j]
            txt.insert(INSERT, nn2+n2_get+'\n')
        else:
            nnn = lastname[j] + firstname[k]
            txt.insert(INSERT, nnn+'\n')
        i += 1
        if i >= 50:
            break
    txt.configure(state='disabled')

def delete_all():
    txt.configure(state='normal')
    txt.delete(1.0, "end")  
    txt.configure(state='disabled')

lastname = pd.read_table("./data/lastname.txt",encoding="utf-8-sig")
firstname = pd.read_table("./data/firstname.txt",encoding="utf-8-sig")
#print(len(firstname))
#print(list(lastname.iloc[0,0]),list(firstname.iloc[3,0]))
#print(str(lastname.iloc[0,0])+str(firstname.iloc[3,0]))
#print(list(lastname.iloc[:,0]))
lastname_s = list(lastname.iloc[:,0])
firstname_s = list(firstname.iloc[:,0])
lastname = list(); firstname = list()
for l_name in lastname_s:
    l_name = l_name.strip(' ')
    lastname.append(l_name)
for f_name in firstname_s:
    f_name = f_name.strip(' ')
    firstname.append(f_name)
#print(lastname[1])
#print(type(firstname))


window = Tk()
window.title("Mandarin Chinese Name Generater")
window.geometry("720x480")


p1 = PhotoImage(file = 'icon.png')
# Setting icon of master window
window.iconphoto(False, p1)

label = Label(window, text = "Mandarin Chinese Name Generater",
              bg = '#bf0d3e',
              fg= '#041e42',
              width=48,
              font='DFKai-SB 22 bold')  # 'DFKai-SB mingLiu', 'PopularGivenNamesGenCN'
label.place(x=0,y=0)
window.resizable(0,0)
label2 = Label(window, text = "This program is made for generating Chinese names.")
label2.place(x=10,y=40)
label3 = Label(window, text = "Please assugn a Chinese lastname:")
label3.place(x=10,y=65)
label4 = Label(window, text = "Please assign a Chinese firstname:")
label4.place(x=10,y=90)

n1 = StringVar()
n2 = StringVar()
e1 = ttk.Entry(window,textvariable = n1)
e2 = ttk.Entry(window,textvariable = n2)
e1.insert(1,"王")
e2.insert(1,"小明")
e1.place(x=210,y=65)
e2.place(x=210,y=90)

txt = Text(window,font=(['Microsoft JhengHei','10']),height=20,width=70)
txt.place(x=20,y=120)
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)
txt.configure(state='disabled')

btn0 = ttk.Button(window,text = "Generate",width=10,command = Gen)
btn1 = ttk.Button(window,text = "Random",width=10,command = RandomGen)
btn2 = ttk.Button(window,text = "Clear",width=10,command = delete_all)
btn3 = ttk.Button(window,text = "Batch (10)",width=10,command = Gen_more_10)
btn4 = ttk.Button(window,text = "Batch (50)",width=10,command = Gen_more_50)
btn5 = ttk.Button(window,text = "Exit",width=10,command = window.destroy)

btn0.place(x=600,y=150)
btn1.place(x=600,y=200)
btn2.place(x=600,y=250)
btn3.place(x=600,y=300)
btn4.place(x=600,y=350)
btn5.place(x=600,y=400)

# define function to cut
# the selected text
def cut_text_2():
    e1.event_generate(("<<Cut>>"))
def cut_text_3():
    e2.event_generate(("<<Cut>>"))

# define function to copy
# the selected text
def copy_text_1():
    txt.event_generate(("<<Copy>>"))
def copy_text_2():
    e1.event_generate(("<<Copy>>"))
def copy_text_3():
    e2.event_generate(("<<Copy>>"))

# define function to paste
# the previously copied text
def paste_text_2():
    e1.event_generate(("<<Paste>>"))
def paste_text_3():
    e2.event_generate(("<<Paste>>"))
    

# create menubar
menu_1 = Menu(window, tearoff = 0)
menu_1.add_command(label="Copy", command=copy_text_1)

menu_2 = Menu(window, tearoff = 0)
menu_2.add_command(label="Cut", command=cut_text_2)
menu_2.add_command(label="Copy", command=copy_text_2)
menu_2.add_command(label="Paste", command=paste_text_2)

menu_3 = Menu(window, tearoff = 0)
menu_3.add_command(label="Cut", command=cut_text_3)
menu_3.add_command(label="Copy", command=copy_text_3)
menu_3.add_command(label="Paste", command=paste_text_3)

# define function to popup the
# context menu on right button click
def context_menu_1(event):
    try:
        menu_1.tk_popup(event.x_root, event.y_root)
    finally:
        menu_1.grab_release()

def context_menu_2(event):
    try:
        menu_2.tk_popup(event.x_root, event.y_root)
    finally:
        menu_2.grab_release()
        
def context_menu_3(event):
    try:
        menu_3.tk_popup(event.x_root, event.y_root)
    finally:
        menu_3.grab_release()

        
# binding right click button to root
txt.bind("<Button-3>", context_menu_1)
e1.bind("<Button-3>", context_menu_2)
e2.bind("<Button-3>", context_menu_3)

window.mainloop()

