"""from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Test").grid(column = 0, row = 0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column = 1, row = 0)
root.mainloop()"""

from dbh import conn, cur

def register_topic():
    #Get current topics
    statement = "SELECT topic_name FROM Topics ORDER BY topic_name ASC"
    data = ()
    cur.execute(statement, data)
    topics = cur.fetchall()
    print ("Total topics: " + str(len(topics)))
    for row in topics:
        print(row[0])
    conn.commit()

while (True):
    choice = input("1 -> Register topic\n2 -> Register Question\n3 -> Add Answer(s)\n4 -> Exit\n-$ ")
    match choice:
        case "1":
            register_topic()
        case "2":
            register_question()
        case "3":
            register_question()
        case "4":
            print("Please enter a valid input")
