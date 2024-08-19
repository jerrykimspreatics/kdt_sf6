# 윈도우 생성 - tkinter
# 체계 : root=Tk() > Frame() > Label(),Button() > mainloop()
# import tkinter as tk
from tkinter import *
# 루트 생성
root = Tk()
root.title("처음 만든 윈도우")
# 창크기(가로x세로)
root.geometry("300x100")

# 콤포넌트(구성요소-레이블, 버튼, 입력상자)
# 출력(Label)
# 배치-pack(side=left): 한줄을 차지(LEFT, RIGHT, TOP, BOTTOM)
# grid(행, 열): 자유롭게 배치(E, W, S, N)
Label(root, text="안녕하세요~").pack(side=TOP)
Button(root, text="확인").pack(side=TOP)

root.mainloop()