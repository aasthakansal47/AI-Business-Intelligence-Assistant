import os
import matplotlib.pyplot as plt


def create_bar_chart(headers, rows):

    # Check if chart can be created
    if len(headers) != 2:
        print("Chart requires exactly 2 columns.")
        return

    if len(rows) == 0:
        print("No data available to plot.")
        return

    x = [str(row[0]) for row in rows]
    y = [float(row[1]) for row in rows]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(x, y)

    plt.title("Business Intelligence Report", fontsize=16)
    plt.xlabel(headers[0], fontsize=12)
    plt.ylabel(headers[1], fontsize=12)

    plt.xticks(rotation=30)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Show values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.tight_layout()

    # Save chart
    output_folder = os.path.join(
        os.path.dirname(__file__),
        "..",
        "Dashboard"
    )

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, "chart.png")

    plt.savefig(output_file, dpi=300)

    print(f"\nChart saved successfully!")
    print(f"Location: {output_file}")

    plt.show()
    plt.close()