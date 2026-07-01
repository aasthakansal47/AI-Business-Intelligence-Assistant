import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@12345",
        database="ai_business_intelligence"
    )

    print("✅ Connected Successfully!")

    cursor = connection.cursor()

    query = """
SELECT Category,
SUM(Sales) AS Total_Sales
FROM samplesuperstore
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nFirst 5 Rows:\n")

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except Exception as e:
    print(e) 