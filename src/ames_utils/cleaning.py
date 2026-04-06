import pandas as pd

def clean_data(df: pd.DataFrame):
    """ Handles and imputes missing values in the dataset.

    Args:
        df (pd.DataFrame): Clean DataFrame with no missing values.
    """

    df_clean = df.copy()
    
    #1 Columns related to extra features such as Pool, Alley, Fireplace
    feature_cols = ['Pool QC', 'Misc Feature', 'Alley', 'Fence', 'Fireplace Qu']

    #for colname in feature_cols:
       
    df_clean[feature_cols] = df_clean[feature_cols].fillna('None')

    #2 Garage cols
    df_clean.loc[(~df_clean['Garage Type'].isna()) & (df_clean['Garage Qual'].isna()), ['Garage Type', 'Garage Cars', 'Garage Area']] = ['None', 0, 0]

    garage_cols = ['Garage Qual','Garage Cond','Garage Finish','Garage Type']

    df_clean[garage_cols] = df_clean[garage_cols].fillna('None')
    df_clean['Garage Yr Blt'] = df_clean['Garage Yr Blt'].fillna(0)

    # 3 Basement cols
    bsmt_categorical = ['Bsmt Exposure','BsmtFin Type 2','Bsmt Qual','Bsmt Cond','BsmtFin Type 1']
    bsmt_numeric = ['Bsmt Full Bath','Bsmt Half Bath','Total Bsmt SF','BsmtFin SF 1','BsmtFin SF 2','Bsmt Unf SF']

    df_clean[bsmt_numeric] = df_clean[bsmt_numeric].fillna(0)
    
    # fixing inconsistencies
    df_clean.loc[df_clean['BsmtFin Type 2'].isna() & df_clean['Bsmt Cond'].notna(), 'BsmtFin Type 2'] = 'Unf'

    df_clean.loc[df_clean['Bsmt Exposure'].isna() & df_clean['Bsmt Cond'].notna(), 'Bsmt Exposure'] = 'No' 

    df_clean[bsmt_categorical] = df_clean[bsmt_categorical].fillna('None')

    # 4 Masonery Veneer
    df_clean['Mas Vnr Type'] = df_clean['Mas Vnr Type'].fillna('None')
    df_clean['Mas Vnr Area'] = df_clean['Mas Vnr Area'].fillna(0)

    # 5 Electrical
    df_clean['Electrical'] = df_clean['Electrical'].fillna(df['Electrical'].mode()[0])

    # 6 Lot Frontage
    df_clean['Lot Frontage'] = df_clean['Lot Frontage'].fillna(0)

    df_clean.columns = df_clean.columns.str.replace(' ','')

    return df_clean

def print_missing(df: pd.DataFrame) -> None:
    """ Lists number of missing values in each column of the DataFrame.

    Args:
        df (pd.DataFrame): Dataset to inspect.
    """
    missing = df.isna().sum().sort_values(ascending=False)
    print(missing[missing > 0])