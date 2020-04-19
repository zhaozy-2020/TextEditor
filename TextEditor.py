'''一个文本编辑器
需求：打开，保存，编辑
 _____________________________________________
|___|___|___|___|___|___|                     |
|hallo wold!                                  |
|!!!!!!                                       |
|                                                         
￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣
做法：filefialog,Menu,Text,……'''
from tkinter import *
from tkinter import filedialog,Menu,Text,messagebox
import subprocess
#主窗体
v = ''
root = Tk()
root.title('文本编辑器')
root.iconbitmap('wd.ico')
root.geometry('1000x1000')

v = IntVar()

#变量
file_ = ''
size = 10
fontt = ''
hy = False
#函数
def Set(event = None):
    if file_:
        root.title(file_+'*')
    else:
        root.title('文本编辑器'+'*')

#菜单函数


def oopen(e = None):
    global file_
    #获取文件名
    filename = filedialog.askopenfilename(title='打开')
    print(filename)
    file_ = filename
    with open(filename,'r') as f:
        root.title(filename)
        text.delete('0.0','end')
        a = f.read()
        text.insert('end',a)


def Save(e = None):
    global file_
    if root.title() == '文本编辑器*' or root.title() == '文本编辑器':
        filename = filedialog.asksaveasfilename(title='新建')
        file_ = filename
        with open(filename,'w+') as f:
            root.title(filename)
            f.write(text.get('0.0','end'))
    else:
        with open(file_,'w+') as f:
            root.title(file_+'    (已保存)')
            f.write(text.get('0.0','end'))
def quit(e = None):
    import sys
    sys.exit()

def up(e = None):
    try:
        text.edit_undo()
    except:
        pass
def done(e = None):
    try:
        text.edit_redo()
    except:
        pass
    
a = []
def cut(event = None):
    text.event_generate("<<Cut>>")
def copy(event = None):
    text.event_generate("<<Copy>>")
def paste(event = None):
    text.event_generate('<<Paste>>')
def fon(event = None):
    from tkinter import font
    fo = Tk()
    fo.title('字体')
    fo.iconbitmap('pen.ico')
    s = Scrollbar(fo)
    s.grid(row = 0,rowspan=5,column = 1, padx=5, pady=5,sticky= "n" + "s")

    List = Listbox(fo,width = 20, yscrollcommand=s.set)
    
    ff = list(font.families(root))
    ff.sort()
    
    for i in ff:
        List.insert('end',i)
    List.grid(row = 0, rowspan=5,column = 0, padx=5, pady=5) 
    
    s.config(command=List.yview)
    button_OK = Button(fo,text = '确定', padx=1, pady=1)
    button_ss = Button(fo,text = '试试', padx=1, pady=1)
    big = Spinbox(fo,values = (1,2,3,4,5,10,16,18,24,28,32,48,82,100,400,1000))
    t = Label(fo,text = '字体大小', padx=1, pady=1)

    def OK(event = None):
        global v,size
        global fontt
        
        d = (List.get(List.curselection()),int(big.get()))
        fontt = d
        f.configure(family = fontt[0],size = fontt[1])
        fo.destroy()
    def ss(event = None):
        global size,fontt
        d = (List.get(List.curselection()),int(big.get()))
        fontt = d
        f.configure(family = fontt[0],size = fontt[1])

    button_OK.bind('<Button-1>',OK)
    button_ss.bind('<Button-1>',ss)
    t.grid(row = 0,column = 2, padx=1, pady=1)
    big.grid(row = 1,column = 2, padx=1, pady=1)

    button_OK.grid(row = 2,column = 2, padx=1, pady=1)
    button_ss.grid(row = 3,column = 2, padx=1, pady=1) 
    
       
    # tt.pack(side = BOTTOM)
    # t.pack(side = BOTTOM)
    fo.mainloop()

def Help(event = None):
    pass

def color(event = None):
    from tkinter import colorchooser
    fileName = colorchooser.askcolor(title = '文字颜色')
    if fileName[0] == None and fileName[1] == None:
        return None
    def col(t):
        return '#%02X%02X%02X' %(int(t[0]), int(t[1]), int(t[2]))
    text.configure(fg = col(fileName[0]))
    
def color2(event = None):
    from tkinter import colorchooser
    fileName = colorchooser.askcolor(title = '背景颜色')
    if fileName[0] == None and fileName[1] == None:
        return None
    def col(t):
        return '#%02X%02X%02X' %(int(t[0]), int(t[1]), int(t[2]))
    text.configure(bg = col(fileName[0]))

