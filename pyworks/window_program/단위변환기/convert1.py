# 단위 변환기 - 함수로 구현
from tkinter import *

def convert():
    # str -> int(형변환)
    kb = int(entry_kb.get())
    mb = kb / 1024  #변환 계산식
    mb = f'{mb: .2f}'
    text_mb.delete(0.0, END)
    text_mb.insert(END, mb)  #출력

root = Tk()
root.title("단위 변환기")
root.geometry("250x100+200+200")

Label(root, text='     KB').grid(row=0, column=0)
entry_kb = Entry(root, width=20)
entry_kb.grid(row=0, column=1)

Label(root, text='     MB').grid(row=1, column=0)
text_mb = Text(root, width=20, height=1)
text_mb.grid(row=1, column=1)

Button(root, text='변환', width=10, command=convert).grid(row=2, columnspan=2)

root.mainloop()