import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
students = df

mean = sum(students)/len(students)
std_deviation = statistics.stdev(students)
median = statistics.median(students)
mode = statistics.mode(students)

first_std_deviation_start,first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation),mean+(3*std_deviation)

thin_1_std_deviation = [result for result in students if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in students if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in students if result > third_std_deviation_start and result < third_std_deviation_end]

fig = ff.create_distplot([students],["Result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

print("Standard Deviation of this data is{}".format(std_deviation))
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))