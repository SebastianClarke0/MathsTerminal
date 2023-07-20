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

def get_questions(topic_id):
    statement = "SELECT id,title FROM Questions WHERE topic_id=?"
    data = (topic_id, )
    cur.execute(statement, data)
    questions = cur.fetchall()
    conn.commit()
    return (questions)

def print_questions(questions):
    for row in questions:
        print(str(row[0]) + ": " + row[1])
    print ("Total questions for this topic: " + str(len(questions)))

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
    is_numeric = False
    while (not is_numeric):
        topic_max_score = input("Enter max score: ")
        if (topic_max_score.isnumeric()):
            is_numeric = True
            topic_max_score = int(topic_max_score)
        else:
            print ("Please enter a numeric value\n")
    
    #Add topic to db
    statement = "INSERT INTO Topics (topic_name, topic_score, topic_max_score"
    data = (topic_name, 0, topic_max_score)
    cur.execute(statement, data)
    conn.commit()

def register_question():
    #Get topics
    print_topics(get_topics())

    #Get topic input
    is_numeric = False
    topic_id = 0
    while (not is_numeric):
        topic_id = input("Enter the topic id: ")
        if (topic_id.isnumeric()):
            is_numeric = True
            topic_id = int(topic_id)
        else:
            print ("Please enter a valid id")
    #Check that the ID exists
    statement = "SELECT id FROM Topics WHERE id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    if not result:
        print ("Please enter a valid topic ID")
        conn.commit()
        return;
    conn.commit()

    #Get the questions
    print ("\nExisting questions for that topic: ")
    print_questions(get_questions(topic_id))

    #Get inputs
    question_title = input("New question title: ")
    Tk().withdraw()
    image_path = askopenfilename()

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
    statement = "INSERT INTO Questions (title, image_path, topic_id) VALUES (?, ?, ?)"
    data = (question_title, new_path, topic_id)
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
