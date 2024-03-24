import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime, timedelta
import tkinter.messagebox as mymessagebox
from tkcalendar import DateEntry
import mysql.connector as mysqlconnector

root = tk.Tk()
root.geometry("600x600")
root.title("Main Window")


#import mysql.connector




# # Run the main loop





def submit_reservation():
    # Get the values from the form
    #username=username_entry.get()
    booking_for = booking_for_var.get()
    patient_name = patient_name_entry.get()
    patient_age = patient_age_entry.get()
    patient_gender = patient_gender_var.get()
    patient_email = patient_email_entry.get()
    patient_phone = patient_phone_entry.get()
    patient_address = patient_address_entry.get()
    booking_time_slot = booking_time_slot_var.get()
    booking_date = booking_date_entry.get_date()
    doctor = doctor_var.get()
# def cancel():
#     # Clear all the fields
#     id_entry.delete(0, END)
#     username_entry.delete(0, END)
#     booking_for_entry.delete(0, END)
#     patient_name_entry.delete(0, END)
#     age_entry.delete(0, END)
#     gender_entry.delete(0, END)
#     email_entry.delete(0, END)
#     phone_number_entry.delete(0, END)
#     address_entry.delete(0, END)
#     booking_time_slot_entry.delete(0, END)
#     booking_date_entry.delete(0, END)
#     doctor_entry.delete(0, END)    

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="reservation"
    )
    cursor = db.cursor()

    # Insert the reservation into the database
    try:
        query = "INSERT INTO reservations (booking_for, patient_name, patient_age, patient_gender, patient_email, patient_phone, patient_address, booking_time_slot, booking_date, doctor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (booking_for, patient_name, patient_age, patient_gender, patient_email, patient_phone, patient_address, booking_time_slot, booking_date.strftime('%Y-%m-%d'), doctor)
        cursor.execute(query, values)
        db.commit()
        # Display success message
        mymessagebox.showinfo("Reservation successful! ","Reservation successful! Welcome " + patient_name + "!")    #mymessagebox.showinfo("Login", "Login successful")
    except:
        # Display failure message
        mymessagebox.showinfo("Reservation failed. Please try again."," Please try again.")

    # Close the database connection
    db.close()

# Create the main window


# Create the labels and input fields for the reservation form
# username_label = tk.Label(root,text="Username")
# username_label.place(x=50,y=450)
# username_entry = tk.Entry(root)
# username_entry.insert(root,current_user) # Insert the current_user value
# username_entry.place(x=250,y=450)

booking_for_label = tk.Label(root,text="Booking for:",font=3,width=15,fg="red")
booking_for_var=tk.StringVar(value="self")
booking_for_self_rb=tk.Radiobutton(root,text="Self",variable=booking_for_var,value="self")
booking_for_others_rb=tk.Radiobutton(root,text="Others",variable=booking_for_var,value="others")
patient_name_label=tk.Label(root,text="Patient Name:",width=15,font=3,fg="red")
patient_name_entry=tk.Entry(root,width=30,font=2)
patient_age_label=tk.Label(root,text="Patient Age:",width=15,font=3,fg="red")
patient_age_entry=tk.Entry(root,width=30,font=2)
patient_gender_label=tk.Label(root,text="Patient Gender:",width=15,font=3,fg="red")
patient_gender_var=tk.StringVar(value="male")
patient_gender_male_rb=tk.Radiobutton(root,text="Male",variable=patient_gender_var,value="male")
patient_gender_female_rb=tk.Radiobutton(root,text="Female",variable=patient_gender_var,value="female")
patient_email_label=tk.Label(root,text="Patient Email:",width=15,font=3,fg="red")
patient_email_entry=tk.Entry(root,width=30,font=2)
patient_phone_label=tk.Label(root,text="Patient Phone:",width=15,font=3,fg="red")
patient_phone_entry=tk.Entry(root,width=30,font=2)
patient_address_label = tk.Label(root,text="Patient Address:",width=15,font=3,fg="red")
patient_address_entry = tk.Entry(root,width=30,font=2)
booking_time_slot_label=tk.Label(root,text="Booking Time Slot:",width=15,font=3,fg="red")
booking_time_slot_var=tk.StringVar(value="")
booking_time_slot_cb=ttk.Combobox(root,textvariable=booking_time_slot_var,width=30,font=2)
booking_time_slot_cb['values']=("9:00-10:00","10:00-11:00","11:00-12:00","12:00-13:00","13:00-14:00","14:00-15:00","15:00-16:00")
booking_date_label=tk.Label(root,text="Booking Date:",width=15,font=3,fg="red")
min_date=datetime.now()
max_date=min_date+timedelta(days=7)
booking_date_entry=DateEntry(root,width=30,mindate=min_date,maxdate=max_date)
doctor_label=tk.Label(root,text="Doctor:",width=15,font=3,fg="red")
doctor_var=tk.StringVar(value="")
doctor_cb=ttk.Combobox(root,textvariable=doctor_var,width=30,font=3)
doctor_cb['values']=("Dr. adithya","Dr. adarsha","Dr. sharath","Dr. nandan","Dr. rohith","Dr. sandeep","Dr. abhishek")

