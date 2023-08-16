from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import shutil

"""
root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Test").grid(column = 0, row = 0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column = 1, row = 0)
root.mainloop()"""

import dbh as d
from dbh import conn, cur

def get_topics():
    statement = "SELECT id,topic_name FROM Topics ORDER BY topic_name ASC"
    data = ()
    cur.execute(statement, data)
    topics = cur.fetchall()
    conn.commit()
    return (topics)

def print_topics(topics):
    for row in topics:
        print(str(row[0]) + ": " + row[1])
    print ("Total Topics: " + str(len(topics)))

def get_questions(topic_id, subtopic_id):
    statement = "SELECT id,title FROM Questions WHERE topic_id=? AND subtopic_id=?"
    data = (topic_id, subtopic_id)
    cur.execute(statement, data)
    questions = cur.fetchall()
    conn.commit()
    return (questions)

def print_questions(questions):
    for row in questions:
        print(str(row[0]) + ": " + row[1])
    print ("Total questions for this topic: " + str(len(questions)))

def get_subtopics(topic_id):
    statement = "SELECT id,topic_name FROM Subtopics WHERE topic_id=? ORDER BY topic_name ASC"
    data = (topic_id,)
    cur.execute(statement, data)
    topics = cur.fetchall()
    conn.commit()
    return (topics)

def print_subtopics(topics):
    print ("\n--------------------")
    print("SUBTOPICS")
    print("--------------------")
    for row in topics:
        print(str(row[0]) + ": " + row[1])
    print ("\n")
    print ("Total subtopics for this topic: " + str(len(topics)))
    print ("--------------------")
    print ("\n")

def add_answer(question_id):
    #Make image dirs if they do not already exist
    Tk().withdraw()
    image_path = askopenfilename()
    if (not os.path.isdir("./resources")):
        os.mkdir("./resources")
    if (not os.path.isdir("./resources/answers")):
        os.mkdir("./resources/answers")
    #Get the id of the last answer
    statement = "SELECT MAX(id) FROM Answers"
    data = ()
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result[0] is None:
        this_id = result[0] + 1
    else:
        this_id = 1
        
    new_path = "./resources/answers/" + str(this_id) + ".png"
    shutil.copyfile(image_path, new_path)

    #Add the answer to the database
    statement = "INSERT INTO Answers(image_path, question_id) VALUES (?, ?)"
    data = (new_path, question_id)
    cur.execute(statement, data)
    conn.commit()

def register_topic():
    #Get current topics
    print_topics(get_topics())
    
    topic_name = input("\nEnter new topic name: ")
    #Check topic doesn't already exist
    statement = "SELECT topic_name FROM Topics WHERE topic_name = ?"
    data = (topic_name)
    cur.execute(statement, data)
    result = cur.fetchone()
    if result:
        print ("A topic with that name already exists!")
        return
    conn.commit()
    #Add topic
    statement = "INSERT INTO Topics (topic_name) VALUES (?)"
    data = (topic_name,)
    cur.execute()
    conn.commit()

def register_subtopic():
    #Get current topics
    print_topics(get_topics())
    topic_id = input("Enter the parent topic: ")
    #Check that the given topic exists
    if not d.check_topic(int(topic_id)):
        print ("Error: Topic not found")
        return
    
    #Get current sub topics
    print_subtopics(get_subtopics(topic_id))

    subtopic_name = input("Enter subtopic name: ")
    #Check subtopic doesn't already exist
    statement = "SELECT topic_name FROM Subtopics WHERE topic_name=? AND topic_id=?"
    data = (subtopic_name, topic_id)
    cur.execute(statement, data)
    result = cur.fetchone()
    if result:
        print ("A subtopic with that name under the given topic already exists!")
        return;
    conn.commit()

    #Add the subtopic
    statement = "INSERT INTO Subtopics (topic_name, topic_id) VALUES (?, ?)"
    data = (subtopic_name, topic_id)
    cur.execute(statement, data)
    conn.commit()
    

def register_question():
    #Get topics
    d.print_topics(d.get_topics())

    is_topic = False
    selected_topic = 0
    while not is_topic:
        print ("\n")
        selected_topic = int(input("Enter topic id: "))
        is_topic = d.check_topic(selected_topic))
        if not is_topic:
            print ("Error: Please enter a valid topic id.")

    #Get subtopics
    is_subtopic = False
    selected_subtopic = 0
    while not is_subtopic:
        print ("\n")
        selected_subtopic = int(input("Enter subtopic id: "))
        is_subtopic = d.check_subtopic(selected_subtopic)
        if not is_subtopic:
            print ("Error: Please enter a valid subtopic id.")

    
    
    #Find what this questions ID would be

    statement = "SELECT MAX(id) FROM Questions"
    data = ()
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit();
    if not result[0] is None:
        this_id = result[0] + 1
    else:
        this_id = 1

    #Get the image, rename it, and move it to correct location
    if (not os.path.isdir("./resources")):
        os.mkdir("./resources")
    if (not os.path.isdir("./resources/questions")):
        os.mkdir("./resources/questions")
    #Now we have the directory, get the image
    new_path = "./resources/questions/" + str(this_id) + ".png"
    shutil.copyfile(image_path, new_path)
    
    #Insert into table
    statement = "INSERT INTO Questions (title, image_path, topic_id, subtopic_id) VALUES (?, ?, ?, ?)"
    data = (question_title, new_path, topic_id, subtopic_id)
    cur.execute(statement, data)
    conn.commit()

    all_entered = False
    while (not all_entered):
        choice = input("1 -> Add an answer\n2 -> continue\n-$ ")
        if (choice == "2"):
            all_entered = True
        elif (choice == "1"):
            add_answer(this_id)

while (True):
    choice = input("1 -> Register topic\n2 -> Register Subtopic\n3 -> Register Question\n4 -> Add Answer(s)\n5 -> Exit\n-$ ")
    match choice:
        case "1":
            register_topic()
        case "2":
            register_subtopic()
        case "3":
            register_question()
        case "4":
            register_question()
        case "5":
            print("Please enter a valid input")
