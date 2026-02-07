from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1544x800+0+0")

        # ================== TEXTVARIABLES ==================
        self.name_of_tablet = StringVar()
        self.ref_no = StringVar()
        self.dose = StringVar()
        self.no_tablets = StringVar()
        self.lot_no = StringVar()
        self.issue_date = StringVar()
        self.exp_date = StringVar()
        self.daily_dose = StringVar()
        self.side_effect = StringVar()

        self.further_info = StringVar()
        self.blood_pressure = StringVar()
        self.storage = StringVar()
        self.medicine = StringVar()
        self.patient_id = StringVar()
        self.nhs_number = StringVar()
        self.patient_name = StringVar()
        self.dob = StringVar()
        self.patient_address = StringVar()

        # ================== UI LAYOUT ==================
        lbltitle=Label(self.root,text="Hospital management system",bd=20,relief=RIDGE,font=("times new roman",40,"bold"),bg="white",fg="red")
        lbltitle.pack(side=TOP,fill=X)

        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)
        
        DataFrameLeft.columnconfigure(1, weight=1)
        DataFrameLeft.columnconfigure(3, weight=1)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="Prescription") 
        DataFrameRight.place(x=990,y=5,width=480,height=350) 

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)
        
        for i in range(7):
            ButtonFrame.columnconfigure(i, weight=1)

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)    
        DetailsFrame.place(x=0,y=600,width=1530,height=190)

        # --- Data Frame Left Widgets ---
        lblNameTablet=Label(DataFrameLeft,text="Name of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.name_of_tablet,font=("times new roman",12,"bold"),width=33)
        comNameTablet["value"]=("","Paracetamol","Ibuprofen","Amoxicillin","Cetirizine","Azithromycin","Morphine","Omeprazole","Aspirin","Metformin","Atorvastatin","Lisinopril","Epinephrine","Albuterol","Prednisone")
        comNameTablet.grid(row=0,column=1, sticky="ew")

        lblRef=Label(DataFrameLeft,text="Reference No",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRef.grid(row=1,column=0,sticky=W)
        txtRef=Entry(DataFrameLeft,textvariable=self.ref_no,font=("times new roman",12,"bold"),width=35)
        txtRef.grid(row=1,column=1, sticky="ew")

        lblDose=Label(DataFrameLeft,text="Dose",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(DataFrameLeft,textvariable=self.dose,font=("times new roman",12,"bold"),width=35)
        txtdose.grid(row=2,column=1, sticky="ew")

        lblNoOfTablets=Label(DataFrameLeft,text="No of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataFrameLeft,textvariable=self.no_tablets,font=("times new roman",12,"bold"),width=35)
        txtNoOfTablets.grid(row=3,column=1, sticky="ew")

        lblLot=Label(DataFrameLeft,text="Lot",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)    
        txtLot=Entry(DataFrameLeft,textvariable=self.lot_no,font=("times new roman",12,"bold"),width=35)
        txtLot.grid(row=4,column=1, sticky="ew")

        lblIssueDate=Label(DataFrameLeft,text="Issue Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)  
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issue_date,font=("times new roman",12,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1, sticky="ew")

        lblExpDate=Label(DataFrameLeft,text="Exp Date",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.exp_date,font=("times new roman",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1, sticky="ew")

        lblDailyDose=Label(DataFrameLeft,text="Daily Dose",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblDailyDose.grid(row=7,column=0,sticky=W)
        lblDailyDose_entry=Entry(DataFrameLeft,textvariable=self.daily_dose,font=("times new roman",12,"bold"),width=35)
        lblDailyDose_entry.grid(row=7,column=1, sticky="ew")

        lblSideEffect=Label(DataFrameLeft,text="Possible Side Effect",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblSideEffect.grid(row=8,column=0,sticky=W) 
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.side_effect,font=("times new roman",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1, sticky="ew")

        lblFurtherInfo=Label(DataFrameLeft,text="Further Information",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,textvariable=self.further_info,font=("times new roman",12,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3, sticky="ew")

        lblbloodPressure=Label(DataFrameLeft,text="Blood pressure",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblbloodPressure.grid(row=1,column=2,sticky=W)
        txtbloodPressure=Entry(DataFrameLeft,textvariable=self.blood_pressure,font=("times new roman",12,"bold"),width=35)
        txtbloodPressure.grid(row=1,column=3, sticky="ew")

        lblStorage=Label(DataFrameLeft,text="Storage",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,textvariable=self.storage,font=("times new roman",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3, sticky="ew")

        lblMedicine=Label(DataFrameLeft,text="Medicine",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,textvariable=self.medicine,font=("times new roman",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3, sticky="ew")

        lblPatientId=Label(DataFrameLeft,text="Patient Id",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,textvariable=self.patient_id,font=("times new roman",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3, sticky="ew")

        lblnhsNumber=Label(DataFrameLeft,text="NHS Number",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblnhsNumber.grid(row=5,column=2,sticky=W)
        txtnhsNumber=Entry(DataFrameLeft,textvariable=self.nhs_number,font=("times new roman",12,"bold"),width=35)
        txtnhsNumber.grid(row=5,column=3, sticky="ew")

        # UPDATED: "Patient Name" now has a capital P
        lblPatientname=Label(DataFrameLeft,text="Patient Name",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataFrameLeft,textvariable=self.patient_name,font=("times new roman",12,"bold"),width=35)
        txtPatientname.grid(row=6,column=3, sticky="ew")

        lbldateOfBirth=Label(DataFrameLeft,text="Date of Birth",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lbldateOfBirth.grid(row=7,column=2,sticky=W)
        txtdateOfBirth=Entry(DataFrameLeft,textvariable=self.dob,font=("times new roman",12,"bold"),width=35)
        txtdateOfBirth.grid(row=7,column=3, sticky="ew")

        lblPatientAddress=Label(DataFrameLeft,text="Patient Address",font=("times new roman",12,"bold"),padx=2,pady=6)    
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,textvariable=self.patient_address,font=("times new roman",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3, sticky="ew")

        # --- Data Frame Right ---
        self.txtPrescription=Text(DataFrameRight,font=("times new roman",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # --- Button Frame ---
        btnPrescription=Button(ButtonFrame,command=self.iPrescriptionData,text="Prescription",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnPrescription.grid(row=0,column=0, sticky="nsew")

        btnPrescriptionData=Button(ButtonFrame,command=self.iPreciptionData,text="Prescription Data",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnPrescriptionData.grid(row=0,column=1, sticky="nsew")

        btnupdate=Button(ButtonFrame,command=self.update_data,text="Update",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnupdate.grid(row=0,column=2, sticky="nsew")

        btnDelete=Button(ButtonFrame,command=self.idelete,text="Delete",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnDelete.grid(row=0,column=3, sticky="nsew")

        btnclear=Button(ButtonFrame,command=self.clear,text="Clear",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnclear.grid(row=0,column=4, sticky="nsew")

        btnSearch=Button(ButtonFrame,command=self.search,text="Search",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnSearch.grid(row=0,column=5, sticky="nsew")

        btnexit=Button(ButtonFrame,command=self.iExit,text="Exit",font=("times new roman",12,"bold"),width=18,bg="green",fg="white")
        btnexit.grid(row=0,column=6, sticky="nsew")

        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("tablet", "ref", "dose", "no", "lot", "issue", "exp", "daily", "side", "info", "bp", "storage", "med", "pid", "nhs", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        headings = ["Name of Tablet", "Ref No", "Dose", "No Tablets", "Lot", "Issue Date", "Exp Date", "Daily Dose", "Side Effect", "Info", "BP", "Storage", "Medicine", "Patient ID", "NHS No", "Patient Name", "DOB", "Address"]
        cols = ["tablet", "ref", "dose", "no", "lot", "issue", "exp", "daily", "side", "info", "bp", "storage", "med", "pid", "nhs", "pname", "dob", "address"]
        
        for i in range(len(cols)):
            self.hospital_table.heading(cols[i], text=headings[i])
            self.hospital_table.column(cols[i], width=100)

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    

        #Functionality Declaration#

    def iPreciptionData(self):
        if self.name_of_tablet.get()=="" or self.ref_no.get()=="":
            messagebox.showerror("ERROR:All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Arpitahegde0312004",database="hospital")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.name_of_tablet.get(),
                self.ref_no.get(),
                self.dose.get(),
                self.no_tablets.get(),
                self.lot_no.get(),
                self.issue_date.get(),
                self.exp_date.get(),
                self.daily_dose.get(),
                self.side_effect.get(),
                self.further_info.get(),
                self.blood_pressure.get(),
                self.storage.get(),
                self.medicine.get(),
                self.patient_id.get(),
                self.nhs_number.get(),
                self.patient_name.get(),
                self.dob.get(),
                self.patient_address.get()
                
            ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Arpitahegde0312004",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital_table set name_of_tablet=%s, dose=%s, No_of_Tablets=%s, lot=%s, issue_date=%s, exp_date=%s, daily_dose=%s, side_effect=%s, Further_Information =%s, blood_pressure=%s, storage=%s, medicine=%s, patient_id=%s, nhs_number=%s, patient_name=%s, Date_of_Birth=%s, patient_address=%s where Reference_No=%s""",(
            self.name_of_tablet.get(),
            self.dose.get(),
            self.no_tablets.get(),
            self.lot_no.get(),
            self.issue_date.get(),
            self.exp_date.get(),
            self.daily_dose.get(),
            self.side_effect.get(),
            self.further_info.get(),
            self.blood_pressure.get(),
            self.storage.get(),
            self.medicine.get(),
            self.patient_id.get(),
            self.nhs_number.get(),
            self.patient_name.get(),
            self.dob.get(),
            self.patient_address.get(),
            self.ref_no.get()
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Arpitahegde0312004",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital_table")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                self.hospital_table.insert("",END,values=row)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.name_of_tablet.set(row[0])
        self.ref_no.set(row[1])
        self.dose.set(row[2])
        self.no_tablets.set(row[3])
        self.lot_no.set(row[4])
        self.issue_date.set(row[5])
        self.exp_date.set(row[6])
        self.daily_dose.set(row[7])
        self.side_effect.set(row[8])
        self.further_info.set(row[9])
        self.blood_pressure.set(row[10])
        self.storage.set(row[11])
        self.medicine.set(row[12])
        self.patient_id.set(row[13])
        self.nhs_number.set(row[14])
        self.patient_name.set(row[15])
        self.dob.set(row[16])
        self.patient_address.set(row[17])




    def iPrescriptionData(self):
        self.txtPrescription.insert(END,"Name of Tablet:\t\t"+self.name_of_tablet.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t"+self.ref_no.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t"+self.dose.get()+"\n")
        self.txtPrescription.insert(END,"No of Tablets:\t\t"+self.no_tablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t"+self.lot_no.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t"+self.issue_date.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t"+self.exp_date.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t"+self.daily_dose.get()+"\n")
        self.txtPrescription.insert(END,"Possible Side Effect:\t\t"+self.side_effect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t"+self.further_info.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t"+self.blood_pressure.get()+"\n")
        self.txtPrescription.insert(END,"Storage:\t\t"+self.storage.get()+"\n")
        self.txtPrescription.insert(END,"Medicine:\t\t"+self.medicine.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t"+self.patient_id.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t"+self.nhs_number.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t"+self.patient_name.get()+"\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t"+self.dob.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t"+self.patient_address.get()+"\n")  


    def idelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Arpitahegde0312004",database="hospital")
        my_cursor=conn.cursor()   
        query="delete from hospital_table where Reference_No=%s"
        value=(self.ref_no.get(),) 
        my_cursor.execute(query,value)
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success","Record has been deleted")
        conn.close()  


    def clear(self):    
        self.name_of_tablet.set("")
        self.ref_no.set("")
        self.dose.set("")
        self.no_tablets.set("")
        self.lot_no.set("")
        self.issue_date.set("")
        self.exp_date.set("")
        self.daily_dose.set("")
        self.side_effect.set("")
        self.further_info.set("")
        self.blood_pressure.set("")
        self.storage.set("")
        self.medicine.set("")
        self.patient_id.set("")
        self.nhs_number.set("")
        self.patient_name.set("")
        self.dob.set("")
        self.patient_address.set("")
        self.txtPrescription.delete("1.0",END)


    def search(self):
        
        if self.ref_no.get() == "":
            messagebox.showerror("Error", "Please enter a Reference Number to search.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Arpitahegde0312004", database="hospital")
                my_cursor = conn.cursor()
                
                # Using LIKE allows for partial matching (e.g., search '10' finds '101', '102')
                query = "SELECT * FROM hospital_table WHERE Reference_No LIKE %s"
                value = ('%' + self.ref_no.get() + '%',)
                
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                
                if len(rows) != 0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for row in rows:
                        self.hospital_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Not Found", "No record matches this Reference Number.")
                
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")


    def iExit(self):
        # Displays a confirmation dialog box
        iExit = messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

def start_hospital(root=None):
    if root is None:
       main_root = Tk()
    else:
        # If root IS passed from login, clear all login widgets first
        main_root = root
        for widget in root.winfo_children():
            widget.destroy()
    ob = Hospital(main_root)
    main_root.state('zoomed')

    if root is None:
        main_root.mainloop()

if __name__ == "__main__":
    start_hospital()
