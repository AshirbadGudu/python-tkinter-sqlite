# importing tkinter
from tkinter import *
import sqlite3
# Create Root
root = Tk()
# Set Title
root.title('Lets Connect with db')
# Set Height and width
root.geometry("400x400")
# Connect with db
con = sqlite3.connect('sqLiteDB.db')
# Create Cursor
c = con.cursor()
# Create Delete Function


def delete():
    # Connect with db
    con = sqlite3.connect('sqLiteDB.db')
    # Create Cursor
    c = con.cursor()
    c.execute("DELETE FROM user WHERE oid = :delete_id",
        {
            "delete_id": delete_box.get()
        }
    )
    # Clear Delete id entry
    delete_box.delete(0, END)    
    # Commit Changes
    con.commit()
    # Close Connection
    con.close()
    # call show
    show()

# Create submit function
def submit():
    # Connect with db
    con = sqlite3.connect('sqLiteDB.db')
    # Create Cursor
    c = con.cursor()
    # Insert into the table
    c.execute("INSERT INTO user VALUES (:name, :age)",
              {
                  'name': name.get(),
                  'age': age.get()
              }
              )
    # Commit Changes
    con.commit()
    # Close Connection
    con.close()
    # Clear Text Entries
    name.delete(0, END)
    age.delete(0, END)

# Lets create show function
def show():
    # Connect with db
    con = sqlite3.connect('sqLiteDB.db')
    # Create Cursor
    c = con.cursor()
    # select command
    c.execute("SELECT *, oid FROM user")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[2]) + ")  " + str(record[0]) + "  " + str(record[1]) + '\n'
    show_lbl = Label(root, text=print_records)
    show_lbl.pack()
    # Create Cursor
    c = con.cursor()
    # Commit Changes
    con.commit()
    # Close Connection
    con.close()

# Create Entries
name = Entry(root, width="30")
age = Entry(root, width="30")
nameLabel = Label(root, text="Enter Name")
ageLabel = Label(root, text="Enter Age")
nameLabel.pack()
name.pack()
ageLabel.pack()
age.pack()

# Create Button
submit_btn = Button(root, text="Add To Database", command=submit)
submit_btn.pack()


# create delete 
delete_box = Entry(root, width="30")
delete_btn = Button(root, text="Enter Id and Delete", command=delete)
delete_box.pack()
delete_btn.pack()


# Create a show button
show_btn = Button(root, text="Show", command=show)
show_btn.pack()
# Event Loop
root.mainloop()
