# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


# %%
feedgrains = pd.read_csv('cdc2019-agriculture/FeedGrains.csv')

feedgrains.head()

# %%
feedgrains.describe(include='all')

# %%
feedgrains.info(verbose=True)


# %%
print('SC_Group_Desc : \n', feedgrains['SC_Group_Desc'].unique(), '\n')
print('SC_GroupCommod_Desc: \n', feedgrains['SC_GroupCommod_Desc'].unique(), '\n')
print('SC_GeographyIndented_Desc: \n', feedgrains['SC_GeographyIndented_Desc'].unique(), '\n')
print('SC_Commodity_Desc: \n', feedgrains['SC_Commodity_Desc'].unique(), '\n')
print('SC_Attribute_Desc: \n', feedgrains['SC_Attribute_Desc'].unique(), '\n')
print('SC_Unit_Desc: \n', feedgrains['SC_Unit_Desc'].unique(), '\n')
print('SC_Frequency_Desc: \n', feedgrains['SC_Frequency_Desc'].unique(), '\n')
print('Timeperiod_Desc: \n', feedgrains['Timeperiod_Desc'].unique()), '\n'



# %%
price_annual = feedgrains[(feedgrains['SC_Group_Desc'] == 'Prices') & (feedgrains['SC_Frequency_Desc'] == 'Annual')]


# %%
price_annual_corn = price_annual[feedgrains['SC_GroupCommod_Desc'] == 'Oats']

# %%
X_train, X_test, y_train, y_test = train_test_split(price_annual_corn['Year_ID'].values.reshape(-1, 1), price_annual_corn['Amount'], test_size=0.2, random_state=101)
corn_linear = linear_model.LinearRegression()
corn_linear.fit(X_train, y_train)


# %%
y_predict = corn_linear.predict(X_test)


# %%
y_predict.shape


# %%
plt.scatter(price_annual_corn['Year_ID'], price_annual_corn['Amount'])
plt.title("Annual Price and Year (1860 - 2020)")
plt.xlabel("Year")
plt.ylabel("Annual Price")
plt.show()

# %%
