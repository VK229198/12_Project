from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter as tk

#------------------------------images--------------------------------------
image3="2.jpg"
image1="lib.jpg"
image2="boston-usa-books-library.jpg"


#-----------------------------submenu or mainscreen-------------------------    
def sub_menu():
    global con
    global cur
    if con.is_connected():
        
        q="create table if not exists BOOKS(BOOKID INT(2) PRIMARY KEY NOT NULL,BOOKNAME VARCHAR(30) NOT NULL,AUTHOR VARCHAR(30) NOT NULL,GENRE VARCHAR(10), COPIES INT ,LANGUAGE VARCHAR(15));"
        cur.execute(q)
        con.commit()
        
        q1="create table if not exists STUDENT(CNO INT PRIMARY KEY NOT NULL,CNAME VARCHAR(30) NOT NULL,TELE CHAR(10),ADR VARCHAR(30),BOOKID INT(2) DEFAULT(NULL),FOREIGN KEY (BOOKID) REFERENCES BOOKS(BOOKID) ON DELETE RESTRICT ON UPDATE RESTRICT,TOKEN INT(1) check(token in (0,1)));"
        cur.execute(q1)
        con.commit()
        
        w = root1.winfo_screenwidth()
        h = root1.winfo_screenheight()
        self=canvases(image1,w,h)
        l1=Button(self,text='BOOK DATA',font='Garamond 22 bold',fg='white',bg='black',width=19,padx=10,borderwidth=0,command=book).place(x=100,y=500)
        l2=Button(self,text='STUDENT DATA',font='Garamond 22 bold',fg='black',bg='yellow',width=19,padx=10,borderwidth=0,command=student).place(x=800,y=500)
        l3=Button(self,text='About',font='Garamond 22 bold',fg='white',bg='#714c32',width=10,padx=3,borderwidth=0,command=aboutit).place(x=10,y=10)

        root1.mainloop()
        
#------------------------------------about the program-------------------------------------
def aboutit():
    f1=tk.Frame(height=450,width=790,bg='grey5')
    f1.place(x=300,y=30)
    
    label=tk.Label(f1,text="Library",font=("blogger light",20))
    label.place(x=300,y=10)

    Frame(f1,width=295,height=2,bg='black').place(x=475,y=50)
    def text(): 
        f=open("ABOUT.txt")
        t=f.read()
        mytext.insert(END,t)
        f.close()

    mytext=Text(f1,width=70,font=("blogger light",14),bg="white")
    mytext.place(x=10,y=70)
    text()

    h1=Button(f1,text='X',font='Papyrus 22 bold',fg='red',bg='black',width=1,padx=3,borderwidth=0,command=sub_menu).place(x=740,y=10)
    
#-----------------------------bookdata and functions-----------------------------------------------         
def book():
    
    w = root1.winfo_screenwidth()
    h = root1.winfo_screenheight()
    self=canvases(image2,w,h)
    l1=Button(self,text='Add Books',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=addbook).place(x=12,y=100)
    l2=Button(self,text='Search Books',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=search).place(x=12,y=200)
    l3=Button(self,text='All Books',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=all).place(x=12,y=300)
#here adding delete and modifying a book
    l5=Button(self,text='Modify Book',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=deletebook).place(x=12,y=390)

    
    l4=Button(self,text='<- Main Menu',font='Papyrus 22 bold',fg='black',bg='honeydew2',width=15,padx=10,command=sub_menu).place(x=12,y=500)

