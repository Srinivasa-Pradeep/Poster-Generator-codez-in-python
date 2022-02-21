import input as o


print("\tselect a template")
#=============================================================

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root= Tk()
root.title("Select a Template")
root.geometry("1655x648")
img = ImageTk.PhotoImage(Image.open("selection.png"))
l = Label(image= img).grid(row=0,column=0)
#l.pack()


def t1():
    root.destroy()
    print("\nTemplate_1 has been selected!\n")
    color_c = input("Would you like to Choose a Background Colour for your Template :(y/n)")
    if color_c=="n":
        BG="white"
        FG="black"
    else:
        color = input("Enter a Background colour for the Template :(Black , Matteyellow , Darkblue):")
        if color == "black":
            BG="black"
            FG="white"
        elif color=="Matteyellow":
            BG="#ffd500"
            FG="black"
        elif color =="Darkblue":
            BG="#0b0b60"
            FG="white"
        else:
             BG="white"
             FG="black"

    global Template
    o.Template = "Template_1"
    o.inputs_1()
    Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    while Next_Data_Entry == "y":
        o.inputs_2()
        Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    o.Templates(o.Template)
            
        
    #======================================================================
    w = Tk()
    w.geometry("1080x1920")
    w.title("Poster Creator")
    l = Label(w,text= o.Title,bg=BG,fg=FG)
    l.config(font=(o.Title_Font,o.Title_FontSize))
    l.pack(side=TOP)
    
    try:
        t = Label(w,text=o.By_Line,bg=BG,fg=FG)
        t.config(font=(o.By_Line_Font,o.By_Line_FontSize))
        t.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t1 = Label(w,text=o.Sub_Title_1,bg=BG,fg=FG)
        t1.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        t1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t2 = Label(w,text=o.Body_1,bg=BG,fg=FG)
        t2.config(font=(o. Body_Font,o.Body_FontSize))
        t2.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    
    try:
        a= Label(w,text=o.Sub_Title_2,bg=BG,fg=FG)
        a.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        a.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        a1 = Label(w,text=o.Body_2,bg=BG,fg=FG)
        a1.config(font=(o. Body_Font,o.Body_FontSize))
        a1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b = Label(w,text=o.Sub_Title_3,bg=BG,fg=FG)
        b.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        b.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b1 = Label(w,text=o.Body_3,bg=BG,fg=FG)
        b1.config(font=(o. Body_Font,o.Body_FontSize))
        b1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c = Label(w,text=o.Sub_Title_4,bg=BG,fg=FG)
        c.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        c.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c1 = Label(w,text=o.Body_4,bg=BG,fg=FG)
        c1.config(font=(o. Body_Font,o.Body_FontSize))
        c1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d = Label(w,text=o.Sub_Title_5,bg=BG,fg=FG)
        d.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        d.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d1 = Label(w,text=o.Body_5,bg=BG,fg=FG)
        d1.config(font=(o. Body_Font,o.Body_FontSize))
        d1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e = Label(w,text=o.Sub_Title_6,bg=BG,fg=FG)
        e.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        e.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e1 = Label(w,text=o.Body_6,bg=BG,fg=FG)
        e1.config(font=(o. Body_Font,o.Body_FontSize))
        e1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f = Label(w,text=o.Sub_Title_7,bg=BG,fg=FG)
        f.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        f.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f1 = Label(w,text=o.Body_7,bg=BG,fg=FG)
        f1.config(font=(o. Body_Font,o.Body_FontSize))
        f1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g = Label(w,text=o.Sub_Title_8,bg=BG,fg=FG)
        g.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        g.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g1 = Label(w,text=o.Body_8,bg=BG,fg=FG)
        g1.config(font=(o. Body_Font,o.Body_FontSize))
        g1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h = Label(w,text=o.Sub_Title_9,bg=BG,fg=FG)
        h.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        h.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h1 = Label(w,text=o.Body_9,bg=BG,fg=FG)
        h1.config(font=(o. Body_Font,o.Body_FontSize))
        h1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    w.config(bg=BG)
r = Button(root,text="Template_1",command=t1)



