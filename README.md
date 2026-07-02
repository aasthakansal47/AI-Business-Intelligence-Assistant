# 🤖 AI Business Intelligence Assistant

An AI-powered Business Intelligence Assistant that converts natural language questions into SQL queries using Google Gemini AI, executes them on a MySQL database, visualizes the results with charts, and generates AI-driven business insights.

---

## 🚀 Features

- 🤖 Convert natural language questions into SQL using Google Gemini AI
- 🗄️ Execute SQL queries on MySQL
- 📊 Automatically generate business charts
- 💡 AI-generated business insights
- 📈 Display results in a formatted table
- 🔐 Secure API key management using .env
- 📂 Save generated charts automatically
- ⚡ Fast and interactive command-line interface

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- MySQL
- Matplotlib
- Tabulate
- Python-dotenv

---

## 📂 Project Structure

```
AI-Business-Intelligence-Assistant/
│
├── dashboard/
│   └── chart.png
│
├── data/
│   └── SampleSuperstore.csv
│
├── python/
│   ├── main.py
│   ├── charts.py
│   ├── database.py
│   ├── filter_data.py
│   ├── groupby_data.py
│   ├── read_data.py
│   └── .env (Not uploaded)
│
├── .gitignore
├── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/aasthakansal47/AI-Business-Intelligence-Assistant.git
```

---

### Install Dependencies

```bash
pip install google-genai
pip install mysql-connector-python
pip install matplotlib
pip install tabulate
pip install python-dotenv
```

---

### Create MySQL Database

Create a MySQL database named:

```sql
ai_business_intelligence
```

Import the **SampleSuperstore** dataset into a table named:

```text
samplesuperstore
```

---

### Create .env File

Inside the **python** folder, create a file named `.env`

Add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Project

```bash
python python/main.py
```

---

## 💬 Sample Questions

- Show total sales by category
- Show total profit by category
- Which segment has the highest sales?
- Show sales by region
- Show top 10 cities by sales
- Show total profit by state
- Which category generated the highest profit?
- Compare sales across regions
- Show average sales by category
- Show total quantity sold by category

---

## 📊 Output

The assistant automatically:

- Converts English questions into SQL
- Executes SQL queries
- Displays formatted tables
- Generates bar charts
- Saves charts inside the dashboard folder
- Generates AI-powered business insights

---

## 📸 Sample Output

Example:

**Question**

```
Show total sales by category
```

Generated SQL

```sql
SELECT Category, SUM(Sales)
FROM samplesuperstore
GROUP BY Category;
```

Output

```
Technology     836154
Furniture      741999
Office Supplies 719047
```

---

## 🔒 Security

The `.env` file is excluded from GitHub using `.gitignore`.

Never upload your API key.

---

## 👩‍💻 Author

**Aastha Kansal**

B.Tech CSE | AI & Data Analytics Enthusiast

GitHub:
https://github.com/aasthakansal47

LinkedIn:
(https://www.linkedin.com/in/aastha-kansal-561533311/)

---

⭐ If you found this project useful, consider giving it a star!
