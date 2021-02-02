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
# Create Table
c.execute("""
    CREATE TABLE user (
        name text,
        age integer
    )
""")
# Commit Changes
con.commit()
# Close Connection
con.close()
# Event Loop
root.mainloop()
