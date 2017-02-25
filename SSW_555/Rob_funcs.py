# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:30:17 2017

@author: basilmajdi
"""

from datetime import datetime
from datetime import date
        
def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d %b %Y')    

def birth_b4_marg(dob, dom):# this function takes the dates of birth and marriage(if any) and 
                            # returns false if the date of marriage is before date of birth 
    
    

    
    if dom == "None": 
        return True
    
    elif convert_2date(dom) <= convert_2date(dob):    
        return False
    else:    
        return True


def birth_b4_dth(dob, dod): # this function takes the dates of birth and death(if any) and 
                            # returns false if the date of death is before date of birth 
    

    
    if dod == "None": 
        return True
    
    elif convert_2date(dod) < convert_2date(dob):    
        return False
    else:    
        return True

def dates_b4_today(dates): #this function compares any givin date to today's date. it returns false if the given date 
                            # is after today's date  
    
    today = date.today()
    
    
    if convert_2date(dates) >= convert_2date(today):
        return False
    else:    
        return True

def marg_b4_dvors(doe, dom):# this function takes the dates of marriage and devorce (if any) and 
                            # returns false if the date of devorce is before date of marriage
    

    if doe == "None": 
        return True
    
    elif convert_2date(doe) < convert_2date(dom):    
        return False
    else:    
        return True
        