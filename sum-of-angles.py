import pandas as pd
import seaborn as sns

#initialize empty dictionary
d = dict()

#create a dictionary of by number of corners
for n in range(4, 21):
	print(n, '|sum of angles:', (n-2)*180, '|angle:', (n-2)*180/n)
	d[n] = [((n-2)*180),((n-2)*180/n)]

#create df, transpose
df = pd.DataFrame(data=d)
df = df.T

#rename columns, reset index
df.columns = ['sum', 'angle']
df.reset_index(inplace=True)

#graph each corner angle
sns.barplot(x='index', y='angle', data=df)

#graph each  sum of angles
sns.barplot(x='index', y='sum', data=df)
