import sqlite3
import time

conn = sqlite3.connect("./database/Maths_Topics.db")
cur = conn.cursor()

def get_topic_name(topic_id):
    #Gets topic name by id
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

def get_subtopic_name(subtopic_id):
    #Gets subtopic name by id
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
    statement = "SELECT id,topic_name FROM Subtopics WHERE topic_id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    subtopics = {}
    for row in result:
        subtopics.update({row[0]:row[1]})
    return(subtopics)

def get_subtopic_names(topic_id):
    #returns a list of subtopic names
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
    statement = "SELECT id FROM Subtopics WHERE topic_id=?"
    data = (topic_id,)
    cur.execute(statement, data)
    result = cur.fetchall()
    conn.commit()
    subtopics = []
    for row in result:
        subtopics.append(row[0])
    return(subtopics)

def get_topic_id_by_subtopic_id(subtopic_id):
    #returns the topic id for a given subtopic id
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
    topic_name = get_topic_name(get_topic_id_by_subtopic_id(subtopic_id))
    return (topic_name)

def get_questions(subtopic_id):
    #Returns all questions for a given subtopic id
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
        questions.update(ids[i]:{"max_score":max_score, "paths":paths})
    return (questions)

def add_score(score, subtopic_id):
    #Adds a score to the scores table
    topic_id = get_topic_id_by_subtopic_id(subtopic_id)
    time = int(time.time())
    statement = "INSERT INTO Scores (subtopic_id,topic_id,score,date) VALUES (?,?,?,?)"
    data = (subtopic_id, topic_id, score, time)
    cur.execute(statement, data)
    conn.commit()









    
