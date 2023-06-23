from dbh import conn, cur

statement = "SELECT topic_name FROM Topics"
data = ()
cur.execute(statement, data)
conn.commit()

