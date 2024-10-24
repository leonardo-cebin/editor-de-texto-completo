from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from functools import partial
from pathlib import Path
import os

def cgfg():
    cor = colorchooser.askcolor()
    cor = cor[1]
    text.config(fg=cor)
def cgbg():
    cor = colorchooser.askcolor()
    cor = cor[1]
    text.config(bg=cor)
def terminalTheme():
    text.config(bg='black')
    text.config(fg='#00FF00')
def changefont(font):
    text.config(font=font)

def newfile(event):
    text.delete(1.0,END)

def save(event):
    try:
        dados = str(text.get(1.0,END))
        file = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text files",".txt"),("Sorria, você está sendo filmado",".bin"),("All files",".*")])
        file.write(dados)   #simples assim

        #window.title(str(os.path.basename(file)) + ' - Bloco de Notas')
        file.close()  #essencial
    except AttributeError:
        return 0

def load(event):
    try:
         newfile(0)
         nome = filedialog.askopenfilename(filetypes=(("text files","*.txt"),("all files","*.*")))
         file = open(nome,'r')
         global informacao
         informacao = file.read()
         text.insert(END, informacao)
         window.title(str(Path(nome).stem) + ' - Bloco de Notas')
         file.close()
    except FileNotFoundError:
         return 0
    except UnicodeDecodeError:
         messagebox.showwarning(title="Erro", message="Parece que você tentou abrir um arquivo não suportado pelo software. O software foi construído para abrir arquivos de text (.txt)")
         return 0
def fechar():
    if messagebox.askokcancel(title="Confirmação",message="Tem certeza mesmo que quer sair do programa?",icon='question'): quit()

def copy():
    text.event_generate('<<Copy>>')
def cutit():
    text.event_generate('<<Cut>>')
def pasteit():
    text.event_generate('<<Paste>>')

def selectall():
    text.event_generate('<<SelectAll>>')


# A interface começa aqui
window = Tk()
window.title("Bloco de Notas")
#icon = PhotoImage(file="note.png")  #APENAS PNG
#window.iconphoto(True,icon) #Icone
window.iconbitmap('bin.ico')    #muito mais preferível do que usar PNG, pois ICO é vetorizável e muito mais apropriado também

#pepe = PhotoImage(file="pepe.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Arquivos",menu=fileMenu)
fileMenu.add_command(label="Limpar (F1)",command=partial(newfile,0))
fileMenu.add_command(label="Abrir (F9)",command=partial(load,0))
fileMenu.add_command(label="Salvar (F6)",command=partial(save,0))
fileMenu.add_separator()
fileMenu.add_command(label="Fechar",command=fechar)

fontMenu = Menu(window,tearoff=0)
editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Editar",menu=editMenu)
editMenu.add_command(label="Mudar cor da fonte",command=cgfg)
editMenu.add_command(label="Mudar cor de fundo",command=cgbg)
editMenu.add_command(label="Tema: Terminal", command=terminalTheme)
editMenu.add_separator()
editMenu.add_cascade(label="Fonte",menu=fontMenu)


for f in range(len(listaFontes := font.families())): fontMenu.add_command(label=listaFontes[f], font=(listaFontes[f],12), command=partial(changefont, (listaFontes[f], 20)))

editMenu.add_separator()
editMenu.add_command(label="Cortar ✂️",command=cutit)
editMenu.add_command(label="Copiar 🖇️",command=copy)
editMenu.add_command(label="Colar 🍼",command=pasteit)
editMenu.add_command(label="Selecionar tudo",command=selectall)

infobox = lambda: messagebox.showinfo('Bloco de Notas/Editor de Texto','Este protótipo de software foi desenvolvido por Leonardo "Pepe Silvia" Cebin como parte de seu projeto de aprendizado em Python, demonstrando através do mesmo capacidades de desenvolvimento Tkinter.\n\nFeito em junho de 2024')

aboutMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Sobre",menu=aboutMenu)
aboutMenu.add_command(label="Contact",command=infobox)

text = Text(window,font=("Arial",20),bg="light yellow",padx=10,pady=10)
text.pack(fill = "both", expand = True,side=TOP)    #the arguments in the pack function garantee that text will expand

#scrollbar = Scrollbar(text)
#scrollbar.pack(side='right', fill='y', expand=False)
#text.config(yscrollcommand=scrollbar.set)

footer = Label(window,text="2024 Made by Pepe 👌",font=("Courier New",9),bg="#CCCCCC",bd=4,relief=RIDGE,padx=10,pady=15,anchor="e")
footer.pack(fill = "x", expand = True, side=BOTTOM)

window.bind("<F6>", save)
window.bind("<F9>", load)
window.bind("<F1>", newfile)

window.geometry('800x600')
window.eval('tk::PlaceWindow . center')    #very useful line!!!
window.mainloop()