import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

table_info = """
create table STUDENTS(NAME VARCHAR(25), CLASS VARCHAR(10), SECTION VARCHAR(10), MARKS INT);"""


cursor.execute(table_info)

cursor.execute('''Insert into STUDENTS values("kirpal", "data science", "A", "90")''')
cursor.execute('''Insert into STUDENTS values("ankit", "data science", "B", "100")''')
cursor.execute('''Insert into STUDENTS values("ujjwal", "web", "A", "70")''')
cursor.execute('''Insert into STUDENTS values("simon", "cyber", "A", "49")''')
cursor.execute('''INSERT INTO STUDENTS values ("emma", "web", "B", "85")''')
cursor.execute('''INSERT INTO STUDENTS values ("alex", "cyber", "B", "78")''')
cursor.execute('''INSERT INTO STUDENTS values ("sara", "data science", "A", "92")''')
cursor.execute('''INSERT INTO STUDENTS values ("michael", "web", "A", "88")''')
cursor.execute('''INSERT INTO STUDENTS values ("olivia", "cyber", "A", "65")''')



print("The inserted records are ")
data = cursor.execute('''Select * from students''')

for row in data:
    print(row)

connection.commit()
connection.close()