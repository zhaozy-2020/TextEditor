import sys
sys.path.append('E:/zzy/git/TextEditor')
import word
f = open('words.py','w',encoding='utf-8')
f.write('word = ')
a = []
for i in word.zzza:
    a.append(i['word'])
f.write(str(a))
f.close()
f.