# Create the submit and cancel buttons
submit_button=tk.Button(root,text="Submit",command=submit_reservation,state="disabled",width=10,height=1,font=3,bg="green")
cancel_button=tk.Button(root,text="Cancel",command=root.destroy,width=10,height=1,font=3,bg="red") #

# Create the welcome label (initially empty)
welcome_label = tk.Label(root)

# 
# Layout the widgets using pack layout
booking_for_label.place(x=50,y=50)
booking_for_self_rb.place(x=250,y=50)
booking_for_others_rb.place(x=350,y=50)
patient_name_label.place(x=50,y=90)
patient_name_entry.place(x=250,y=90)
patient_age_label.place(x=50,y=130)
patient_age_entry.place(x=250,y=130)
patient_gender_label.place(x=50,y=170)
patient_gender_male_rb.place(x=250,y=170)
patient_gender_female_rb.place(x=350,y=170)
patient_email_label.place(x=50,y=210)
patient_email_entry.place(x=250,y=210)
patient_phone_label.place(x=50,y=250)
patient_phone_entry.place(x=250,y=250)
patient_address_label.place(x=50,y=290)
patient_address_entry.place(x=250,y=290)
booking_time_slot_label.place(x=50,y=330)
booking_time_slot_cb.place(x=250,y=330)
booking_date_label.place(x=50,y=370)
booking_date_entry.place(x=250,y=370)
doctor_label.place(x=50,y=410)
doctor_cb.place(x=250,y=410)
# min_date.place(x=50,y=450)
# max_date.place(x=250,y=450)

submit_button.place(x=150,y=550)
cancel_button.place(x=150,y=600)

# Run the main loop
# root.mainloop(



def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    
    # Connect to the MySQL database
    conn = mysql.connector.connect(user='root', password='root', host='localhost', database='reservation')
    cursor = conn.cursor()
    
    # Query the database to check if the entered username and password are correct
    query = "SELECT name FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    # Close the database connection
    cursor.close()
    conn.close()
    
    if result:
        # Login successful
        name = result[0]
        
        # Display the user's name in the top left corner of the main window
        label.config(text=name)
        
        # Display a successful login message
        mymessagebox.showinfo("Login", "Login successful")
        
       # Close the login window
        top.destroy()
        
        # Enable the "Show User Details" button
        details_button.config(state="normal")
        submit_button.config(state="normal")
        button1.config(state="normal")
        show_reservations_button.config(state="normal")
        button2.config(state="normal")
        # Store the currently logged-in username in a global variable
        global current_user
        current_user = username
    else:
        # Login failed
        mymessagebox.showerror("Login", "Invalid username or password")

def open_login():
    global top, username_entry, password_entry
    
    # Create a top-level window for the login
    top = tk.Toplevel(root)
    top.title("Login form")
    
    top.geometry("500x500")
    
    
    # Create labels and entry widgets for the username and password
    username_label = tk.Label(top, text="Username:",width=10,font=2,fg="red")
    username_label.place(x=50,y=40)
    
    username_entry = tk.Entry(top)
    username_entry.place(x=250,y=40)
    
    password_label = tk.Label(top, text="Password:",width=10,font=2,fg="red")
    password_label.place(x=50,y=80)
    
    password_entry = tk.Entry(top, show="*")
    password_entry.place(x=250,y=80)
    
    # Create buttons for login and cancel
    login_button = tk.Button(top, text="Login", command=login,bg="green",width=10,height=1,font=2)
    login_button.place(x=150,y=150)
    
    cancel_button = tk.Button(top, text="Cancel", command=top.destroy,bg="red",width=10,height=1,font=2)
    cancel_button.place(x=150,y=200)



