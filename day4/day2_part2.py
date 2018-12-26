#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 22:52:37 2018
@author: toothlesswonder
"""



'''NOTE: lines 14-75 are the same as part 1; jump to line 80 for what's new '''



# imports
import pandas as pd
import numpy as np



''' INGEST '''

# create dataframe with event data
df = pd.read_csv('advent/puzzle_input.txt', sep='] ', engine="python", header=None)
df.columns = ['date', 'event']



''' CLEAN '''

# being lazy
df['date'] = [row.replace("[1518","2018") for row in df.date]

''' Note: parsing the date gets an out of bounds datetime error! 32 bit integer 
can't handle year 1518.  I should come back and learn to do a period index:
http://pandas-docs.github.io/pandas-docs-travis/timeseries.html#representing-out-of-bounds-spans
'''

# parse times 
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M')

# code to set datetime as index and then sort
df = df.set_index('date').sort_index()

#this is just to make my data look cleaner; not really needed 
def parse_status(event_string):
    if event_string[0] == 'G':
        status = 'start'
    elif event_string[0] == 'f':
        status= "asleep"
    elif event_string[0] == 'w':
        status = "awake"
    else:
        print('unexpected status:', event_string)
    return status

# create clean status
df['status'] = [parse_status(row) for row in df.event]

# get numeric guard ID as a column; fill non-guard columns with NaN (for now)
df['guard'] = [row.split()[1][1:] if "Guard" in row else np.NaN for row in df.event]

# fill guard ID for following events (that have NaN)
df = df.fillna(method='ffill')

# calculate durations
# note: calculating for all rows, but these only make sense for "asleep" rows
df['shift'] = df.index
df['shift'] = df['shift'].shift(-1)
df['duration'] = df['shift'] - df.index

# drop everything but the asleep rows (which now contain all needed info)
df = df[df['status'] == 'asleep'][['status', 'guard', 'duration']]

# mmm, so fresh and clean!
df.head(25)




''' this is what's different for part 2 '''


def generate_minute_dataframe():
    # create new df with minutes of the day (1440 rows)
    df2 = pd.DataFrame(pd.date_range('2018-01-01', '2018-01-02', freq="1min")[:-1].time)
    df2.columns = ['time']
    df2 = df2.set_index('time')
    df2['count'] = 0
    return df2


# get list of guards
guards = df['guard'].unique()

df3 = pd.DataFrame(guards)
df3.columns = ['guard']

max_counts = []

for guard in guards:
    df2 = generate_minute_dataframe()
    for index, row in df[df['guard'] == guard].iterrows():
        datelist = pd.date_range(index, index + row['duration'], freq="1min").time
        df3 = pd.DataFrame(datelist)
        df3.columns = ['time']
        for row in df3['time']:
            df2.at[row, 'count'] = df2.loc[row]['count'] + 1
    max_count = df2['count'].max()
    df2 = df2.sort_values('count', ascending=False)
    for index, row in df2[df2['count'] == max_count].iterrows():
        max_counts.append((guard,index,row['count']))

df4 = pd.DataFrame.from_dict(max_counts)  
df4.columns = ['guard','minute','count']    


# get max across all guards
max_count = df4['count'].max()

print('There are %s possible answers:' % (len(df4.index[df4['count'] == max_count])))

print(df4[df4['count'] == max_count])
