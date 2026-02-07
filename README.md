# Hospital-management-System
A comprehensive, GUI-based Hospital Management System built using Python and Tkinter. This application streamlines hospital administration by managing patient records, prescriptions, and medical data through a secure login system and a MySQL database.
A comprehensive, GUI-based Hospital Management System built using Python and Tkinter. This application streamlines hospital administration by managing patient records, prescriptions, and medical data through a secure login system and a MySQL database.

✨ Features
User Authentication: Secure Login and Registration system to protect sensitive medical data.

Patient Record Management: Full CRUD (Create, Read, Update, Delete) functionality for patient information.

Prescription Generation: Automated prescription formatting based on tablet name, dosage, and patient ID.

Real-time Search: Quick-search functionality using Reference Numbers to find patient records instantly.

Database Integration: Robust backend powered by MySQL to store large volumes of hospital data.

Modern UI: Organized layout with interactive Treeview for data visualization and a "zoomed" responsive interface.

🛠️ Technologies Used
Language: Python 3.x

Frontend: Tkinter (GUI Toolkit)

Database: MySQL

Libraries: mysql-connector-python, messagebox, ttk

🚀 Getting Started
Prerequisites
Python installed on your system.

MySQL Server installed and running.

The mysql-connector-python library:

Bash
pip install mysql-connector-python
Database Setup
Open MySQL Workbench.

Create a database named hospital:

SQL
CREATE DATABASE hospital;
Create the table structure:

SQL
USE hospital;
CREATE TABLE hospital_table (
    Name_of_tablet VARCHAR(100), Reference_No VARCHAR(100) PRIMARY KEY,
    Dose VARCHAR(100), No_of_Tablets VARCHAR(100), Lot VARCHAR(100),
    Issue_date VARCHAR(100), Exp_date VARCHAR(100), Daily_dose VARCHAR(100),
    Side_effect VARCHAR(100), Further_Information VARCHAR(100),
    Blood_pressure VARCHAR(100), Storage VARCHAR(100), Medicine VARCHAR(100),
    Patient_id VARCHAR(100), NHS_number VARCHAR(100), Patient_name VARCHAR(100),
    Date_of_Birth VARCHAR(100), Patient_address VARCHAR(100)
);
Running the App
Clone the repository:

Bash
git clone https://github.com/YourUsername/Hospital-Management.git
Run the login page:

Bash
python login.py
