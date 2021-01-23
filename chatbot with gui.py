from tkinter import *
from re import *
from bs4 import BeautifulSoup 
import requests
global ids
ids=1
root=Tk()
root.title("Chatbot")
root.geometry('450x500')
main_menu=Menu(root)

file_menu=Menu(root)
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit..")

###
edit_menu=Menu(root)
edit_menu.add_command(label="Crop..")
edit_menu.add_command(label="Format..")
edit_menu.add_command(label="Undo..")
###

main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow=Text(root,bd=1,bg='white',width=50,height=8)
chatWindow.place(x=6,height=385,width=400)

messageWindow=Text(root,bg='white',width=30,height=4,)

messageWindow.place(x=6,y=400,height=88,width=260)
greet=" Hey I am Bot . I am here to assist you\n------------------------------------------\n"
chatWindow.insert(END, greet)

def gr(a):
    a=a.lower()
    if(a=="how are you?" or a=="how are you" or a=="how r u" or a==" how r u?" or a=="how are u"):
        w="Bot: I am good"
            
    elif(a=="what’s up?" or a=="sup?"):
        w="Bot: I am here to assist you. SUP\n"
    elif(a=="good morning" or a=="good evening" or a=="good night"):
        w="Bot: Greetings of the day to you\n"
    
    elif(a=="hello" or a=="hi" or a=="hey"):
        w="Bot: Hey\n"
    else:
        w="Bot: I didn`t get you"
        w=w+"\n\n"
    chatWindow.insert(END, w)
    chatWindow.tag_add("start", "1.0","2.0")
    #chatWindow.tag_config('start',background="red", foreground="green")
def conf():
    con_book.destroy()
    ch=messageWindow.get("0.0","end-1c")
    ch=ch.lower()
    if(ch=="yes" or ch=='yeah'):
        r="\nBot: Appointment Confirmed\n"
        
    else:
        r="\nBot: Appointment Cancelled\n"
    chatWindow.insert(END, r)
    
def date_code():
    global L
    dat.destroy()
    date=messageWindow.get("0.0","end-1c")
    st="\nUser : "+date+"\n"
    chatWindow.insert(END, st)
    L+=[date]
    final="\nBot: Account id: "+str(ids)+" has an appointment \nin "+L[0]+" in the "+L[1]+" Hospital\n on "+L[0]+"\n"
    chatWindow.insert(END, final)
    global con_book
    con_book=Button(root,text="Confirm Appointment",bg='green',activebackground='white',width=12,height=5,font=('Arial',12),command=lambda : conf())
    con_book.place(x=270,y=400,height=88,width=120)
    
def nam_code():
    global L
    da.destroy()
    nam=messageWindow.get("0.0","end-1c")
    st="\nUser : "+nam+"\n"
    chatWindow.insert(END, st)
    
    L+=[nam]
    u="\nBot: Enter the checkin data \n"
    chatWindow.insert(END, u)
    global dat
    dat=Button(root,text="Confirm date",bg='green',activebackground='white',width=12,height=5,font=('Arial',12),command=lambda : date_code())
    dat.place(x=270,y=400,height=88,width=120)

    
a=''
global d
L=[]
d={}
def get_city():
    b1.destroy()
    global L
    
    city=messageWindow.get("0.0","end-1c")
    st="\nUser : "+city+"\n"
    chatWindow.insert(END, st)
    city=city.lower()
    L+=[city]
    
    URL = "https://www.google.com/search?q=google+hospital+in+"+city
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html.parser')
    l=[]
    s=""
    for link in soup.findAll('span'):
        if(link.string!=None):
            l+=[link.string]
    
    s="\nBot: Few hospitals in "+city+" are as follows \n1) "+l[15]+" "+l[16]+" "+"\n2)"+l[18]+" "+l[19]+" "+"\n2)"+l[21]+" "+l[22]+" "+"\n"
    chatWindow.insert(END, s)
    nam="\nBot: enter the Name of Hospital\n"
    chatWindow.insert(END, nam)
    global da
    da=Button(root,text="Confirm",bg='green',activebackground='white',width=12,height=5,font=('Arial',20),command=lambda : nam_code())
    da.place(x=270,y=400,height=88,width=120)

def get_text_book():
    q.destroy()
    n=messageWindow.get("0.0","end-1c")
    st="\nUser : "+n+"\n"
    chatWindow.insert(END, st)
    n=n.lower()
    if(n=="nah" or n=="no"):
        e="\nBot: Okay I will stop the booking process\n"
        chatWindow.insert(END, e)

    elif(n=="yes" or n=="yeah"):
        global b1
        t="\nBot: In which city do you want  ?\n"
        
        chatWindow.insert(END, t)
        b1=Button(root,text="Continue",bg='green',activebackground='white',width=12,height=5,font=('Arial',20),command=lambda : get_city())
        b1.place(x=270,y=400,height=88,width=120)
    messageWindow.delete('1.0', END)

def get_text():
    a=messageWindow.get("0.0","end-1c")
    st="\nUser : "+a+"\n"
    chatWindow.insert(END, st)
    chatWindow.tag_add("start", "1.0","2.0")
    messageWindow.delete('1.0', END)
    a=a.lower()
    #chatWindow.tag_config('start',background="yellow", foreground="green")
    y=re.search("^hospital", a) or re.search("appointment", a) or re.search("booking", a) or re.search("disease", a) or re.search("book", a)
    x = re.search("^good", a) or re.search("^how", a) or re.search("hey", a) or re.search("hello", a) or re.search("hi", a)
    if(x):
        gr(a)
    elif(y):
        t="\nBot: Do you want to book a hospital appointment ?\n"
        chatWindow.insert(END, t)
        global q

        q=Button(root,text="Book",bg='green',activebackground='white',width=12,height=5,font=('Arial',20),command=lambda : get_text_book())
        q.place(x=270,y=400,height=88,width=120)
        



input_button=Button(root,text="Send",bg='green',activebackground='white',width=12,height=5,font=('Arial',20),command=lambda : get_text())
input_button.place(x=270,y=400,height=88,width=120)

scrollbar=Scrollbar(root,command=chatWindow.yview())
scrollbar.place(x=400,y=5,height=385)


root.mainloop()













