import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
	@staticmethod
	def histogram(data: pd.DataFrame, features: list):
		_, ax = plt.subplots(ncols=len(features))
		for i, f in enumerate(features):
			ax[i].hist(data[f])
			ax[i].set_title(f)
			ax[i].grid(True)
		plt.show()

	@staticmethod
	def density(data: pd.DataFrame, features: list):
		sns.kdeplot(data=data[features])
		plt.show()

	@staticmethod
	def pair_plot(data: pd.DataFrame, features: list):
		pd.plotting.scatter_matrix(data[features], marker = 'o', s = 20, alpha = 0.5)
		plt.show()

	@staticmethod
	def box_plot(data: pd.DataFrame, features: list):
		sns.boxplot(data=data[features])
		plt.show()
