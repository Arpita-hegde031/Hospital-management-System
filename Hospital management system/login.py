from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import hospital_main  # Links to your main dashboard file
import Register       # Links to your registration file

class BeautifulLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System | Login")
        
        # --- SCREEN DIMENSIONS (80% of Monitor) ---
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = int(screen_width * 0.8)
        height = int(screen_height * 0.8)
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.config(bg="#f0f2f5") 

        # --- VARIABLES ---
        self.var_id = StringVar()
        self.var_pass = StringVar()

        # --- UI DESIGN ---
        # Top Banner
        header = Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", font=("Helvetica", 35, "bold"), 
                      bg="#2c3e50", fg="white", bd=10, relief=RIDGE)
        header.pack(side=TOP, fill=X)

        # Login Center Card
        login_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=450, height=550)

        title = Label(login_frame, text="USER LOGIN", font=("Impact", 35), bg="white", fg="#2c3e50")
        title.pack(pady=(40, 40))

        # Login ID Field
        lbl_user = Label(login_frame, text="LOGIN ID", font=("Helvetica", 11, "bold"), bg="white", fg="#34495e")
        lbl_user.pack(anchor=W, padx=50)
        txt_user = Entry(login_frame, textvariable=self.var_id, font=("Helvetica", 15), bg="#f8f9fa", bd=1, relief=SOLID)
        txt_user.pack(fill=X, padx=50, pady=(5, 20), ipady=7)

        # Password Field
        lbl_pass = Label(login_frame, text="PASSWORD", font=("Helvetica", 11, "bold"), bg="white", fg="#34495e")
        lbl_pass.pack(anchor=W, padx=50)
        txt_pass = Entry(login_frame, textvariable=self.var_pass, show="*", font=("Helvetica", 15), bg="#f8f9fa", bd=1, relief=SOLID)
        txt_pass.pack(fill=X, padx=50, pady=(5, 30), ipady=7)

        # Login Button
        btn_login = Button(login_frame, text="LOGIN", command=self.login_logic, font=("Helvetica", 14, "bold"),
                          bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", 
                          cursor="hand2", bd=0)
        btn_login.pack(fill=X, padx=50, pady=10, ipady=8)

        # Register Link
        btn_reg = Button(login_frame, text="New Staff? Register Here", command=self.open_register, 
                        font=("Helvetica", 11, "underline"), bg="white", fg="#e67e22", bd=0, cursor="hand2", activebackground="white")
        btn_reg.pack(pady=20)

    def login_logic(self):
        """Validates credentials and directs to the main hospital dashboard"""
        if self.var_id.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "Please enter both ID and Password", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="Arpitahegde0312004", 
                    database="hospital"
                )
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE login_id=%s AND password=%s", 
                              (self.var_id.get(), self.var_pass.get()))
                row = cursor.fetchone()
                
                if row == None:
                    messagebox.showerror("Error", "Invalid Login ID or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome {row[1]}!")
                    
                    # --- TRANSITION TO MAIN FILE ---
                    # We call the 'start_hospital' function from hospital_main.py
                    # Passing self.root allows the main file to take over the window
                    hospital_main.start_hospital(self.root)
                
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Could not connect to MySQL: {str(e)}", parent=self.root)

    def open_register(self):
        """Redirects to the registration page"""
        self.root.destroy()
        new_root = Tk()
        Register.RegisterSystem(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = BeautifulLogin(root)
    root.mainloop()