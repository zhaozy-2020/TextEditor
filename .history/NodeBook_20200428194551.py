from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

#窗口
root = Tk()
root.title('文本编辑器')
root.iconbitmap('textEer.ico')
root.geometry('1200x600+0+0')

notebook =  Notebook(root)
#词典API
with open('words.txt') as f:
    dicts = f.read().split('\n')
import sys
sys.path.append('E:/zzy/git/TextEditor')
import words
dict2=words.word
#图片素材
saveimage = PhotoImage(file = 'save.gif')
saveimage2 = PhotoImage(file = 'new.gif')
saveasimage = PhotoImage(file = 'saveas.gif')
openimage = PhotoImage(file = 'open.gif')
upimage = PhotoImage(file = 'done.gif')
doneimage = PhotoImage(file = 'up.gif')

itr = 0
def New__(name = '',title = 'Untitled'):
    global dicts,saveimage,saveimage2,itr,openimage,upimage,doneimage,dict2
    frame = Frame(root)
    filename = title
    notebook.add(frame,text = filename)
    # notebook.select(notebook.index(itr)) 
    # itr+=1
    toll = Frame(frame,height = 20)
    toll.pack(side = TOP,fill = X)
    tag = True


    def famlis(evend = None):
        nonlocal tag
        try:
            f = Font(frame,family = familyVar.get(),weight = weightVar.get(),size = sizeVar.get())
            text.tag_add('big',SEL_FIRST,SEL_LAST)
            text.tag_config('big',font = f)
        except:
            f = Font(frame,family = familyVar.get())
            text.configure(font = f)


    def weight(evend = None):
        
        try:
            if weightVar.get() == ITALIC:
                f = Font(frame,family = familyVar.get(),slant = weightVar.get(),size = sizeVar.get())
            else:
                f = Font(frame,family = familyVar.get(),weight = weightVar.get(),size = sizeVar.get())
            text.tag_add('big',SEL_FIRST,SEL_LAST)
            text.tag_config('big',font = f)
        except:
            if weightVar.get() == ITALIC:
                f = Font(frame,family = familyVar.get(),slant = weightVar.get(),size = sizeVar.get())
            else:
                f = Font(frame,family = familyVar.get(),weight = weightVar.get(),size = sizeVar.get())
            text.configure(font = f)


    def sizeslen(evend = None):
        try:
            f = Font(frame,size = sizeVar.get())
            text.tag_add('big',SEL_FIRST,SEL_LAST)
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
            if notebook.select() == '':
                root.destroy()
            root.update()
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
                for i in word:
                    if i in dict2:
                        pass
                    else:
                        return ''
                return 's'
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


    def hide(event = None):
        notebook.forget(notebook.select())


    def LnOrNone(event = None):
        if lnVar.get() == 1:
            text.configure(wrap = 'char')
        else:
            text.configure(wrap = 'none')

    def color_b(event = None):
        from tkinter import colorchooser
        fileName = colorchooser.askcolor(title = '背景颜色')
        if fileName[0] == None and fileName[1] == None:
            return None
        def col(t):
            return '#%02X%02X%02X' %(int(t[0]), int(t[1]), int(t[2]))
        text.configure(bg = col(fileName[0]))
        lebel_b.configure(background = col(fileName[0]))
    def color_f(event = None):
        from tkinter import colorchooser
        fileName = colorchooser.askcolor(title = '文字颜色')
        if fileName[0] == None and fileName[1] == None:
            return None
        def col(t):
            return '#%02X%02X%02X' %(int(t[0]), int(t[1]), int(t[2]))
        text.configure(fg =  col(fileName[0]))
        lebel_f.configure(background =  col(fileName[0]))
    def color_cursor(event = None):
        from tkinter import colorchooser
        fileName = colorchooser.askcolor(title = '光标颜色')
        if fileName[0] == None and fileName[1] == None:
            return None
        def col(t):
            return '#%02X%02X%02X' %(int(t[0]), int(t[1]), int(t[2]))
        text.configure(insertbackground =  col(fileName[0]))
        lebel_c.configure(background =  col(fileName[0]))
    #toolbox
    fr = Frame(toll)
    from tkinter import Label
    
    from tkinter.ttk import Button
    savebutton = Button(fr,image = saveimage,compound = TOP,text = 'save',command = save,width = 6)
    savebutton.pack(side = LEFT)

    savebutton = Button(fr,image = saveasimage,compound = TOP,text = 'save as',command = saveasButton,width = 6)
    savebutton.pack(side = LEFT)

    new_file = Button(fr,text = 'new file',command = newfile,image = saveimage2,compound = TOP,width = 6)
    new_file.pack(side = LEFT)

    openfileButton = Button(fr,text = 'open',command = Openfile,image = openimage,compound = TOP,width = 6)
    openfileButton.pack(side = LEFT)

    familyVar = StringVar(frame)
    Family = tuple(families(root))
    Familyss = list(Family)
    Familyss.sort()
    combo = Combobox(toll,textvariable = familyVar,value = Familyss)
    familyVar.set(Familyss[0])
    combo.bind('<<ComboboxSelected>>',famlis)

    weightVar = StringVar(frame)
    weightFamly = ("normal","bold","normal",ITALIC)
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
    
    close = Button(toll,text = '关闭',command = hide)

    lnVar = IntVar()
    yOrn = Checkbutton(toll,text = '自动换行',variable = lnVar,command = LnOrNone)
    lnVar.set(1)

    colors = Frame(toll)
    from tkinter import Button
    ff = Font(size = 8,family = '微软雅黑')
    color_bg = Button(colors,text = '背景颜色',command = color_b,font = ff)
    color_fg = Button(colors,text = '文字颜色',command = color_f,font = ff)
    color_cur = Button(colors,text = '光标颜色',command = color_cursor,font = ff)
    lebel_b = Label(colors,background = 'white')
    lebel_f = Label(colors,background = 'black')
    lebel_c = Label(colors,background = 'black')
    

