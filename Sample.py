import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

fig = ff.create_distplot([data], ["aver"], show_hist=False)
# fig.show()


def RandomSetOFMean(counter):
    data_set = []
    for i in range(0, counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return(mean)


def ShowFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.show()


def setup():
    mean_list = []
    for i in range(0, 1000):
        mean = RandomSetOFMean(100)
        mean_list.append(mean)

    ShowFig(mean_list)

    mean = statistics.mean(mean_list)
    standard_deviation = statistics.stdev(mean_list)

    print("Mean = ", mean)
    print("Standard Deviation = ", standard_deviation)


setup()
