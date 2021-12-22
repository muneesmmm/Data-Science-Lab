from matplotlib import pyplot
import pandas
df=pandas.read_csv('iris.csv')
fig,ax=pyplot.subplots(1,1)
colors={'Setosa':'red','Versicolor':'green','Virginica':'blue'}
grouped=df.groupby('species')
for key,group in grouped:
    group.plot(ax=ax,kind='scatter',x='sepal.length',y='sepal.width',label=key,color=colors[key])
ax.set_title("scatter plot")
ax.set_xlabel('Sepal length')
ax.set_ylabel('sepal width')
pyplot.show()
