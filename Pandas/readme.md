import numpy as np

import pandas as pd

## Creating dataframes, adding and dropping columns

df = pd.DataFrame(np.arange(1,10).reshape(3,3),['A','B','C'],['w','x','y'])

df.columns = ['W','X','Y'] # change column names

df['Z']=df['X']+df['Y'] # new column with values X+Y

df['XX']=df.apply(lambda row: row['X']*2, axis=1) # new column with values twice of column X

df['YY']=1 # new column of ones
df.insert(2, column='D', value=100) # new column of '100's called 'D' at position 2 (3rd column)
df.drop('B',axis=0, inplace=True) # drop row
df.drop('Z',axis=1) # drop column
Z = df.pop('Z') # drop column and store series to a variable

#### selecting from dataframes

# select columns

df.X # column X (does not work when column name has spaces)
df['X'] # column X
df[['X','Y']] # columns X and Y

# select rows using loc and iloc
# can also use ix, but it's slightly tricky to use: https://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation
# ix is useful for mixing usage of loc and iloc (use both labels and positions at the same time)
# returns a series if single row selected

df.loc['A'] # row A
df.loc['A':] # row A onwards
df.loc[:'X'] # until row X (inclusive!)
df.loc['A','X'] # row A, column X
df.loc[['A','doesnotexist']] # return row with NaN for doesnotexist, check if exists via "doesnotexist" in df.index
df.loc[['A','C'],['X','Y']] # rows A and C, columns X and Y

df.iloc[0] # row at position 0
df.iloc[:,0:3] # column from position 0 to before 3
df.iloc[[0,1],[0,1]] # rows 0 and 1, and columns 0 and 1

#### broadcasting operations

df['X'].add(5) # == df['X'] + 5
df['X'].sub(5) # == df['X'] - 5 == df['X'].subtract(5)
df['X'].mul(5) # == df['X'] * 5 == df['X'].multiply(5)
df['X'].div(5) # == df['X'] / 5 == df['X'].divide(5)

#### basic attributes and methods

# general data exploration
df.info()  # type, index, columns, dtypes, memory usage - printed automatically
df.head()
df.tail()
df.sample(n=2) # return 2 random rows
df.sample(frac=.25) # return 25% random rows
df.nlargest(n=2, columns='X') # returns 2 rows for largest X
df.nsmallest(n=2, columns='X') # returns 2 rows for smallest X
df.index # RangeIndex
df.columns # nparray of column names
df.axes # index and columns
df.values # nparray of nparrays
df.dtypes # series
df.shape # tuple
df.get_dtype_counts() # count number of columns for each datatype
df.sum() # sums summable columns into a series (where column names become the index)
df.sum(axis = "columns")

# methods for columns
df.sort_values(by=['X','Y'], ascending=[False,True]) # sort df by column X (descending) then Y (ascending)
df['X'].isnull() # series of booleans
df['X'].rank() # rank values in column X in ascending order
df['X'].unique() # nparray: unique values from column X
df['X'].nunique() # number of unique values from column X, does not include null by default!
df['X'].value_counts() # returns count of each value from column X
df.drop_duplicates(subset = ['X'], keep ="first") # keep only first instance of X values

# index-related
df.set_index('X') # sets column X as the index
df.set_index('Y') # sets column Y as the index, removes column X!
df.reset_index() # resets index (removes current index, resets dataframe, inserts new index starting from 0)
df.sort_index() # important for optimization

# parse columns
df.astype(int) # convert to int
df['X'].astype("category") # convert to category (important for optimization)
pd.to_datetime(df['X']) # convert to date (important for optimization)

# rename columns
df.rename(columns = {'X': 'A', 'Y': 'B'}, inplace=True)
df.columns = ['X', 'Y', 'Z', 'XX', 'YY', 'ZZ']

#### selecting with conditional operators

# create mask, which is a series of booleans
mask1 = df['X'] < 5
mask2 = df['Y'].isin([4,5,6])
mask3 = df['Y'].isnull()
mask4 = df['Y'].notnull()
mask5 = df['Y'].between(4,6)
mask6 = df['Y'].duplicated(keep = False) # return True if duplicated
mask7 = ~df['Y'].duplicated(keep = False) # return True if unique

# use mask to select from dataframe
df[mask1] # return rows where X<5
df[mask1][['X','Y']] # return only columns X and Y
df[mask1 & mask2]
df[mask1 | mask2]
df[(mask1 | mask2) & mask3]
df.where(mask1) # return NaN for entire row when condition not met

# alernatively, use query (possibly better performance)
# ensure column names dont have spaces: use df.columns = [col.replace(" ","_") for col in df.columns]
df.query('X < 5') # return rows where X<5
df.query('X in [4,5,6]')
df.query('X not in [4,5,6]')

#### missing values - dropna and fillna

df.dropna() # removes any rows with NaN values (how = "any" by default)
df.dropna(how="all") # removes rows with all NaN values
df.dropna(subset=["X"]) # remove rows where value is NaN in column X
df.dropna(axis=1,thresh=10) # drop all columns containing at least 10 NaN values

df.fillna(0) # replace all NaN values with 0
df['Y'].fillna(0, inplace=True) # replace all NaN values in column 'Y' with 0
df['X'].fillna(value=df['XX'].mean()) # replace NaN on column X with mean of column XX

#### groupby with aggregate function

df.groupby('X').describe()

#### concat

df1 = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['v','w','x','y','z'])
df2 = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['v','w','x','y','z'])
df3 = pd.DataFrame(np.random.randn(5, 5), columns=['a', 'b', 'c', 'd', 'e'], index=['v','w','x','y','z'])
pd.concat([df1,df2,df3]) # concat vertically (match columns)
pd.concat([df1,df2,df3],axis=1) # concat horizontally (match rows)

#### merge (== join)

left = pd.DataFrame([[1,'A'],[1,'B'],[2,'B']], columns=['C1','C2'], index=['I1','I2','I3'])
right = pd.DataFrame([['B','C','D']], columns=['C2','C3','C4'], index=['I1'])
pd.merge(left,right,how='inner',on='C2') # same as inner join in sql (concats horizontally)

#### pivot tables

pivot = {'A': ['foo','foo','foo','bar','bar','bar'],
         'B': ['one','one','two','two','one','one'],
         'C': ['x','y','x','y','x','y'],
         'D': [1,3,2,5,4,1]}
df = pd.DataFrame(pivot)
df.pivot_table(values='D',index=['A','B'],columns=['C'])

#### multi-level index dataframes (ie dataframes within dataframes)

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = pd.MultiIndex.from_tuples(list(zip(outside,inside)))
df = pd.DataFrame(np.arange(1,13).reshape(6,2),hier_index,['A','B'])
df.index.names = ['Groups','Num']
df.loc['G1'].loc[1]['A'] # access elements using multiple loc
df.xs(1,level='Num') # return rows where 'num'=1

#### input output
# df = pd.read_csv('data_2d.csv', header=None) # headers included by default
# df.to_csv('out',index=False)
# df = pd.read_excel('Excel.xlsx',sheetname='Sheet1')
# df.to_excel('out.xlsx',sheet_name='NewSheet')
# data = pd.read_html('somelink') # returns a list
# don't use pandas to read sql (better alternatives available)
