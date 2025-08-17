import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Database connection - try multiple connection methods
db = None
my_cur = None

# Method 1: Try with auth_plugin
try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='hotel',
        auth_plugin='mysql_native_password'
    )
    my_cur = db.cursor()
    print("Database connected successfully with auth_plugin!")
except mysql.connector.Error as err1:
    print(f"Method 1 failed: {err1}")
    
    # Method 2: Try without auth_plugin
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='hotel'
        )
        my_cur = db.cursor()
        print("Database connected successfully without auth_plugin!")
    except mysql.connector.Error as err2:
        print(f"Method 2 failed: {err2}")
        
        # Method 3: Try with different parameters
        try:
            db = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                database='hotel',
                port=3306
            )
            my_cur = db.cursor()
            print("Database connected successfully with IP address!")
        except mysql.connector.Error as err3:
            print(f"Method 3 failed: {err3}")
            print("\nAll connection methods failed!")
            print("Please try one of these solutions:")
            print("1. Run in MySQL: ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';")
            print("2. Update mysql-connector: pip install --upgrade mysql-connector-python")
            print("3. Check if MySQL service is running")
            db = None
            my_cur = None

# If connection successful, create table
if db is not None:
    try:
        my_cur.execute('''CREATE TABLE IF NOT EXISTS hotelki 
                          (sno VARCHAR(10), name VARCHAR(50), cin VARCHAR(20), 
                           cout VARCHAR(20), mob VARCHAR(15), suit VARCHAR(20), pay VARCHAR(20))''')
        db.commit()
        print("Table 'hotelki' created/verified successfully!")
    except Exception as e:
        print(f"Error creating table: {e}")

