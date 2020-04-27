from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

#窗口
root = Tk()
root.title('文本编辑器')
root.iconbitmap('textEer.ico')
root.geometry('1000x1000')

notebook =  Notebook(root)
#词典API
with open('words.txt') as f:
    dicts = f.read().split('\n')
#图片素材
saveimage = PhotoImage(file = 'save.gif')
saveimage2 = PhotoImage(file = 'new.gif')
saveasimage = PhotoImage(file = 'saveas.gif')
openimage = PhotoImage(file = 'open.gif')
upimage = PhotoImage(file = 'done.gif')
doneimage = PhotoImage(file = 'up.gif')

itr = 0
def New__(name = '',title = 'Untitled'):
    global dicts,saveimage,saveimage2,itr,openimage,upimage,doneimage
    frame = Frame(root)
    filename = title
    notebook.add(frame,text = filename)
    notebook.select(notebook.index(itr)) 
    itr+=1
    toll = Frame(frame,height = 20)
    toll.pack(side = TOP,fill = X)
    tag = True


    def famlis(evend = None):
        nonlocal tag
        try:
            f = Font(frame,family = familyVar.get())
            if tag:
                text.tag_add('big',SEL_FIRST,SEL_LAST)
                text.tag_config('big',font = f)
                tag = False
            else:
                text.tag_config('big',font = f)
        except:
            f = Font(frame,family = familyVar.get())
            text.configure(font = f)


    def weight(evend = None):
        
        try:
            f = Font(frame,weight = weightVar.get())
            if tag:
                text.tag_add('bigs',SEL_FIRST,SEL_LAST)
                text.tag_config('bigs',font = f)
            else:
                text.tag_config('bigs',font = f)
        except:
            f = Font(frame,weight = weightVar.get())
            text.configure(font = f)


    def sizeslen(evend = None):
        try:
            f = Font(frame,size = sizeVar.get())
            if tag:
                text.tag_add('big',SEL_FIRST,SEL_LAST)
                text.tag_config('big',font = f)
            else:
                text.tag_config('big',font = f)
        except:
            f = Font(frame,size = sizeVar.get())
            text.configure(font = f)


    def ztl(evend = None):
        try:
            a = text.index(INSERT).split('.')
            zt.config(text = 'ln:{0} co:{1}'.format(
                    *(
                    tuple
                        (
                            (a
                        )))))
            zt.after(100,ztl)
        except TclError:
            pass


    def cut(event = None):
        text.event_generate("<<Cut>>")


    def copy(event = None):
        text.event_generate("<<Copy>>")


    def paste(event = None):
        text.event_generate('<<Paste>>')


    def pop(event = None):
        popopmenu.post(event.x_root,event.y_root)


    def ondo(e = None):
        try:
            text.edit_undo()
        except:
            pass


    def redo(e = None):
        try:
            text.edit_redo()
        except:
            pass


    def fand(event = None):
        text.tag_remove("found",'1.0',END)
        start = "1.0"
        key = F.get()

        if (len(key.split()) == 0):
            return
        while 1:
            pos = text.search(key,start,END)
            if pos == "":
                break
            text.tag_add('found',pos,"%s+%dc"%(pos,len(key)))
            start = '%s+%dc'%(pos,len(key))
    

    def check(event = None):
        d = []
        for i in dicts:
            d.append(i.lower())
        def getindex(wordd):
            try:
                return d.index(wordd)
            except:
                return ''
        text.tag_remove('Error','1.0',END)
        textwords = text.get('1.0',END)
        chars = [']', '·', '：', '》', '>', 
                    '_', '"', '`', '，', '”', 
                    '×', '#', '}', '『', '|', 
                    ':', '<', '（', '?', '】', 
                    '\\', '!', '？', '(', '【', 
                    '《', '@', '=', '——', '$', 
                    '+', '%', '^', '*', ')', 
                    '&', '！', '’', '、', '/', 
                    '）', '￥', '』', ';', "'", 
                    '；', '[', ',', '.', '-', 
                    '……', '{', '。', '~', '～']
        start = '1.0'
        for i in chars:
	        textwords = textwords.replace(i,' ')
        textwords = textwords.split()
        for word in textwords:
            try:
                if (not getindex(word) and  not getindex(word.lower()) and not int(word)):
                    pos = text.search(word,start,END)
                    text.tag_add('Error',pos,"%s+%dc"%(pos,len(word)))
                    pos = '%s+%dc'%(pos,len(word))
            except:
                if (not getindex(word) and  not getindex(word.lower())):
                    pos = text.search(word,start,END)
                    text.tag_add('Error',pos,"%s+%dc"%(pos,len(word)))
                    pos = '%s+%dc'%(pos,len(word))
    

    def clean(event = None):
        text.tag_remove('Error','1.0',END)
        text.tag_remove("found",'1.0',END)


    def saveasButton():
        nonlocal filename
        textContent = text.get("1.0",END)
        filename = asksaveasfilename(title = 'save as')
        if filename == '':
            return
        with open(filename,"w") as output:
            output.write(textContent)
            notebook.tab(notebook.select(),text = filename)


    def newfile():
        New__()


    def Openfile():
        nonlocal filename
        filename = askopenfilename()
        if filename == '':
            return
        with open(filename,'r') as f:
            content = f.read()
        New__(content,filename)


    def save():
        nonlocal filename
        textContent = text.get("1.0",END)
        if (filename == 'Untitled'):
            saveasButton()
            print(filename)
        with open(filename,"w") as output:
            output.write(textContent)
            notebook.tab(notebook.select(),text = filename)
    #toolbox
    fr = Frame(toll)
    from tkinter import Button

    savebutton = Button(fr,image = saveimage,compound = TOP,text = 'save',command = save)
    savebutton.pack(side = LEFT)

    savebutton = Button(fr,image = saveasimage,compound = TOP,text = 'save as',command = saveasButton)
    savebutton.pack(side = LEFT)

    new_file = Button(fr,text = 'new file',command = newfile,image = saveimage2,compound = TOP)
    new_file.pack(side = LEFT)

    openfileButton = Button(fr,text = 'open',command = Openfile,image = openimage,compound = TOP)
    openfileButton.pack(side = LEFT)

    from tkinter.ttk import Button
    familyVar = StringVar(frame)
    Family = tuple(families(root))
    Family = list(Family)
    combo = Combobox(toll,textvariable = familyVar,value = Family)
    familyVar.set(Family[0])
    combo.bind('<<ComboboxSelected>>',famlis)

    weightVar = StringVar(frame)
    weightFamly = ("normal","bold")
    weightVar.set(weightFamly[0])
    wei = OptionMenu(toll,weightVar,*weightFamly,command = weight)

    sizeVar = IntVar(frame)
    sizeFamly = [i for i in range(8,30)]
    size = Combobox(toll,textvariable = sizeVar,width = 3)
    size['value'] = sizeFamly
    size.current(4) 
    size.bind('<<ComboboxSelected>>',sizeslen)

    up = Button(toll,image = upimage,command = ondo)
    dong = Button(toll,image = doneimage,command = redo)

    F = Entry(toll)
    L = Label(toll,text = '查找')
    F.bind('<Return>',fand)

    jianc = Button(toll,text = '检查',command = check)
    
    
    clenr = Button(toll,text = '清除标记',command = clean)
    
    