#----------------------------adding book + validation------------------------------------------       
def addbook():
    global  aid,aauthor,aname,acopies,agenre,aloc
    
    aid=IntVar()
    aauthor=StringVar()
    aname=StringVar()
    acopies=IntVar()
    agenre=StringVar()
    aloc=StringVar()

    #call back function
    def checkname(name):
        if name.isdigit():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('error','not allowed')
            return False

    #validation
    def validation():
        global aid
        if aid=='':
            messagebox.showerror('error','pls enter bookid',parent=root1)


 
    f1=tk.Frame(height=500,width=650,bg='grey5')
    f1.place(x=500,y=100)
    
    l1=Label(f1,text='Book ID : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=50)
    e1=Entry(f1,width=45,bg='orange',fg='black',textvariable=aid)
    e1.place(x=150,y=50)

    #callback and validation
    validate_name=root1.register(checkname)
    e1.config(validate='key',validatecommand=(validate_name,'%P'))


    l2=Label(f1,text='Title : ',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=100)
    e2=Entry(f1,width=45,bg='orange',fg='black',textvariable=aname)
    e2.place(x=150,y=100)
    
    l3=Label(f1,text='Author : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=150)
    e3=Entry(f1,width=45,bg='orange',fg='black',textvariable=aauthor)
    e3.place(x=150,y=150)
    
    l4=Label(f1,text='Genre : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=200)
    e4=Entry(f1,width=45,bg='orange',fg='black',textvariable=agenre)
    e4.place(x=150,y=200)
    
    l5=Label(f1,text='Copies : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=250)
    e5=Entry(f1,width=45,bg='orange',fg='black',textvariable=acopies)
    e5.place(x=150,y=250)
    
    l6=Label(f1,text='Language : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=300)
    e6=Entry(f1,width=45,bg='orange',fg='black',textvariable=aloc)
    e6.place(x=150,y=300)
    
    b1=Button(f1,text='Add',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[adddata([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()]),e1.delete(0,END),e2.delete(0,END),e3.delete(0,END),e4.delete(0,END),e5.delete(0,END),e6.delete(0,END)])
    b1.place(x=150,y=400)
  
    
    b2=Button(f1,text='Back',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=book).place(x=350,y=400)    

            
    root1.mainloop()
    

  
def adddata(l):
    global  aid,aauthor,aname,acopies,agenre,aloc
    global con
    global cur
    

    if ((l[0]=='') or (l[1]=='') or (l[2]=='') or (l[3]=='') or (l[4]=='') or (l[5]=='')):
            messagebox.showinfo("Error","Fields cannot be empty.")
    else:
        if not(l[0].isdigit()):
            messagebox.showerror('','invalid bookid')
        elif not(l[2].isalpha()):
            messagebox.showerror('','invalid author')
        elif not(l[3].isalpha()):
            messagebox.showerror('','invalid genre')
        elif not(l[4].isdigit()):
            messagebox.showerror('','invalid number of copies')
        elif not(l[5].isalpha()):
            messagebox.showerror('','unknown language')
        else:
            q='select bookid from BOOKS'
            cur.execute(q)
            a=cur.fetchall()
            print (a)
           
            m=int(l[0])
            print(m)
            for tuple1 in a:
                if m in tuple1:
                    messagebox.showinfo("fail","bookid already exsists")
                    break
            else:
                print('how')
                q="insert into BOOKS values(%s,%s,%s,%s,%s,%s)"
                cur.execute(q,l)
                con.commit()
                messagebox.showinfo("Success","Book added successfully")
        
    con.commit()
    
#---------------------------------------search data------------------------------------------
def search():
    global aid
    aid=StringVar()
    
    f1=Frame(height=500,width=650,bg='black')
    f1.place(x=500,y=100)
    
    l1=Label(f1,text='Book ID/Title/Author/Genre: ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=20,y=40)
    e1=Entry(f1,width=25,bd=5,bg='orange',fg='black',textvariable=aid).place(x=260,y=40)
    
    b1=Button(f1,text='Search',bg='orange',font='Papyrus 10 bold',width=9,bd=2,command=serch1).place(x=500,y=37)
    b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=2,command=book).place(x=250,y=450)
    

    
def serch1():
    global aid,k

    k=aid.get()
    if k!="":
        tree=ttk.Treeview(root1,selectmode='browse')
        tree.place(x=527,y=215)
        tree['columns']=("BOOKID","BOOKNAME","AUTHOR","GENRE")
        tree['show']='headings'
        tree.column("BOOKID",width=150,anchor='c')
        tree.column("BOOKNAME",width=150,anchor='c')
        tree.column("AUTHOR",width=150,anchor='c')
        tree.column("GENRE",width=150,anchor='c')
        tree.heading("BOOKID",text='BOOKID')
        tree.heading("BOOKNAME",text='BOOKNAME')
        tree.heading("AUTHOR",text='AUTHOR')
        tree.heading("GENRE",text='GENRE')
        x="select BOOKID,BOOKNAME,AUTHOR,GENRE from BOOKS where BOOKID=%s OR BOOKNAME=%s OR AUTHOR=%s OR GENRE=%s"
        s=(k,k,k,k)
        cur.execute(x,s)
        a=cur.fetchall()
        if len(a)!=0:    
            for i in a:
                tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3]))
    
        else:
            messagebox.showinfo("Error","Data not found")



    else:
        messagebox.showinfo("Error","Search field cannot be empty.")





        
#-----------------------------displaying book data-------------------------------------
def all():
    
    f1=tk.Frame(height=500,width=650,bg='black')
    f1.place(x=500,y=100)
    
    tree=ttk.Treeview(f1,selectmode='browse')
    tree.place(x=25,y=50)
    tree['columns']=("BOOKID","BOOKNAME","AUTHOR","GENRE","COPIES","LANGUAGE")
    tree['show']='headings'
    tree.column("BOOKID",width=100,anchor='c')
    tree.column("BOOKNAME",width=100,anchor='c')
    tree.column("AUTHOR",width=100,anchor='c')
    tree.column("GENRE",width=100,anchor='c')
    tree.column("COPIES",width=100,anchor='c')
    tree.column("LANGUAGE",width=100,anchor='c')
    tree.heading("BOOKID",text='BOOKID')
    tree.heading("BOOKNAME",text='BOOKNAME')
    tree.heading("AUTHOR",text='AUTHOR')
    tree.heading("GENRE",text='GENRE')
    tree.heading("COPIES",text='COPIES')
    tree.heading("LANGUAGE",text='LANGUAGE')
    x="select * from BOOKS"
    cur.execute(x)
    a=cur.fetchall()
    if len(a)!=0:    
        for i in a:
            tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))

    b1=Button(f1,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=book).place(x=250,y=400)