def fand(e = None):
    try:
        jm = Toplevel(root)
        jm.title('查找')
        
        t = Label(jm,text = '请输入查找的内容')
        i = Entry(jm)
        b = Button(jm,text = '查找')
        def getIndex(text, index):
            return tuple(map(int, str.split(text.index(index), ".")))
        def inpot(event = None):
            global a
            start = 1.0
            s = len(a)
            while True:
                pos = text.search(i.get(), start, stopindex="end")
                if not pos:
                    break
                a.append(getIndex(text,pos))
                l = Label(jm,text = '')
                start = pos + "+1c"
            destroy()
            try:
                for ii in a[s:]:
                    print(ii)
                    print('%s.%s'%ii,'%s.%s'%(ii[0],ii[1]+len(i.get())))
                    text.tag_add(
                    "tag%s.%s"%ii,
                    '%s.%s'%ii,
                    '%s.%s'%(ii[0],ii[1]+len(i.get()))
                    )
                    text.tag_config("tag%s.%s"%ii, background="yellow", foreground="red")
                    
                    
            except Exception as e: 
                pass
        def destroy(event = None):
            global a
            for ii in a:
                text.tag_delete("tag%s.%s"%ii)
            
        jm.bind('<Destroy>',destroy)
        b.bind('<Button-1>',inpot)
        t.pack(side = TOP)
        i.pack(side = TOP)
        b.pack(side = TOP)
    except _tkinter.TclError:
        pass
    finally:
        a = 0


def day(event = None):
    text.configure(bg='white',fg='black')
    mainmenu.configure(bg='white',fg='black')
    file_Menu.configure(bg='white',fg='black')
    bj_Menu.configure(bg='white',fg='black')
    sz_menu.configure(bg='white',fg='black')
    co_Menu.configure(bg='white',fg='black')
    fg_Menu.configure(bg='white',fg='black')
    menu.configure(bg='white',fg='black')
def evening(event = None):
    text.configure(bg='black',fg='gray',insertbackground='white')
    mainmenu.configure(bg='black',fg='gray')
    file_Menu.configure(bg='black',fg='gray')
    bj_Menu.configure(bg='black',fg='gray')
    sz_menu.configure(bg='black',fg='gray')
    co_Menu.configure(bg='black',fg='gray')
    fg_Menu.configure(bg='black',fg='gray')
    menu.configure(bg='black',fg='gray')
    print('sss')

def hh(event = None):
    global v
    print(v)
    if v == 1:
        text.configure(wrap = "none")
    else:
        text.configure(wrap = "char")
def login(event = None):
    def com(event = None):
        import gessleter
    def test2(event = None):
        global hy
        from tkinter import messagebox
        if E1.get() == "zzy":
            if E2.get() == "123456":
                messagebox.showinfo('OK','您已登录会员。',parent=loging )
                game_mu = Menu(mainmenu,tearoff = False)
                game_mu.add_command(label = "猜数字           Ctrl-G",command = com)
                mainmenu.add_cascade(label ='会员游戏',menu = game_mu)
                hy = True
                loging.destroy()
            else:
                messagebox.showerror('错误','密码不正确。',parent=loging)
                E2.icursor(0)
                E2.delete(0, "end")
        else:
            E1.icursor(0)
            messagebox.showerror('错误','用户名不正确。',parent=loging)
            E1.delete(0, "end")
            
            
    loging = Toplevel(root)
    t1 = Label(loging,text = '用户名')
    t2 = Label(loging,text = '密码')
    E1 = Entry(loging)
    E2 = Entry(loging,show = '▪')
    r1 = Button(loging,text = '提交')
    t1.grid(row = 0)
    t2.grid(row = 1)
    E1.grid(row = 0,column = 1)
    E2.grid(row = 1,column = 1)
    r1.bind('<Button-1>',test2)
    r1.grid(row = 3, columnspan=3)

def hyy(event = None):
    global hy
    if hy:
        huiy = Toplevel(root)
        huiy.title('会员')
        huiy.iconbitmap('wd.ico')

        
        group = LabelFrame(huiy, text="zzy", padx=5, pady=5)
        group.pack(padx=10, pady=10)

        v = IntVar()
        r1 = Radiobutton(group, text="aaa", variable=v, value=1).pack(anchor="w")
        r2 = Radiobutton(group, text="vvv", variable=v, value=2).pack(anchor="w")
        r3 = Radiobutton(group, text="ccc", variable=v, value=3).pack(anchor="w")
 

