cursor = conn.cursor()  # Don't rename the cursor


def insert_records(data):
    cursor.executemany("INSERT into patients VALUES (?, ?)", data)
    cursor.execute("SELECT * FROM patients ORDER BY name ASC")
    for record in cursor.fetchall():
        print(record)
# In this task you mustn't close connection to DB.(Due to the checking features)