def t2():
    root.destroy()
    print("\nTemplate_2 has been selected!\n")
    color_c = input("Would you like to Choose a Background Colour for your Template :(y/n)")
    if color_c=="n":
        BG="white"
        FG="black"
    else:
        color = input("Enter a Background colour for the Template :(Black , Matteyellow , Darkblue):")
        if color == "black":
            BG="black"
            FG="white"
        elif color=="Matteyellow":
            BG="#ffd500"
            FG="black"
        elif color =="Darkblue":
            BG="#0b0b60"
            FG="white"
        else:
             BG="white"
             FG="black"

    global Template
    o.Template = "Template_2"
    o.inputs_1()
    Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    while Next_Data_Entry == "y":
        o.inputs_2()
        Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    o.Templates(o.Template)
            
        
    #======================================================================
    w = Tk()
    w.geometry("1080x1920")
    w.title("Poster Creator")
    l = Label(w,text= o.Title,bg=BG,fg=FG)
    l.config(font=(o.Title_Font,o.Title_FontSize))
    l.pack(side=TOP)
    
    try:
        t = Label(w,text=o.By_Line,bg=BG,fg=FG)
        t.config(font=(o.By_Line_Font,o.By_Line_FontSize))
        t.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t1 = Label(w,text=o.Sub_Title_1,bg=BG,fg=FG)
        t1.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        t1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t2 = Label(w,text=o.Body_1,bg=BG,fg=FG)
        t2.config(font=(o. Body_Font,o.Body_FontSize))
        t2.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    
    try:
        a= Label(w,text=o.Sub_Title_2,bg=BG,fg=FG)
        a.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        a.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        a1 = Label(w,text=o.Body_2,bg=BG,fg=FG)
        a1.config(font=(o. Body_Font,o.Body_FontSize))
        a1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b = Label(w,text=o.Sub_Title_3,bg=BG,fg=FG)
        b.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        b.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b1 = Label(w,text=o.Body_3,bg=BG,fg=FG)
        b1.config(font=(o. Body_Font,o.Body_FontSize))
        b1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c = Label(w,text=o.Sub_Title_4,bg=BG,fg=FG)
        c.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        c.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c1 = Label(w,text=o.Body_4,bg=BG,fg=FG)
        c1.config(font=(o. Body_Font,o.Body_FontSize))
        c1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d = Label(w,text=o.Sub_Title_5,bg=BG,fg=FG)
        d.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        d.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d1 = Label(w,text=o.Body_5,bg=BG,fg=FG)
        d1.config(font=(o. Body_Font,o.Body_FontSize))
        d1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e = Label(w,text=o.Sub_Title_6,bg=BG,fg=FG)
        e.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        e.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e1 = Label(w,text=o.Body_6,bg=BG,fg=FG)
        e1.config(font=(o. Body_Font,o.Body_FontSize))
        e1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f = Label(w,text=o.Sub_Title_7,bg=BG,fg=FG)
        f.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        f.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f1 = Label(w,text=o.Body_7,bg=BG,fg=FG)
        f1.config(font=(o. Body_Font,o.Body_FontSize))
        f1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g = Label(w,text=o.Sub_Title_8,bg=BG,fg=FG)
        g.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        g.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g1 = Label(w,text=o.Body_8,bg=BG,fg=FG)
        g1.config(font=(o. Body_Font,o.Body_FontSize))
        g1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h = Label(w,text=o.Sub_Title_9,bg=BG,fg=FG)
        h.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        h.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h1 = Label(w,text=o.Body_9,bg=BG,fg=FG)
        h1.config(font=(o. Body_Font,o.Body_FontSize))
        h1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    w.config(bg=BG)
r1 = Button(root,text="Template_2",command=t2)

