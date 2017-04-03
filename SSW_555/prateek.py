from datetime import datetime
from datetime import date

from Rob_funcs import convert_2date

def sibling_nos(sibs):
	return len(sibs)

def calculate_age(dob,dod):
    if dob == "NA" or dob == "ERR":
        return "NA"
    if dod == "NA" or dod == "ERR":
        today = date.today()
    else:
        today = convert_2date(dod)
    dob2=convert_2date(dob)
    return today.year - dob2.year - ((today.month, today.day) <= (dob2.month, dob2.day))
    
def check_age(child,parent,f):
    if child=="NA" or parent=="NA":
        return True
    if f==0:
        age=80
    else:
        age=60
    if age>parent-child:
        return True
    else:
        return False

def check_marriage_before14(dob,dom):
    if dob == "NA" or dob == "ERR" or dom == "NA" or dom == "ERR":
        return False
    elif convert_2date(dom) - convert_2date(dob) < 14:    
        return False
    else:    
        return True
