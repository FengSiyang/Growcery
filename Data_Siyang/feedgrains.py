# %%
import numpy as np
import pandas as pd
import matplotlib


# %%
feedgrains = pd.read_csv('cdc2019-agriculture/FeedGrains.csv')

feedgrains.head()

# %%
feedgrains.describe(include='all')

# %%
feedgrains.info(verbose=True)

# %%
feedgrains.columns

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