def t3():
    root.destroy()
    print("\nTemplate_3 has been selected!\n")
    color_c = input("Would you like to Choose a Background Colour for your Template :(y/n)")
    if color_c=="n":
        BG="white"
        FG="black"
    else:
        color = input("Enter a Background colour for the Template :(Black , Matteyellow , Darkblue):")
        if color == "Black":
            BG="black"
            FG="white"
        elif color=="Matteyellow":
            BG="#ffd500"
            FG="black"
        elif color =="Darkblue":
            BG="#0b0b60"
            FG="white"
        else:
             BG="white"
             FG="black"

    global Template
    o.Template = "Template_3"
    o.inputs_1()
    Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    while Next_Data_Entry == "y":
        o.inputs_2()
        Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
    o.Templates(o.Template)
            
        
    #======================================================================
    w = Tk()
    w.geometry("1080x1920")
    w.title("Poster Creator")
    l = Label(w,text= o.Title,bg=BG,fg=FG)
    l.config(font=(o.Title_Font,o.Title_FontSize))
    l.pack(side=TOP)
    
    try:
        t = Label(w,text=o.By_Line,bg=BG,fg=FG)
        t.config(font=(o.By_Line_Font,o.By_Line_FontSize))
        t.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t1 = Label(w,text=o.Sub_Title_1,bg=BG,fg=FG)
        t1.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        t1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        t2 = Label(w,text=o.Body_1,bg=BG,fg=FG)
        t2.config(font=(o. Body_Font,o.Body_FontSize))
        t2.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    
    try:
        a= Label(w,text=o.Sub_Title_2,bg=BG,fg=FG)
        a.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        a.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        a1 = Label(w,text=o.Body_2,bg=BG,fg=FG)
        a1.config(font=(o. Body_Font,o.Body_FontSize))
        a1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b = Label(w,text=o.Sub_Title_3,bg=BG,fg=FG)
        b.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        b.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        b1 = Label(w,text=o.Body_3,bg=BG,fg=FG)
        b1.config(font=(o. Body_Font,o.Body_FontSize))
        b1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c = Label(w,text=o.Sub_Title_4,bg=BG,fg=FG)
        c.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        c.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        c1 = Label(w,text=o.Body_4,bg=BG,fg=FG)
        c1.config(font=(o. Body_Font,o.Body_FontSize))
        c1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d = Label(w,text=o.Sub_Title_5,bg=BG,fg=FG)
        d.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        d.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        d1 = Label(w,text=o.Body_5,bg=BG,fg=FG)
        d1.config(font=(o. Body_Font,o.Body_FontSize))
        d1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e = Label(w,text=o.Sub_Title_6,bg=BG,fg=FG)
        e.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        e.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        e1 = Label(w,text=o.Body_6,bg=BG,fg=FG)
        e1.config(font=(o. Body_Font,o.Body_FontSize))
        e1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f = Label(w,text=o.Sub_Title_7,bg=BG,fg=FG)
        f.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        f.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        f1 = Label(w,text=o.Body_7,bg=BG,fg=FG)
        f1.config(font=(o. Body_Font,o.Body_FontSize))
        f1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g = Label(w,text=o.Sub_Title_8,bg=BG,fg=FG)
        g.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        g.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        g1 = Label(w,text=o.Body_8,bg=BG,fg=FG)
        g1.config(font=(o. Body_Font,o.Body_FontSize))
        g1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h = Label(w,text=o.Sub_Title_9,bg=BG,fg=FG)
        h.config(font=(o.Sub_Title_Font,o.Sub_Title_FontSize))
        h.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    try:
        h1 = Label(w,text=o.Body_9,bg=BG,fg=FG)
        h1.config(font=(o. Body_Font,o.Body_FontSize))
        h1.pack(anchor=o.File_Justification)
    except NameError and AttributeError:
        pass
    w.config(bg=BG)
r2 = Button(root,text="Template_3",command=t3)

