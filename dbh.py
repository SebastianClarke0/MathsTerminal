import sqlite3

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
    











    
