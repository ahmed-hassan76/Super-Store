import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv') 

df = df.drop('Postal Code', axis=1)

print(df.columns)
print(df.describe(include='all'))
print(df.groupby('Category')['Sales'].sum())
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by Category')
plt.show()

sns.boxplot(x='Region', y='Sales', data=df)
plt.title('Sales Distribution by Region')
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

sns.lineplot(x='Month', y='Sales', data=monthly_sales)
plt.xticks(rotation=45)
plt.title('Monthly Sales Trend')
plt.show()
