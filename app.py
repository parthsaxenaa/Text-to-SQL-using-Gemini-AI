from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
import sqlite3

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([combined_prompt, question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = ["""You are an expert in converting English questions to SQL query!The SQL database has the name STUDENTS and has the following columns NAME, CLASS, SECTION and MARKS \n\nFor example, \nExample 1 How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS; \nExample 2 - Tell me all the students studying in Data Science class?,the SQL command will be something like this SELECT * FROM STUDENTS where CLASS="data science";also the sql code should not have ''' or any quotes symbol in beginning or end and sql word in the output.""",
"""You are an expert in converting English questions to SQL queries! The SQL database has the name STUDENTS and has the following columns NAME, CLASS, SECTION, and MARKS.
Example: Retrieve the names of students in class 10.\nSQL Query: SELECT NAME FROM STUDENTS WHERE CLASS = "10";""", """You are an expert in converting English questions to SQL queries! The SQL database has the name STUDENTS and has the following columns NAME, CLASS, SECTION, and MARKS.\nExample: Update the section of the student named "John" to "B".\nSQL Query: UPDATE STUDENTS SET SECTION = "B" WHERE NAME = "John";"""]

combined_prompt = " ".join(prompt)





st.set_page_config(page_title="SQL Query Retriever")
st.header("Gemini App to retrieve SQL Queries")
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "students.db")
    st.subheader("The response is: ")
    for row in data:
        print(row)
        st.header(row)