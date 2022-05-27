import matplotlib.pyplot as plt


class Charts:
    x_cordinate = []
    y_cordinate = []

    def __init__(self):
        pass

    def pie_chart(self, list_item):
        slices = []
        activities = []
        colors = ['r', 'y', 'g', 'b', 'c', 'm']
        for item in list_item.values():
            slices.append(item)
        print(slices)
        for item in list_item:
            activities.append(item)
        print(activities)

        plt.pie(slices, labels=activities, colors=colors,
                startangle=90, shadow=True, explode=[0.2, 0, 0, 0, 0, 0])

        # plotting legend
        plt.legend(title="budget")

        # showing the plot
        plt.show()


