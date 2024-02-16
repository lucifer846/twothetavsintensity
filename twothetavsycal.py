import matplotlib.pyplot as plt
import pandas
import csv

file = "S-1.csv"
df = pandas.read_csv(file)
df = df.rename(columns = {' yobs': 'yobs', ' ycal': 'ycal', ' bkg': 'Low', ' diff': 'Close'})
two_theta = df['#twotheta']
yobs = df['ycal']
plt.plot(two_theta,yobs)
plt.show()