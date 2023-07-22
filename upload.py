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
    statement = "INSERT INTO Topics (topic_name, score, max_score) VALUES (?, ?, ?)"
    data = (topic_name, 0, 0)
    cur.execute()
    conn.commit()

def register_subtopic():
    #Get current topics
    print_topics(get_topics())
    topic_id = input("Enter the parent topic: ")
    #Check that the given topic exists
    statement = "SELECT id FROM Topics WHERE id=?"
    data = (int(topic_id),)
    cur.execute(statement, data)
    result = cur.fetchone()
    if not result:
        print("Topic not found")
        return
    conn.commit()
    
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
    statement = "INSERT INTO Subtopics (topic_name, score, max_score, topic_id) VALUES (?, ?, ?, ?)"
    data = (subtopic_name, 0, 0, topic_id)
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

    #Get subtopics
    print_subtopics(get_subtopics(topic_id))

    #Get sub topic input
    numeric = False
    subtopic_id = 0
    while (not numeric):
        subtopic_id = input("Enter the subtopic id: ")
        if (subtopic_id.isnumeric):
            subtopic_id = int(subtopic_id)
            numeric = True
        else:
            print("Please enter a valid id")
    #Check the id exists
    statement = "SELECT id FROM subtopics WHERE id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    if not result:
        print("Please enter a valid ID")
    conn.commit()

    #Get the questions
    print ("\nExisting questions for that topic: ")
    print_questions(get_questions(topic_id, subtopic_id))

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

def edit_question():
    print_topics(get_topics())
    topic_correct = False
    while (not topic_correct):
        topic_id = input("Enter the topic id: ")
        if (topic_id.isnumeric()):
            topic_id = int(topic_id)
            #Check that the topic exists
            statement = "SELECT id FROM Topics WHERE id=?"
            data = (topic_id,)
            cur.execute(statement, data)
            result = cur.fetchone()
            if not result:
                print ("Please enter a valid id")
                continue
            conn.commit()
            topic_correct = True
        else:
            print("Please enter a valid id")
    #We now have a valid topic id, check subtopics

    print_subtopics(get_subtopics())
    subtopic_correct = False;
    while (not subtopic_correct):
        subtopic_id = input("Enter the subtopic id: ")
        if (not subtopic_id.isnumeric()):
            print("Please enter a valid id")
            continue
        #Check that the subtopic is in the database
        subtopic_id = int(subtopic_id)
        statement = "SELECT id FROM Subtopics WHERE id=?"
        data = (subtopic_id,)
        cur.execute(statement, data)
        result = cur.fetchone()
        if not result:
            print("Please enter a valid ID")
            continue
        conn.commit()
        subtopic_correct = True

    #We now have a correct subtopic id, get the question ID

    print_questions(get_questions())

    question_correct = False
    while (not question_correct):
        question_id = input("Enter question ID: ")
        if (not question_id.isnumeric()):
            print("Please enter a valid ID")
            continue
        subtopic_id = int(subtopic_id)
        statement = "SELECT id FROM Questions WHERE id=?"
        data = (subtopic_id,)
        cur.execute(statement, data)
        result = cur.fetchone()
        if not result:
            print("Question not found!")
            continue
        conn.commit()
        question_correct = True

    valid_choice = False
    while (not valid_choice):
        choice = input("1 -> Edit Title\n2 -> 

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
