from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

##configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCION TO LOAD GGL GEMINI MODEL

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve from dbms

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

#prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION AND MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

st.set_page_config(page_title="SQL Query Generator & Retriever")
st.header("🔍 Gemini AI - SQL Query Assistant")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    # Get the SQL query from Gemini
    sql_query = get_gemini_response(question, prompt)
    print("Generated SQL Query:", sql_query)

    # Execute the SQL query on the database
    result = read_sql_query(sql_query, "student.db")

    # Display SQL Query
    st.subheader("📝 Converted SQL Query:")
    st.code(sql_query, language="sql")  # Displays the query in a nice SQL code block

    # Explanation of SQL Query
    st.subheader("💡 Explanation of the Query:")
    if "COUNT" in sql_query:
        st.write("This query counts the number of records in the `STUDENT` table.")
    elif "WHERE" in sql_query:
        st.write("This query filters records based on a specific condition, such as class or marks.")
    elif "ORDER BY" in sql_query:
        st.write("This query sorts the data based on a specified column (e.g., highest marks first).")
    else:
        st.write("This query retrieves specific details from the `STUDENT` table.")

    # Display Retrieved Data
    st.subheader("📊 Retrieved Data:")

    if result:
        for row in result:
            formatted_row = " | ".join(str(item) for item in row)  # Format row nicely
            st.write(f"✅ {formatted_row}")  # Display row with bullet points
    else:
        st.warning("⚠ No data found for the given query.")