#文本框
    sb = Scrollbar(frame)
    sb.pack(side="right", fill="y")
    
    zt = Label(frame,text = (' '*(root.winfo_screenwidth()-3000))+'ln:1 co:0',background = 'white',foreground = 'black')
    zt.pack(fill ='both')

    text = Text(frame,undo = True,height = 45,yscrollcommand=sb.set,wrap = 'none',insertofftime = 500,insertontime= 500)
    text.pack(fill = BOTH,expand = TRUE)
    sb.config(command=text.yview)

    text.tag_config('Error',foreground = 'red')
    text.tag_configure('found',background = "yellow")
    text.insert(END,name)

    popopmenu = Menu(text,tearoff = False)
    popopmenu.add_command(label = '复制',command = copy)
    popopmenu.add_command(label = '剪贴',command = cut)
    popopmenu.add_command(label = '贴粘',command = paste)
    text.bind('<Button-3>',pop)

    #布局
    fr.grid(row = 0,rowspan =2,sticky = W+E+N+S,padx = 5,pady = 2)
    size.grid(row = 0,column = 1+5,sticky = W+E,pady = 2,padx = 5)
    wei.grid(row = 0,column = 0+5,sticky = W+E,pady = 2,padx = 5)
    combo.grid(row = 1,columnspan = 2,column = 0+5,sticky = W+E,pady = 2)
    up.grid(row = 0,column = 2,sticky = W+E,padx = 5,pady = 2)
    dong.grid(row = 1,column = 2,sticky = W+E,padx = 5,pady = 2)
    L.grid(row = 0,column = 3+5,pady = 2)
    F.grid(row = 0,column = 4+5,columnspan = 2,sticky = W+E,padx = 5,pady = 2)
    jianc.grid(row = 1,column = 3+5,columnspan = 2)
    clenr.grid(row = 1,column = 5+5)
    ztl()
#创建页签对象
New__()

notebook.pack(expand = TRUE,fill = BOTH)
root.mainloop()