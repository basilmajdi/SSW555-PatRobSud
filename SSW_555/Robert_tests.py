#!/usr/bin/python

import unittest
from Rob_funcs import upcoming_events

'''from Rob_funcs import birth_b4_marg  # birth_b4_marg(dob, dom)
from Rob_funcs import birth_b4_dth   # birth_b4_dth(dob, dod)
from Rob_funcs import marg_b4_dvors  # marg_b4_dvors(doe, dom)

dob1="1-JAN-2011"
dob2="17-MAR-1997"

dom1="12-DEC-2012"
dom2="10-JUL-2001"

dod1="NA" #Always false
dod2="31-OCT-2009"

doe1="19-AUG-1985"
doe2="ERR" #Always false

class TestMyFunctions(unittest.TestCase):
	### BIRTH BEFORE MARRIAGE START ###
	def test_bb4m_t(self):
		self.assertFalse(birth_b4_marg(dob1, dom2)) # DOB < DOM, hence false
	def test_bb4m_f(self):
		self.assertTrue(birth_b4_marg(dob2, dom2)) # DOB > DOM, hence true
	#### BIRTH BEFORE MARRIAGE END ####

	### BIRTH BEFORE DEATH START ###
	def test_bb4d_t(self):
		self.assertFalse(birth_b4_dth(dob1, dod1)) # DOD=NA, hence false
	def test_bb4d_f(self):
		self.assertTrue(birth_b4_dth(dob1, dod2)) # DOB > DOD, hence true
	#### BIRTH BEFORE DEATH END ####

	### MARRIAGE BEFORE DIVORCE START ###
	def test_mb4d_t(self):
		self.assertFalse(marg_b4_dvors(doe1, dom1)) #DOE < DOM, hence true
	def test_mb4d_f(self):
		self.assertTrue(marg_b4_dvors(doe2, dom2)) # DOE2=ERR, hence false
	#### MARRIAGE BEFORE DIVORCE END ####'''

 
date_1 = "30-APR-2017"
date_2 = '13-OCT-2017'
date_3 = '15-APR-2017'
 
class TestMyFunctions(unittest.TestCase): 
    def test_upcoming(self): 
        self.assertTrue(upcoming_events(date_1))
    def test_upcoming2(self):
        self.assertTrue(upcoming_events(date_2))
    def test_upcoming3(self):
        self.assertTrue(upcoming_events(date_3))

def main():
	unittest.main()

if __name__=='__main__':
	main()