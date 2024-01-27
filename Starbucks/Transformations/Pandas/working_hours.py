# -*- coding: utf-8 -*-
"""Working_Hours.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lz9_-BKFCrREqeK1aDa5z1yIA8cW_q9d
"""

ofrom google.colab import drive

drive.mount('_content_drive')

import pandas as pd

data=pd.read_json('/content/_content_drive/MyDrive/Starbucks /Starbucks/locations.json')

data.head()

data.drop(['city','name','country','longitude','latitude'], axis=1, inplace=True)

data.head()

for index, row in data.iterrows():data.at[index, 'storeId'] = 'S' + str(1000 + index)

data.head()

data = data.dropna()

data.head()

df_normalized = pd.json_normalize(data['storeHours'])

df_result = pd.concat([data[['storeId']], df_normalized], axis=1)

df_result.head()

def calculate_working_hours(time_range):
    if pd.notna(time_range) and ' to ' in time_range:
        start, end = time_range.split(' to ')
        start_time = pd.to_datetime(start.replace(' AM', '').replace(' PM', ''), format='%I:%M')
        end_time = pd.to_datetime(end.replace(' AM', '').replace(' PM', ''), format='%I:%M')
        end_time += pd.Timedelta(hours=12)
        return (end_time - start_time).seconds / 3600
    else:
        return 0

for day in df_result.columns[1:]:
    df_result[day] = df_result[day].apply(calculate_working_hours)

df_result.head()

df_result.to_json('Working_Hours.json', orient='records', lines=True)

df_result = df_result.loc[~(df_result == 0).any(axis=1)]

df_result.to_json('working_hours.json', orient='records', lines=True)

df
