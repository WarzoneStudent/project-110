import pandas as pd
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("medium_data.csv")
average = df["reading_time"].tolist()

pman = statistics.mean(average)
pstdev = statistics.stdev(average)
print("The mean of the Population(readingTime) is ",pman)
print("The Standard Deviation of the Population(readingTime) is ",pstdev)

def samples_ss() :
    
    sample = []
    for i in range(0,100):
        random_index = random.randint(0,len(average)-1)
        value = average[random_index]
        sample.append(value)

    mean1sample = statistics.mean(sample)
    return mean1sample

def show_displot(meanlist):
    mean = statistics.mean(meanlist)
    meanstdv = statistics.stdev(meanlist)
    print("The mean of the Samples is ",mean)
    print("The Standard Deviation of the Samples is ",meanstdv)

    fig = ff.create_distplot([meanlist],["Sampling mean distribution"],show_hist = False)
    fig.show()

def main():
    means_of_samples = []
    for i in range (0,1000):
        value_mean = samples_ss()
        means_of_samples.append(value_mean)

    show_displot(means_of_samples)

main()
    