#---------------------------------------------------------- deleting a book------------------------------
def deletebook():
    global con
    global cur
    global aid,aauthor,aname,acopies,agenre,aloc
    
    aid=StringVar()
    aname=StringVar()
    aauthor=StringVar()
    acopies=IntVar()
    agenre=StringVar()
    aloc=StringVar()

    f1=tk.Frame(height=500,width=650,bg='grey5')
    f1.place(x=500,y=100)

    l1=Label(f1,text='Book ID : ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=70,y=40)
    e1=Entry(f1,width=25,bd=5,bg='orange',fg='black',textvariable=aid).place(x=260,y=40)

    b1=Button(f1,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=book).place(x=50,y=400)
    b2=Button(f1,text='modify',bg='orange' ,fg='black',width=10,bd=3,command=modifier).place(x=500,y=400)
    b3=Button(f1,text='to delete',bg='orange' ,fg='black',width=10,bd=3,command=deleter).place(x=400,y=400)

    root1.mainloop()

def modifier():
    global con
    global cur
    #global aid,aauthor,aname,acopies,agenre,aloc

    aname = tk.StringVar()
    aauthor = tk.StringVar()
    acopies = tk.IntVar()
    agenre = tk.StringVar()
    aloc = tk.StringVar()


    k=aid.get()
    if k!="":
        if k.isdigit():
            l=int(k)
            t=''
            x="select BOOKID from BOOKS"
            cur.execute(x)
            a=cur.fetchall()
            if len(a)!=0:
                for t in a:
                    if l in t:
                        #messagebox.showinfo("","GIVEN ID EXISTS")
                        f2=tk.Frame(height=270,width=600,bg='black').place(x=520,y=200)
                        
                        l1=Label(f2,text='NEW TITLE :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l1.place(x=530,y=210)
                        g1=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=aname)
                        g1.place(x=640,y=210)
                        
                        #b1=Button(f2,text='UPDATE TITLE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e1.get()]),e1.delete(0,END),])
                        #b1.place(x=820,y=210)

                        l2=Label(f2,text='NEW AUTHOR :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l2.place(x=530,y=250)
                        g2=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=aauthor)
                        g2.place(x=640,y=250)
                        
                        #b2=Button(f2,text='UPDATE AUTHOR',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e2.get()]),e2.delete(0,END),])
                        #b2.place(x=820,y=250)
                        

                        l3=Label(f2,text='NEW GENRE :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l3.place(x=530,y=290)
                        g3=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=agenre)
                        g3.place(x=640,y=290)
                        
                        #b3=Button(f2,text='UPDATE GENRE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e3.get()]),e3.delete(0,END),])
                        #b3.place(x=820,y=290)

                        l4=Label(f2,text='NEW COPIES :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l4.place(x=530,y=330)
                        g4=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=acopies)
                        g4.place(x=640,y=330)
                        
                        #b4=Button(f2,text='UPDATE COPIES',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e4.get()]),e4.delete(0,END),])
                        #b4.place(x=820,y=330)
                        

                        l5=Label(f2,text='NEW LANGUAGE :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l5.place(x=530,y=370)
                        g5=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=aloc)
                        g5.place(x=640,y=370)
                        
                        #b5=Button(f2,text='UPDATE LANGUAGE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e5.get()]),e5.delete(0,END),])
                        #b5.place(x=820,y=370)
                        

                        b6=Button(f2,text='UPDATE ALL',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([g1.get(),g2.get(),g3.get(),g4.get(),g5.get()],l),g1.delete(0,END),g2.delete(0,END),g3.delete(0,END),g4.delete(0,END),g5.delete(0,END)])
                        b6.place(x=640,y=440)

                        #root1.mainloop()
                        break
     
                        
                else:
                    messagebox.showinfo('',"ID  does not exist")
        else:
            messagebox.showinfo('',"ID cannot be a letter")

    else:
        messagebox.showinfo("Error","Search field cannot be empty.")
        
    root1.mainloop()
    

def updatedata(l,x):
    global con
    global cur
    #global aid,aauthor,aname,acopies,agenre,aloc

    if ((l[0]=='') or (l[1]=='') or (l[2]=='') or (l[3]=='') or (l[4]=='')):
            messagebox.showinfo("Error","Fields cannot be empty.")
    else:
        if not(l[0].isalpha()):
            messagebox.showerror('','invalid title')
        elif not(l[1].isalpha()):
            messagebox.showerror('','invalid author')
        elif not(l[2].isalpha()):
            messagebox.showerror('','invalid genre')
        elif not(l[3].isdigit()):
            messagebox.showerror('','invalid number of copies')
        elif not(l[4].isalpha()):
            messagebox.showerror('','unknown language')
        else:
            print(x)
            l.append(x)
            q='UPDATE BOOKS SET BOOKNAME=%s,AUTHOR=%s,GENRE=%s,COPIES=%s,LANGUAGE=%s WHERE BOOKID=%s;'
            cur.execute(q,l)
    con.commit()
