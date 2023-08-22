from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
import csv
import main
import os
import shutil


def valid_phone(phn):
    if phn.isdigit() and len(phn)==10:
        return True
    return False

def valid_pwd(pwd):
    if len(pwd)>=8:
        return True
    return False

class Mentee:
    def __init__(self, mentee,a=1):
        self.a=a
        def logoutf():
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                self.sel.clear()
                self.mentee.destroy()
                main.page()

        def exitf():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=mentee)
            if sure == True:
                self.sel.clear()
                self.mentee.destroy()
                
            
        self.mentee=mentee
        self.mentee.geometry("1366x768")
        self.mentee.resizable(0, 0)
        self.mentee.title("Mentee Management")

        self.canvas = Canvas(
                self.mentee,
                bg = "#f0f0f0",
                height = 768,
                width = 1366,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Mentor Main/background.png")
        self.background = self.canvas.create_image(
                                        669.5, 69.5,
                                        image=self.background_img)

        global parent_dir

        parent_dir = f"C:\\Users\\Sachin\\Desktop\\Project\\Mentor\\Mentor {self.a}"
        

        
        self.entry1_img = PhotoImage(file = f"./images/Mentor Main/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(1175.5, 183.5,image = self.entry1_img)
        self.entry1 = Entry(bd = 0,bg = "#d9d9d9",highlightthickness = 0,font=int(30))
        self.entry1.place(x = 1045.5, y = 154, width=260, height=57)
        
        self.button1_img = PhotoImage(file = f"./images/Mentor Main/img2.png")
        self.button1 = Button(
                image = self.button1_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.search_mentee,
                relief = "flat")

        self.button1.place(
                x = 1268, y = 160,
                width = 47,
                height = 47)
        self.button1.configure(cursor="hand2")
        
        self.button2_img = PhotoImage(file = f"./images/Mentor Main/img3.png")
        self.button2 = Button(
                image = self.button2_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.add_mentee,
                relief = "flat")

        self.button2.place(
                x = 147, y = 154,
                width = 171,
                height = 60)
        self.button2.configure(cursor="hand2")

        self.button3_img = PhotoImage(file = f"./images/Mentor Main/img4.png")
        self.button3 = Button(
                image = self.button3_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.ask_q,
                relief = "flat")

        self.button3.place(
                x = 232, y = 662,
                width = 171,
                height = 60)
        self.button3.configure(cursor="hand2")

        self.button4_img = PhotoImage(file = f"./images/Mentor Main/img5.png")
        self.button4 = Button(
                image = self.button4_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.view_answer,
                relief = "flat")

        self.button4.place(
                x = 584, y = 662,
                width = 171,
                height = 60)
        self.button4.configure(cursor="hand2")
        

        

        self.button5_img = PhotoImage(file = f"./images/Mentor Main/img6.png")
        self.button5 = Button(
                image = self.button5_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.view_meeting,
                relief = "flat")

        self.button5.place(
                x = 930, y = 662,
                width = 171,
                height = 60)
        self.button5.configure(cursor="hand2")

        self.button6_img = PhotoImage(file = f"./images/Mentor Main/img7.png")
        self.button6 = Button(
                image = self.button6_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.update_mentee,
                relief = "flat")

        self.button6.place(
                x = 466, y = 154,
                width = 171,
                height = 60)
        self.button6.configure(cursor="hand2")

        self.button7_img = PhotoImage(file = f"./images/Mentor Main/img8.png")
        self.button7 = Button(
                image = self.button7_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = self.delete_mentee,
                relief = "flat")

        self.button7.place(
                x = 785, y = 154,
                width = 171,
                height = 60)
        self.button7.configure(cursor="hand2")

        self.button8_img = PhotoImage(file = f"./images/Mentor Main/img0.png")
        self.button8 = Button(
                image = self.button8_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = exitf,
                relief = "flat")

        self.button8.place(
                x = 1217, y = 17,
                width = 118,
                height = 64)
        self.button8.configure(cursor="hand2")

        self.button9_img = PhotoImage(file = f"./images/Mentor Main/img1.png")
        self.button9 = Button(
                image = self.button9_img,
                borderwidth = 0,
                highlightthickness = 0,
                command = logoutf,
                relief = "flat")

        self.button9.place(
                x = 2, y = 15,
                width = 171,
                height = 60)
        self.button9.configure(cursor="hand2")

        self.scrollbarx = Scrollbar(mentee, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(mentee, orient=VERTICAL)
        self.tree = ttk.Treeview(mentee)
        self.tree.place(x=147, rely=0.303, width=1050, height=380)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.8752, rely=0.303, width=22, height=380)
        self.scrollbarx.place(x=147, rely=0.799, width=1050, height=22)

        self.tree.configure(
            columns=(
                "Mentee ID",
                "Name",
                "Email",
                "Password",
                "Phone No.",
                "DOB",
                "Gender"
                
                
            )
        )

        self.tree.heading("Mentee ID", text="Mentee ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading('Email', text="Email", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Phone No.", text="Phone No.", anchor=W)
        self.tree.heading("DOB", text="DOB", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)

        self.tree.column("#0", stretch=YES, minwidth=0, width=0)
        self.tree.column("#1", stretch=YES, minwidth=0, width=80)
        self.tree.column("#2", stretch=YES, minwidth=0, width=90)
        self.tree.column("#3", stretch=YES, minwidth=0, width=100)
        self.tree.column("#4", stretch=YES, minwidth=0, width=80)
        self.tree.column("#5", stretch=YES, minwidth=0, width=80)
        self.tree.column("#6", stretch=YES, minwidth=0, width=200)
        self.tree.column("#7", stretch=YES, minwidth=0, width=80)

        self.DisplayData()

    
        
    def DisplayData(self):
        global acc
        f=open(f"{parent_dir}\\Details.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree.insert("", "end", values=(data))
            
    sel=[]
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def search_mentee(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
            
        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-2])
                self.tree.focus(val[val.index(search)-2])
                messagebox.showinfo("Success!!", "Account with Name: {} found.".format(self.entry1.get()), parent=self.mentee)
                break
        else: 
            messagebox.showerror("Oops!!", "Account with Name: {} not found.".format(self.entry1.get()), parent=self.mentee)

    def add_mentee(self):
        self.mentee.destroy()
        global e_add
        e_add = Tk()
        page1 = add_mentee(e_add)
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()

    def update_mentee(self):
        global vall
        vall = []
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        
        if len(self.sel)==1:
            self.mentee.destroy()
            global e_update
            e_update = Tk()
            page2 = update_mentee(e_update)
            
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            
            
            global menteeid
            menteeid=vall[0]


            page2.entry1.insert(0, vall[1])
            page2.entry2.insert(0, vall[5])
            page2.entry3.insert(0, vall[4])
            page2.entry4.insert(0, vall[2])
            page2.entry5.insert(0, vall[3])
            page2.entry6.insert(0, vall[6])
            e_update.mainloop()
            

        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select an Mentee to update.")
        else:
            messagebox.showerror("Error","Can only update one Mentee at a time.")

    def delete_mentee(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected mentee(s)?", parent=self.mentee)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])

                path=os.path.join(parent_dir,str(val[0]))
                shutil.rmtree(path)
                
                f=open(f"{parent_dir}//Details.csv","r")
                a=csv.reader(f)
                acc=[]    
        
                for row in a:
                    acc.append(row)
                
                for r in range(len(to_delete)):
                    for r2 in range(len(acc)):
                        if str(to_delete[r])==str(acc[r2][0]):
                            del acc[r2]
                            break

                f=open(f"{parent_dir}//Details.csv","w",newline="")
                a=csv.writer(f)
                a.writerows(acc)
                f.close()
                
                messagebox.showinfo("Success!!", "Account(s) deleted from database.", parent=self.mentee)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
                                  
        else:
            messagebox.showerror("Error!!","Please select an mentee.", parent=self.mentee)
    
    def ask_q(self):
        global q_ask
        q_ask= Toplevel()
        page3= ask_question(q_ask)
        q_ask.protocol("WM_DELETE_WINDOW", self.ex3)
        q_ask.mainloop()

    def view_answer(self):
        if len(self.sel)==1:
            global v_answer
            v_answer = Toplevel()
            

            v_answer.protocol("WM_DELETE_WINDOW",self.ex4)

            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            
            global menteename
            global menteeid
            menteeid=vall[0]
            menteename=vall[1]
            
            global path
            path=os.path.join(parent_dir, str(menteeid))
            page4 = ViewAnswer(v_answer)

        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select a mentee.")
        else:
            
            messagebox.showerror("Error","Can only choose one Mentee at a time.")

    def view_meeting(self):
            
            global v_meeting
            v_meeting = Toplevel()
            v_meeting.protocol("WM_DELETE_WINDOW",self.ex5)
            page5 = ViewMeeting(v_meeting)
        
    def ex(self):
        e_add.destroy()
        page()

    def ex2(self):
        e_update.destroy() 
        page()

    def ex3(self):
        q_ask.destroy()
        self.DisplayData()
               

    def ex4(self):
        v_answer.destroy()
        self.DisplayData()   

    def ex5(self):
        v_meeting.destroy()

    
    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.mentee.destroy()

class add_mentee:
    
        
    def __init__(self, top=None):

        def backf():
            e_add.destroy()
            page()

        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Mentee")
        self.canvas = Canvas(
                        top,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Add Mentee/background.png")
        self.background = self.canvas.create_image(
                                    423.5, 245.5,
                                    image=self.background_img)
        
        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)
        
        self.entry1_img = PhotoImage(file = f"./images/Add Mentee/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(
                            390.0, 208.0,
                            image = self.entry1_img)

        self.entry1 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry1.place(
                x = 223.0, y = 173,
                width = 334.0,
                height = 68)
        self.entry1.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry2_img = PhotoImage(file = f"./images/Add Mentee/img_textBox6.png")
        self.entry2_bg = self.canvas.create_image(
                            390.0, 314.0,
                            image = self.entry2_img)

        self.entry2 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry2.place(
                x = 223.0, y = 279,
                width = 334.0,
                height = 68)
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3_img = PhotoImage(file = f"./images/Add Mentee/img_textBox1.png")
        self.entry3_bg = self.canvas.create_image(
                            390.0, 420.0,
                            image = self.entry2_img)

        self.entry3 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry3.place(
                x = 223.0, y = 385,
                width = 334.0,
                height = 68)
        

        self.entry4_img = PhotoImage(file = f"./images/Add Mentee/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
                            946.0, 208.0,
                            image = self.entry2_img)

        self.entry4 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry4.place(
                x = 779.0, y = 173,
                width = 334.0,
                height = 68)

        self.entry5_img = PhotoImage(file = f"./images/Add Mentee/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
                            946.0, 314.0,
                            image = self.entry2_img)

        self.entry5 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry5.place(
                x = 779.0, y = 279,
                width = 334.0,
                height = 68)
        

        self.entry6_img = PhotoImage(file = f"./images/Add Mentee/img_textBox3.png")
        self.entry6_bg = self.canvas.create_image(
                            946.0, 419.0,
                            image = self.entry2_img)

        self.entry6 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry6.place(
                x = 779.0, y = 384,
                width = 334.0,
                height = 68)
        self.entry6.configure(show="*")
        
        
        self.entry7_img = PhotoImage(file = f"./images/Add Mentee/img_textBox2.png")
        self.entry7_bg = self.canvas.create_image(
                            390.0, 526.0,
                            image = self.entry2_img)

        self.entry7 = Entry(e_add,
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry7.place(
                x = 223.0, y = 491,
                width = 334.0,
                height = 68)

        self.img0 = PhotoImage(file = f"./images/Add Mentee/img0.png")
        self.button1 = Button(e_add,
                        image = self.img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = self.add,
                        relief = "flat")

        self.button1.place(
                    x = 421, y = 654,
                    width = 171,
                    height = 60)
        self.button1.configure(cursor="hand2")
        

        self.img1 = PhotoImage(file = f"./images/Add Mentee/img1.png")
        self.button2 = Button(e_add,
                        image = self.img1,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = self.clearr,
                        relief = "flat")

        self.button2.place(
                    x = 719, y = 654,
                    width = 171,
                    height = 60)
        self.button2.configure(cursor="hand2")

        self.img2 = PhotoImage(file = f"./images/Add Mentee/img2.png")
        self.button3 = Button(e_add,
                        image = self.img2,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = backf,
                        relief = "flat")

        self.button3.place(
                    x = 1208, y = 21,
                    width = 118,
                    height = 64)
        self.button3.configure(cursor="hand2")



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
    
    def add(self):
        menteeid = self.entry1.get()
        menteenum = self.entry2.get()
        menteemail = self.entry3.get()
        menteename = self.entry4.get()      
        menteedob = self.entry5.get()
        menteepass = self.entry6.get()
        menteegender = self.entry7.get()


        if menteename.strip():
            if valid_phone(menteenum):
                if menteeid:
                    if menteedob:
                        if "@" in menteemail:
                            if valid_pwd(menteepass):
                                if menteegender in 'mfMFothers':
                                    path = os.path.join(parent_dir, menteeid)
                                    os.mkdir(path)
                                    data=[menteeid,menteename.title(),menteemail,menteepass,menteenum,menteedob,menteegender]
                                    print()
                                    f=open(f"{parent_dir}\\Details.csv",'a',newline='')
                                    cw=csv.writer(f)
                                    cw.writerow(data)
                                    f.close()
                                    f=open(f"{path}\\Details.csv",'a',newline='')
                                    cw=csv.writer(f)
                                    cw.writerow(data)
                                    f.close()
                                    messagebox.showinfo("Success!!", "Account successfully added in database.", parent=e_add)
                                    self.clearr()
                                    e_add.destroy()
                                    page()
                                else:
                                    messagebox.showerror("Oops!", "Please enter m/f/others in gender.", parent=e_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter a proper password more than 8 characters.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter a proper email address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter DOB.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Please enter Mentee ID.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter the name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0,END)

class update_mentee:
    def __init__(self, top=None):
        def backf():
            e_update.destroy()
            page()
        
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Mentee")

        self.canvas = Canvas(
                        e_update,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Update Mentee/background.png")
        self.background = self.canvas.create_image(
                                    474.5, 192.0,
                                    image=self.background_img)
        
        
        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)
        
        self.entry1_img = PhotoImage(file = f"./images/Update Mentee/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(
                            390.0, 208.0,
                            image = self.entry1_img)

        self.entry1 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry1.place(
                x = 223.0, y = 173,
                width = 334.0,
                height = 68)
        

        self.entry2_img = PhotoImage(file = f"./images/Update Mentee/img_textBox5.png")
        self.entry2_bg = self.canvas.create_image(
                            390.0, 314.0,
                            image = self.entry2_img)

        self.entry2 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry2.place(
                x = 223.0, y = 279,
                width = 334.0,
                height = 68)
        

        self.entry3_img = PhotoImage(file = f"./images/Update Mentee/img_textBox1.png")
        self.entry3_bg = self.canvas.create_image(
                            390.0, 420.0,
                            image = self.entry2_img)

        self.entry3 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry3.place(
                x = 223.0, y = 385,
                width = 334.0,
                height = 68)
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4_img = PhotoImage(file = f"./images/Update Mentee/img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(
                            946.0, 208.0,
                            image = self.entry2_img)

        self.entry4 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry4.place(
                x = 779.0, y = 173,
                width = 334.0,
                height = 68)

        self.entry5_img = PhotoImage(file = f"./images/Update Mentee/img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(
                            946.0, 314.0,
                            image = self.entry2_img)

        self.entry5 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry5.place(
                x = 779.0, y = 279,
                width = 334.0,
                height = 68)
        self.entry5.configure(show="*")

        self.entry6_img = PhotoImage(file = f"./images/Update Mentee/img_textBox3.png")
        self.entry6_bg = self.canvas.create_image(
                            946.0, 419.0,
                            image = self.entry2_img)

        self.entry6 = Entry(
                    bd = 0,
                    bg = "#d9d9d9",
                    highlightthickness = 0,font=int(30))

        self.entry6.place(
                x = 779.0, y = 384,
                width = 334.0,
                height = 68)
        
        

        self.img0 = PhotoImage(file = f"./images/Update Mentee/img0.png")
        self.button1 = Button(
                        image = self.img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = self.update,
                        relief = "flat")

        self.button1.place(
                    x = 417, y = 536,
                    width = 171,
                    height = 60)
        self.button1.configure(cursor="hand2")
        

        self.img1 = PhotoImage(file = f"./images/Update Mentee/img1.png")
        self.button2 = Button(
                        image = self.img1,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = self.clearr,
                        relief = "flat")

        self.button2.place(
                    x = 710, y = 536,
                    width = 171,
                    height = 60)
        self.button2.configure(cursor="hand2")

        self.img2 = PhotoImage(file = f"./images/Update Mentee/img2.png")
        self.button3 = Button(
                        image = self.img2,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = backf,
                        relief = "flat")

        self.button3.place(
                    x = 1208, y = 21,
                    width = 118,
                    height = 64)
        self.button2.configure(cursor="hand2")


        


    def update(self):
        menteename = self.entry1.get()
        menteedob = self.entry2.get()
        menteenum = self.entry3.get()
        menteemail = self.entry4.get()
        menteepass = self.entry5.get()
        menteegender = self.entry6.get()
        

        if menteename.strip():
            if valid_phone(menteenum):
                if menteedob:
                    if "@" in menteemail:
                        if valid_pwd(menteepass):
                            if menteegender in 'mfMFothers':
                                f=open(f"{parent_dir}\\Details.csv","r")
                                a=csv.reader(f)
                                acc=[]    
        
                                for row in a:
                                    acc.append(row)
                                
                                for r in range(len(acc)):
                                    if str(menteeid)==str(acc[r][0]) :
                                        print(menteeid)
                                        data=[menteeid,menteename.title(),menteemail,menteepass,menteenum,menteedob,menteegender]
                                        acc[r]=data
                                        break
                                    
                            
                                f=open(f"{parent_dir}\\Details.csv","w",newline="")
                                a=csv.writer(f)
                                a.writerows(acc)
                                f.close()

                                messagebox.showinfo("Success!!", "Account successfully updated in database.", parent=e_update)
                                self.clearr()
                                e_update.destroy()
                                self.tree.delete(*self.tree.get_children())
                                self.DisplayData()
                                

                            else:
                                messagebox.showerror("Oops!", "Please enter m/f/others.", parent=e_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter valid password.", parent=e_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter vaild email id.", parent=e_update)
                else:
                    messagebox.showerror("Oops!", "Please enter DOB.", parent=e_update)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_update)
        else:
            messagebox.showerror("Oops!", "Please enter mentee name.", parent=e_update)


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
        
class ask_question:
    def __init__(self, top=None):
        def backf():
            q_ask.destroy()
        

        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Ask Question")
        self.canvas = Canvas(
                        q_ask,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Post Question/background.png")
        self.background = self.canvas.create_image(
                                    383.5, 181.5,
                                    image=self.background_img)

        self.entry1_img = PhotoImage(file = f"./images/Post Question/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(
                                        390.0, 268.0,
                                        image = self.entry1_img)

        self.entry1 = Entry(q_ask,
                        bd = 0,
                        bg = "#d9d9d9",
                        highlightthickness=0,font=int(30) )

        self.entry1.place(
                    x = 223.0, y = 233,
                    width = 334.0,
                    height = 68)

        self.entry2_img = PhotoImage(file = f"./images/Post Question/img_textBox1.png")
        self.entry2_bg = self.canvas.create_image(
                        694.5, 398.0,
                        image = self.entry2_img)

        self.entry2 = Entry(q_ask,
                        bd = 0,
                        bg = "#d9d9d9",
                        highlightthickness=0,font=int(30) )

        self.entry2.place(
                    x = 223.0, y = 363,
                    width = 943.0,
                    height = 68)


        self.img0 = PhotoImage(file = f"./images/Post Question/img0.png")
        self.b0 = Button(q_ask,
                    image = self.img0,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = self.addq,
                    relief = "flat")

        self.b0.place(
            x = 482, y = 591,
            width = 392,
            height = 60)

        self.img1 = PhotoImage(file = f"./images/Post Question/img1.png")
        self.b1 = Button(q_ask,
                image = self.img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = backf,
                relief = "flat")

        self.b1.place(
                x = 1208, y = 21,
                width = 118,
                height = 64)

    def addq(self):
            menteeid=self.entry1.get()
            question=self.entry2.get()

            flag=0
            
            with open(f"{parent_dir}\\Details.csv",'r') as f :
                data=list(csv.reader(f))
                for i in range(len(data)):
                    if data[i][0]==menteeid:
                        flag=1
            if flag==0:
                    messagebox.showwarning('#Error', 'Mentee Id Doesnt Exist')
            else:
                path = os.path.join(parent_dir, menteeid)
                data=[question]
                f=open(f"{path}\\QnA.csv",'a',newline='')
                cw=csv.writer(f)
                cw.writerow(data)
                f.close()
                messagebox.showinfo("Success!!", "Question posted.", parent=q_ask)
            q_ask.destroy()
            page()

class ViewAnswer:
    def __init__(self,top=None):
        def backf():
            v_answer.destroy()
        self.window=top
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.title(f"{str(menteeid)}:{menteename} Answers")
        self.canvas = Canvas(
                        self.window,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/View Answers/background.png")
        self.background = self.canvas.create_image(
                                    383.5, 60.5,
                                    image=self.background_img)


        self.scrollbarx = Scrollbar(self.window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.window, orient=VERTICAL)
        self.tree = ttk.Treeview(self.window)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=878, height=22)

        self.tree.configure(
            columns=(
                'Question',
                'Answer'     
            )
        )

        self.tree.heading("Question", text="Question", anchor=W)
        self.tree.heading ('Answer',text="Answer",anchor=W)
        

        self.tree.column("#0", stretch=YES, minwidth=0, width=0)
        self.tree.column("#1", stretch=YES, minwidth=0, width=300)
        self.tree.column("#2", stretch=YES, minwidth=0, width=500)
    

        self.DisplayData()


        self.img1 = PhotoImage(file = f"./images/View Answers/img0.png")
        self.b1 = Button(self.window,
                image = self.img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = backf,
                relief = "flat")

        self.b1.place(
                x = 1208, y = 21,
                width = 118,
                height = 64)
    
        
    def DisplayData(self):
        global acc
        if os.path.exists(f"{path}\\QnA.csv"):
            f=open(f"{path}\\QnA.csv","r")
            a=csv.reader(f)
            acc=[]    
        
            for row in a:
                acc.append(row)

            for data in acc:
                self.tree.insert("", "end", values=(data))
        else:
            messagebox.showerror('Error!',f'No questions asked to Mentee {menteeid} yet!')
            self.window.destroy()
            

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
    
class ViewMeeting:
    def __init__(self,top):
        def backf():
            self.window.destroy()
        self.window=top
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.title('Scheduled Meetings')
        self.canvas = Canvas(
                        self.window,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/View Meetings/background.png")
        self.background = self.canvas.create_image(
                                    383.5, 60.5,
                                    image=self.background_img)

        self.scrollbarx = Scrollbar(self.window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.window, orient=VERTICAL)
        self.tree = ttk.Treeview(self.window)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=878, height=22)

        self.tree.configure(
            columns=(
                'Mentee ID',
                'Date',
                'Time Slot'
                
                
            )
        )

        self.tree.heading("Mentee ID", text="Mentee ID", anchor=W)
        self.tree.heading ('Date',text="Date",anchor=W)
        self.tree.heading ('Time Slot',text="Time Slot",anchor=W)
        

        self.tree.column("#0", stretch=YES, minwidth=0, width=0)
        self.tree.column("#1", stretch=YES, minwidth=0, width=300)
        self.tree.column("#2", stretch=YES, minwidth=0, width=500)
        self.tree.column("#3", stretch=YES, minwidth=0, width=500)
    

        self.DisplayData()

        self.img1 = PhotoImage(file = f"./images/View Meetings/img0.png")
        self.b1 = Button(self.window,
                image = self.img1,
                borderwidth = 0,
                highlightthickness = 0,
                command = backf,
                relief = "flat")

        self.b1.place(
                x = 1208, y = 21,
                width = 118,
                height = 64)
        
    def DisplayData(self):
        global acc
        f=open(f"{parent_dir}\\Meetings.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree.insert("", "end", values=(data))

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
  
def page(a=1):
    mentee = Tk()
    Mentee(mentee,a)
    mentee.mainloop()

if __name__ == '__main__':
    page()
