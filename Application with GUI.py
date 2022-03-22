from tkinter import *

root=Tk()

mylabel1=Label(root,text="Hallo in our application :)")
mylabel2=Label(root,text="choose country ")
mylabel3=Label(root,text="           ")

mylabel1.pack()
mylabel2.pack()
mylabel3.pack()
def myClick_15():
    mylabel27=Label(root,text="Lowest populatioin in Taxis")
    mylabel27.pack()

def myClick_14():
    mylabel26=Label(root,text="Highest population in California")
    mylabel26.pack()

def myClick_13():
    mylabel29=Label(root,text="total population is 120,000,000")
    mylabel29.pack()

def myClick_12():
            mylabel30=Label(root,text="Taxis,sanFransisco,NewYourk")
            mylabel30.pack()


def myClick_11():
    s=Button(root,text="states",command=myClick_12)        
    t_p=Button(root,text="total population",command=myClick_13)
    H_p=Button(root,text="Highest state",command=myClick_14)
    L_p=Button(root,text="lowest state",command=myClick_15)

    s.pack()
    t_p.pack()
    H_p.pack()
    L_p.pack()

def myClick_10():
    mylabel7=Label(root,text="Lowest populatioin in BM")
    mylabel7.pack()

def myClick_9():
    mylabel6=Label(root,text="Highest population in Alberta")
    mylabel6.pack()

def myClick_8():
    mylabel9=Label(root,text="total population is 20,000,000")
    mylabel9.pack()

def myClick_7():
            mylabel8=Label(root,text="BM,onteria,Alberta")
            mylabel8.pack()
            
def myClick_6():
    state=Button(root,text="states",command=myClick_7)        
    total_population=Button(root,text="total population",command=myClick_8)
    Highest_population=Button(root,text="Highest state",command=myClick_9)
    Lowest_population=Button(root,text="lowest state",command=myClick_10)

    state.pack()
    total_population.pack()
    Highest_population.pack()
    Lowest_population.pack()

def myClick_5():
    mylabel7=Label(root,text="Lowest populatioin in Saini")
    mylabel7.pack()

def myClick_4():
    mylabel6=Label(root,text="Highest population in Cairo")
    mylabel6.pack()

def myClick_3():
    mylabel5=Label(root,text="total population is 100,000,000")
    mylabel5.pack()

def myClick_2():
            mylabel4=Label(root,text="Cairo,Giza,Sharkia,Sohag")
            mylabel4.pack()

def myClick_1():
    A=Button(root,text="states",command=myClick_2)        
    B=Button(root,text="total population",command=myClick_3)
    C=Button(root,text="Highest state",command=myClick_4)
    D=Button(root,text="lowest state",command=myClick_5)

    
    A.pack()
    B.pack()
    C.pack()
    D.pack()

myButton1=Button(root,text="Egypt",command=myClick_1)
myButton2=Button(root,text="Canada",command=myClick_6)
myButton3=Button(root,text="USA",command=myClick_11)


myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()


