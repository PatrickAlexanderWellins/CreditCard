#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:08:21 2017

@author: patrickwellins
"""

import numpy as np

def get_all_times(df):

    # initialize a list for the times converted into
    # hours to go in
    
    times1 = []
    for time in df['Time']:
        # // 3600 converts seconds into hours with
        # no remainder
        
        times1.append(time // 3600)
     
    # initialize three lists
    # one for all the times, one for day 1, one for day 2
    all_times = []
    times_day2_ = []
    times_day1_ = []
    
    for time in times1:
        if time < 24:
            times_day1_.append(time)
        else:
            # subtract 24 from day 2 times to restart
            # the clock, modularize
            times_day2_.append(time - 24)
            
    for time in times_day2_:
        all_times.append(time)
        
    for time in times_day1_:
        all_times.append(time)
        # return a list of all of the hours tied to the
        # transactions
        
        return(all_times)
        


def get_class0_times(df):
    
# Make a list of all the times that a legitimate transaction occured
# The objective is to convert the seconds into a hour in the range 0 - 23
# This is done by seconds // 3600, any hours between 24 and
    
    
    times = []
    for time in df[df['Class'] == 0]['Time']:
        times.append(time // 3600)
     
    all_times = []
    times_day2 = []
    times_day1 = []
    
    for time in times:
        if time < 24:
            times_day1.append(time)
        else:
            times_day2.append(time - 24)
            
    for time in times_day2:
        all_times.append(time)
    for time in times_day1:
        all_times.append(time)
            
            

            
    # Making a dictionary for legitimate charges the Hour is the key and the value
    # is the frequency of charges at that hour
    
    l = {}
    for t in times_day2:
        if t not in l:
            l[t] = 1
        else:
            l[t] += 1
            
    for t in times_day1:
        if t not in l:
            l[t] = 1
        else:
            l[t] += 1
            
    # Create probabilites for each hour
        
    for key in l:
        l[key] = l[key] / len(times)
        
    
    # Create a list of hours and the corresponding probabilities for visualization
    
    hoursl = []
    frequenciesl = []
    
    for i in range(24):
        hoursl.append(i)
        frequenciesl.append(l[i])
        
    return(hoursl, frequenciesl)

def get_class1_times(df):

# Make a list of all the times that a legitimate transaction occured
# The objective is to convert the seconds into a hour in the range 0 - 23
# This is done by seconds // 3600, any hours between 24 and
    

            
    # Make a list of all the times that a fraudulent transaction occured
    
    timesf = []
    for time in df[df['Class'] == 1]['Time']:
        timesf.append(time // 3600)
       
    times_day2f = []
    times_day1f = []
    
    for time in timesf:
        if time < 24:
            times_day1f.append(time)
        else:
            times_day2f.append(time - 24)
            
            
    # Making a dictionary for fraudulent charges the Hour is the key and the value
    # is the frequency of charges at that hour
    
    tf = {}
    for t in times_day2f:
        if t not in tf:
            tf[t] = 1
        else:
            tf[t] += 1
            
    for t in times_day1f:
        if t not in tf:
            tf[t] = 1
        else:
            tf[t] += 1
    

    # Create probabilites for each hour
    
    for key in tf:
        tf[key] = tf[key] / 492
        

    # Create a list of hours and the corresponding probabilities for visualization
    
    hours = []
    frequencies = []
    
    for i in range(24):
        hours.append(i)
        frequencies.append(tf[i])
        
        
    return(hours, frequencies)

def benford_f(df):
    
# This function returns the distribution of
# digits 1 - 9 of the 'Amount' variable for
# fraudulent charges
    
    fraudsd = {}
    legitimate = {}
    for i in range(len(df)):
        if df['Class'][i] == 1 and str(df['Amount'][i])[0] != '0':
            if str(df['Amount'][i])[0] not in fraudsd:
                fraudsd[str(df['Amount'][i])[0]] = []
                fraudsd[str(df['Amount'][i])[0]].append(1)
            else:
                fraudsd[str(df['Amount'][i])[0]].append(1)
                
        if df['Class'][i] == 0 and str(df['Amount'][i])[0] != '0':
            if str(df['Amount'][i])[0] not in legitimate:
                legitimate[str(df['Amount'][i])[0]] = []
                legitimate[str(df['Amount'][i])[0]].append(1)
            else:
                legitimate[str(df['Amount'][i])[0]].append(1)
                

    Nfrauds = 0
    Nlegit = 0
    for key in fraudsd:
        Nfrauds += len(fraudsd[key])
        
    for key in legitimate:
        Nlegit += len(legitimate[key])
        
    digit_f = []
    digit_g = []    
        
    for i in range(1,10):
        digit_f.append(np.sum(fraudsd[str(i)])/ Nfrauds)
        
    return(digit_f)
        

def benford_g(df):
    
# This function returns the distribution of
# digits 1 - 9 of the 'Amount' variable for
# genuine charges

    fraudsd = {}
    legitimate = {}
    for i in range(len(df)):
        if df['Class'][i] == 1 and str(df['Amount'][i])[0] != '0':
            if str(df['Amount'][i])[0] not in fraudsd:
                fraudsd[str(df['Amount'][i])[0]] = []
                fraudsd[str(df['Amount'][i])[0]].append(1)
            else:
                fraudsd[str(df['Amount'][i])[0]].append(1)
                
        if df['Class'][i] == 0 and str(df['Amount'][i])[0] != '0':
            if str(df['Amount'][i])[0] not in legitimate:
                legitimate[str(df['Amount'][i])[0]] = []
                legitimate[str(df['Amount'][i])[0]].append(1)
            else:
                legitimate[str(df['Amount'][i])[0]].append(1)
                

    Nfrauds = 0
    Nlegit = 0
    for key in fraudsd:
        Nfrauds += len(fraudsd[key])
        
    for key in legitimate:
        Nlegit += len(legitimate[key])
        
    digit_f = []
    digit_g = []    
        
    for i in range(1,10):
        digit_g.append(np.sum(legitimate[str(i)])/ Nlegit)
        
    return(digit_g)
        
