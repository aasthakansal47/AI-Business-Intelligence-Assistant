import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

question = input("Ask your business question: ")

prompt = f"""
You are an SQL Expert.

Database Name: ai_business_intelligence

Table Name: samplesuperstore

Columns:
Ship Mode
Segment
Country
City
State
Postal Code
Region
Category
Sub-Category
Sales
Quantity
Discount
Profit

Convert the user's question into ONLY a MySQL query.

Do not explain anything.

User Question:
{question}
"""

response = model.generate_content(prompt)

print("\nGenerated SQL Query:\n")
print(response.text)