from datetime import datetime
from datetime import date

def sibling_nos(sibs):
	if len(sibs)>16:
		sibs.append('MoreThan16')
	return len(sibs)

def convert_2date(date1): 
    return datetime.strptime(date1, '%d %b %Y') 

def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
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
