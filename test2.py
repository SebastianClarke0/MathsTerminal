import dbh as d

subtopics = d.get_subtopics(1)
for key, value in subtopics.items():
    print(str(key) + " : " + str(value))
