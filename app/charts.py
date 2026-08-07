import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig("bar_chart.png")  # Save the bar chart as an image file
    plt.close()  # Close the figure to free up memory
    #plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%")
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("pie_chart.png")  # Save the pie chart as an image file
    plt.close()  # Close the figure to free up memory
    #plt.show()


if __name__ == "__main__":
    labels = ["A", "B", "C", "D", "E"]
    values = [30, 500, 100, 200, 90]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
