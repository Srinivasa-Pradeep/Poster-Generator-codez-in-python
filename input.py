
def inputs_1():
    global Title
    Title = input("Enter the title of document: ")
    txt_File= open("User's Data.txt","a")
    #txt_File= open(str(Title),"a")
    txt_File.write("Title : ")
    txt_File.write(Title)
    txt_File.write("\n")
    txt_File.close()
    
    if Template not in ["Template_1","Template_2","Template_3"]:
        global Title_Font
        global Title_FontSize
        Title_Font =input("Enter the Title font: ")
        Title_FontSize =input("Enter the Title font size: ")
        


        global Title_Justification
        Title_Justification = input("Enter the Title Justification(Left- w or Right- e or centre- center) : ")

        global File_Justification
        File_Justification = "n"
        #if File_Justification is "y" :
            
        
        

    
    yes_no =  input("Would you like to enter a By line:(y/n) ")
    if yes_no == "y" :
        global By_Line
        By_Line =input("Enter a By line: ")
        
        txt_File= open("User's Data.txt","a")
        #txt_File= open(str(Title),"a")
        txt_File.write("By_Line : ")
        txt_File.write(By_Line)
        txt_File.write("\n")
        txt_File.close()
        


        if Template not in ["Template_1","Template_2","Template_3"]:
            global By_Line_Font
            global By_Line_FontSize
            By_Line_Font =input("Enter the By line font: ")
            By_Line_FontSize =input("Enter the By line font size: ")

            if File_Justification != "y" :
                global By_Line_Justification
                By_Line_Justification = input("Enter the By line Justification(Left- w or Right- e or centre- center) : ")
            
    

    
def inputs_2():
    global Sub_Title_Count
    yes_no =  input("Would you like to enter a Sub Title:(y/n) ")
    if yes_no == "y" :
        
        x="Sub_Title_" + str(Sub_Title_Count)
        globals() [x] = input("Enter a Sub Title: ")
        txt_File= open("User's Data.txt","a")
        #txt_File= open(str(Title),"a")
        txt_File.write(x)
        txt_File.write(" : ") 
        txt_File.write(globals()[x])
        txt_File.write("\n")
        txt_File.close()

        
        
        if Template not in ["Template_1","Template_2","Template_3"]:

            global Sub_Title_Font_Permission
            if Sub_Title_Font_Permission in [1,2] :
                    x="Sub_Title_Font_" + str(Sub_Title_Count)
                    globals() [x] = input("Enter Sub Title Font: ")
                    
                    global Sub_Title_Font
                     
                    if Sub_Title_Font_Permission == 1:
                        Sub_Title_Font_Permission = "n"
                        if Sub_Title_Font_Permission == "y" :
                            Sub_Title_Font = globals()[x]
                            Sub_Title_Font_Permission = 3
                        if Sub_Title_Font_Permission == "n" :
                            Sub_Title_Font_Permission = 2

            global Sub_Title_FontSize_Permission
            if Sub_Title_FontSize_Permission in [1,2] :
                    x="Sub_Title_FontSize_" + str(Sub_Title_Count)
                    globals() [x] = input("Enter Sub Title Font Size: ")

                    global Sub_Title_FontSize
                     
                    if Sub_Title_FontSize_Permission == 1:
                        Sub_Title_FontSize_Permission = "n"
                        if Sub_Title_FontSize_Permission == "y" :
                            Sub_Title_FontSize = globals()[x]
                            Sub_Title_FontSize_Permission = 3
                        if Sub_Title_FontSize_Permission == "n" :
                            Sub_Title_FontSize_Permission = 2
            
            if File_Justification != "y" :
                
                global Sub_Title_Justification_Permission
                if Sub_Title_Justification_Permission in [1,2] :
                    
                    
                    x = "Sub_Title_Justification_" + str(Sub_Title_Count)
                    globals() [x] = input("Enter Sub Title Justification:(Left- w or Right- e or centre- center): ")
                    

                    
                    global Sub_Title_Justification
                     

                    if Sub_Title_Justification_Permission == 1:
                        Sub_Title_Justification_Permission = "n"
                        if Sub_Title_Justification_Permission == "y" :
                            Sub_Title_Justification = globals()[x]
                            Sub_Title_Justification_Permission = 3
                        if Sub_Title_Justification_Permission == "n" :
                            Sub_Title_Justification_Permission = 2


           
    global Body_Count
    yes_no =  input("Would you like to enter a Body:(y/n) ")
    if yes_no == "y" :
        x="Body_" + str(Body_Count)
        globals() [x] = input("Enter a Body: ")
        
        txt_File= open("User's Data.txt","a")
        #txt_File= open(str(Title),"a")
        txt_File.write(x)
        txt_File.write(" : ") 
        txt_File.write(globals()[x])
        txt_File.write("\n")
        txt_File.close()
        
        
        if Template not in ["Template_1","Template_2","Template_3"]:
            global Body_Font_Permission
            if Body_Font_Permission in [1,2] :
                        x="Body_Font_" + str(Body_Count)
                        globals() [x] = input("Enter a Body Font: ")
                        
                        global Body_Font
                         
                        if Body_Font_Permission == 1:
                            Body_Font_Permission = "n"
                            if Body_Font_Permission == "y" :
                                Body_Font = globals()[x]
                                Body_Font_Permission = 3
                            if Body_Font_Permission == "n" :
                                Body_Font_Permission = 2
            
            global Body_FontSize_Permission
            if Body_FontSize_Permission in [1,2] :
                        x="Body_FontSize_" + str(Body_Count)
                        globals() [x] = input("Enter a Body Font Size: ")
                         
                        if Body_FontSize_Permission == 1:
                            Body_FontSize_Permission = "n"
                            if Body_FontSize_Permission == "y" :
                                Body_FontSize = globals()[x]
                                Body_FontSize_Permission = 3
                            if Body_FontSize_Permission == "n" :
                                Body_FontSize_Permission = 2
            


            if File_Justification != "y" :

                global Body_Justification_Permission
                if Body_Justification_Permission in [1,2] :

                        
                        x = "Body_Justification_" + str(Body_Count)
                        globals() [x] = input("Enter Body Justification:(Left- w or Right- e or centre- center): ")

                        global Body_Justification
                        

                        if Body_Justification_Permission == 1:
                            Body_Justification_Permission = "n"
                            if Body_Justification_Permission == "y" :
                                Body_Justification = globals()[x]
                                Body_Justification_Permission = 3
                                
                            if Body_Justification_Permission == "n" :
                                Body_Justification_Permission = 2
                        

        
        



    Sub_Title_Count +=1
    Body_Count +=1


def Templates(a):
    global Title_Font
    Title_Font="Times New Roman"
    
    global Title_FontSize
    Title_FontSize=50
    
    global By_Line_Font
    By_Line_Font = "Times New Roman"
    global By_Line_FontSize
    By_Line_FontSize = 30

    global Sub_Title_Font
    Sub_Title_Font= "Times New Roman"
    global Sub_Title_FontSize
    Sub_Title_FontSize = 30

    global Body_Font
    Body_Font = "Aerial"
    global Body_FontSize
    Body_FontSize = 24

    global File_Justification
    if a == "Template_1":
        File_Justification="w"
    if a == "Template_2":
        File_Justification="center"
    if a == "Template_3":
        File_Justification="e"

#=============================================================
Sub_Title_Count=1
Body_Count=1

Sub_Title_Font_Permission = 1
Sub_Title_FontSize_Permission = 1
Sub_Title_Justification_Permission = 1

Body_Font_Permission = 1
Body_FontSize_Permission = 1
Body_Justification_Permission = 1


            
