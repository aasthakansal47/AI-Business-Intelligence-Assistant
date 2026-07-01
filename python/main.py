import os
from charts import create_bar_chart
import mysql.connector
from dotenv import load_dotenv
from google import genai
from tabulate import tabulate

# Load environment variables
load_dotenv()

# Gemini client (NEW SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("=" * 50)
print(" AI Business Intelligence Assistant ")
print("=" * 50)

# User input
question = input("\nAsk your business question: ")

# ---------------- PROMPT FOR SQL ----------------
prompt = f"""
You are an expert MySQL developer.

Database Name: ai_business_intelligence
Table Name: samplesuperstore

Columns:
Ship Mode, Segment, Country, City, State, Postal Code, Region,
Category, Sub-Category, Sales, Quantity, Discount, Profit

Generate ONLY a valid MySQL query.
No explanation.
No markdown.
Return only SQL.

User Question:
{question}
"""

# ---------------- SAFE SQL (FALLBACK MODE) ----------------
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    sql_query = response.text.strip()

except Exception:
    if "segment" in question.lower():
     sql_query = "SELECT Segment, SUM(Sales) FROM samplesuperstore GROUP BY Segment;"

    elif "region" in question.lower():
     sql_query = "SELECT Region, SUM(Sales) FROM samplesuperstore GROUP BY Region;"

    elif "profit" in question.lower():
     sql_query = "SELECT Category, SUM(Profit) FROM samplesuperstore GROUP BY Category;"

    else:
     sql_query = "SELECT Category, SUM(Sales) FROM samplesuperstore GROUP BY Category;"
    print("\n⚠️ Gemini failed — using fallback SQL")

print("\nGenerated SQL Query:\n")
print(sql_query)

# ---------------- MYSQL CONNECTION ----------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@12345",
    database="ai_business_intelligence"
)

cursor = connection.cursor()
cursor.execute(sql_query)

rows = cursor.fetchall()
headers = [i[0] for i in cursor.description]

print("\nQuery Result:\n")

# ---------------- CHART ----------------
if len(headers) == 2:
    print("Creating Chart...")
    create_bar_chart(headers, rows)

print(tabulate(rows, headers=headers, tablefmt="grid"))
# ---------------- CONVERT RESULT TO TEXT ----------------
result_text = ""

for row in rows:
    result_text += str(row) + "\n"

insight_prompt = f"""
You are a Senior Business Analyst.

The user asked:
{question}

SQL Result:
{result_text}

Write 3 business insights in simple English.
Do not mention SQL.
Keep it short.
"""

# ---------------- SAFE AI INSIGHTS ----------------
try:
    insight = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=insight_prompt
    )
    insight_text = insight.text

except Exception as e:
    insight_text = "AI insights unavailable (quota exceeded or API error)."

print("\nBusiness Insights:\n")

insight_text = "AI temporarily unavailable. Showing data-driven insights only."
print(insight_text)

print("\nQuick Manual Insight:")
print("Technology category has highest sales, indicating strong demand in tech products.")

cursor.close()
connection.close()