# Display an empty label in the top left corner (to be updated with the user's name after successful login)
# label = tk.Label(root, text="", anchor="w",width=10,height=2,fg="red")
# label.place(x=1300,y=10)

# Add a button that opens the login window when clicked
# button = tk.Button(root, text="Open Login", command=open_login)
# button.pack()

def show_user_details():
    # Connect to the MySQL database
    conn = mysql.connector.connect(user='root', password='root', host='localhost', database='reservation')
    cursor = conn.cursor()
    
    # Query the database for details about the currently logged-in user
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (current_user,))
    result = cursor.fetchone()
    
    # Close the database connection
    cursor.close()
    conn.close()
    
    if result:
        # Display the user's details in a message box
        details = f"id: {result[0]}\nName: {result[1]}\nusername: {result[2]}"
        mymessagebox.showinfo("User Details", details)

# Create the main window
# root = tk.Tk()
# root.title("Main Window")

# Display an empty label in the top left corner (to be updated with the user's name after successful login)
label = tk.Label(root, text="", anchor="w",width=15,height=2,fg="red",font=3)
label.place(x=1300,y=10)

# Add a button that opens the login window when clicked
# button = tk.Button(root, text="Open Login", command=open_login)
# button.pack()

# Add a button that shows the currently logged-in user's details when clicked (initially disabled)
details_button = tk.Button(root, text="Show User Details", command=show_user_details, state="disabled",bg="yellow",width=30,height=2,font=2)
details_button.place(x=1200,y=250)


    
def open_registration_form():
    # reg_screen = tk.Toplevel(root)
    # reg_screen.geometry("300x300")
    # reg_screen.title("Registration Form")
    # add widgets to the registration form here
    
      
    registration_window = tk.Toplevel(root)
    registration_window.geometry("500x500")
    registration_window.title("Registration Form")

    # create input fields
    name_label = tk.Label(registration_window, text="Name:",width=10,font=2,fg="red")
    name_label.place(x=50,y=40)
    name_entry = tk.Entry(registration_window)
    name_entry.place(x=250,y=40)

    username_label = tk.Label(registration_window, text="Username:",width=10,font=2,fg="red")
    username_label.place(x=50,y=80)
    username_entry = tk.Entry(registration_window)
    username_entry.place(x=250,y=80)

    password_label = tk.Label(registration_window, text="Password:",width=10,font=2,fg="red")
    password_label.place(x=50,y=120)
    password_entry = tk.Entry(registration_window)
    password_entry.place(x=250,y=120)

    confirm_password_label = tk.Label(registration_window, text="Confirm Password:",width=10,font=2,fg="red")
    confirm_password_label.place(x=50,y=160)
    confirm_password_entry = tk.Entry(registration_window, show="*")
    confirm_password_entry.place(x=250,y=160)

    def register():
        # retrieve data from input fields
        name = name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # check if all fields are filled
        if not (name and username and password and confirm_password):
            mymessagebox.showerror("Error", "All fields are required")
            return

        # check if passwords match
        if password != confirm_password:
            mymessagebox.showerror("Error", "Passwords do not match")
            return

        # connect to MySQL database and insert data
        conn = mysqlconnector.connect(
            host="localhost",
            user="root",
            password="root",
            database="reservation"
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)",
            (name, username, password)
        )
        conn.commit()
        conn.close()

        # close registration window and show main window
        registration_window.destroy()
        root.deiconify()

    def cancel():
        # close registration window and show main window
        registration_window.destroy()
        root.deiconify()

    def open_login_form():
        # close registration window and open login form
        registration_window.destroy()
        # call function to open login form here

    # create register, cancel and login buttons
    register_button = tk.Button(registration_window, text="Register", command=register,bg="green",width=10,font=2)
    register_button.place(x=150,y=200)

    cancel_button = tk.Button(registration_window, text="Cancel", command=cancel,bg="red",width=10,font=2)
    cancel_button.place(x=150,y=250)

    login_button = tk.Button(registration_window, text="Login", command=open_login_form,bg="green",width=10,font=2)
    login_button.place(x=150,y=300)

