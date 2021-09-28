import pandas as pd
import numpy as np
df=pd.read_excel("Random/Exer1.xls")

bins = np.arange(0,4000,250)

df=df[df["Spcork"]==1]

df=df.groupby(pd.cut(df['Monetary'], bins=bins)).size().reset_index(name='count')
print (df)

