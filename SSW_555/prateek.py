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
        return Falsedef father_age(father_dob, child_dob):
    if father_dob-child_dob > 80:
         return False
    else:    
        return True