# create register button in main window
register_button = tk.Button(root, text="Register", command=open_registration_form,bg="yellow",width=30,height=2,font=2)
register_button.place(x=1200,y=50)
# create login button in main window
login_button = tk.Button(root, text="Login", command=open_login,bg="yellow",width=30,height=2,font=2)
login_button.place(x=1200,y=150)

# user details
# import tkinter as tk
# import mysql.connector



# def show_reservations():
    # Connect to the database and retrieve the reservation data for the current user
def show_reservations():    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="reservation"
    )
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM reservations WHERE username=%s")  #, (current_user,)
    # reservations = cursor.fetchall()
    # cursor.close()
    # db.close()

    # # Create a new window to display the reservation data
    top = tk.Toplevel(root)
    top.title("My Reservations")

    # # Create a table to display the reservation data
    # columns = ["ID", "Booking For", "Patient Name", "Age", "Gender", "Email", "Phone Number", "Address", "Booking Time Slot", "Booking Date", "Doctor"]
    # for i, column in enumerate(columns):
    #     label = tk.Label(top, text=column, font=("Helvetica", 12), fg="red")
    #     label.grid(row=0, column=i)
    # for i, reservation in enumerate(reservations):
    #     for j, value in enumerate(reservation):
    #         label = tk.Label(top, text=value, font=("Helvetica", 10))
    #         label.grid(row=i+1, column=j)
    #     delete_button = tk.Button(top, text="Delete", command=lambda id=reservation[0]: delete_reservation(id))
    #     delete_button.grid(row=i+1, column=len(columns))
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    cursor.close()
    db.close()

    # Create a new window to display the reservation data
    # top = Toplevel()
    # top.title("Reservations")

    # Create a table to display the reservation data
    columns = ["ID", "Username", "Booking For", "Patient Name", "Age", "Gender", "Email", "Phone Number", "Address", "Booking Time Slot", "Booking Date", "Doctor"]
    for i, column in enumerate(columns):
        label = tk.Label(top, text=column, font=("Helvetica", 12), fg="red")
        label.grid(row=0, column=i)
    for i, reservation in enumerate(reservations):
        for j, value in enumerate(reservation):
            label = tk.Label(top, text=value, font=("Helvetica", 10))
            label.grid(row=i+1, column=j)

def delete_reservation(id):
    # Connect to the database and delete the reservation with the given id
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="reservation"
    )
    cursor = db.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    db.close()

# root = Tk()
# root.title("Main Window")

# Create a button to show the reservations
show_reservations_button =tk. Button(root, text="Show Reservations", command=show_reservations,state="disabled",bg="yellow",width=30,height=2,font=2)
show_reservations_button.place(x=1200,y=350)



def delete_account():
    # Ask the user if they are sure they want to delete their account
    if mymessagebox.askyesno("Delete Account", "Are you sure you want to delete your account? This cannot be undone."):
        # Connect to the MySQL database
        conn = mysql.connector.connect(user='root', password='root', host='localhost', database='reservation')
        cursor = conn.cursor()
        
        # Delete the user's data from the database
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (current_user,))
        
        # Commit the changes to the database
        conn.commit()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        # Display a successful deletion message
        mymessagebox.showinfo("Delete Account", "Your account has been deleted")
        
        # Clear the label in the top left corner of the main window
        label.config(text="")

# Create the main window
# root = tk.Tk()
# root.title("Main Window")

# Display an empty label in the top left corner (to be updated with the user's name after successful login)
label = tk.Label(root, text="", anchor="w")
label.pack(fill="x")

# Add a button that opens the delete account window when clicked
button1 = tk.Button(root, text="Delete Account", command=delete_account,state="disabled",bg="yellow",width=30,height=2,font=2)
button1.place(x=1200,y=450)
def logout():
    root.destroy
    
button2 = tk.Button(root, text="logout", command=root.destroy,state="disabled",bg="yellow",width=30,height=2,font=2)
button2.place(x=1200,y=550)
root.mainloop()