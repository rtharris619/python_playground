import pandas as pd
import matplotlib.pyplot as plt

def plot_chart():
	data = {'Category': ['A', 'B', 'C', 'D', 'E'],
					'Frequency': [50, 30, 15, 5, 2]}

	df = pd.DataFrame(data)

	df = df.sort_values(by='Frequency', ascending=False)

	df['Cumulative %'] = df['Frequency'].cumsum() / df['Frequency'].sum() * 100

	fig, ax1 = plt.subplots()
	ax1.bar(df['Category'], df['Frequency'], color='C4')
	ax1.set_ylabel('Frequency')

	ax2 = ax1.twinx()
	ax2.plot(df['Category'], df['Cumulative %'], 'C1D')
	ax2.set_ylabel('Cumulative %')

	plt.title('Pareto Chart')
	plt.show()


def driver():
	plot_chart()
