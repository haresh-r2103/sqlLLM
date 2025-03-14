SQL LLM - AI-Powered SQL Query Assistant
🔗 Live Demo: https://sqlllm-zpxunk6wqjhrtvmfjzgxlp.streamlit.app/



🌟 Overview
SQL LLM is an AI-powered assistant that converts natural language questions into optimized SQL queries and retrieves data from a database. It helps users interact with databases effortlessly, making data retrieval intuitive and efficient—no SQL knowledge required!

🚀 Why This Project?

SQL can be complex, and not everyone is fluent in writing optimized queries.
This app bridges the gap between human language and structured queries.
With Google Gemini AI, it translates questions into SQL and fetches results instantly.
✨ Features
✅ Natural Language to SQL – Ask questions in plain English, and the app generates the corresponding SQL query.
✅ Live Database Querying – Retrieves real-time data from an SQLite database.
✅ AI-Powered Optimization – Uses Google Gemini AI to ensure efficient SQL queries.
✅ Query Explanation – Provides a breakdown of what the generated SQL query does.
✅ User-Friendly Interface – Built with Streamlit for an interactive and seamless experience.

🛠️ Tech Stack
🔹 Python – Backend logic
🔹 Streamlit – Web UI
🔹 Google Gemini API – AI-driven query conversion
🔹 SQLite – Database for storing and retrieving data
🔹 Dotenv – Secure API key management

🚀 How It Works
1️⃣ Enter a question (e.g., "Show all students in Data Science class")
2️⃣ AI generates the SQL query
3️⃣ Query executes on the database
4️⃣ Results are displayed in a structured format

Example:

🔹 Input: "How many students are in the database?"
🔹 Generated SQL: SELECT COUNT(*) FROM STUDENT;
🔹 Output: 5 students
