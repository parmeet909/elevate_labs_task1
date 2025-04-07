import pandas as pd
from datetime import datetime
df = pd.read_csv("C:\\Users\\PARMEET KAUR\\Downloads\\marketing_campaign.csv")
print(df.shape)
df.head()
df.info()
df.describe()
df.isnull().sum()

df['Income'].fillna(df['Income'].median(), inplace=True)

df.dropna(subset=['Income'], inplace=True)
df.drop_duplicates()

df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True)

df['Customer_Since_Days'] = (pd.to_datetime('today') - df['Dt_Customer']).dt.days
df['Total_Spend'] = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts', 'MntGoldProds']].sum(axis=1)
df['Customer_Age'] = datetime.now().year - df['Year_Birth']
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
df['Total_Spent'] = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts',
                        'MntSweetProducts','MntGoldProds']].sum(axis=1)
df['Education'] = df['Education'].str.strip().replace({
    '2n Cycle': 'Second Cycle'
})

df['Marital_Status'] = df['Marital_Status'].replace({
    'Alone': 'Single',
    'Absurd': 'Single',
    'YOLO': 'Single',
    'Widow': 'Widowed'
})
# Clean data
print(df[['Year_Birth', 'Education', 'Marital_Status', 'Income', 'Dt_Customer',
          'Customer_Age', 'Total_Children', 'Total_Spent']].head(20))