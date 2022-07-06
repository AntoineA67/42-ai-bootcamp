import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Komparator:
	def __init__(self, df: pd.DataFrame) -> None:
		self.df = df

	def compare_box_plots(self, categorical_var, numerical_var):
		if type(numerical_var) != list:
			_, ax = plt.subplots()
			gb = self.df.groupby(categorical_var)[numerical_var]

			# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
			d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
			sns.boxplot(data=d, ax=ax)

			# Add var name as ylabel
			ax.set_ylabel(numerical_var)
		else:
			_, ax = plt.subplots(ncols=len(numerical_var))
			for i, var in enumerate(numerical_var):

				# Group by categorical variable and keep only numerical variable
				gb = self.df.groupby(categorical_var)[var]

				# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
				d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
				sns.boxplot(data=d, ax=ax[i])

				# Add numerical var name as ylabel
				ax[i].set_ylabel(var)

		plt.show()

	def density(self, categorical_var, numerical_var):
		
		if type(numerical_var) != list:
			_, ax = plt.subplots()
			# Group by categorical variable and keep only numerical variable
			gb = self.df.groupby(categorical_var)[numerical_var]

			# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
			d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
			sns.kdeplot(data=d, ax=ax)

			# Add numerical var name as ylabel
			ax.set_xlabel(numerical_var)
		else:
			_, ax = plt.subplots(ncols=len(numerical_var))
			for i, var in enumerate(numerical_var):

				# Group by categorical variable and keep only numerical variable
				gb = self.df.groupby(categorical_var)[var]

				# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
				d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
				sns.kdeplot(data=d, ax=ax[i])

				# Add var name as ylabel
				ax[i].set_xlabel(var)

		plt.show()

	def compare_histograms(self, categorical_var, numerical_var):
		if type(numerical_var) != list:
			_, ax = plt.subplots()
			gb = self.df.groupby(categorical_var)[numerical_var]

			# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
			d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
			# sns.boxplot(data=d, ax=ax[i])
			ax.hist(d)

			# Add numerical_var name as ylabel
			ax.set_xlabel(numerical_var)
			ax.legend(gb.groups)
		else:
			_, ax = plt.subplots(ncols=len(numerical_var))

			for i, var in enumerate(numerical_var):

				# Group by categorical variable and keep only numerical variable
				gb = self.df.groupby(categorical_var)[var]

				# Transform into a dictionary of key 'column name' and value 'column values' for each categories of gb
				d = pd.DataFrame(data={x: gb.get_group(x) for x in gb.groups})
				# sns.boxplot(data=d, ax=ax[i])
				ax[i].hist(d)

				# Add var name as ylabel
				ax[i].set_xlabel(var)
				ax[i].legend(gb.groups)

		plt.show()