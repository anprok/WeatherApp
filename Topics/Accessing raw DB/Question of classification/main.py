cursor = conn.cursor()
cursor.execute("UPDATE patients SET disease='B36C16' WHERE disease='A35B15'")


# In this task you mustn't close connection to DB.(Due to the checking features)