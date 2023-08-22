from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
from PIL import ImageTk, Image
import csv
import main
import os
from datetime import date




class Mentee:
    def __init__(self, mentee,a=101,b=1):
        self.a=a
        global menteeid
        menteeid=a
        
        self.b=b
        
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

        self.background_img = PhotoImage(file = f"./images/Mentee Main/background.png")
        self.background = self.canvas.create_image(
                                682.5, 68.5,
                                image=self.background_img)
        
        self.img2 = PhotoImage(file = f"./images/Mentee Main/img2.png")
        self.button1 = Button(
                    image = self.img2,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = self.view_question,
                    relief = "flat")
        self.button1.configure(cursor="hand2")
        self.button1.place(
                    x = 97, y = 324,
                    width = 171,
                    height = 60)

        self.img3 = PhotoImage(file = f"./images/Mentee Main/img3.png")
        self.button2 = Button(
                    image = self.img3,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = self.set_meeting,
                    relief = "flat")
        self.button2.configure(cursor="hand2")
        self.button2.place(
                    x = 97, y = 493,
                    width = 171,
                    height = 60)

        self.img0 = PhotoImage(file = f"./images/Mentee Main/img0.png")
        self.button0 = Button(
                    image = self.img0,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = exitf,
                    relief = "flat")
        self.button0.configure(cursor="hand2")
        self.button0.place(
                    x = 1230, y = 16,
                    width = 118,
                    height = 64)
                    
        self.img1 = PhotoImage(file = f"./images/Mentee Main/img1.png")
        self.button3 = Button(
                    image = self.img1,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = logoutf,
                    relief = "flat")
        self.button3.configure(cursor="hand2")
        self.button3.place(
                    x = 12, y = 20,
                    width = 171,
                    height = 60)
        
        global parent_dir
        global mentor_dir
        mentor_dir=f"C:\\Users\\Sachin\\Desktop\\Project\\Mentor\\Mentor {self.b}"
        parent_dir = f"C:\\Users\\Sachin\\Desktop\\Project\\Mentor\\Mentor {self.b}\\{self.a}"
        print(parent_dir)
        
        self.scrollbarx = Scrollbar(self.mentee, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.mentee, orient=VERTICAL)
        self.tree = ttk.Treeview(self.mentee)
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

        child_id = self.tree.get_children()[-1]
        print(child_id)
        self.tree.focus(child_id)
        self.tree.selection_set(child_id)
    
        
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
                
    def view_question(self):
        if len(self.sel)==1:
            
            global v_ques
            v_ques = Toplevel()
            

            v_ques.protocol("WM_DELETE_WINDOW",self.ex1)

            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            
            global menteename
            
            menteeid=vall[0]
            menteename=vall[1]
            print(menteeid,menteename)
            global path
            path=os.path.join(parent_dir, str(menteeid))
            page1 = ViewQuestion(v_ques)
        
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select the mentee.")
        else:
            messagebox.showerror("Error","Please select the mentee")
            
    def set_meeting(self):
        flag=0
        with open(f"{mentor_dir}\\Meetings.csv",'r') as f :
            data=list(csv.reader(f))
            
            for i in range(len(data)):
                if data[i][0]==str(menteeid):
                    
                    messagebox.showwarning('Failed!',f'A meeting is already scheduled on {data[i][1]}')
                    flag=1
                    break
        if flag==0:        
            global set_m
            set_m= Toplevel()
            page3= SetMeeting(set_m)
            set_m.protocol("WM_DELETE_WINDOW", self.ex2)
            set_m.mainloop()
        

    def ex1(self):
        v_ques.destroy()
        
    def ex2(self):
        set_m.destroy()
           

