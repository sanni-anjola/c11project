import sqlite3

# with sqlite3.connect("testdb.db") as connection:
with sqlite3.connect(":memory:") as connection:

    cursor = connection.cursor()

    # cursor.execute("CREATE TABLE User (name TEXT, age INT);")
    # name = "Uche"
    # age = 45
    # cursor.execute("INSERT INTO User VALUES (?, ?)", (name, age))
    cursor.execute("SELECT * FROM User")
    print(cursor.fetchone())
    # cursor.executemany("")
    # cursor.executescript("")