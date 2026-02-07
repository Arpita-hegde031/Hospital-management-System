from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class RegisterSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System | Staff Registration")
        
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
        self.var_name = StringVar()
        self.var_type = StringVar()
        self.var_pass = StringVar()
        self.var_conf_pass = StringVar()

        # --- UI DESIGN ---
        header = Label(self.root, text="STAFF REGISTRATION SYSTEM", font=("Helvetica", 35, "bold"), 
                      bg="#27ae60", fg="white", bd=10, relief=RIDGE)
        header.pack(side=TOP, fill=X)

        # Registration Card
        register_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        register_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=620)

        title = Label(register_frame, text="CREATE ACCOUNT", font=("Impact", 30), bg="white", fg="#27ae60")
        title.pack(pady=(20, 10))

        # Helper function for entries to keep code clean
        def create_label_entry(label_text, variable, is_password=False):
            Label(register_frame, text=label_text, font=("Helvetica", 11, "bold"), bg="white", fg="#34495e").pack(anchor=W, padx=50)
            show_char = "*" if is_password else ""
            Entry(register_frame, textvariable=variable, font=("Helvetica", 13), bg="#f8f9fa", bd=1, relief=SOLID, show=show_char).pack(fill=X, padx=50, pady=(2, 12), ipady=5)

        # Fields
        create_label_entry("LOGIN ID", self.var_id)
        create_label_entry("FULL NAME", self.var_name)
        
        Label(register_frame, text="STAFF ROLE", font=("Helvetica", 11, "bold"), bg="white", fg="#34495e").pack(anchor=W, padx=50)
        self.combo_type = ttk.Combobox(register_frame, textvariable=self.var_type, font=("Helvetica", 12), state="readonly")
        self.combo_type["values"] = ("Doctor", "Nurse", "Admin", "Pharmacist")
        self.combo_type.pack(fill=X, padx=50, pady=(2, 12), ipady=3)
        self.combo_type.current(0)

        create_label_entry("PASSWORD", self.var_pass, is_password=True)
        create_label_entry("CONFIRM PASSWORD", self.var_conf_pass, is_password=True)

        # Register Button
        btn_reg = Button(register_frame, text="REGISTER NOW", command=self.register_data, font=("Helvetica", 14, "bold"),
                          bg="#27ae60", fg="white", activebackground="#219150", activeforeground="white", 
                          cursor="hand2", bd=0)
        btn_reg.pack(fill=X, padx=50, pady=(15, 10), ipady=8)

        # Back to Login Link
        btn_back = Button(register_frame, text="Already have an account? Login here", command=self.back_to_login, 
                          font=("Helvetica", 10, "underline"), bg="white", fg="#2980b9", bd=0, cursor="hand2", activebackground="white")
        btn_back.pack()

    def register_data(self):
        """Validates input and inserts data into MySQL"""
        if self.var_id.get()=="" or self.var_pass.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_conf_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password must match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="Arpitahegde0312004", 
                    database="hospital"
                )
                cursor = conn.cursor()
                
                # Check if Login ID is already taken
                cursor.execute("SELECT * FROM users WHERE login_id=%s", (self.var_id.get(),))
                if cursor.fetchone() is not None:
                    messagebox.showerror("Error", "Login ID already exists! Please use a different ID.", parent=self.root)
                else:
                    cursor.execute("INSERT INTO users (login_id, username, password, user_type) VALUES (%s, %s, %s, %s)",
                                  (self.var_id.get(), self.var_name.get(), self.var_pass.get(), self.var_type.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registration Successful! Moving to Login Page.")
                    self.back_to_login() # Automatically transition
                    
            except Exception as e:
                messagebox.showerror("Database Error", f"Error: {str(e)}", parent=self.root)

    def back_to_login(self):
        """Destroys registration window and re-launches login"""
        self.root.destroy()
        import login  # Launches your login.py
        root = Tk()
        login.BeautifulLogin(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = RegisterSystem(root)
    root.mainloop()