#文本框
    sb = Scrollbar(frame)
    sb.pack(side="right", fill="y")
    
    zt = Label(frame,text = 'ln:1 co:0',background = 'white',foreground = 'black',justify = LEFT,anchor = 'nw')
    zt.pack(fill ='both',anchor = 'nw')

    text = Text(frame,undo = True,height = 45,wrap = 'char',yscrollcommand=sb.set,insertofftime = 500,insertontime= 500)
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
    size.grid(row = 0,column = 2,sticky = W+E,pady = 2,padx = 5)
    wei.grid(row = 0,column = 1,sticky = W+E,pady = 2,padx = 5)
    combo.grid(row = 1,columnspan = 2,column = 1,sticky = W+E,pady = 2)
    up.grid(row = 0,column = 3,sticky = W+E,padx = 5,pady = 2)
    dong.grid(row = 1,column = 3,sticky = W+E,padx = 5,pady = 2)
    L.grid(row = 0,column = 4,pady = 2)
    F.grid(row = 0,column = 5,columnspan = 2,sticky = W+E,padx = 5,pady = 2)
    jianc.grid(row = 1,column = 4,columnspan = 2)
    clenr.grid(row = 1,column = 6)
    close.grid(row = 0,column = 7,sticky = W+E+N+S,pady = 5)
    yOrn.grid(row = 1,column = 7,sticky = W+E+N+S,pady = 5)
    colors.grid(row = 0,column = 8,rowspan = 2,pady = 5)
    color_bg.grid(row = 0,column = 9,sticky = W+E+N+S,pady = 5)
    color_fg.grid(row = 0,column = 10,sticky = W+E+N+S,pady =5)
    color_cur.grid(row = 0,column = 11,sticky = W+E+N+S,pady = 5)
    lebel_b.grid(row = 1,column = 9,sticky = W+E+N+S,pady = 5)
    lebel_f.grid(row = 1,column = 10,sticky = W+E+N+S,pady = 5)
    lebel_c.grid(row = 1,column = 11,sticky = W+E+N+S,pady = 5)

    main_menu = Menu(root)
    filemenu = Menu(main_menu)
    filemenu.add_command(label = "New file",command = newfile)
    filemenu.add_command(label = "Open",command = Openfile)
    filemenu.add_command(label = "Save",command = save)
    filemenu.add_command(label = "Save as..",command = saveasButton)
    main_menu.add_cascade(label = 'File',menu = filemenu)
    bianjmenu = Menu(main_menu)
    bianjmenu.add_command(label = "Undo",command = ondo)
    bianjmenu.add_command(label = "Redo",command = redo)
    bianjmenu.add_separator()
    bianjmenu.add_command(label = "Cut",command = cut)
    bianjmenu.add_command(label = "Copy",command = copy)
    bianjmenu.add_command(label = "Paste",command = paste)
    main_menu.add_cascade(label = 'Edit',menu = bianjmenu)
    optionmenu = Menu(main_menu)
    optionmenu.add_command(label = "Background color",command = color_b)
    optionmenu.add_command(label = "Text color",command = color_f)
    optionmenu.add_command(label = "Cursor color",command = color_cursor)
    optionmenu.add_checkbutton(label = "Auto wrap",command = LnOrNone,variable = lnVar)
    optionmenu.add_checkbutton(label = "check",command = LnOrNone)
    main_menu.add_cascade(label = 'Options',menu = optionmenu)
    root.config(menu = main_menu)
    ztl()
#创建页签对象
New__()

notebook.pack(expand = TRUE,fill = BOTH)
root.mainloop()