def New(event = None):
    import os
    os.popen('python TextEditor.py')
def run(event = None):
    global file_
    import os
    print(file_)
    f = open(file_)
    f.close()
    ttt = subprocess.Popen(['python',file_])
    r = Toplevel(root)
    r.title('Run')
    m = Label(r,text = ttt.read())
    m.pack()
#菜单
mainmenu = Menu(root,tearoff = True)
mainmenu.add_command(label = "会员",command = hyy)
file_Menu = Menu(mainmenu,tearoff = False)
file_Menu.add_command(label="打开           Ctrl-O", command=oopen)
file_Menu.add_command(label="run           Ctrl-O", command=run)
file_Menu.add_command(label="保存           Ctrl-S", command=Save)
file_Menu.add_command(label='新建           Ctrl-N',command = New)
file_Menu.add_separator()
file_Menu.add_command(label="退出           Ctrl-Q", command=root.quit)
mainmenu.add_cascade(label="文件", menu=file_Menu)

bj_Menu = Menu(mainmenu,tearoff = False)
bj_Menu.add_command(label="上一步         Ctrl-Z", command=up)
bj_Menu.add_command(label="下一步         Ctrl-D", command=done)
bj_Menu.add_separator()
bj_Menu.add_command(label="剪贴           Ctrl-X",command=cut)
bj_Menu.add_command(label="复制           Ctrl-C",command=copy)
bj_Menu.add_command(label="贴粘           Ctrl-V",command=paste)
bj_Menu.add_separator()
bj_Menu.add_command(label="查找       Ctrl-Alt-F",command=fand)
mainmenu.add_cascade(label="编辑", menu=bj_Menu)

sz_menu = Menu(mainmenu,tearoff = False)
sz_menu.add_command(label='字体           Ctrl-F',command = fon)

co_Menu = Menu(mainmenu,tearoff = False)
co_Menu.add_command(label='文字颜色   Ctrl-Alt-T',command = color)
co_Menu.add_command(label='背景颜色   Ctrl-Alt-B',command = color2)
sz_menu.add_cascade(label='颜色',menu = co_Menu)

fg_Menu = Menu(mainmenu,tearoff = False)

fg_Menu.add_command(label='白天       Ctrl-Alt-D',command = day)
fg_Menu.add_command(label='黑夜       Ctrl-Alt-E',command = evening)
sz_menu.add_cascade(label='风格',menu = fg_Menu)
sz_menu.add_checkbutton(label = '自动换行',command = hh,variable= v,onvalue =2,offvalue= 1)
sz_menu.add_command(label = '登录会员',command = login)
mainmenu.add_cascade(label = '设置',menu = sz_menu)

mainmenu.add_command(label='帮助',command = print)

menu = Menu(root, tearoff=False)

menu.add_command(label="上一步        Ctrl-Z", command=up)
menu.add_command(label="下一步        Ctrl-D", command=done)
menu.add_separator()
menu.add_command(label="粘贴          Ctrl-V", command=paste)
menu.add_command(label="复制          Ctrl-C", command=copy)
menu.add_command(label="剪切          Ctrl-X", command=cut)
 
def popup(event):
    menu.post(event.x_root, event.y_root)
# 绑定
root.bind("<Button-3>", popup)

root.bind('<Control-Key-s>',Save)
root.bind('<Control-Key-o>',oopen)
root.bind('<Control-Key-q>',quit)
root.bind('<Control-Key-f>',fon)
root.bind('<Control-Alt-Key-t>',color)
root.bind('<Control-Alt-Key-b>',color2)


root.bind('<Control-Alt-Key-f>',fand)
root.bind('<Control-Key-d>',done)
root.bind('<Key>',Set)

sb = Scrollbar(root)
sb.pack(side="right", fill="y")
sb2 = Scrollbar(root,orient =  "horizontal"	)
sb2.pack(side="bottom", fill="x")
from tkinter import font
import _tkinter
f = font.Font(root)
#文本框
text = Text(root,undo = True,width = 200,height = 400,yscrollcommand=sb.set,font = f,xscrollcommand=sb2.set,wrap = "none")
text.pack(side="left", fill="both")
sb.config(command=text.yview)
sb2.config(command = text.xview)
root.config(menu=mainmenu)


root.mainloop()
