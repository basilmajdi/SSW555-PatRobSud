#!/usr/bin/python

import unittest
from sudhansh import no_reps
from sudhansh import valid_date
from sudhansh import sibs_no_marry
from sudhansh import gender_roles


# For no rep tests
i=["I0922","I0065","I1994","133262"]
f=["F3600","753F","GD192","BLINK182"]
empty=[]
ii="I0922"
ip="147699"
fi="BLINK182"
fp="TUPAC"

hid="112209"
wid="12345"
cid1=["12345","potato"]
cid2=["12345","112209"]

class TestMyFunctions(unittest.TestCase):
	### TESTS FOR NO REPETITION BEGIN ###
	def test_indi_contains(self):
		self.assertTrue(no_reps(i,ii,1))
	def test_indi_no_contain(self):
		self.assertFalse(no_reps(i,ip,1))
	def test_indi_no_contain_E(self):
		# EMPTY LIST
		self.assertFalse(no_reps(empty,ip,1))
	def test_fam_contains(self):
		self.assertTrue(no_reps(f,fi,2))
	def test_fam_no_contain(self):
		self.assertFalse(no_reps(f,fp,2))
	def test_fam_no_contain_E(self):
		# EMPTY LIST
		self.assertFalse(no_reps(empty,fp,2))
	def test_diff_flag(self):
		self.assertFalse(no_reps(i,"90771",9))
	### TESTS FOR NO REPETITION END ###

	### VALID DATES START ###
	# FORMAT DD-MM-YYYY #
	def test_valid_correct(self):
		self.assertTrue(valid_date("01-JAN-1996"))
	def test_valid_feb(self):
		self.assertTrue(valid_date("29-FEB-2004"))
	def test_invalid_feb(self):
		self.assertFalse(valid_date("31-FEB-1910"))
	def test_invalid_format(self):
		self.assertFalse(valid_date("02-13-2001"))
	def test_future_date(self):
		self.assertFalse(valid_date("02-FEB-2020"))
	def test_invalid_ivalid(self):
		self.assertFalse(valid_date("32-13-1080"))
	def test_alphabet_wtf(self):
		self.assertFalse(valid_date("13p09-2001"))
	def test_date_na(self):
		self.assertTrue(valid_date("NA"))
	#### VALID DATES END ####

	### SIBLINGS DON'T MARRY START ###
	def test_true(self):
		self.assertTrue(sibs_no_marry(hid,wid,cid1))
	def test_false(self):
		self.assertFalse(sibs_no_marry(hid,wid,cid2))
	#### SIBLINGS DON'T MARRY END ####

	### GENDER ROLES START ###
	def test_dad_corr(self):
		self.assertFalse(gender_roles("M", 1))
	def test_mom_corr(self):
		self.assertFalse(gender_roles("F", 0))
	def test_dad_wrong(self):
		self.assertTrue(gender_roles("F", 1))
	def test_mom_wrong(self):
		self.assertTrue(gender_roles("M", 0))
	def test_na_one(self):
		self.assertFalse(gender_roles("NA",1))
	def test_na_zero(self):
		self.assertFalse(gender_roles("NA",0))
	#### GENDER ROLES END ####

def main():
	unittest.main()

if __name__=='__main__':
	main()