class ViewQuestion:
    def __init__(self,v_ques):
        def backf():
            v_ques.destroy()
        v_ques.geometry("1366x768")
        v_ques.resizable(0, 0)
        v_ques.title(f"{str(menteeid)}:{menteename} Answers")
        self.canvas = Canvas(
                    v_ques,
                    bg = "#f0f0f0",
                    height = 768,
                    width = 1366,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/View Question/background.png")
        self.background = self.canvas.create_image(
                                682.5, 68.5,
                                image=self.background_img)

        self.img0 = PhotoImage(file = f"./images/View Question/img0.png")
        self.b0 = Button(v_ques,
                    image = self.img0,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = backf,
                    relief = "flat")

        self.b0.place(
                    x = 1230, y = 16,
                    width = 118,
                    height = 64)
        self.b0.configure(cursor="hand2")

        self.img1 = PhotoImage(file = f"./images/View Question/img1.png")
        self.b1 = Button(v_ques,
                    image = self.img1,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = self.answer,
                    relief = "flat")

        self.b1.place(
                x = 117, y = 384,
                width = 171,
                height = 60)
        self.b1.configure(cursor="hand2")
        self.canvas.create_text(
                    114.0, 25.5,
                    text = "Post Answer",
                    fill = "#000000",
                    font = ("PatuaOne-Regular", int(32.0)))
        

        self.scrollbarx = Scrollbar(v_ques, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(v_ques, orient=VERTICAL)
        self.tree = ttk.Treeview(v_ques)
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

        
  
        
    sel=[]
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
    
        
    def answer(self):
        global p_answer
        global vall
        vall = []
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        
        
        p_answer= Toplevel()
        page7= answer_class(p_answer)
        page7.entry2.insert(0,vall[0])
        page7.entry2.config(state='disabled')
        p_answer.protocol("WM_DELETE_WINDOW", self.ex3)
        p_answer.mainloop()  
   
            
    def ex3(self):
        p_answer.destroy()
           
           
    def DisplayData(self):
        global acc
        f=open(f"{parent_dir}\\QnA.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree.insert("", "end", values=(data))
            
class answer_class:
    def __init__(self, p_answer):
        def backf():
            p_answer.destroy()
        p_answer.geometry("1366x768")
        p_answer.resizable(0, 0)
        p_answer.title("Ask Question")
        self.canvas = Canvas(
                        p_answer,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Post Answer/background.png")
        self.background = self.canvas.create_image(
    597.5, 206.0,
    image=self.background_img)

        self.img0 = PhotoImage(file = f"./images/Post Answer/img0.png")
        self.b0 = Button(p_answer,
                    image = self.img0,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = self.addq,
                    relief = "flat")

        self.b0.place(
                x = 482, y = 591,
                width = 392,
                height = 60)

        self.img1 = PhotoImage(file = f"./images/Post Answer/img1.png")
        self.b1 = Button(p_answer,
                    image = self.img1,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = backf,
                    relief = "flat")

        self.b1.place(
                x = 1208, y = 21,
                width = 118,
                height = 64)

        self.entry1_img = PhotoImage(file = f"./images/Post Answer/img_textBox0.png")
        self.entry1_bg = self.canvas.create_image(
                                688.5, 447.0,
                                image = self.entry1_img)

        self.entry1 = Entry(p_answer,
                        bd = 0,
                        bg = "#d9d9d9",
                        highlightthickness = 0,font=int(30))

        self.entry1.place(
                    x = 217.0, y = 412,
                    width = 943.0,
                    height = 68)

        self.entry2_img = PhotoImage(file = f"./images/Post Answer/img_textBox0.png")
        self.entry2_bg = self.canvas.create_image(
                                688.5, 320.0,
                                image = self.entry2_img)

        self.entry2 = Entry(p_answer,
                        bd = 0,
                        bg = "black",
                        fg='black',
                        highlightthickness = 0,font=int(30))
                        
        
        self.entry2.place(
                    x = 217.0, y = 288,
                    width = 943.0,
                    height = 68)
        
        

    def addq(self):
        f=open(f"{parent_dir}\\QnA.csv","r")
        a=csv.reader(f)
        acc=[]    
        ans=self.entry1.get()
        for row in a:
            acc.append(row)
            for r in range(len(acc)):
                                    
                if acc[r][0]==vall[0]:                      
                    data=[vall[0],ans]
                    acc[r]=data
                    break
                                    
                            
            f=open(f"{parent_dir}\\QnA.csv","w",newline="")
            a=csv.writer(f)
            a.writerows(acc)
            f.close()

            messagebox.showinfo(title="Success!!",message= "Account successfully updated in database.",parent=p_answer)

            p_answer.destroy()
            v_ques.destroy()

class SetMeeting:
    def __init__(self,set_m):
        def backf():
            set_m.destroy()
        set_m.geometry("1366x768")
        set_m.resizable(0, 0)
        set_m.title("Set Meeting")
        self.canvas = Canvas(
                        set_m,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Set Meeting/background.png")
        self.background = self.canvas.create_image(
                                383.5, 255.0,
                                image=self.background_img)
        
        self.img0 = PhotoImage(file = f"./images/Set Meeting/img0.png")
        self.b0 = Button(set_m,
                        image = self.img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = self.set_meet,
                        relief = "flat")

        self.b0.place(
                    x = 482, y = 591,
                    width = 392,
                    height = 60)

        self.img1 = PhotoImage(file = f"./images/Set Meeting/img1.png")
        self.b1 = Button(set_m,
                        image = self.img1,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = backf,
                        relief = "flat")

        self.b1.place(
                    x = 1208, y = 21,
                    width = 118,
                    height = 64)


        today = date.today()

        d1 = today.strftime("%d/%m/%Y")
        self.dd=int(d1[0:2])
        self.mm=int(d1[3:5])
        self.yy=int(d1[6:])
        self.menu1= StringVar(set_m)
        self.menu1.set(str(self.dd))

        dates=[ str(i) for i in range(1,31)]
        self.drop1= OptionMenu(set_m, self.menu1,*dates)
        self.drop1.place(relx=0.148,rely=0.346)
        


        
        self.menu2= StringVar(set_m)
        self.menu2.set(str(self.mm))

        months=[str(i) for i in range(1,13)]
        self.drop2= OptionMenu(set_m, self.menu2,*months)
        self.drop2.place(relx=0.270,rely=0.346)
        

        
        self.menu3= StringVar(set_m)
        self.menu3.set(str(self.yy))        

        years=[ str(i) for i in range(2022,2030)]
        self.drop3= OptionMenu(set_m, self.menu3,*years)
        self.drop3.place(relx=0.388,rely=0.346)
        
        

        
        
        
        
        
        self.menu4= StringVar(set_m)
        self.menu4.set("Select Time Slots")
        

        time_slots=['15:30-16:00','16:00-16:30','16:30-17:00','17:00-17:30','17:30-18:00']
        drop4= OptionMenu(set_m, self.menu4,*time_slots)
        drop4.place(relx=0.132,rely=0.600)
        
        
    def set_meet(self):
        
        self.date,self.month,self.year=((self.menu1.get()),(self.menu2.get()),(self.menu3.get()))
        if len(self.menu2.get())==1:
            self.month='0'+str(self.menu2.get())
        if len(self.menu1.get())==1:
            self.date='0'+str(self.menu1.get())
        self.meetdate=date(int(self.year),int(self.month),int(self.date))
        self.todate=date.today()
        self.meetdatestr=self.menu1.get()+'/'+self.menu2.get()+'/'+self.menu3.get()
        self.timeslot=self.menu4.get()
        days=self.number_of_days(self.todate,self.meetdate)
        print(days)
        flag=0
        with open(f"{mentor_dir}\\Meetings.csv",'r') as f :
            data=list(csv.reader(f))
            for i in range(len(data)):
                if data[i][1]==self.meetdatestr:
                    if data[i][2]==self.timeslot:
                        flag=1
                        break 
        if self.meetdate <= self.todate:
                flag=2

        if flag == 1 :
            messagebox.showwarning('Error', 'Timeslot not available')
        elif flag == 2 :
            messagebox.showwarning('Error', 'Meeting has to be set in future')
        elif days>90:
            messagebox.showwarning('Error', 'Meeting should be set within 90 days from today')
        else:
            msg='Meeting has been scheduled on'+self.menu1.get()+'/'+self.menu2.get()+'/'+self.menu3.get()
            data=[menteeid,self.meetdatestr,self.timeslot]
            f=open(f"{mentor_dir}\\Meetings.csv",'a',newline='')
            cw=csv.writer(f)
            cw.writerow(data)
            f.close()
            messagebox.showinfo('Success!',msg)
    
    def number_of_days(self,date_1, date_2):  
        return (date_2 - date_1).days  


            
            
def page(a=101,b=1):
    mentee = Tk()
    Mentee(mentee,a,b)
    mentee.mainloop()

if __name__ == '__main__':
    page()