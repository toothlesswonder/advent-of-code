# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:17:26 2018
@author: toothlesswonder
"""

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



''' STEP 1: find guard that is asleep most often '''

# thank you pandas for doing this in *ONE LINE*  :)
guard_sums = df[['guard', 'duration']].groupby(['guard']).sum().reset_index()

# the guard with the most minutes is: 1993
guard = guard_sums.sort_values('duration', ascending=False).iloc[0]['guard']
print('Guard #%s has the most minutes' % (guard))


      
''' STEP 2: find the minute of the day when the guard is asleep most often '''

# create new df with minutes of the day (1440 rows)
df2 = pd.DataFrame(pd.date_range('2018-01-01', '2018-01-02', freq="1min")[:-1].time)
df2.columns = ['time']
df2 = df2.set_index('time')

# create a column for counts
df2['count'] = 0

# iterate through the 24 sleep sessions of guard 1993
for index, row in df[df['guard'] == guard].iterrows():
    datelist = pd.date_range(index, index + row['duration'], freq="1min").time
    df3 = pd.DataFrame(datelist)
    df3.columns = ['time']
    for row in df3['time']:
        df2.at[row, 'count'] = df2.loc[row]['count'] + 1

max_count = df2['count'].max()

print('There are %s possible answers:' % (len(df2.index[df2['count'] == max_count])))

for item in df2.index[df2['count'] == max_count]:
    print(int(guard)*item.minute)


''' Note: the second possible answer was right. Why am I getting two? '''