def t4():
    root.destroy()
    print("\nCustomised Template has been selected!\n")
    option = input("Would you like to Choose Background Colour or Background Image for your Template :(colour/image):")
    if option=="image":
            filename = filedialog.askopenfilename(initialdir="" , title="Select An Image",filetypes=(("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
            i = filename
            
            print("\nPath is Successfully Copied! and the path is",i,"\n")

            BG=input("Enter the Background colour for your text:")
            FG=input("Enter the Foreground colour for your text:")
            print("")
            
            global Template
            o.Template = "Template_4"
            o.inputs_1()
            Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
            while Next_Data_Entry == "y":
                o.inputs_2()
                Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
            #=================================================
            w = Tk()
            w.geometry("1080x1920")
            w.title("Poster Creator")
            img1= Image.open(i)
            new = img1.resize((1080,1260),Image.ANTIALIAS)
            new_bg = ImageTk.PhotoImage(new)
            l1 = Label(image= new_bg)
            l1.place(x=0,y=0)
            
            l = Label(w,text= o.Title,bg=BG,fg=FG)
            l.config(font=(o.Title_Font,o.Title_FontSize))
            l.pack(anchor=o.Title_Justification)
            
            try:
                t = Label(w,text=o.By_Line,bg=BG,fg=FG)
                t.config(font=(o.By_Line_Font,o.By_Line_FontSize))
                t.pack(anchor=o.By_Line_Justification)
            except NameError and AttributeError:
                pass
            try:
                t1 = Label(w,text=o.Sub_Title_1,bg=BG,fg=FG)
                t1.config(font=(o.Sub_Title_Font_1,o.Sub_Title_FontSize_1))
                t1.pack(anchor=o.Sub_Title_Justification_1)
            except NameError and AttributeError:
                pass
            try:
                t2 = Label(w,text=o.Body_1,bg=BG,fg=FG)
                t2.config(font=(o. Body_Font_1,o.Body_FontSize_1))
                t2.pack(anchor=o.Body_Justification_1)
            except NameError and AttributeError:
                pass
            
            try:
                a= Label(w,text=o.Sub_Title_2,bg=BG,fg=FG)
                a.config(font=(o.Sub_Title_Font_2,o.Sub_Title_FontSize_2))
                a.pack(anchor=o.Sub_Title_Justification_2)
            except NameError and AttributeError:
                pass
            try:
                a1 = Label(w,text=o.Body_2,bg=BG,fg=FG)
                a1.config(font=(o. Body_Font_2,o.Body_FontSize_2))
                a1.pack(anchor=o.Body_Justification_2)
            except NameError and AttributeError:
                pass
            try:
                b = Label(w,text=o.Sub_Title_3,bg=BG,fg=FG)
                b.config(font=(o.Sub_Title_Font_3,o.Sub_Title_FontSize_3))
                b.pack(anchor=o.Sub_Title_Justification_3)
            except NameError and AttributeError:
                pass
            try:
                b1 = Label(w,text=o.Body_3,bg=BG,fg=FG)
                b1.config(font=(o. Body_Font_3,o.Body_FontSize_3))
                b1.pack(anchor=o.Body_Justification_3)
            except NameError and AttributeError:
                pass
            try:
                c = Label(w,text=o.Sub_Title_4,bg=BG,fg=FG)
                c.config(font=(o.Sub_Title_Font_4,o.Sub_Title_FontSize_4))
                c.pack(anchor=o.Sub_Title_Justification_4)
            except NameError and AttributeError:
                pass
            try:
                c1 = Label(w,text=o.Body_4,bg=BG,fg=FG)
                c1.config(font=(o. Body_Font_4,o.Body_FontSize_4))
                c1.pack(anchor=o.Body_Justification_4)
            except NameError and AttributeError:
                pass
            try:
                d = Label(w,text=o.Sub_Title_5,bg=BG,fg=FG)
                d.config(font=(o.Sub_Title_Font_5,o.Sub_Title_FontSize_5))
                d.pack(anchor=o.Sub_Title_Justification_5)
            except NameError and AttributeError:
                pass
            try:
                d1 = Label(w,text=o.Body_5,bg=BG,fg=FG)
                d1.config(font=(o. Body_Font_5,o.Body_FontSize_5))
                d1.pack(anchor=o.Body_Justification_5)
            except NameError and AttributeError:
                pass
            try:
                e = Label(w,text=o.Sub_Title_6,bg=BG,fg=FG)
                e.config(font=(o.Sub_Title_Font_6,o.Sub_Title_FontSize_6))
                e.pack(anchor=o.Sub_Title_Justification_6)
            except NameError and AttributeError:
                pass
            try:
                e1 = Label(w,text=o.Body_6,bg=BG,fg=FG)
                e1.config(font=(o. Body_Font_6,o.Body_FontSize_6))
                e1.pack(anchor=o.Body_Justification_6)
            except NameError and AttributeError:
                pass
            try:
                f = Label(w,text=o.Sub_Title_7,bg=BG,fg=FG)
                f.config(font=(o.Sub_Title_Font_7,o.Sub_Title_FontSize_7))
                f.pack(anchor=o.Sub_Title_Justification_7)
            except NameError and AttributeError:
                pass
            try:
                f1 = Label(w,text=o.Body_7,bg=BG,fg=FG)
                f1.config(font=(o. Body_Font_7,o.Body_FontSize_7))
                f1.pack(anchor=o.Body_Justification_7)
            except NameError and AttributeError:
                pass
            try:
                g = Label(w,text=o.Sub_Title_8,bg=BG,fg=FG)
                g.config(font=(o.Sub_Title_Font_8,o.Sub_Title_FontSize_8))
                g.pack(anchor=o.Sub_Title_Justification_8)
            except NameError and AttributeError:
                pass
            try:
                g1 = Label(w,text=o.Body_8,bg=BG,fg=FG)
                g1.config(font=(o. Body_Font_8,o.Body_FontSize_8))
                g1.pack(anchor=o.Body_Justification_1)
            except NameError and AttributeError:
                pass
            try:
                h = Label(w,text=o.Sub_Title_9,bg=BG,fg=FG)
                h.config(font=(o.Sub_Title_Font_9,o.Sub_Title_FontSize_9))
                h.pack(anchor=o.Sub_Title_Justification_9)
            except NameError and AttributeError:
                pass
            try:
                h1 = Label(w,text=o.Body_9,bg=BG,fg=FG)
                h1.config(font=(o. Body_Font_9,o.Body_FontSize_9))
                h1.pack(anchor=o.Body_Justification_9)
            except NameError and AttributeError:
                pass
            w.config(bg=BG)
            #w.bind('<Configure>',resizer)
            w.mainloop()
            
    if option=="colour":
        color = input("Choose a Background colour for the Template :(Black , Matteyellow , Darkblue or Default):")
        if color == "Black":
            BG="black"
            FG="white"
        elif color=="Matteyellow":
            BG="#ffd500"
            FG="black"
        elif color =="Darkblue":
            BG="#0b0b60"
            FG="white"
        else:
             BG="white"
             FG="black"


        global Template
        o.Template = "Template_4"
        o.inputs_1()
        Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")
        while Next_Data_Entry == "y":
            o.inputs_2()
            Next_Data_Entry=input("Would you like to Enter more data :(y/n) ")

    #================================================
   
        w = Tk()
        w.geometry("1080x1920")
        w.title("Poster Creator")
        l = Label(w,text= o.Title,bg=BG,fg=FG)
        l.config(font=(o.Title_Font,o.Title_FontSize))
        l.pack(anchor=o.Title_Justification)
        
        try:
            t = Label(w,text=o.By_Line,bg=BG,fg=FG)
            t.config(font=(o.By_Line_Font,o.By_Line_FontSize))
            t.pack(anchor=o.By_Line_Justification)
        except NameError and AttributeError:
            pass
        try:
            t1 = Label(w,text=o.Sub_Title_1,bg=BG,fg=FG)
            t1.config(font=(o.Sub_Title_Font_1,o.Sub_Title_FontSize_1))
            t1.pack(anchor=o.Sub_Title_Justification_1)
        except NameError and AttributeError:
            pass
        try:
            t2 = Label(w,text=o.Body_1,bg=BG,fg=FG)
            t2.config(font=(o. Body_Font_1,o.Body_FontSize_1))
            t2.pack(anchor=o.Body_Justification_1)
        except NameError and AttributeError:
            pass
        
        try:
            a= Label(w,text=o.Sub_Title_2,bg=BG,fg=FG)
            a.config(font=(o.Sub_Title_Font_2,o.Sub_Title_FontSize_2))
            a.pack(anchor=o.Sub_Title_Justification_2)
        except NameError and AttributeError:
            pass
        try:
            a1 = Label(w,text=o.Body_2,bg=BG,fg=FG)
            a1.config(font=(o. Body_Font_2,o.Body_FontSize_2))
            a1.pack(anchor=o.Body_Justification_2)
        except NameError and AttributeError:
            pass
        try:
            b = Label(w,text=o.Sub_Title_3,bg=BG,fg=FG)
            b.config(font=(o.Sub_Title_Font_3,o.Sub_Title_FontSize_3))
            b.pack(anchor=o.Sub_Title_Justification_3)
        except NameError and AttributeError:
            pass
        try:
            b1 = Label(w,text=o.Body_3,bg=BG,fg=FG)
            b1.config(font=(o. Body_Font_3,o.Body_FontSize_3))
            b1.pack(anchor=o.Body_Justification_3)
        except NameError and AttributeError:
            pass
        try:
            c = Label(w,text=o.Sub_Title_4,bg=BG,fg=FG)
            c.config(font=(o.Sub_Title_Font_4,o.Sub_Title_FontSize_4))
            c.pack(anchor=o.Sub_Title_Justification_4)
        except NameError and AttributeError:
            pass
        try:
            c1 = Label(w,text=o.Body_4,bg=BG,fg=FG)
            c1.config(font=(o. Body_Font_4,o.Body_FontSize_4))
            c1.pack(anchor=o.Body_Justification_4)
        except NameError and AttributeError:
            pass
        try:
            d = Label(w,text=o.Sub_Title_5,bg=BG,fg=FG)
            d.config(font=(o.Sub_Title_Font_5,o.Sub_Title_FontSize_5))
            d.pack(anchor=o.Sub_Title_Justification_5)
        except NameError and AttributeError:
            pass
        try:
            d1 = Label(w,text=o.Body_5,bg=BG,fg=FG)
            d1.config(font=(o. Body_Font_5,o.Body_FontSize_5))
            d1.pack(anchor=o.Body_Justification_5)
        except NameError and AttributeError:
            pass
        try:
            e = Label(w,text=o.Sub_Title_6,bg=BG,fg=FG)
            e.config(font=(o.Sub_Title_Font_6,o.Sub_Title_FontSize_6))
            e.pack(anchor=o.Sub_Title_Justification_6)
        except NameError and AttributeError:
            pass
        try:
            e1 = Label(w,text=o.Body_6,bg=BG,fg=FG)
            e1.config(font=(o. Body_Font_6,o.Body_FontSize_6))
            e1.pack(anchor=o.Body_Justification_6)
        except NameError and AttributeError:
            pass
        try:
            f = Label(w,text=o.Sub_Title_7,bg=BG,fg=FG)
            f.config(font=(o.Sub_Title_Font_7,o.Sub_Title_FontSize_7))
            f.pack(anchor=o.Sub_Title_Justification_7)
        except NameError and AttributeError:
            pass
        try:
            f1 = Label(w,text=o.Body_7,bg=BG,fg=FG)
            f1.config(font=(o. Body_Font_7,o.Body_FontSize_7))
            f1.pack(anchor=o.Body_Justification_7)
        except NameError and AttributeError:
            pass
        try:
            g = Label(w,text=o.Sub_Title_8,bg=BG,fg=FG)
            g.config(font=(o.Sub_Title_Font_8,o.Sub_Title_FontSize_8))
            g.pack(anchor=o.Sub_Title_Justification_8)
        except NameError and AttributeError:
            pass
        try:
            g1 = Label(w,text=o.Body_8,bg=BG,fg=FG)
            g1.config(font=(o. Body_Font_8,o.Body_FontSize_8))
            g1.pack(anchor=o.Body_Justification_1)
        except NameError and AttributeError:
            pass
        try:
            h = Label(w,text=o.Sub_Title_9,bg=BG,fg=FG)
            h.config(font=(o.Sub_Title_Font_9,o.Sub_Title_FontSize_9))
            h.pack(anchor=o.Sub_Title_Justification_9)
        except NameError and AttributeError:
            pass
        try:
            h1 = Label(w,text=o.Body_9,bg=BG,fg=FG)
            h1.config(font=(o. Body_Font_9,o.Body_FontSize_9))
            h1.pack(anchor=o.Body_Justification_9)
        except NameError and AttributeError:
            pass
        w.config(bg=BG)
        
r3 = Button(root,text="Customised Template",command=t4,bg="black",fg="white")

r.place(x=150,y=600)
r1.place(x=680,y=600)
r2.place(x=1180,y=600)
r3.place(x=1480,y= 300)
root.mainloop()
    
    
   


    

    
    
    
