import os
import mysql.connector
from dotenv import load_dotenv
from google import genai
from tabulate import tabulate
from charts import create_bar_chart

# ---------------- LOAD API KEY ----------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Loaded API Key:", api_key)

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

print("=" * 50)
print(" AI Business Intelligence Assistant ")
print("=" * 50)

# ---------------- USER QUESTION ----------------
question = input("\nAsk your business question: ")

# ---------------- PROMPT ----------------
prompt = f"""
You are an expert MySQL developer.

Database Name: ai_business_intelligence

Table Name:
samplesuperstore

Columns:
Ship Mode,
Segment,
Country,
City,
State,
Postal Code,
Region,
Category,
Sub-Category,
Sales,
Quantity,
Discount,
Profit

Rules:
1. Return ONLY valid MySQL query.
2. No markdown.
3. No explanation.
4. No ```sql
5. Query must work directly in MySQL.

User Question:
{question}
"""

# ---------------- GEMINI SQL ----------------
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    sql_query = response.text.strip()

    sql_query = (
        sql_query.replace("```sql", "")
                 .replace("```", "")
                 .strip()
    )

except Exception as e:
    print("\nGemini Error:")
    print(e)
    exit()

print("\nGenerated SQL Query:\n")
print(sql_query)

# ---------------- MYSQL ----------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@12345",
    database="ai_business_intelligence"
)

cursor = connection.cursor()

try:
    cursor.execute(sql_query)

except Exception as e:
    print("\nSQL Error:")
    print(e)
    cursor.close()
    connection.close()
    exit()

rows = cursor.fetchall()
headers = [i[0] for i in cursor.description]

print("\nQuery Result:\n")

print(tabulate(rows, headers=headers, tablefmt="grid"))

# ---------------- CHART ----------------
if len(headers) == 2:
    print("\nCreating Chart...")
    create_bar_chart(headers, rows)

# ---------------- AI INSIGHTS ----------------
result_text = ""

for row in rows:
    result_text += str(row) + "\n"

insight_prompt = f"""
You are a Senior Business Analyst.

User Question:
{question}

SQL Result:
{result_text}

Give exactly 3 business insights.

Keep them short.

Simple English.
"""

try:

    insight = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=insight_prompt
    )

    print("\nBusiness Insights:\n")
    print(insight.text)

except Exception as e:

    print("\nGemini Insight Error:")
    print(e)

cursor.close()
connection.close()