#=================================deleting==========================================

def deleter():
    global con
    global cur
    global aid,k

    k=aid.get()
    if k!="":
        tree=ttk.Treeview(root1,selectmode='browse')
        tree.place(x=527,y=190)
        
        f1=tk.Frame(height=70,width=590,bg='black').place(x=527,y=420)
        
        b1=Button(f1,text='DELETE DATA',bg='orange' ,fg='black',width=10,bd=3,command=lambda:[deleteoff([k,]),tree.destroy()])
        b1.place(x=550,y=440)

        tree['columns']=("BOOKID","BOOKNAME","AUTHOR","GENRE")
        tree['show']='headings'
        tree.column("BOOKID",width=140,anchor='c')
        tree.column("BOOKNAME",width=150,anchor='c')
        tree.column("AUTHOR",width=150,anchor='c')
        tree.column("GENRE",width=150,anchor='c')
        
        tree.heading("BOOKID",text='BOOKID')
        tree.heading("BOOKNAME",text='BOOKNAME')
        tree.heading("AUTHOR",text='AUTHOR')
        tree.heading("GENRE",text='GENRE')
        
        x="select BOOKID,BOOKNAME,AUTHOR,GENRE from BOOKS where BOOKID=%s OR BOOKNAME=%s OR AUTHOR=%s OR GENRE=%s"
        s=(k,k,k,k)
        cur.execute(x,s)
        a=cur.fetchall()
        if len(a)!=0:    
            for i in a:
                tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3]))
    
        else:
            messagebox.showinfo("Error","Data not found")

    else:
        messagebox.showinfo("Error","Search field cannot be empty.")
        
#==
def deleteoff(l):
    global con
    global cur
   
    q2='select bookid from books'
    cur.execute(q2)
    a=cur.fetchall()
    
    print(a)
    k=int(l[0])
    
    for t in a:
        if k in t:
            
            q1='select token from student where bookid=%s'
            cur.execute(q1,l)
            b=cur.fetchone()   
            if b!=None and b!=1:
                messagebox.showinfo("error","CANNOT DELETE BOOK")
                break
            else: 
                q='DELETE FROM BOOKS WHERE BOOKID=%s;'
                cur.execute(q,l)
                messagebox.showinfo("DELETED","RECORD HAS BEEN DELETED")
                break
    else:
        messagebox.showinfo("error","RECORD DOESNT EXIST")
    con.commit()

 
#--------------------------------------student data---------------------------------------------
def student():
    w = root1.winfo_screenwidth()
    h = root1.winfo_screenheight()
    self=canvases(image2,w,h)
    l1=Button(self,text='Issue/return book',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=issue).place(x=12,y=100)
    l2=Button(self,text='Modify',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=deletestudent).place(x=12,y=200)
    l3=Button(self,text='Student Activity',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=activity).place(x=12,y=300)
#new button registration
    l5=Button(self,text='Registration',font='Papyrus 22 bold',fg='black',bg='orange1',width=15,padx=10,command=register).place(x=12,y=390)

    
    l4=Button(self,text='<< Main Menu',font='Papyrus 22 bold',fg='black',bg='honeydew2',width=15,padx=10,command=sub_menu).place(x=12,y=500)

    
def issue():
    global aidd,astudentt
    
    aidd=StringVar()
    astudentt=StringVar()

    f1=tk.Frame(height=450,width=500,bg='black')
    f1.place(x=500,y=100)
    
    l1=Label(f1,text='Book ID : ',font='papyrus 15 bold',bg='black',fg='orange')
    l1.place(x=50,y=100)
    e1=Entry(f1,width=25,bd=4,bg='orange',textvariable=aidd)
    e1.place(x=180,y=100)
    
    l2=Label(f1,text='Student Id : ',font='papyrus 15 bold',bg='black',fg='orange')
    l2.place(x=50,y=150)
    e2=Entry(f1,width=25,bd=4,bg='orange',textvariable=astudentt)
    e2.place(x=180,y=150)

    
    b1=Button(f1,text='BACK',font='Papyrus 10 bold',fg='black',bg='orange',width=10,bd=3,command=student).place(x=50,y=350)
    b2=Button(f1,text='ISSUE',font='Papyrus 10 bold',fg='black',bg='orange',width=10,bd=3,command=lambda:[issuedbook([e1.get(),e2.get()])])
    b2.place(x=210,y=250)
    b3=Button(f1,text='RETURN',font='Papyrus 10 bold',fg='black',bg='orange',width=10,bd=3,command=lambda:[returnn([e1.get(),e2.get()])])
    b3.place(x=70,y=250)

