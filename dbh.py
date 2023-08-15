import sqlite3

conn = sqlite3.connect("./database/Maths_Topics.db")
cur = conn.cursor()

def get_subtopics(topic_id):
    statement = "SELECT id,topic_name FROM Subtopics WHERE topic_id=? ORDER BY topic_name ASC"
    data = (topic_id,)
    cur.execute(statement, data)
    topic = cur.fetchall()
    conn.commit()
    return(topic)

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
    
