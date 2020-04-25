from tkinter import *
import random
root = Tk()
root.title('猜数')
a = random.randint(1,100)
def gess(e = None):
    global a
    r = Toplevel(root)
    r.geometry('200x30')
    try:
        s = int(inpot.get())
        inpot.delete(0, "end")
        if a == s:
            r.title('答对了')
        else:
            r.title('答错了')
        w = ''
        if a == s:
            w = '猜对了，就是%s。'%s
        elif s < a:
            w = '猜小了。'
        elif s > a:
            w = '猜大了。'
        else:
            w = '出错了'
        
    except:
        r.title('错误')
        w = '出错了'
    def q(e = None):
            r.destroy()
    t = Label(r,text = w,padx = 10)
    t.pack(side = LEFT)
    e = Button(r,text = '退出',command = q)
    e.pack(side = RIGHT)

tip = Label(root,text = '请输入0~100的数字')
tip.grid(row = 0,column=1,columnspan=3)
inpot = Entry(root)
inpot.grid(row = 1,column=1,columnspan=2)
gessbutton = Button(root,text = '猜数',command = gess)
gessbutton.grid(row = 1,column= 3)
root.bind('<Control-Key-s>',gess)
root.mainloop()