def issuedbook(l):
    global con
    global cur
    if (l[0]=='' or l[1]==''):
        messagebox.showinfo("Error","Fields cannot be blank.")
    else:
        if not(l[0].isdigit()):
            messagebox.showerror('','invalid bookid')
        elif not(l[1].isdigit()):
            messagebox.showerror('','invalid studentid')
        else:
            m=int(l[0])
            n=int(l[1])
            cur.execute('select bookid from books')
            a=cur.fetchall()
            print(a)
            if a!=[]:
                for i in a:
                    if i[0]==m:
                        p=[m]
                        q=('select cno,copies,token from student,books where books.bookid=%s')
                        cur.execute(q,p)
                        b=cur.fetchall()
                        print(b)
                        if b!=[]:
                            for j in b:
                               if (j[0]==n and j[1]>=1 and j[2]==0):
                                    print('here')
                                    cur.execute('update books set copies=copies-1 where bookid=%s',(l[0],))
                                    
                                    cur.execute('update student set token=1 where cno=%s',(l[1],))
                                 
                                    q=('update STUDENT set BOOKID=%s where CNO=%s')
                                    cur.execute(q,l)
                                    
                                    messagebox.showinfo("Updated","Book Issued sucessfully.")
                                    con.commit()
                                    break 
                            else:
                                messagebox.showinfo("Unavailable","cannot borrow book")
                                break
                            break
                
                        else:
                            messagebox.showinfo("","student id does not exit")
                            break
                    else:
                        messagebox.showinfo("","book id does not exit")
                        break

            else:
                messagebox.showinfo("Unavailable","no such bookid.")
                    

                        

def returnn(l):
    global con
    global cur
    if (l[0]=='' or l[1]==''):
        messagebox.showinfo("Error","Fields cannot be blank.")
    else:
        if not(l[0].isdigit()):
            messagebox.showerror('','invalid bookid')
        elif not(l[1].isdigit()):
            messagebox.showerror('','invalid studentid')
        
        else:
            m=int(l[0])
            n=int(l[1])
            cur.execute('select bookid from books')
            a=cur.fetchall()
            print(a)
            if a!=[]:
                for i in a:
                    if i[0]==m:
                        cur.execute('select cno,copies,token from student,books where books.bookid=student.bookid')
                        b=cur.fetchall()
                        if b!=[]:
                            for j in b:
                               if (j[0]==n and j[1]>=0 and j[2]==1):
                                    print('here')
                                    cur.execute('update books set copies=copies+1 where bookid=%s',(l[0],))
                                    
                                    cur.execute('update student set token=0 where cno=%s',(l[1],))
                                    k=[n]
                                 
                                    q=('update STUDENT set BOOKID = null where CNO=%s')
                                    cur.execute(q,k)
                                    
                                    messagebox.showinfo("Updated","Book returned sucessfully.")
                                    con.commit()
                                    break
                                
                            else:
                                messagebox.showinfo("Unavailable","cannot return book")
                                break
                            break
                        else:
                            messagebox.showinfo('','invalid student id')
                            break
                    else:
                        messagebox.showinfo("","bookid does not exit")
                        break
                                    
            else:
                messagebox.showinfo("Unavailable","no such bookid.")

    
def activity():
    global astudentt
    f1=tk.Frame(height=450,width=500,bg='black')
    f1.place(x=500,y=80)
    

    astudentt=StringVar()
    
    
    #l1=Label(f1,text='Book/Student ID : ',font='Papyrus 15 bold',fg='Orange',bg='black').place(x=50,y=30)
    #e1=Entry(f1,width=20,bd=4,bg='orange',textvariable=aidd).place(x=280,y=35)
    
    l2=Label(f1,text='Student Id : ',font='papyrus 15 bold',fg='orange',bg='black').place(x=50,y=80)
    e2=Entry(f1,width=20,bd=4,bg='orange',textvariable=astudentt).place(x=280,y=80)
    
    b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=student).place(x=40,y=400)
    b1=Button(f1,text='Search',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=searchact).place(x=250,y=400)
    b1=Button(f1,text='All',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=searchall).place(x=350,y=400)#to remove the box after execution
    

    
def searchact():
    global astudentt,k
    global con
    global cur
    
    k=astudentt.get()
    if k!='':
        f1=tk.Frame(height=500,width=650,bg='black')
        f1.place(x=500,y=100)
        b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=lambda:[activity,f1.destroy()]).place(x=40,y=400)
        
        tree=ttk.Treeview(f1,selectmode='browse')
        tree.place(x=15,y=100)
        tree['columns']=("CN0","CNAME","TELE","ADR","BOOKID","TOKEN")
        tree['show']='headings'
        
        tree.column("CN0",width=100,anchor='c')
        tree.column("CNAME",width=100,anchor='c')
        tree.column("TELE",width=100,anchor='c')
        tree.column("ADR",width=100,anchor='c')
        tree.column("BOOKID",width=100,anchor='c')
        tree.column("TOKEN",width=100,anchor='c')
        
        tree.heading("CN0",text='ID N0.')
        tree.heading("CNAME",text='NAME')
        tree.heading("TELE",text='PHONE NO.')
        tree.heading("ADR",text='ADDRESS')
        tree.heading("BOOKID",text='BOOKID')
        tree.heading("TOKEN",text='TOKEN')
        
        cur.execute("select * from STUDENT where CNO=%s",(k,))
        a=cur.fetchall()
        if len(a)!=0:    
            for i in a:
                tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        else:
            messagebox.showinfo('error','no student id present')
    else:
        messagebox.showinfo('Error',"invalid input")


    
