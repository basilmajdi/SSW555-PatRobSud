# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:30:17 2017

@author: basilmajdi
"""

from datetime import datetime, timedelta, date


def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d-%b-%Y')  

def date_check(date_big, date_small): 
    # Returns false if date_big > date_small, else true
    if date_big == "NA" or date_small == "NA" or date_big == "ERR" or date_small == "ERR":
        return True
    elif convert_2date(date_big) < convert_2date(date_small):    
        return False
    else:    
        return True  

'''def birth_b4_marg(dob, dom):# this function takes the dates of birth and marriage(if any) and 
                            # returns true if the date of marriage is before date of birth 
    if dom == "NA" or dob == "NA" or dom == "ERR" or dob == "ERR": 
        return True
    elif convert_2date(dom) < convert_2date(dob):    
        return False
    else:    
        return True'''


'''def birth_b4_dth(dob, dod): # this function takes the dates of birth and death(if any) and 
                            # returns true if the date of death is before date of birth    
    if dod == "NA" or dob == "NA" or dod == "ERR" or dob == "ERR": 
        return False
    elif convert_2date(dod) < convert_2date(dob):    
        return True
    else:    
        return False'''

'''def marg_b4_dvors(doe, dom):# this function takes the dates of marriage and divorce (if any) and 
                            # returns false if the date of divorce is before date of marriage
    if doe == "NA" or dom == "NA" or doe == "ERR" or dom == "ERR":
        return True   
    elif convert_2date(doe) < convert_2date(dom):    
        return False
    else:    
        return True'''

'''def marg_b4_dth(dom, dod):
    # this function checks if the date of marriage happened after death. 
    if dom == "NA" or dod == "NA": 
        return True
    elif convert_2date(dod) < convert_2date(dom):    
        return False
    else:    
        return True'''
        
def list_events(date_): # this func checks for dates that happen in the period of 30 days from current 
    if date_ == "NA" or date_ == 'ERR':
        return False
    if convert_2date(date_) < datetime.now() - timedelta(days = 30): 
        return False
    else:
        return True

def upcoming_events(dt1): # checks the difference between two days
    if dt1 == "NA" or dt1 == "ERR": 
        return False
    else:
        dt1 = convert_2date(dt1)
        dt2 = date.today()
        dt3 = date(dt2.year, dt1.month, dt1.day)
        dt4 = dt2 + timedelta(days=30)
        if dt3 >= dt2 and dt3 <= dt4:
            return True
        else:
            return False



        
            
    
