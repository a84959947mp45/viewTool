# coding: utf-8

import re
from tkinter import *
from tkinter import filedialog
import matplotlib
import matplotlib.pyplot as plt
import svgutils.compose as sc
import numpy as np
from matplotlib import transforms

def ImportImage():
    
    x =np.array([])
    y =np.array([])
    filename =  filedialog.askopenfilename(initialdir = "~/Desktop",title = "Select file",filetypes = (("svg files","*.txt"),("jpeg files","*.jpg"),("png files", "*.png")))
    with open(filename) as f:
        n=0
        for line in f:
            point=re.split(",|\n",line)
            if(point[0]==""):
                break
            if(point[0]=="#"):
                continue
            x=np.append(x,round(float(point[0]),6))
            y=np.append(y,round(float(point[1]),6))
            n+=1

        print("trick point size: ",str(n))
        
        

        s = [0.01 for n in range(len(x))]
        plt.scatter(x, y,s=s)
        plt.title("World")

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.show()

def ImportImage2():
        
    x =np.array([])
    y =np.array([])
    filename =  filedialog.askopenfilename(initialdir = "~/Desktop",title = "Select file",filetypes = (("svg files","*.txt"),("jpeg files","*.jpg"),("png files", "*.png")))
    with open(filename) as f:
        for line in f:
            point=re.split(" ",line)
            print(len(point))
            for i in range(0,len(point),2):
                if(point[i]=="\n"):
                    break
                #hanle data 
                point[i]=(lambda x:-float(re.search('[\d]+', x).group()) if '-' in x else float(x),point[i])[1]
                point[i+1]=(lambda x:-float(re.search('[\d]+', x).group()) if '-' in x else float(x),point[i+1])[1]
                
               # print(point[i]+" "+point[i+1])
                x=np.append(x,round(float(point[i]),6))
                y=np.append(y,round(float(point[i+1]),6))

        s = [1 for n in range(len(x))]

        fig = plt.figure(dpi=180) 
        ax  = fig.add_subplot(111)

        ax.scatter(x, y,s=s)

        plt.title("World")

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.show()

def ImportImage3():
        
    x =np.array([])
    y =np.array([])
    filename =  filedialog.askopenfilename(initialdir = "~/Desktop",title = "Select file",filetypes = (("svg files","*.txt"),("jpeg files","*.jpg"),("png files", "*.png")))
    with open(filename) as f:
        for line in f:
            point=re.split(" ",line)
            print(len(point))
            for i in range(0,len(point),3):
                if(point[i]=="\n"):
                    break
                #hanle data 
                point[i]=(lambda x:-float(re.search('[\d]+', x).group()) if '-' in x else float(x),point[i])[1]
                point[i+1]=(lambda x:-float(re.search('[\d]+', x).group()) if '-' in x else float(x),point[i+1])[1]
                
               # print(point[i]+" "+point[i+1])
                x=np.append(x,round(float(point[i]),6))
                y=np.append(y,round(float(point[i+1]),6))

        s = [5 for n in range(len(x))]

        plt.figure(dpi=180) 
        plt.scatter(x, y,s=s)

        plt.title("World")

        plt.xlabel("X")
        plt.ylabel("Y")

       # plt.xlim(0,)
     #   plt.ylim(0,)
        plt.show()


if __name__ == '__main__':
 
    root = Tk()
    root.geometry('1080x720')
    ImportButton = Button(root,text="import .svg binary position txt file",command=ImportImage)
    ImportButton2 = Button(root,text="import .dae use position txt file-2point",command=ImportImage2)
    ImportButton3 = Button(root,text="import .dae use position txt file-3point",command=ImportImage3)
    ImportButton.pack()
    ImportButton2.pack()
    ImportButton3.pack()


    root.mainloop()