def searchall():
    f1=tk.Frame(height=500,width=650,bg='black')
    f1.place(x=500,y=70)
    b1=Button(f1,text='Back',bg='orange',font='Papyrus 10 bold',width=10,bd=3,command=lambda:[activity,f1.destroy()]).place(x=40,y=400)
    
    tree=ttk.Treeview(f1,selectmode='browse')
    tree.place(x=15,y=100)
    tree['columns']=("CN0","CNAME","TELE","ADR","BOOKID","TOKEN")
    tree['show']='headings'
    
    tree.column("CN0",width=100,anchor='c')
    tree.column("CNAME",width=100,anchor='c')
    tree.column("TELE",width=100,anchor='c')
    tree.column("ADR",width=100,anchor='c')
    tree.column("BOOKID",width=100,anchor='c')
    tree.column("TOKEN",width=100,anchor='c')
    
    tree.heading("CN0",text='ID N0.')
    tree.heading("CNAME",text='NAME')
    tree.heading("TELE",text='PHONE NO.')
    tree.heading("ADR",text='ADDRESS')
    tree.heading("BOOKID",text='BOOKID')
    tree.heading("TOKEN",text='TOKEN')
    
    x="select * from STUDENT"
    cur.execute(x)
    a=cur.fetchall()
    if len(a)!=0:    
        for i in a:
            tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5]))

