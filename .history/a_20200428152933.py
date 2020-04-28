import sys
sys.path.append('E:/zzy/git/TextEditor')
import word
f = open('words.py','w',encoding='gbk')
f.write('word = ')
a = []
for i in word.a:
    a.append(i['word'])
f.write(str(a))
f.close()