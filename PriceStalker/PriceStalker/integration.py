#module to read/write data

#imports
import pandas as pd


#reads a csv file into and returns a pandas dataframe
def read_csv(path):

    data_dtypes = {'email': str, 'url': str, 'price_filter': float}

    df_data = pd.read_csv(path, sep=',', dtype=data_dtypes,thousands=',')

    #TODO Error checking

    return df_data


