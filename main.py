from tkinter import *
from PIL import ImageTk, Image
import mentorlogin,menteelogin,adminlogin

class LoginPage:    
    def __init__(self, window):   
        self.window = window
        self.window.geometry('1366x768')
        self.window.configure(bg = "#f0f0f0")
        self.window.title('Login Page')
        self.window.resizable(False,False)
        self.canvas = Canvas(
            self.window,
            bg = "#f0f0f0",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./images/Login/background.png")
        self.background = self.canvas.create_image(
            593.5, 384.0,
            image=self.background_img)


        # ========================================================================
        # ============================background image============================
        # ========================================================================
        

         # ========================================================================
        # ============================mentor button================================
        # ========================================================================
        def mentorf():
            self.window.destroy()
            mentorlogin.page()
    

        self.img0 = PhotoImage(file = f"./images/Login/img0.png")
        self.b0 = Button(
                    image = self.img0,
                    borderwidth = 0,
                    background='#7e71cb',
                    highlightthickness = 0,
                    command = mentorf,
                    relief = "flat")
        self.b0.place(
                    x = 861, y = 325,
                    width = 296,
                    height = 98)

         # ========================================================================
        # ============================mentee button================================
        # ========================================================================

        def menteef():
            self.window.destroy()
            menteelogin.page()
            
        self.img1 = PhotoImage(file = f"./images/Login/img2.png")
        self.b1 = Button(
                    image = self.img1,
                    borderwidth = 0,
                    background='#7e71cb',
                    highlightthickness = 0,
                    command = menteef,
                    relief = "flat")
        self.b1.place(
                x = 861, y = 427,
                width = 296,
                height = 98)



        def adminf():
            self.window.destroy()
            adminlogin.page()

        self.img2 = PhotoImage(file = f"./images/Login/img1.png")
        self.b2 = Button(
                    image = self.img2,
                    borderwidth = 0,
                    background='#7e71cb',
                    highlightthickness = 0,
                    command = adminf,
                    relief = "flat")
        self.b2.place(
                x = 861, y = 529,
                width = 296,
                height = 98)
        #=========== EXIT ==================================================
        def exitf():
            self.window.destroy()

        self.img3 = PhotoImage(file = f"./images/Login/img3.png")
        self.b3 = Button(
                    image = self.img3,
                    borderwidth = 0,
                    highlightthickness = 0,
                    command = exitf,
                    relief = "flat")

        self.b3.place(
                    x = 919, y = 681,
                    width = 182,
                    height = 71)
   
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
