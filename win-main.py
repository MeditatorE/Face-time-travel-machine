# this file use to create GUI for face-aging

import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter.ttk import *
import subprocess
from PIL import Image
from PIL import ImageTk
from shutil import copy



global acc
acc=1

while(acc<2):

    #Set GUI

    # 0. initialize
    path="./results/aging_cyclegan/test_latest/images/.DS_Store"
    if os.path.exists(path):
        os.remove(path)

    path="./datasets/young2old/testA/.DS_Store"
    if os.path.exists(path):
        os.remove(path)
    
    path="./datasets/young2old/testB/.DS_Store"
    if os.path.exists(path):
        os.remove(path)
    
    
    # 1. set window object
    window = Tk()
    window.geometry("808x540+200+100")
    window.title('face-aging')
    window.resizable(0,0)
    window["bg"]="White" # 白色



    # 2. set sessions

    # 此处采用 panedWindow 和 LabelFrame 容器控件
    window.left_pane = PanedWindow(width=256,height=256)  # 这里是规定容器的长宽
    window.left_pane.place(x=10,y=125) # 这里是决定将这个容器放在哪个位置

    window.mid_pane = PanedWindow(width=256,height=256)
    window.mid_pane.place(x=276,y=125) # 这个坐标应该指的是左上角的点的位置

    window.right_pane = PanedWindow(width=256,height=256)
    window.right_pane.place(x=542,y=125) # 这个坐标应该指的是左上角的点的位置

    window.bottom_pane = PanedWindow(width=788,height=145)
    window.bottom_pane.place(x=10,y=390) # 这个坐标应该指的是左上角的点的位置

    window.top_pane = PanedWindow(width=808,height=120)
    window.top_pane.place(x=0,y=0) # 这个坐标应该指的是左上角的点的位置



    # 3. set button

    window.button_upload = Button(window,text="Upload",width=10)
    window.button_upload.place(x =150, y = 440)

    window.button_start = Button(window,text="Let's start",width=10)
    window.button_start.place(x = 350 , y = 440 )

    window.button_clear = Button(window,text="Clear",width=10)
    window.button_clear.place(x = 550 , y = 440)



    # 4. set hyperlink

    def callback1(event):
        webbrowser.open_new("https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix")
    link1=tk.Label(window, text="Reference", fg="grey")
    link1.pack()
    link1.place(x=582,y=490)
    link1.bind("<Button-1>", callback1)

    def callback2(event):
        webbrowser.open_new("https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix")
    link2=tk.Label(window, text="About us", fg="grey")
    link2.pack()
    link2.place(x=384,y=490)
    link2.bind("<Button-1>", callback2)

    def callback3(event):
        webbrowser.open_new("https://arxiv.org/abs/1703.10593")
    link3=tk.Label(window, text="Manual", fg="grey")
    link3.pack()
    link3.place(x=188,y=490)
    link3.bind("<Button-1>", callback3)



    # 5. add text

    text=Text(window,width=5,height=1)
    text.pack()
    text.insert(INSERT,"Youth")
    text.place(x=115,y=390)

    text=Text(window,width=8,height=1)
    text.pack()
    text.insert(INSERT,"Original")
    text.place(x=380,y=390)

    text=Text(window,width=5,height=1)
    text.pack()
    text.insert(INSERT,"Aging")
    text.place(x=655,y=390)



    # 6. show the pictures

    top_image = PhotoImage(file="gaitubao_300_png.png")
    top_label = Label(window,image=top_image)
    top_label.place(x=0,y=0)

    # show results
    i=0
    file = "./results/aging_cyclegan/test_latest/images"
    path_dir = os.listdir(file)
    for filename in path_dir:  # 遍历pathDir下的所有文件filename
        i=i+1

    if(i>1):
        path = "./datasets/young2old/testA"
        path_dir = os.listdir(path)
        i=0
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i=i+1
            if(i==1):
                fileName = os.path.splitext(filename)[0]
        
        path1="./results/aging_cyclegan/test_latest/images/"+fileName+"_fake_A.png"
        path2="./results/aging_cyclegan/test_latest/images/"+fileName+"_real_A.png"
        path3="./results/aging_cyclegan/test_latest/images/"+fileName+"_fake_B.png"

        image1=Image.open(path1)
        left_image = ImageTk.PhotoImage(image1)
        left_label = Label(window,image=left_image)
        left_label.place(x=10,y=125)

        image2=Image.open(path2)
        mid_image = ImageTk.PhotoImage(image2)
        mid_label = Label(window,image=mid_image)
        mid_label.place(x=276,y=125)

        image3=Image.open(path3)
        right_image = ImageTk.PhotoImage(image3)
        right_label = Label(window,image=right_image)
        right_label.place(x=542,y=125)



    # 7. implement the button function

    # implement button start
    def start(*args):
        file_path="./datasets/young2old/testA/"
        save_path="./datasets/young2old/testB/"
        path_dir=os.listdir(file_path)
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            from_path = os.path.join(file_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
            to_path = save_path       # 新文件的绝对路径
            copy(from_path, to_path)  # 完成复制黏贴

        cmd='python test.py --dataroot ./datasets/young2old --name aging_cyclegan --model cycle_gan --gpu_ids -1'
        os.system(cmd)
        window.destroy()
        
        global acc
        acc=0

    window.button_start.bind('<Button-1>',start)

    # implement button clear
    def clear(*args):
        left_label.destroy()
        mid_label.destroy()
        right_label.destroy()

        path = r"./datasets/young2old/testA"
        path_dir = os.listdir(path)
        i = 0
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if(i > 0):
                os.remove(full_path)

        path = r"./datasets/young2old/testB"
        path_dir = os.listdir(path)
        i = 0
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if (i > 0):
                os.remove(full_path)

        path = r"./results/aging_cyclegan/test_latest/images"
        path_dir = os.listdir(path)
        i = 0
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if (i > 0):
                os.remove(full_path)

        full_path = r"./results/aging_cyclegan/test_latest/index.html"
        os.remove(full_path)

    window.button_clear.bind('<Button-1>',clear)

    # implement button upload
    def upload(*args):
        path = r".\datasets\young2old\testA\\"
        os.startfile(path)

    window.button_upload.bind('<Button-1>',upload)

# 8. start GUI
    window.mainloop()

    acc=acc+1


