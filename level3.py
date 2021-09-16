from tkinter import *
import sqlite3


data = Tk()
data.title('data storage')
data.geometry("400x400")

# creating data base
database = sqlite3.connect('address_storage.db')
c = database.cursor()

# creating table
'''
c.execute("""CREATE TABLE address (
            NAME text,
            ADDRESS text,
            CONTACT integer)""")
'''
# submit function for database
def submit():
        database = sqlite3.connect('address_storage.db')
        c = database.cursor()

        c.execute("INSERT INTO address VALUES(:NAME, :ADDRESS, :contact)",
                  {
                      'NAME': NAME.get(),
                      'EMAIL': ADDRESS.get(),
                      'CONTACT': CONTACT.get()
                  })
        database.commit()
        database.close()
        NAME.delete(0, END)
        ADDRESS.delete(0, END)
        CONTACT.delete(0, END)


def query():
    database = sqlite3.connect('address_storage.db')
    c = database.cursor()
    c.execute("SELECT *,oid FROM address")
    record = c.fetchall()
    print(record)
    for records in record:
        record += str(records[0]) + '\n'

    query_labels = Label(data, text=record)
    query_labels.grid(row=7, column=0, columnspan=2)

    database.commit()
    database.close()

# text boxes
NAME = Entry(data, width=40)
NAME.grid(row=2, column=2, padx=25)
ADDRESS = Entry(data, width=40)
ADDRESS.grid(row=3, column=2)
CONTACT = Entry(data, width=40)
CONTACT.grid(row=4, column=2)
# text labels
NAME_labels = Label(data, text='name')
NAME_labels.grid(row=2, column=0)
ADDRESS_labels = Label(data, text='email')
ADDRESS_labels.grid(row=3, column=0)
CONTACT_labels = Label(data, text='contact')
CONTACT_labels.grid(row=4, column=0)

# creating button
submit_btn = Button(data, text="Add data to database", command=submit)
submit_btn.grid(row=5, column=0, columnspan=3, pady=30, padx=30, ipadx=50)

query_btn = Button(data,text="show data",command=query)
query_btn.grid(row=6, column=0,  columnspan=2, pady=20, padx=20, ipadx=50)



database.commit()
database.close()
data.mainloop()