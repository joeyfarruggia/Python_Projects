import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import ttest_ind
import statsmodels.api as sm
import warnings

#Load the dataset
dataset = pd.read_csv("C:\\Users\\Joey\\OneDrive\\Documents\\GitHub\\Python_Projects\\CSV_Assignment\\dataset_1.csv")

#Data Analysis
nuw_rows, num_cols = dataset.shape
print(f"Number of rows: {nuw_rows}")
print(f"Number of columns: {num_cols}")

#Descriptive Statistics
summary_stats = dataset.describe()
print("Summary Statistics:")
print(summary_stats)

#Probability calculation
if len(dataset) > 8:
    prob = norm.cdf(2.5, loc=dataset['Column_1'].mean(), scale=dataset['Column_1'].std())
    print(f"Probability: {prob}")
else:
    print("Not enough data to calculate probability.")

#Hypothesis Testing
warnings.filterwarnings("ignore") # Ignore warnings for small sample size
group_a_data = dataset[dataset['Group'] =='A']['Column_2']
group_b_data = dataset[dataset['Group'] =='B']['Column_2']
if len(group_a_data) >= 8 and len(group_b_data) >=8:
    t_stat, p_value = ttest_ind(group_a_data, group_b_data)
    print(f"T-statistic: {t_stat}, P-value: {p_value}")
else:
    print("Not enough data to perform hypothesis testing.")

#Correlation Analysis
numeric_columns = dataset.select_dtypes(include=[np.number]).columns
corr_matrix = dataset[numeric_columns].corr()
print("Correlation Matrix:")
print(corr_matrix)

#Regression Analysis
if len(dataset) >= 8:
    X = dataset[['Column_1', 'Column_2', 'Feature_1', 'Feature_2']]
    y = dataset['target']
    X = sm.add_constant(X)  # Add a constant term for the intercept
    model = sm.OLS(y, X).fit()
    print(model.summary())
else:
    print("Not enough data to perform regression analysis.")