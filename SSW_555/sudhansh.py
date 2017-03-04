#!/usr/bin/python

### MADE BY SUDHANSH AGGARWAL

from datetime import datetime
from time import strftime
#from RobPratSud_Proj03 import individual

#noreps makes sure there are no repeated IDs
def no_reps(group,id_, flag):
    if flag !=1 and flag !=2:
        return False
    else:
        if id_ in group:
            return True
        return False

#Returns false if the date is invalid or in the future
def valid_date(date_):
    try:
        if date_ == "NA":
            return True
        datetime.strptime(date_, '%d-%b-%Y')
        if datetime.strptime(date_, '%d-%b-%Y') <= datetime.now():
            return True
        else:
            return False
        raise ValueError
        
    except ValueError:
        return False

#Returns false if siblings are married
def sibs_no_marry(hid, wid, cids):
    #Checks each family's hid and wid in all other families' cids. 
    if hid in cids and wid in cids:
        return False
    return True

#Returns true if people marry their cousins.
def cuz_no_marry(h, w):

#Returns true is people marry their nephews or nieces.
def dont_marry_niecenephew():

#Returns true is husband isn't male/Wife isn't female
def gender_roles(gen, flag):
    if flag==1:
        sex='M'
    else:
        sex=='F'
    if gen != sex
        return True

#Returns true if name and DOB combination isn't unique
def unique_name_dob(a,b):
    for i in length(indis):
        for j in (i+1:lenth(indis)):
            if a.dob == b.dob and a.name == b.name:
                return True

