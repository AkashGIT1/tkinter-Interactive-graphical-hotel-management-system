import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
db=mysql.connector.connect(host='localhost',
                           user='root',
                           password='root',
                           database='hotel'
                           )
my_cur=db.cursor()

 


def entry():
    root=Tk()
    root.title('Hotel Management System')
    root.geometry('900x400')
    Label(root,text="Hotel Management System",
          font='bold 18 italic',fg='white',bg='Deepskyblue2',bd=6,relief=RAISED).grid(row=0, column=1)
    Label(root,text='',bg='goldenrod1').grid(row=2,column=0)
    Label(root,text='',bg='goldenrod1').grid(row=3,column=0)
    Label(root,text='',bg='goldenrod1').grid(row=4,column=0)
    Label(root,text="  Click Here To Check Inn            ⟶   ",font='ariel 14 bold',fg='seagreen1',bg='Royalblue1',bd=6).grid(row=8,column=0)
    Label(root,text='',bg='goldenrod1').grid(row=9, column=0)
    Label(root,text="  Click Here To Edit or Check Out ⟶ ",font='ariel 14 bold',fg='seagreen1',bg='Royalblue1',bd=6).grid(row=10,column=0)
    Label(root,text='',bg='goldenrod1').grid(row=11, column=0)
    Label(root,text="  Click Here To Delete Entries  ⟶       ",font='ariel 14 bold',fg='seagreen1',bg='Royalblue1',bd=6).grid(row=14,column=0)
    Label(root,text='',bg='goldenrod1').grid(row=15, column=0)
    Label(root,text='',bg='goldenrod1').grid(row=17, column=0)
    Label(root,text="  Click Here To Search Entries ⟶       ",font='ariel 14 bold',fg='seagreen1',bg='Royalblue1',bd=6).grid(row=16,column=0)
    def insert():
        root.destroy()
        root1=Tk()
        root1.title("Customer's Registeration Details")
        root1.geometry('900x570')
        Label(root1,text="Customer's Registeration Details !",font='bold 18 italic',bg='Deepskyblue',bd=6,relief=RAISED).grid(row=0, column=1)
        Label(root1,text="",bg='darkslategray1').grid(row=1, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=2, column=0)
        Label(root1,text="  Room No.          ⟶                 ",font='bold 15 italic',bg='darkslategray1').grid(row=3, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=4, column=0)
        Label(root1,text="  Name                ⟶                 ",font='bold 15 italic',bg='darkslategray1').grid(row=5, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=6, column=0)
        Label(root1,text="  Check in (date)  ⟶                 ",font='bold 15 italic',bg='darkslategray1').grid(row=7, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=8, column=0)
        Label(root1,text="  Check out (Leave this field)⟶ ",font='bold 15 italic',bg='darkslategray1').grid(row=9, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=10, column=0)
        Label(root1,text="   Mobile no.        ⟶                  ",font='bold 15 italic',bg='darkslategray1').grid(row=11, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=12, column=0)
        Label(root1,text="   Enter your Suite type  ⟶        ",font='bold 15 italic',bg='darkslategray1').grid(row=13, column=0)
        Label(root1,text="   Your Amount (per day)⟶        ",font='bold 15 italic',bg='darkslategray1').grid(row=15, column=0)
        a1=ttk.Combobox(root1,width=17,values=["Classic","Deluxe","Full Deluxe","Executive","Presidential"])
        a1.grid(row=13,column=1)
        a2=ttk.Combobox(root1,width=17,values=["₹ 10999","₹ 18999","₹ 55999","₹ 88999","₹ 99999"])
        a2.grid(row=15,column=1)
        Label(root1,text="",bg='darkslategray1').grid(row=14, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=17, column=0)
        Label(root1,text="",bg='darkslategray1').grid(row=19, column=0)
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        
        e1=Entry(root1,textvariable=v1).grid(row=3, column=1)
        e2=Entry(root1,textvariable=v2).grid(row=5, column=1)
        e3=Entry(root1,textvariable=v3).grid(row=7, column=1)
        e4=Entry(root1,textvariable=v4).grid(row=9, column=1)
        e5=Entry(root1,textvariable=v5).grid(row=11, column=1)
        
        
        def insert1():
            sno=v1.get()
            name=v2.get()
            cin=v3.get()
            cout=v4.get
            mob=v5.get()
            suit=a1.get()
            pay=a2.get()
            my_cur=db.cursor()
            my_cur.execute('insert into hotelki values(%s,%s,%s,%s,%s,%s,%s)',(sno,name,cin,cout,mob,suit,pay))
            db.commit()
            messagebox.showinfo('WOW','Room is Booked')               
            v1.set('')
            v2.set('')
            v3.set('')
            v4.set('')
            v5.set('')
           
            a1.set('')
            a2.set('')
        def clear():
            v1.set('')
            v2.set('')
            v3.set('')
            v4.set('')
            v5.set('')
            a1.set('')
            a2.set('')
        def close():
            root1.destroy()
            
        Button(root1,text=' EXIT',font='ariel 12 bold',width=15,bg='gold',fg='black',bd=6,relief=RAISED,command=close).grid(row=18, column=2)
        
        Button(root1,text='BOOK IT ☺ ',font='ariel 12 bold',width=15,bg='gold',fg='black',bd=6,relief=RAISED,command=insert1).grid(row=18, column=0)
        Button(root1,text='RESET',font='ariel 12 bold',width=15,bg='gold',fg='black',bd=6,relief=RAISED,command=clear).grid(row=18, column=1)
        Button(root1,text='MAIN MENU',font='ariel 12 bold',width=15,bg='gold2',fg='black',bd=6,relief=RAISED,command=entry).grid(row=20, column=1)
        
        root1['bg']='DarkSlateGray1'
        root1.mainloop()
        
    
    def delete():
        root.destroy()
        root1=Tk()
        root1.title("Customer's Registeration Details")
        root1.geometry('800x400')
        Label(root1,text="Delete Customer's details!",font='bold 18 italic',bg='Deepskyblue',bd=6,relief=RAISED).grid(row=0, column=1)
        Label(root1,text="",bg='purple1').grid(row=1, column=0)
        Label(root1,text='Enter The Correct Room         ',font='bold 15 italic',bg='orange',bd=4).grid(row=2, column=0)
        Label(root1,text='Number to Delete Record   ⟶',font='bold 15 italic',bg='orange',bd=3).grid(row=3, column=0)
        Label(root1,text="",bg='purple1').grid(row=4, column=0)
        v1=StringVar()
        e1=Entry(root1,width=29,textvariable=v1).grid(row=3, column=1)
        def delete1():
            sno=v1.get()
            a=(sno,)
            my_cur=db.cursor()
            sql='delete from hotelki where sno=%s'
            my_cur.execute(sql,a)
            db.commit()
            messagebox.showinfo("DONE!","Customer's Record Deleted")
        def close():
            root1.destroy()
        Button(root1,text='Exit  ',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=close).grid(row=14, column=0)

        Button(root1,text='Main Menu',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=entry).grid(row=14, column=2)
        Label(root1,text="",bg='purple1').grid(row=15, column=0)
        Button(root1,text='Delete',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=delete1).grid(row=14, column=1)
        root1['bg']='purple1'
        root1.mainloop()
    def search():
        root.destroy()
        root1=Tk()
        root1.title("Customer's Registeration Details")
        root1.geometry('900x600')
        Label(root1,text="Search Customer's Details !",font='bold 18 italic',bg='Deepskyblue',bd=6,relief=RAISED).grid(row=0, column=2)
        Label(root1,text="",bg='bisque').grid(row=1, column=0)
        Label(root1,text="",bg='bisque').grid(row=2, column=0)
        Label(root1,text="  Room no. ⟶                          ",font='bold 15 italic',bg='tan1').grid(row=3, column=0)
        Label(root1,text="",bg='bisque').grid(row=4, column=0)
        Label(root1,text="  Name        ⟶                          ",font='bold 15 italic',bg='tan1').grid(row=5, column=0)
        Label(root1,text="",bg='bisque').grid(row=6, column=0)
        Label(root1,text="  Check inn (Date)    ⟶            ",font='bold 15 italic',bg='tan1').grid(row=7, column=0)
        Label(root1,text="",bg='bisque').grid(row=8, column=0)
        Label(root1,text="  Check out (Date)    ⟶            ",font='bold 15 italic',bg='tan1').grid(row=9, column=0)
        Label(root1,text="",bg='bisque').grid(row=10, column=0)
        Label(root1,text="   Mobile no.  ⟶                        ",font='bold 15 italic',bg='tan1').grid(row=11, column=0)
        Label(root1,text="",bg='bisque').grid(row=12, column=0)
        Label(root1,text="",bg='bisque').grid(row=14, column=0)
        Label(root1,text="",bg='bisque').grid(row=13,column=0)
        Label(root1,text="   Enter your Suite type ⟶        ",font='bold 15 italic',bg='tan1').grid(row=13, column=0)
        Label(root1,text="",bg='bisque').grid(row=14, column=0)
        a1=ttk.Combobox(root1,width=17,values=["Classic","Deluxe","Full Deluxe","Executive","Presidential"])
        a1.grid(row=13,column=2)
        Label(root1,text=" Your Amount.  ⟶                     ",font='bold 15 italic',bg='tan1').grid(row=15, column=0)
        a2=ttk.Combobox(root1,width=17,values=["₹ 10999","₹ 18999","₹ 55999","₹ 88999","₹ 99999"])
        a2.grid(row=15,column=2)
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        e1=Entry(root1,textvariable=v1).grid(row=3, column=2)
        e2=Entry(root1,textvariable=v2).grid(row=5, column=2)
        e3=Entry(root1,textvariable=v3).grid(row=7, column=2)
        e4=Entry(root1,textvariable=v4).grid(row=9, column=2)
        e5=Entry(root1,textvariable=v5).grid(row=11, column=2)
        def search1():
            my_cur=db.cursor()
            sno=v1.get()
            a=(sno,)
            my_cur=db.cursor()
            sql='select * from hotelki where sno=%s'
            my_cur.execute(sql,a)
            res=my_cur.fetchall()
            for x in res:
                v1.set(x[0])
                v2.set(x[1])
                v3.set(x[2])
                v4.set(x[3])
                v5.set(x[4])
                a1.set(x[5])
                a2.set(x[6])
        def close():
            root1.destroy()
        def clear():
            v1.set('')
            v2.set('')
            v3.set('')
            v4.set('')
            v5.set('')
            a1.set('')
            a2.set('')
        Label(root1,text="",bg='bisque').grid(row=16,column=0)
        Label(root1,text="",bg='bisque').grid(row=18,column=0)
        Label(root1,text="",bg='bisque').grid(row=20,column=0)
        Button(root1,text='MAIN MENU',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=entry).grid(row=19, column=3)
        Button(root1,text='Exit',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=close).grid(row=19, column=2)
        Button(root1,text='RESET',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=clear).grid(row=17, column=3)
        Button(root1,text='Search',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=search1).grid(row=17, column=2)
        root1['bg']='bisque'
        root1.mainloop()
    def update():
        root.destroy()
        root2=Tk()
        root2.title("Customer's Registered Details")
        root2.geometry('930x550')
        Label(root2,text="Customer's Registeration Details !",font='bold 18 italic',bg='Deepskyblue',bd=6,relief=RAISED).grid(row=0, column=1)
        Label(root2,text="",bg='darkslategray1').grid(row=1, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=2, column=0)
        Label(root2,text="  Room No.   ⟶                      ",font='bold 15 italic',bg='darkslategray1').grid(row=3, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=4, column=0)
        Label(root2,text="  Name         ⟶                       ",font='bold 15 italic',bg='darkslategray1').grid(row=5, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=6, column=0)
        Label(root2,text="  Check in    ⟶                        ",font='bold 15 italic',bg='darkslategray1').grid(row=7, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=8, column=0)
        Label(root2,text="  Check out(Enter Date) ☻⟶   ",font='bold 15 italic',bg='darkslategray1').grid(row=9, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=10, column=0)
        Label(root2,text="  Mobile no.  ⟶                        ",font='bold 15 italic',bg='darkslategray1').grid(row=11, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=12, column=0)
        Label(root2,text="  Here is your suite type.  ⟶     ",font='bold 15 italic',bg='darkslategray1').grid(row=13, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=14, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=16, column=0)
        Label(root2,text="",bg='darkslategray1').grid(row=18,column=0)
        Label(root2,text=" Your Amount.  ⟶                     ",font='bold 15 italic',bg='darkslategray1').grid(row=15, column=0)
        a1=ttk.Combobox(root2,width=17,values=["Classic","Deluxe","Full Deluxe","Executive","Presidential"])
        a1.grid(row=13,column=1)
        a2=ttk.Combobox(root2,width=17,values=["₹ 4999","₹ 8999","₹ 15999","₹ 25999","₹ 45999"])
        a2.grid(row=15,column=1)
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        e1=Entry(root2,textvariable=v1).grid(row=3, column=1)
        e2=Entry(root2,textvariable=v2).grid(row=5, column=1)
        e3=Entry(root2,textvariable=v3).grid(row=7, column=1)
        e4=Entry(root2,textvariable=v4).grid(row=9, column=1)
        e5=Entry(root2,textvariable=v5).grid(row=11, column=1)
        def search():
            my_cur=db.cursor()
            sno=v1.get()
            a=(sno,)
            my_cur=db.cursor()
            sql='select * from hotelki where sno=%s'
            my_cur.execute(sql,a)
            res=my_cur.fetchall()
            for x in res:
                v1.set(x[0])
                v2.set(x[1])
                v3.set(x[2])
                v4.set(x[3])
                v5.set(x[4])
                a1.set(x[5])
                a2.set(x[6])
                
        def close():
            root2.destroy()
        def update1():
            sno=v1.get()
            name=v2.get()
            cin=v3.get()
            cout=v4.get()
            mob=v5.get()
            suit=a1.get()
            pay=a2.get()
                
            my_cur=db.cursor()
            my_cur.execute('update hotelki set name=%s,cin=%s,cout=%s,mob=%s,suit=%s,pay=%s where sno=%s',(name,cin,cout,mob,suit,pay,sno))
        
            db.commit()
            messagebox.showinfo('DONE!','DETAILS ARE UPADATED')
            v1.set('')
            v2.set('')
            v3.set('')
            v4.set('')
            v5.set('')
            a1.set('')
            a2.set('')
        Button(root2,text='MAIN MENU',font='ariel 12 bold',width=15,bg='PALE GREEN',fg='black',bd=6,relief=RAISED,command=entry).grid(row=19, column=1)
        Button(root2,text=' EXIT',font='ariel 12 bold',width=19,bg='gold',fg='black',bd=6,relief=RAISED,command=close).grid(row=17, column=2)
        Label(root2,text="",bg='darkslategray1').grid(row=15,column=0)
        Button(root2,text='UPDATE RECORD',font='ariel 12 bold',width=20,bg='gold',fg='black',bd=6,relief=RAISED,command=update1).grid(row=17, column=0)
        Button(root2,text=' SEARCH RECORD',font='ariel 12 bold',width=20,bg='gold',fg='black',bd=6,relief=RAISED,command=search).grid(row=17, column=1)
        root2['bg']='DarkSlateGray1' 
        root2.mainloop()
    def close():
        root.destroy()
    
    Button(root,text=' UPDATE          ☺',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=update).grid(row=10, column=2)
    Button(root,text='DELETE           ☺',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=delete).grid(row=14, column=2)
    Button(root,text='SEARCH          ☺',font='ariel 12 bold',width=15,bg='black',fg='white',bd=6,relief=RAISED,command=search).grid(row=16, column=2)
    Button(root,text='BOOK NOW !   ☺',bg='black',width=15,bd=6,fg='white',font='ariel 12 bold',relief=RAISED,command=insert).grid(row=8,column=2)
    Button(root,text=' EXIT                ☻',font='ariel 12 bold',width=15,bg='gold',fg='black',bd=6,relief=RAISED,command=close).grid(row=18, column=2)
    root['bg']='goldenrod1'
    
    root.mainloop()
entry()

    
    



    
