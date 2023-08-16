#This file contains useful functions for accessing the database

#get_topic_name() -> Returns topic name from ID
#get_topic_id()   -> Returns a topic id from Name
#get_topics()     -> Returns a dictionary of all topics
#print_topics()   -> Lists all topics in console
#get_topic_names()-> Returns a list of topic names
#get_topic_ids()  -> Returns a list of all topic ids
#check_topic()    -> Returns a bool indicating whether a topic exists

import sqlite3
import time

conn = sqlite3.connect("./database/Maths_Topics.db")
cur = conn.cursor()

def get_topic_name(topic_id):
    #Gets topic name by id
    try:
        topic_id = int(topic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT topic_name FROM Topics WHERE id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print("Error: No topic with the id " + str(topic_id) + " could be found.")
        return (False)
    return (result)

def get_topic_id(topic_name):
    #Gets topic id by name
    topic_name = str(topic_name)
    statement = "SELECT id FROM Topics WHERE topic_name=?"
    data = (topic_name,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print("Error: No topic with the name " + str(topic_name) + " could be found.")
        return(False)
    return (result)

def get_topics():
    #Returns a dictionary of topic ids and topic names.
    statement = "SELECT id,topic_name FROM Topics ORDER BY topic_name ASC"
    data = ()
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    topics_dict = {}
    for row in result:
        topics_dict.update({row[0]:row[1]})
    return(topics_dict)

def print_topics(topics):
    #Prints all topics
    print ("\n----------TOPICS----------\n")
    for key, value in topics.items():
        print(str(key) + " -> " + str(value) + "\n")
    print ("--------------------------\n")

def get_topic_names():
    #Returns a list of all topic names
    statement = "SELECT topic_name FROM Topics ORDER BY topic_name ASC"
    data = ()
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    topic_array = []
    for row in result:
        topic_array.append(row[0])
    return (topic_array)

def get_topic_ids():
    #Returns a list of all topic ids
    statement = "SELECT id FROM Topics ORDER BY topic_name ASC"
    data = ()
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    topic_array = []
    for row in result:
        topic_array.append(row[0])
    return(topic_array)

def check_topic(topic_id):
    #Returns a bool if found
    try:
        topic_id = int(topic_id)
    except:
        print ("Error: Input must be of type Integer")
        return False
    statement = "SELECT id FROM Topics WHERE id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        return False
    else:
        return True

def get_subtopic_name(subtopic_id):
    #Gets subtopic name by id
    try:
        subtopic_id = int(subtopic_id)
    except:
        print ("Error: Input must be of type Integer")
        return False
    statement = "SELECT topic_name FROM Subtopics WHERE id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print("Error: No subtopic with the id " + str(subtopic_id) + " could be found.")
        return (False)
    return (result)

def get_subtopic_id(subtopic_name, topic_id):
    #Gets subtopic id by name and topic id
    try:
        topic_id = int(topic_id)
    except:
        print("Error: Topic id must be of type Integer")
        return False
    subtopic_name = str(subtopic_name)
    statement = "SELECT topic_name FROM Subtopics WHERE topic_name=? AND topic_id=?"
    data = (subtopic_name, topic_id)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print("Error: No subtopic with the name " + subtopic_name + " and topic id " + str(topic_id) + " could be found.")
        return (False)
    return (result)

def get_subtopics(topic_id):
    #Returns a dictionary of subtopic and their id based on the topic id
    try:
        topic_id = int(topic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT id,topic_name FROM Subtopics WHERE topic_id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    subtopics = {}
    for row in result:
        subtopics.update({int(row[0]):str(row[1])})
    return(subtopics)

def get_subtopic_names(topic_id):
    #returns a list of subtopic names
    try:
        topic_id = int(topic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT topic_name FROM Subtopics WHERE topic_id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    subtopics = []
    for row in result:
        subtopics.append(row[0])
    return(subtopics)

def get_subtopic_ids(topic_id):
    #returns a list of subtopic ids
    try:
        topic_id = int(topic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT id FROM Subtopics WHERE topic_id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    subtopics = []
    for row in result:
        subtopics.append(row[0])
    return(subtopics)

def check_subtopic(subtopic_id):
    #Returns a bool indicating if a subtopic exists
    try:
        subtopic_id = int(subtopic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT id FROM Subtopics WHERE id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        return (False)
    else:
        return (True)

def print_subtopics(subtopics):
    print ("\n----------SUBTOPICS----------\n")
    for key, value in subtopics.items():
        print (str(key) + " : " + str(value) + "\n")
    print ("\n-----------------------------\n")

def get_topic_id_by_subtopic_id(subtopic_id):
    #returns the topic id for a given subtopic id
    try:
        subtopic_id = int(subtopic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT topic_id FROM Subtopics WHERE id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print ("Error: No subtopic with that ID exists")
        return (False)
    return (result)

def get_topic_name_by_subtopic_id(subtopic_id):
    #returns the name of the parent topic of a given subtopic
    try:
        subtopic_id = int(subtopic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    topic_name = get_topic_name(get_topic_id_by_subtopic_id(subtopic_id))
    return (topic_name)

def get_questions(subtopic_id):
    #Returns all questions for a given subtopic id
    try:
        subtopic_id = int(subtopic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT topic_name FROM Subtopics WHERE id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    if not result:
        print("Error: A subtopic with the id " + str(subtopic_id) + " could not be found.")
        return
    statement = "SELECT id FROM Questions WHERE subtopic_id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    questions = []
    for row in result:
        questions.append(row[0])
    return (questions)

def get_question_paths(question_id):
    #returns the image paths for a given question
    try:
        question_id = int(question_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    statement = "SELECT path FROM QuestionImages WHERE question_id=?"
    data = (question_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    if not result:
        print("Error: No question with the id " + str(question_id) + " could not be found.")
        return
    paths = []
    for row in result:
        paths.append(row[0])
    return (paths)

def get_questions_random(subtopic_id):
    #Returns up to 10 random questions
    try:
        subtopic_id = int(subtopic_id)
    except:
        print("Error: Input must be of type Integer")
        return False
    #First count how many questions exist
    statement = "SELECT COUNT(*) FROM Questions WHERE subtopic_id=?"
    data = (subtopic_id,)
    cur.execute(statement, data)
    result = cur.fetchone()
    conn.commit()
    limit = 10 if result > 10 else result

    #Get random questions
    statement = "SELECT id FROM Questions WHERE subtopic_id=? ORDER BY RANDOM() LIMIT ?"
    data = (subtopic_id, limit)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()

    #Generate an array of ids
    ids = []
    for row in result:
        ids.append(row[0])

    #Itterate through
    questions = {}
    statement1 = "SELECT max_score FROM Questions WHERE id=?"
    statement2 = "SELECT path FROM QuestionImages WHERE question_id=?"
    for i in range(0, len(ids)):
        data = (ids[i],)
        cur.execute(statement1, data)
        max_score = cur.fetchone()
        conn.commit()

        cur.execute(statement2, data)
        result = cur.fetchall()
        conn.commit()
        paths = []
        for row in result:
            paths.append(row[0])

        #Add to dictionary
        temp_dict = {"max_score":max_score, "paths":paths}
        temp_dict2 = {ids[i]:temp_dict}
        questions.update(temp_dict2)
    return (questions)

def add_score(score, subtopic_id):
    #Adds a score to the scores table
    topic_id = get_topic_id_by_subtopic_id(subtopic_id)
    time = int(time.time())
    statement = "INSERT INTO Scores (subtopic_id,topic_id,score,date) VALUES (?,?,?,?)"
    data = (subtopic_id, topic_id, score, time)
    cur.execute(statement, data)
    conn.commit()









    
