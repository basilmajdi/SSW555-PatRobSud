#!/usr/bin/python

import unittest
from prateek import sibling_nos

s1=[] # EMPTY LIST
s2=["one","two","three","four","five","six","seven","eight","nine"] # Under 16
s3=["one","two","three","four","five","six","seven","eight","nine","onety","twoty","threety","abcd","fourty","fivety","sixty","seventy","eightty","ninety"] # Over 16

class TestMyFunctions(unittest.TestCase):
	### TESTS CASES FOR NO REPETITION BEGIN ###
	def test_empty(self):
		self.assertLess((sibling_nos(s1)),16)
	def test_less(self):
		self.assertLess((sibling_nos(s2)),16)
	def test_more(self):
		self.assertGreater((sibling_nos(s3)),16)
	### TESTS FOR NO REPETITION END ###

def main():
	unittest.main()

if __name__=='__main__':
	main()
