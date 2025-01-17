from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import  ImageTk,Image
from PyDictionary import PyDictionary
from googletrans import Translator


root=tk.Tk()
root.title('My Dictionary')
root.geometry('600x300')
root['bg']='white'
frame=Frame(root,width=200,height=300,borderwidth=1,relief=RIDGE)
frame.grid(sticky='W')

def get_meaning():
    dictionary=PyDictionary()
    get_word=entry.get()
    languages=language.get()
    
    if get_word =='':
        messagebox.showerror('Dictionary','Please write the word')
    
    elif languages == 'English-to-English':
        d=dictionary.meaning(get_word)
        output.insert('end',d['Noun'])
    elif languages == 'English-to-Hindi':
        translator=Translator()
        t=translator.translate(get_word,dest='hi')
        output.insert('end',t.text)

def quit():
    root.destroy()
    
img=ImageTk.PhotoImage(Image.open('dic.png'))
pic=Label(root,image=img)
pic.place(x=0,y=30)
word=Label(root,text='Enter word',bg='white',font=('verdana',10,'bold'))
word.place(x=250,y=23)
a=tk.StringVar()
language=ttk.Combobox(root,width=20,textvariable=a,state='readonly',font=('verdana',10,'bold'))

language['values']=('English-to-English','English-to-Hindi')
language.place(x=380,y=10)
language.current(0)

entry=Entry(root,width=50,borderwidth=2,relief=RIDGE)
entry.place(x=250,y=50)

search=Button(root,text='Search',font=('verdana',10,'bold'),cursor='hand2',relief=RIDGE,command=get_meaning)
search.place(x=380,y=80)

quit=Button(root,text='Quit',font=('verdana',10,'bold'),cursor='hand2',relief=RIDGE,command=quit)
quit.place(x=450,y=80)

meaning=Label(root,text='Meaning',bg='white',font=('verdana',12,'bold'))
meaning.place(x=230,y=120)

output=Text(root,height=8,width=40,borderwidth=3,relief=RIDGE)
output.place(x=230,y=160)

root.mainloop()
