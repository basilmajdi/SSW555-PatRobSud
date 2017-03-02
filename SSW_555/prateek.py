from datetime import datetime
from datetime import date

from Rob_funcs import convert_2date


def sibling_nos(sibs):
	# if len(sibs)>16:
	# 	sibs.append('MoreThan16')
	return len(sibs)

# def convert_2date(date1): 
#     return datetime.strptime(date1, '%d %b %Y') 

def calculate_age(dob,dod):
    if dob == "NA" or dob == "ERR":
        return "NA"
    if dod == "NA" or dod == "ERR":
        today = date.today()
    else:
        today = convert_2date(dod)
    dob2=convert_2date(dob)
    return today.year - dob2.year - ((today.month, today.day) <= (dob2.month, dob2.day))
    
def father_age(father_dob, child_dob):
    if father_dob-child_dob > 80:
         return False
    else:    
        return True

def mother_age(mother_dob, child_dob):
    if mother_dob-child_dob > 60:
         return False
    else:    
        return True
