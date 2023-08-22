from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import main,csv
import adminmain

class LoginPage:
    
    def show(self):
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="#D9D9D9"
                                  , borderwidth=0, background="#D9D9D9", cursor="hand2")
        self.hide_button.place(x = 1200, y = 556)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#D9D9D9"
                                  , borderwidth=0, background="#D9D9D9", cursor="hand2")
        self.show_button.place(x = 1200, y = 556)
        self.password_entry.config(show='*')

        
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.title('Admin Login Page')

        self.canvas = Canvas(
                        self.window,
                        bg = "#f0f0f0",
                        height = 768,
                        width = 1366,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Admin Login/background.png")
        self.background = self.canvas.create_image(
                                        585.0, 384.0,
                                        image=self.background_img)


        self.userid_entry_img = PhotoImage(file = f"./images/Admin Login/img_textBox0.png")
        self.userid_entry_bg = self.canvas.create_image(
                                                1027.0, 420.5,
                                                image = self.userid_entry_img)

        self.userid_entry = Entry(
                                bd = 0,
                                bg = "#d9d9d9",
                                highlightthickness = 0)

        self.userid_entry.place(
                            x = 866.5, y = 379,
                            width = 321.0,
                            height = 81)

        self.password_entry_img = PhotoImage(file = f"./images/Admin Login/img_textBox1.png")
        self.password_entry_bg = self.canvas.create_image(
                                                1027.0, 562.5,
                                                image = self.password_entry_img)

        self.password_entry = Entry(
                                bd = 0,
                                bg = "#d9d9d9",
                                highlightthickness = 0, show="*")

        self.password_entry.place(
                            x = 866.5, y = 521,
                            width = 321.0,
                            height = 81)
        
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        def adminf():
            self.window.destroy()

            adminmain.page()
        
        def signinf():
            flag=0
            adminidcheck=self.userid_entry.get()
            
            parent_dir=f"C:\\Users\\Sachin\\Desktop\\Project"
            pwdcheck=self.password_entry.get()
            with open(f"{parent_dir}\\Admin Login Details.csv",'r') as f :
                data=list(csv.reader(f))
                for i in range(len(data)):
                    if data[i][0]==adminidcheck and data[i][1]==pwdcheck:
                        flag=1
                        messagebox.showinfo('#Success!', 'Login Successful!')
                        adminf()
                        
                    
                if flag==0:
                    messagebox.showwarning('#Error!', 'Account Type/Userid/Password Incorrect')

        self.img1 = PhotoImage(file = f"./images/Admin Login/img1.png")
        self.signinbutton = Button(
                            image = self.img1,
                            borderwidth = 0,
                            highlightthickness = 0,
                            command = signinf,
                            relief = "flat")

        self.signinbutton.place(
                        x = 938, y = 641,
                        width = 178,
                        height = 60)
        
        # ========================================================================
        # ============================password====================================
        # ========================================================================

        

        #=========== BACK ==================================================
        def backf():
            self.window.destroy()
            main.page()

        self.img0 = PhotoImage(file = f"./images/Admin Login/img0.png")
        self.backbutton = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = backf,
            relief = "flat")

        self.backbutton.place(
                        x = 1172, y = 44,
                        width = 171,
                        height = 60)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='./images/show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='./images/hide.png')

        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#D9D9D9"
                                  , borderwidth=0, background="#D9D9D9", cursor="hand2")
        self.show_button.place(x = 1200, y = 556)

        # ===========================================================================================
    
        
        

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
