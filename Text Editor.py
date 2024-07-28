from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Text Editor")

upper_line = Frame(root) 

to_find = Entry(upper_line) 
to_find.pack(side = LEFT, fill = BOTH, expand = 1) 
  
Search = Button(upper_line, text ='Search')
Search.pack(side = LEFT)
 
to_replace = Entry(upper_line)
to_replace.pack(side = LEFT, fill = BOTH, expand = 1)
 
Replace = Button(upper_line, text = 'Replace')
Replace.pack(side = LEFT)
 
upper_line.pack(side = TOP) 

text = Text(root, width=100, height=50)
text.insert('1.0', '''''') 
text.pack(side = BOTTOM) 

name = "Untitled.txt"

def find(): 

    text.tag_remove('found', '1.0', END)               

    thing_to_search = to_find.get()
     
    if (thing_to_search): 
        idx = '1.0'
        while 1: 

            idx = text.search(thing_to_search, idx, nocase = 1, 
                            stopindex = END)
             
            if not idx: break
  
            lastidx = '% s+% dc' % (idx, len(thing_to_search))
             
 

            text.tag_add('found', idx, lastidx) 
            idx = lastidx 
 

         
        text.tag_config('found', foreground ='red')
    to_find.focus_set()
 
def findNreplace(): 
     

    text.tag_remove('found', '1.0', END) 

    thing_to_search = to_find.get()
    thing_to_replace = to_replace.get()
     
    if (s and r): 
        idx = '1.0'
        while 1: 
     
            idx = text.search(thing_to_search, idx, nocase = 1, 
                            stopindex = END)
            print(idx)
            if not idx: break
             

            lastidx = '% s+% dc' % (idx, len(thing_to_search))
 
            text.delete(idx, lastidx)
            text.insert(idx, thing_to_replace)
 
            lastidx = '% s+% dc' % (idx, len(thing_to_replace))
             

            text.tag_add('found', idx, lastidx) 
            idx = lastidx 
 

        text.tag_config('found', foreground ='green', background = 'yellow')
    to_find.focus_set()
 
def MakeNewFile():
    global name
    root.title("Untitled")
    text.delete("1.0", END)

def Open():
    global name
    f = filedialog.askopenfile(mode="r")
    if f is None:
        return
    t = f.read()
    text.delete("1.0", END)
    text.insert("1.0", t)
    name = f.name
    f.close()
    
def Save():
    f = open(name, "w")
    f.write(text.get("1.0", END))
    f.close()

def SaveAs():
    global name 
    f = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    if f is None:
        return
    t = text.get("1.0", END)
    f.write(t)
    f.close()
    name = f.name


                 
Search.config(command = find)
Replace.config(command = findNreplace)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=MakeNewFile)
filemenu.add_command(label='Open', command=Open)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
filemenu.add_command(label='Save', command=Save)
filemenu.add_command(label='Save As', command=SaveAs)

root.mainloop()

