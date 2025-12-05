from tkinter import*

import tkinter as tk

win = Tk()

win.title("전라북도 관광지") #창 이름



lab = Label(win, text="원하는 관광지", width =50, height =10)

lab.pack()





def btnCallback(): #버튼 클릭 때 처리되는 함수

    win.destroy()



def 산들(): 

    window = Tk()



    window.geometry("400x400")

    window.title("전북의 산")

    window.resizable(False, False)



    btn1 = Button (window,width=10, text ="모악산",command = 모악산)

    btn1.pack(side=TOP,padx=10, pady=8)



    btn2 = Button (window,width=10, text ="지리산",command = 지리산)

    btn2.pack(side=TOP,padx=10, pady=8)



    btn3 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn3.pack(side=TOP,padx=10, pady=8)



def 모악산():

    window = Toplevel()

    window.geometry("400x400")

    window.title("모악산")

    window.resizable(False, False)

    canvas=Canvas(window, bg="white", width=300, height=200)

    canvas.pack()

    img=PhotoImage(file="moak.png")

    canvas.create_image(0, 0, anchor=NW, image=img)

    lab = Label(window, text="모악산에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)

    window.mainloop()



def 지리산(): 

    window = Tk()



    window.geometry("400x400")

    window.title("지리산")

    window.resizable(False, False)

    lab = Label(window, text="지리산에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)





def 바다들(): 

    window = Tk() 



    window.geometry("400x400")

    window.title("전북의 바다")

    window.resizable(False, False)



    btn1 = Button (window,width=10, text ="바다1",command = 바다1)

    btn1.pack(side=TOP,padx=10, pady=8)



    btn2 = Button (window,width=10, text ="바다2",command = 바다2)

    btn2.pack(side=TOP,padx=10, pady=8)



    btn3 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn3.pack(side=TOP,padx=10, pady=8)



def 바다1(): 

    window = Tk()



    window.geometry("400x400")

    window.title("바다1")

    window.resizable(False, False)

    lab = Label(window, text="바다1에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)





def 바다2(): 

    window = Tk()



    window.geometry("400x400")

    window.title("바다2")

    window.resizable(False, False)

    lab = Label(window, text="바다2에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)



    

def 관광지(): 

    window = Tk() 



    window.geometry("400x400")

    window.title("전북의 바다")

    window.resizable(False, False)



    btn1 = Button (window,width=10, text ="관광지1",command = 관광지1)

    btn1.pack(side=TOP,padx=10, pady=8)



    btn2 = Button (window,width=10, text ="관광지2",command = 관광지2)

    btn2.pack(side=TOP,padx=10, pady=8)



    btn3 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn3.pack(side=TOP,padx=10, pady=8)



def 관광지1(): 

    window = Tk()



    window.geometry("400x400")

    window.title("관광지1")

    window.resizable(False, False)

    lab = Label(window, text="관광지1에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)

    

def 관광지2(): 

    window = Tk()



    window.geometry("400x400")

    window.title("관광지2")

    window.resizable(False, False)

    lab = Label(window, text="관광지2에 관하여", width =40, height =20)

    lab.pack()

    btn1 = Button (window,width=10, text ="닫기", command = window.destroy)

    btn1.pack(side=TOP,padx=10, pady=8)







btn1 = Button (width=10, text ="산",command = 산들)

btn1.pack(side=TOP,padx=10, pady=8) 





btn2 = Button (width=10, text ="바다",command = 바다들)

btn2.pack(side=TOP,padx=10, pady=8) 





btn3 = Button (width=10, text ="관광지",command = 관광지)

btn3.pack(side=TOP,padx=10, pady=8) 





btn4 = Button (win,width=10, text ="닫기", command =btnCallback)

btn4.pack(side=TOP,padx=10, pady=8)







win.mainloop()


