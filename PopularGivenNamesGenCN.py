import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


def Gen():
    txt.configure(state='normal')
    j = int(np.random.randint(0,len(lastname),1).astype(int))
    k = int(np.random.randint(0,len(firstname),1).astype(int))
    if (n1.get()!="") & (n2.get()!=""):
        txt.insert(INSERT, n1.get()+n2.get()+'\n')
    elif n1.get()!="":
        nn1 = firstname[k]
        txt.insert(INSERT, n1.get()+nn1+'\n')
    elif n2.get()!="":
        nn2 = lastname[j]
        txt.insert(INSERT, nn2+n2.get()+'\n')
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
            txt.insert(INSERT, n1.get()+n2.get()+'\n')
        elif n1.get()!="":
            nn1 = firstname[k]
            txt.insert(INSERT, n1.get()+nn1+'\n')
        elif n2.get()!="":
            nn2 = lastname[j]
            txt.insert(INSERT, nn2+n2.get()+'\n')
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
            txt.insert(INSERT, n1.get()+n2.get()+'\n')
        elif n1.get()!="":
            nn1 = firstname[k]
            txt.insert(INSERT, n1.get()+nn1+'\n')
        elif n2.get()!="":
            nn2 = lastname[j]
            txt.insert(INSERT, nn2+n2.get()+'\n')
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
lastname = list(lastname.iloc[:,0])
firstname = list(firstname.iloc[:,0])
#print(lastname[1])
#print(type(firstname))


window = Tk()
window.title("菜市場名生成")
window.geometry("720x480")

label = Label(window, text = "菜市場名生成",
              bg = "saddlebrown",
              fg= "gold",
              width=48,
              font='DFKai-SB 22')  # 'DFKai-SB mingLiu', 'PopularGivenNamesGenCN'
label.place(x=0,y=0)
window.resizable(0,0)
label2 = Label(window, text = "本程式是用於生成隨機中文人名的產生器。")
label2.place(x=10,y=40)
label3 = Label(window, text = "請指定姓氏：")
label3.place(x=10,y=65)
label4 = Label(window, text = "請指定名字：")
label4.place(x=10,y=90)

n1 = StringVar()
n2 = StringVar()
e1 = ttk.Entry(window,textvariable = n1)
e2 = ttk.Entry(window,textvariable = n2)
e1.insert(1,"王")
e2.insert(1,"小明")
e1.place(x=90,y=65)
e2.place(x=90,y=90)

txt = Text(window,height=25,width=80)
txt.place(x=20,y=120)
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)
txt.configure(state='disabled')

btn0 = ttk.Button(window,text = "產生",width=10,command = Gen)
btn1 = ttk.Button(window,text = "隨機",width=10,command = RandomGen)
btn2 = ttk.Button(window,text = "清除",width=10,command = delete_all)
btn3 = ttk.Button(window,text = "大量(10)",width=10,command = Gen_more_10)
btn4 = ttk.Button(window,text = "大量(50)",width=10,command = Gen_more_50)
btn5 = ttk.Button(window,text = "離開",width=10,command = window.destroy)

btn0.place(x=600,y=150)
btn1.place(x=600,y=200)
btn2.place(x=600,y=250)
btn3.place(x=600,y=300)
btn4.place(x=600,y=350)
btn5.place(x=600,y=400)

window.mainloop()