def entry():
    root = Tk()
    root.title('Hotel Management System')
    root.geometry('900x400')
    
    Label(root, text="Hotel Management System",
          font='bold 18 italic', fg='white', bg='Deepskyblue2', bd=6, relief=RAISED).grid(row=0, column=1)
    Label(root, text='', bg='goldenrod1').grid(row=2, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=3, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=4, column=0)
    Label(root, text="  Click Here To Check Inn            ⟶   ", font='ariel 14 bold', fg='seagreen1', bg='Royalblue1', bd=6).grid(row=8, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=9, column=0)
    Label(root, text="  Click Here To Edit or Check Out ⟶ ", font='ariel 14 bold', fg='seagreen1', bg='Royalblue1', bd=6).grid(row=10, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=11, column=0)
    Label(root, text="  Click Here To Delete Entries  ⟶       ", font='ariel 14 bold', fg='seagreen1', bg='Royalblue1', bd=6).grid(row=14, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=15, column=0)
    Label(root, text='', bg='goldenrod1').grid(row=17, column=0)
    Label(root, text="  Click Here To Search Entries ⟶       ", font='ariel 14 bold', fg='seagreen1', bg='Royalblue1', bd=6).grid(row=16, column=0)
    
    def insert():
        root.destroy()
        root1 = Tk()
        root1.title("Customer's Registration Details")
        root1.geometry('900x570')
        
        Label(root1, text="Customer's Registration Details !", font='bold 18 italic', bg='Deepskyblue', bd=6, relief=RAISED).grid(row=0, column=1)
        Label(root1, text="", bg='darkslategray1').grid(row=1, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=2, column=0)
        Label(root1, text="  Room No.          ⟶                 ", font='bold 15 italic', bg='darkslategray1').grid(row=3, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=4, column=0)
        Label(root1, text="  Name                ⟶                 ", font='bold 15 italic', bg='darkslategray1').grid(row=5, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=6, column=0)
        Label(root1, text="  Check in (date)  ⟶                 ", font='bold 15 italic', bg='darkslategray1').grid(row=7, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=8, column=0)
        Label(root1, text="  Check out (Leave this field)⟶ ", font='bold 15 italic', bg='darkslategray1').grid(row=9, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=10, column=0)
        Label(root1, text="   Mobile no.        ⟶                  ", font='bold 15 italic', bg='darkslategray1').grid(row=11, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=12, column=0)
        Label(root1, text="   Enter your Suite type  ⟶        ", font='bold 15 italic', bg='darkslategray1').grid(row=13, column=0)
        Label(root1, text="   Your Amount (per day)⟶        ", font='bold 15 italic', bg='darkslategray1').grid(row=15, column=0)
        
        a1 = ttk.Combobox(root1, width=17, values=["Classic", "Deluxe", "Full Deluxe", "Executive", "Presidential"])
        a1.grid(row=13, column=1)
        a2 = ttk.Combobox(root1, width=17, values=["₹ 10999", "₹ 18999", "₹ 55999", "₹ 88999", "₹ 99999"])
        a2.grid(row=15, column=1)
        
        Label(root1, text="", bg='darkslategray1').grid(row=14, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=17, column=0)
        Label(root1, text="", bg='darkslategray1').grid(row=19, column=0)
        
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        
        e1 = Entry(root1, textvariable=v1).grid(row=3, column=1)
        e2 = Entry(root1, textvariable=v2).grid(row=5, column=1)
        e3 = Entry(root1, textvariable=v3).grid(row=7, column=1)
        e4 = Entry(root1, textvariable=v4).grid(row=9, column=1)
        e5 = Entry(root1, textvariable=v5).grid(row=11, column=1)
        
        def insert1():
            if db is None:
                messagebox.showerror('Error', 'Database not connected!')
                return
                
            sno = v1.get()
            name = v2.get()
            cin = v3.get()
            cout = v4.get()
            mob = v5.get()
            suit = a1.get()
            pay = a2.get()
            
            if not all([sno, name, cin, mob, suit, pay]):
                messagebox.showerror('Error', 'Please fill all required fields!')
                return
            
            try:
                my_cur.execute('INSERT INTO hotelki VALUES(%s,%s,%s,%s,%s,%s,%s)', 
                             (sno, name, cin, cout, mob, suit, pay))
                db.commit()
                messagebox.showinfo('WOW', 'Room is Booked')
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')
                v5.set('')
                a1.set('')
                a2.set('')
            except Exception as e:
                messagebox.showerror('Error', f'Database error: {str(e)}')
        
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
        
        Button(root1, text=' EXIT', font='ariel 12 bold', width=15, bg='gold', fg='black', bd=6, relief=RAISED, command=close).grid(row=18, column=2)
        Button(root1, text='BOOK IT ☺ ', font='ariel 12 bold', width=15, bg='gold', fg='black', bd=6, relief=RAISED, command=insert1).grid(row=18, column=0)
        Button(root1, text='RESET', font='ariel 12 bold', width=15, bg='gold', fg='black', bd=6, relief=RAISED, command=clear).grid(row=18, column=1)
        Button(root1, text='MAIN MENU', font='ariel 12 bold', width=15, bg='gold2', fg='black', bd=6, relief=RAISED, command=entry).grid(row=20, column=1)
        
        root1['bg'] = 'DarkSlateGray1'
        root1.mainloop()
    
    def delete():
        root.destroy()
        root1 = Tk()
        root1.title("Customer's Registration Details")
        root1.geometry('800x400')
        
        Label(root1, text="Delete Customer's details!", font='bold 18 italic', bg='Deepskyblue', bd=6, relief=RAISED).grid(row=0, column=1)
        Label(root1, text="", bg='purple1').grid(row=1, column=0)
        Label(root1, text='Enter The Correct Room         ', font='bold 15 italic', bg='orange', bd=4).grid(row=2, column=0)
        Label(root1, text='Number to Delete Record   ⟶', font='bold 15 italic', bg='orange', bd=3).grid(row=3, column=0)
        Label(root1, text="", bg='purple1').grid(row=4, column=0)
        
        v1 = StringVar()
        e1 = Entry(root1, width=29, textvariable=v1).grid(row=3, column=1)
        
        def delete1():
            if db is None:
                messagebox.showerror('Error', 'Database not connected!')
                return
                
            sno = v1.get()
            if not sno:
                messagebox.showerror('Error', 'Please enter room number!')
                return
                
            try:
                a = (sno,)
                sql = 'DELETE FROM hotelki WHERE sno=%s'
                my_cur.execute(sql, a)
                db.commit()
                messagebox.showinfo("DONE!", "Customer's Record Deleted")
                v1.set('')
            except Exception as e:
                messagebox.showerror('Error', f'Database error: {str(e)}')
        
        def close():
            root1.destroy()
        
        Button(root1, text='Exit  ', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=close).grid(row=14, column=0)
        Button(root1, text='Main Menu', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=entry).grid(row=14, column=2)
        Label(root1, text="", bg='purple1').grid(row=15, column=0)
        Button(root1, text='Delete', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=delete1).grid(row=14, column=1)
        
        root1['bg'] = 'purple1'
        root1.mainloop()
    
    def search():
        root.destroy()
        root1 = Tk()
        root1.title("Customer's Registration Details")
        root1.geometry('900x600')
        
        Label(root1, text="Search Customer's Details !", font='bold 18 italic', bg='Deepskyblue', bd=6, relief=RAISED).grid(row=0, column=2)
        Label(root1, text="", bg='bisque').grid(row=1, column=0)
        Label(root1, text="", bg='bisque').grid(row=2, column=0)
        Label(root1, text="  Room no. ⟶                          ", font='bold 15 italic', bg='tan1').grid(row=3, column=0)
        Label(root1, text="", bg='bisque').grid(row=4, column=0)
        Label(root1, text="  Name        ⟶                          ", font='bold 15 italic', bg='tan1').grid(row=5, column=0)
        Label(root1, text="", bg='bisque').grid(row=6, column=0)
        Label(root1, text="  Check inn (Date)    ⟶            ", font='bold 15 italic', bg='tan1').grid(row=7, column=0)
        Label(root1, text="", bg='bisque').grid(row=8, column=0)
        Label(root1, text="  Check out (Date)    ⟶            ", font='bold 15 italic', bg='tan1').grid(row=9, column=0)
        Label(root1, text="", bg='bisque').grid(row=10, column=0)
        Label(root1, text="   Mobile no.  ⟶                        ", font='bold 15 italic', bg='tan1').grid(row=11, column=0)
        Label(root1, text="", bg='bisque').grid(row=12, column=0)
        Label(root1, text="", bg='bisque').grid(row=14, column=0)
        Label(root1, text="", bg='bisque').grid(row=13, column=0)
        Label(root1, text="   Enter your Suite type ⟶        ", font='bold 15 italic', bg='tan1').grid(row=13, column=0)
        Label(root1, text="", bg='bisque').grid(row=14, column=0)
        
        a1 = ttk.Combobox(root1, width=17, values=["Classic", "Deluxe", "Full Deluxe", "Executive", "Presidential"])
        a1.grid(row=13, column=2)
        Label(root1, text=" Your Amount.  ⟶                     ", font='bold 15 italic', bg='tan1').grid(row=15, column=0)
        a2 = ttk.Combobox(root1, width=17, values=["₹ 10999", "₹ 18999", "₹ 55999", "₹ 88999", "₹ 99999"])
        a2.grid(row=15, column=2)
        
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        
        e1 = Entry(root1, textvariable=v1).grid(row=3, column=2)
        e2 = Entry(root1, textvariable=v2).grid(row=5, column=2)
        e3 = Entry(root1, textvariable=v3).grid(row=7, column=2)
        e4 = Entry(root1, textvariable=v4).grid(row=9, column=2)
        e5 = Entry(root1, textvariable=v5).grid(row=11, column=2)
        
        def search1():
            if db is None or my_cur is None:
                messagebox.showerror('Error', 'Database not connected!')
                return
                
            sno = v1.get()
            if not sno:
                messagebox.showerror('Error', 'Please enter room number!')
                return
                
            try:
                # Clear previous values first
                v2.set('')
                v3.set('')
                v4.set('')
                v5.set('')
                a1.set('')
                a2.set('')
                
                a = (sno,)
                sql = 'SELECT * FROM hotelki WHERE sno=%s'
                my_cur.execute(sql, a)
                res = my_cur.fetchall()
                
                if res:
                    for x in res:
                        v1.set(x[0])
                        v2.set(x[1])
                        v3.set(x[2])
                        v4.set(x[3])
                        v5.set(x[4])
                        a1.set(x[5])
                        a2.set(x[6])
                    messagebox.showinfo("Success", "Record found and loaded!")
                else:
                    messagebox.showinfo("Not Found", "No record found for this room number!")
            except Exception as e:
                messagebox.showerror('Error', f'Database error: {str(e)}')
                print(f"Search error details: {e}")
        
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
        
        Label(root1, text="", bg='bisque').grid(row=16, column=0)
        Label(root1, text="", bg='bisque').grid(row=18, column=0)
        Label(root1, text="", bg='bisque').grid(row=20, column=0)
        
        Button(root1, text='MAIN MENU', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=entry).grid(row=19, column=3)
        Button(root1, text='Exit', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=close).grid(row=19, column=2)
        Button(root1, text='RESET', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=clear).grid(row=17, column=3)
        Button(root1, text='Search', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=search1).grid(row=17, column=2)
        
        root1['bg'] = 'bisque'
        root1.mainloop()
    
    def update():
        root.destroy()
        root2 = Tk()
        root2.title("Customer's Registered Details")
        root2.geometry('930x550')
        
        Label(root2, text="Customer's Registration Details !", font='bold 18 italic', bg='Deepskyblue', bd=6, relief=RAISED).grid(row=0, column=1)
        Label(root2, text="", bg='darkslategray1').grid(row=1, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=2, column=0)
        Label(root2, text="  Room No.   ⟶                      ", font='bold 15 italic', bg='darkslategray1').grid(row=3, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=4, column=0)
        Label(root2, text="  Name         ⟶                       ", font='bold 15 italic', bg='darkslategray1').grid(row=5, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=6, column=0)
        Label(root2, text="  Check in    ⟶                        ", font='bold 15 italic', bg='darkslategray1').grid(row=7, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=8, column=0)
        Label(root2, text="  Check out(Enter Date) ☻⟶   ", font='bold 15 italic', bg='darkslategray1').grid(row=9, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=10, column=0)
        Label(root2, text="  Mobile no.  ⟶                        ", font='bold 15 italic', bg='darkslategray1').grid(row=11, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=12, column=0)
        Label(root2, text="  Here is your suite type.  ⟶     ", font='bold 15 italic', bg='darkslategray1').grid(row=13, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=14, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=16, column=0)
        Label(root2, text="", bg='darkslategray1').grid(row=18, column=0)
        Label(root2, text=" Your Amount.  ⟶                     ", font='bold 15 italic', bg='darkslategray1').grid(row=15, column=0)
        
        a1 = ttk.Combobox(root2, width=17, values=["Classic", "Deluxe", "Full Deluxe", "Executive", "Presidential"])
        a1.grid(row=13, column=1)
        a2 = ttk.Combobox(root2, width=17, values=["₹ 4999", "₹ 8999", "₹ 15999", "₹ 25999", "₹ 45999"])
        a2.grid(row=15, column=1)
        
        v1 = StringVar()
        v2 = StringVar()
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        
        e1 = Entry(root2, textvariable=v1).grid(row=3, column=1)
        e2 = Entry(root2, textvariable=v2).grid(row=5, column=1)
        e3 = Entry(root2, textvariable=v3).grid(row=7, column=1)
        e4 = Entry(root2, textvariable=v4).grid(row=9, column=1)
        e5 = Entry(root2, textvariable=v5).grid(row=11, column=1)
        
        def search():
            if db is None or my_cur is None:
                messagebox.showerror('Error', 'Database not connected!')
                return
                
            sno = v1.get()
            if not sno:
                messagebox.showerror('Error', 'Please enter room number!')
                return
                
            try:
                # Clear previous values first
                v2.set('')
                v3.set('')
                v4.set('')
                v5.set('')
                a1.set('')
                a2.set('')
                
                a = (sno,)
                sql = 'SELECT * FROM hotelki WHERE sno=%s'
                my_cur.execute(sql, a)
                res = my_cur.fetchall()
                
                if res:
                    for x in res:
                        v1.set(x[0])
                        v2.set(x[1])
                        v3.set(x[2])
                        v4.set(x[3])
                        v5.set(x[4])
                        a1.set(x[5])
                        a2.set(x[6])
                    messagebox.showinfo("Success", "Record found and loaded!")
                else:
                    messagebox.showinfo("Not Found", "No record found for this room number!")
            except Exception as e:
                messagebox.showerror('Error', f'Database error: {str(e)}')
                print(f"Search error details: {e}")
        
        def close():
            root2.destroy()
        
        def update1():
            if db is None:
                messagebox.showerror('Error', 'Database not connected!')
                return
                
            sno = v1.get()
            name = v2.get()
            cin = v3.get()
            cout = v4.get()
            mob = v5.get()
            suit = a1.get()
            pay = a2.get()
            
            if not all([sno, name, cin, mob, suit, pay]):
                messagebox.showerror('Error', 'Please fill all required fields!')
                return
            
            try:
                my_cur.execute('UPDATE hotelki SET name=%s,cin=%s,cout=%s,mob=%s,suit=%s,pay=%s WHERE sno=%s',
                             (name, cin, cout, mob, suit, pay, sno))
                db.commit()
                messagebox.showinfo('DONE!', 'DETAILS ARE UPDATED')
                v1.set('')
                v2.set('')
                v3.set('')
                v4.set('')
                v5.set('')
                a1.set('')
                a2.set('')
            except Exception as e:
                messagebox.showerror('Error', f'Database error: {str(e)}')
        
        Button(root2, text='MAIN MENU', font='ariel 12 bold', width=15, bg='PALE GREEN', fg='black', bd=6, relief=RAISED, command=entry).grid(row=19, column=1)
        Button(root2, text=' EXIT', font='ariel 12 bold', width=19, bg='gold', fg='black', bd=6, relief=RAISED, command=close).grid(row=17, column=2)
        Label(root2, text="", bg='darkslategray1').grid(row=15, column=0)
        Button(root2, text='UPDATE RECORD', font='ariel 12 bold', width=20, bg='gold', fg='black', bd=6, relief=RAISED, command=update1).grid(row=17, column=0)
        Button(root2, text=' SEARCH RECORD', font='ariel 12 bold', width=20, bg='gold', fg='black', bd=6, relief=RAISED, command=search).grid(row=17, column=1)
        
        root2['bg'] = 'DarkSlateGray1'
        root2.mainloop()
    
    def close():
        root.destroy()
    
    Button(root, text=' UPDATE          ☺', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=update).grid(row=10, column=2)
    Button(root, text='DELETE           ☺', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=delete).grid(row=14, column=2)
    Button(root, text='SEARCH          ☺', font='ariel 12 bold', width=15, bg='black', fg='white', bd=6, relief=RAISED, command=search).grid(row=16, column=2)
    Button(root, text='BOOK NOW !   ☺', bg='black', width=15, bd=6, fg='white', font='ariel 12 bold', relief=RAISED, command=insert).grid(row=8, column=2)
    Button(root, text=' EXIT                ☻', font='ariel 12 bold', width=15, bg='gold', fg='black', bd=6, relief=RAISED, command=close).grid(row=18, column=2)
    
    root['bg'] = 'goldenrod1'
    root.mainloop()

if __name__ == "__main__":
    entry()

    
    



    
