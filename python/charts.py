import os
import matplotlib.pyplot as plt

def create_bar_chart(headers, rows):

    if len(headers) != 2:
        print("Chart requires exactly 2 columns.")
        return

    x = [str(row[0]) for row in rows]
    y = [float(row[1]) for row in rows]

    plt.figure(figsize=(8, 5))
    plt.bar(x, y)

    plt.xlabel(headers[0])
    plt.ylabel(headers[1])
    plt.title("Business Intelligence Report")

    plt.xticks(rotation=45)
    plt.tight_layout()

    # ---------------- SAVE PATH ----------------
    output_folder = os.path.join(os.path.dirname(__file__), "..", "Dashboard")
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, "chart.png")

    plt.savefig(output_file)
    print(f"Chart saved at: {output_file}")

    plt.show()
    plt.close()