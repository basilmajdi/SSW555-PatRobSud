# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:30:17 2017

@author: basilmajdi
"""

from datetime import datetime

        
def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d-%b-%Y')    

def birth_b4_marg(dob, dom):# this function takes the dates of birth and marriage(if any) and 
                            # returns true if the date of marriage is before date of birth 
    if dom == "NA" or dob == "NA" or dom == "ERR" or dob == "ERR": 
        return True
    elif convert_2date(dom) < convert_2date(dob):    
        return False
    else:    
        return True


def birth_b4_dth(dob, dod): # this function takes the dates of birth and death(if any) and 
                            # returns true if the date of death is before date of birth    
    if dod == "NA" or dob == "NA" or dod == "ERR" or dob == "ERR": 
        return False
    elif convert_2date(dod) < convert_2date(dob):    
        return True
    else:    
        return False


''' @ROBERT: COVERED IN SUDHANSH.PY VALID_DATE '''
def dates_b4_today(date_): #this function compares any givin date to today's date. it returns true if the given date 
                            # is after today's date  
    today = datetime.now()
    if convert_2date(date_) >= convert_2date(today):
        return False
    else:    
        return True

def marg_b4_dvors(doe, dom):# this function takes the dates of marriage and divorce (if any) and 
                            # returns false if the date of divorce is before date of marriage
    if doe == "NA" or dom == "NA" or doe == "ERR" or dom == "ERR":
        return True   
    elif convert_2date(doe) < convert_2date(dom):    
        return False
    else:    
        return True

def marg_b4_dth(dom, dod):
    # this function checks if the date of marriage happened after death. 
    if dom == "NA" or dod == "NA": 
        return True
    elif convert_2date(dod) < convert_2date(dom):    
        return False
    else:    
        return True

def date_check(date_big, date_small): 
    if date_big == "NA" or date_small == "NA" or date_big == "ERR" or date_small == "ERR":
        return False
    elif convert_2date(date_big) < convert_2date(date_small):    
        return False
    else:    
        return True
        
    

    