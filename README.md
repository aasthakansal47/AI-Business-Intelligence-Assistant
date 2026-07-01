# AI Business Intelligence Assistant

An AI-powered Business Intelligence project that converts natural language questions into SQL queries, runs them on a MySQL database, and generates charts and business insights automatically.

---

## Features

- Convert natural language into SQL queries using AI
- Connect with MySQL database
- Execute SQL queries and fetch results
- Automatically generate bar charts
- Generate business insights using AI
- Fallback SQL support if AI fails
- Save charts locally in dashboard folder

---

## Tech Stack

- Python
- MySQL
- Google Gemini API
- Matplotlib
- Tabulate
- Python-dotenv

---

## Project Structure

AI-Business-Intelligence-Assistant/
│
├── python/
│   ├── main.py
│   ├── charts.py
│   ├── database.py
│   ├── read_data.py
│   ├── filter_data.py
│   ├── groupby_data.py
│   └── .env
│
├── data/
│   └── SampleSuperstore.csv
│
├── dashboard/
│   └── chart.png
│
└── README.md

---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/aasthakansal47/AI-Business-Intelligence-Assistant.git

---

### 2. Install dependencies
pip install mysql-connector-python
pip install google-genai
pip install matplotlib
pip install tabulate
pip install python-dotenv

---

### 3. Create MySQL database
CREATE DATABASE ai_business_intelligence;

Use table: samplesuperstore

---

### 4. Create .env file
GEMINI_API_KEY=your_api_key_here

---

### 5. Run project
python python/main.py

---

## Example Questions

- Show total sales by category
- Which segment has highest sales?
- Show profit by region
- Top 5 cities by sales
- Sales distribution by state

---

## Output

- SQL query generated automatically
- Data displayed in table format
- Bar chart saved in dashboard folder
- Business insights generated using AI

---

## Important Note

Do NOT upload .env file to GitHub.  
It contains your API key.

Add this to .gitignore:
.env
__pycache__/

---

## Author

Aastha Kansal