#-------------------------------------------register-----------------------------------       
def register():
    global con
    global cur
    global sno,sname,stele,sadr,stoken

    sno=IntVar()
    sname=StringVar()
    stele=StringVar()
    sadr=StringVar()
    stoken=IntVar()

    f1=tk.Frame(height=500,width=650,bg='grey5')
    f1.place(x=500,y=100)

    l1=Label(f1,text='Student ID :',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=70)
    e1=Entry(f1,width=45,bg='orange',fg='black',textvariable=sno)
    e1.place(x=150,y=70)


    l2=Label(f1,text='Name :',font='Papyrus 12 bold',fg='Orange',bg='Black',pady=1).place(x=50,y=120)
    e2=Entry(f1,width=45,bg='orange',fg='black',textvariable=sname)
    e2.place(x=150,y=120)
    
    l3=Label(f1,text='Telephone : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=170)
    e3=Entry(f1,width=45,bg='orange',fg='black',textvariable=stele)
    e3.place(x=150,y=170)
    
    l4=Label(f1,text='Address : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=230)
    e4=Entry(f1,width=45,bg='orange',fg='black',textvariable=sadr)
    e4.place(x=150,y=230)
    
    #l5=Label(f1,text='BOOKID : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=250)
    #e5=Entry(f1,width=45,bg='orange',fg='black',textvariable=aid)
    #e5.place(x=150,y=250)
    
    l6=Label(f1,text='Token : ',font='Papyrus 12 bold',fg='orange',bg='Black',pady=1).place(x=50,y=300)
    e6=Entry(f1,width=45,bg='orange',fg='black',textvariable=stoken)
    e6.place(x=150,y=300)
    
    b1=Button(f1,text='Add',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[sadddata([e1.get(),e2.get(),e3.get(),e4.get(),e6.get()]),e1.delete(0,END),e2.delete(0,END),e3.delete(0,END),e4.delete(0,END),e6.delete(0,END)])
    b1.place(x=150,y=400)

    b2=Button(f1,text='Back',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=student).place(x=350,y=400)
    '''
    b3=Button(f1,text='MODIFY',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=student).place(x=200,y=370)

    b4=Button(f1,text='DELETE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=student).place(x=390,y=370)
    '''
            
    root1.mainloop()

def sadddata(l):
    global con
    global cur
    global sno,sname,stele,sadr,stoken
    s1=l[1].split()
    

    if ((l[0]=='') or (l[1]=='') or (l[2]=='') or (l[3]=='') or (l[4]=='')):
        messagebox.showinfo("Error","Fields cannot be empty.")
    else:
        if not(l[0].isdigit()):
            messagebox.showerror('','invalid studentid')
            
        elif not(l[1].isalpha()):
            messagebox.showerror('','invalid name')                 #to make space available
            
        elif not(l[2].isdigit()):
            messagebox.showerror('','invalid phone number')                
        elif not(len(l[2])==10):
            messagebox.showerror('','invalid phone number')          
        elif not(l[3].isalpha()):
            messagebox.showerror('','invalid address')
        elif not(l[4].isdigit):
            messagebox.showerror('','invalid token')
        elif not(str(l[4]) in ['0',]):
            messagebox.showerror('','invalid token')
            
        else:
            q='select CNO from STUDENT'
            cur.execute(q)
            a=cur.fetchall()
            print (a)
            m=int(l[0])
            print(m)
            for tuple1 in a: 
                if m in tuple1:
                    messagebox.showinfo("fail","studentid already exsists")
                    break

            else:
                q="insert into STUDENT (cno,cname,tele,adr,token) values (%s,%s,%s,%s,%s)"
                cur.execute(q,l)
                con.commit()
                messagebox.showinfo("Success","student added successfully")
    
    con.commit()

#==================================
def deletestudent():
    global con
    global cur
    global sno,sname,stele,sadr,stoken
    
    sno=StringVar()
    sname=StringVar()
    stele=StringVar()
    sadr=StringVar()
    stoken=IntVar()


    f1=tk.Frame(height=500,width=650,bg='grey5')
    f1.place(x=500,y=100)

    l1=Label(f1,text='STUDENT ID : ',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black').place(x=70,y=40)
    e1=Entry(f1,width=25,bd=5,bg='orange',fg='black',textvariable=sno).place(x=260,y=40)

    b1=Button(f1,text='Back',bg='orange' ,fg='black',width=10,bd=3,command=student).place(x=50,y=400)
    b2=Button(f1,text='modify',bg='orange' ,fg='black',width=10,bd=3,command=moditiy).place(x=500,y=400)
    b3=Button(f1,text='delete',bg='orange' ,fg='black',width=10,bd=3,command=deletestu).place(x=400,y=400)


def moditiy():
    global con
    global cur

    sname=StringVar()
    stele=StringVar()
    sadr=StringVar()
    stoken=IntVar()

    k=sno.get()
    if k!="":
        if k.isdigit():
            l=int(k)
            t=''
            x="select CNO from STUDENT"
            cur.execute(x)
            a=cur.fetchall()
            if len(a)!=0:
                for t in a:
                    if l in t:
                        #messagebox.showinfo("","GIVEN ID EXISTS")
                        f2=tk.Frame(height=270,width=600,bg='black').place(x=520,y=200)
                        
                        l1=Label(f2,text='NEW NAME :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l1.place(x=530,y=210)
                        g1=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=sname)
                        g1.place(x=640,y=210)
                        
                        #b1=Button(f2,text='UPDATE TITLE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e1.get()]),e1.delete(0,END),])
                        #b1.place(x=820,y=210)

                        l2=Label(f2,text='NEW TELE :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l2.place(x=530,y=250)
                        g2=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=stele)
                        g2.place(x=640,y=250)
                        
                        #b2=Button(f2,text='UPDATE AUTHOR',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e2.get()]),e2.delete(0,END),])
                        #b2.place(x=820,y=250)
                        

                        l3=Label(f2,text='NEW ADR :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l3.place(x=530,y=290)
                        g3=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=sadr)
                        g3.place(x=640,y=290)
                        
                        #b3=Button(f2,text='UPDATE GENRE',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e3.get()]),e3.delete(0,END),])
                        #b3.place(x=820,y=290)
                        '''

                        l4=Label(f2,text='NEW COPIES :',font=('Papyrus 10 bold'),bd=2, fg='orange',bg='black')
                        l4.place(x=530,y=330)
                        g4=Entry(f2,width=25,bd=5,bg='orange',fg='black',textvariable=stoken)
                        g4.place(x=640,y=330)
                        '''
                        
                        #b4=Button(f2,text='UPDATE COPIES',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updatedata([e4.get()]),e4.delete(0,END),])
                        #b4.place(x=820,y=330)


                        b6=Button(f2,text='UPDATE ALL',font='Papyrus 10 bold',fg='black',bg='orange',width=15,bd=3,command=lambda:[updates([g1.get(),g2.get(),g3.get()],l),g1.delete(0,END),g2.delete(0,END),g3.delete(0,END)])
                        b6.place(x=640,y=440)

                        #root1.mainloop()
                        break
     
                        
                else:
                    messagebox.showinfo('',"ID  does not exist")
        else:
            messagebox.showinfo('',"ID cannot be a letter")

    else:
        messagebox.showinfo("Error","Search field cannot be empty.")
        
    root1.mainloop()
    

def updates(l,x):
    global con
    global cur
    #global aid,aauthor,aname,acopies,agenre,aloc

    if ((l[0]=='') or (l[1]=='') or (l[2]=='')):
            messagebox.showinfo("Error","Fields cannot be empty.")
    else:
        if not(l[0].isalpha()):
            messagebox.showerror('','invalid name')
        elif not(l[1].isdigit()):
            messagebox.showerror('','invalid phone number')
        elif not(l[2].isalnum()):
            messagebox.showerror('','invalid address')
        else:
            print(x)
            l.append(x)
            q='UPDATE STUDENT SET CNAME=%s,TELE=%s,ADR=%s WHERE CNO=%s;'
            messagebox.showinfo("success","data updated.")
            cur.execute(q,l)
    con.commit()
#=========================================================
def deletestu():
    global con
    global cur
    global sno,k

    k=sno.get()
    if k!="":
        tree=ttk.Treeview(root1,selectmode='browse')
        tree.place(x=527,y=190)
        
        f1=tk.Frame(height=70,width=590,bg='black').place(x=527,y=420)
        
        b1=Button(f1,text='DELETE DATA',bg='orange' ,fg='black',width=10,bd=3,command=lambda:[deletepls([k,]),tree.destroy()])
        b1.place(x=550,y=440)

        tree['columns']=("CNO","CNAME","TELE","ADR","TOKEN")
        tree['show']='headings'
        tree.column("CNO",width=120,anchor='c')
        tree.column("CNAME",width=120,anchor='c')
        tree.column("TELE",width=120,anchor='c')
        tree.column("ADR",width=120,anchor='c')
        tree.column("TOKEN",width=120,anchor='c')

        tree.heading("CNO",text='STUDENT ID')
        tree.heading("CNAME",text='NAME')
        tree.heading("TELE",text='TELEPHONE')
        tree.heading("ADR",text='ADDRESS')
        tree.heading("TOKEN",text='TOKEN')
        
        x="select CNO,CNAME,TELE,ADR,TOKEN from STUDENT where CNO=%s"
        s=(k,)
        cur.execute(x,s)
        a=cur.fetchall()
        if len(a)!=0:    
            for i in a:
                tree.insert('','end',iid=i[0],text=i[0],values=(i[0],i[1],i[2],i[3],i[4]))
    
        else:
            messagebox.showinfo("Error","Data not found")

    else:
        messagebox.showinfo("Error","Search field cannot be empty.")
#==
def deletepls(l):
    global con
    global cur
    q2='select CNO from STUDENT'
    cur.execute(q2)
    a=cur.fetchall()
    print(a)
    k=int(l[0])
    for t in a:
        if k in t:
            q1='select token from student where CNO=%s'
            cur.execute(q1,l)
            b=cur.fetchone()   
            if b!=None and b!=1:
                 messagebox.showinfo("Error","Cannot delete student")
            else:
                q='DELETE FROM STUDENT WHERE CNO=%s;'
                cur.execute(q,l)
                messagebox.showinfo("DELETED","RECORD HAS BEEN DELETED")
                break
        else:
            messagebox.showinfo("error","RECORD DOESNT EXIST")
    con.commit()


    
#-------------------------------------end of backend---------------------------------------
    
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize((w,h),Image.Resampling.LANCZOS)
    photo2=ImageTk.PhotoImage(photo1)
    canvas = Canvas(root1, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas

def Login(event=None):


    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
        lbl_text.config(text="Please complete the required field!", fg="red")
    elif USERNAME.get() =="vishvesh" and PASSWORD.get()=="2410":
        messagebox.showinfo("","login successful")
        
        sub_menu()
        #dest(root1)

        
    else:
        messagebox.showinfo("Error","Invalid username or password.")
        USERNAME.set("")
        PASSWORD.set("")
    
root1 = Tk()
root1.title("PROJECT")

w = root1.winfo_screenwidth()
h = root1.winfo_screenheight()
canvas=canvases(image3,w,h)

USERNAME = StringVar()
PASSWORD = StringVar()

self_label3 = Label(canvas, text="LIBRARY MANAGEMENT SYSTEM", bg='#abc123', fg='black', font=("Papyrus", 28, 'bold'))
self_label3.place(x=325,y=25)
lbl_title = Label(canvas, text = "ADMIN LOGIN ", font=('Papyrus', 30,'bold', ),bg='#abc123', fg='black')
lbl_title.place(x=520,y=100)
lbl_username = Label(canvas, text = "Username:", font=('Papyrus', 15,'bold'),bd=4,bg='orange', fg='black')
lbl_username.place(x=500,y=230)
lbl_password = Label(canvas, text = "Password :", font=('Papyrus', 15,'bold'),bd=3, bg='orange', fg='black')
lbl_password.place(x=500, y=330)
lbl_text = Label(canvas)
lbl_text.place(x=450,y=500)
lbl_text.grid_propagate(0)



username = Entry(canvas, textvariable=USERNAME, font=(14), bg='black', fg='orange',bd=6)
username.place(x=650, y=230,)
password = Entry(canvas, textvariable=PASSWORD, show="*", font=(14),bg='black', fg='orange',bd=6)
password.place(x=650, y=330)


btn_login = Button(canvas, text="LOGIN", font=('Papyrus 15 bold'),width=10,command=Login, bg='#abc123', fg='black')
btn_login.place(x=600,y=420)
btn_login.bind('<Return>', Login)


con=mc.connect(host='localhost',user='root',password='Vishks31$',database='school')
if con.is_connected():
    cur=con.cursor()
    
root1.mainloop()
