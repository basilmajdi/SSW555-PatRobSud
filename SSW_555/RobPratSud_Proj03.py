#!/usr/bin/python

'''
Parser for Robert Basil Majdi, Prateek Tyagi and Sudhansh Aggarwal
CS-555/SSW-555 
'''

import os
import sys
import codecs
import prettytable
from datetime import datetime 
from datetime import date
import datetime

from Rob_funcs import date_check #this function takes two parameters, bigger date and smaller date

from sudhansh import no_reps
from sudhansh import sibs_no_marry
from sudhansh import valid_date
from sudhansh import gender_roles

from prateek import sibling_nos
from prateek import calculate_age
from prateek import check_age

def getdate(d,m,y):
    date = d+'-'+m+'-'+y
    return date

def refresh():
    global iden, name, sex, dob, dod, famc, fams, flag, hid, wid, dom, doe, cid
    iden = name = sex = "NA"
    dob = dod = famc = "NA"
    fams = hid = wid = "NA"
    dom = doe = "NA"
    cid = []
    flag = 0 # 1 for indi, 2 for family in level 0 lines.

class individual:

    def __init__(self):
        self.pid="NA"
        self.name="NA"
        self.sex="NA"
        self.dob="NA"
        self.dod="NA"
        self.famc="NA"
        self.fams="NA"
        self.age=0
        self.err=[]

    def info(self, pid, name, sex, dob, dod, famc, fams):
        self.pid=pid
        self.name=name
        self.sex=sex
        self.dob=dob
        self.dod=dod
        self.famc=famc
        self.fams=fams
        #Checking correctness of dates
        if not valid_date(dod):
            # checks if date format is correct and that date is not in future 
            self.err.append("US42-DOD")
            self.dod="ERR"
        if not valid_date(dob):
            # checks if date format is correct and that date is not in future
            self.err.append("US42-DOB")
            self.dob="ERR"
        if not date_check(self.dod, self.dob):
            # checks for birth before death 
            self.err.append('US03')   

        # Calculate Age
        self.age=calculate_age(self.dob,self.dod)
           
    def showinfo(self):
        print('{} : {}'.format("ID",self.pid))
        print('{} : {}'.format("NAME",self.name))
        print('{} : {}'.format("SEX",self.sex))
        print('{} : {}'.format("D.O.B",self.dob))
        print('{} : {}'.format("D.O.D",self.dod))
        print('{} : {}'.format("FAMC",self.famc))
        print('{} : {}'.format("FAMS",self.fams))

    def update_table(self):
        x.add_row([self.pid,self.name,self.sex,self.dob,self.dod,self.age,self.famc,self.fams,self.err])

class family:
    def __init__(self):
        self.fid="NA" 
        self.hid="NA"
        self.wid="NA"
        self.dom="NA"
        self.doe="NA"
        self.cid=[]
        # self.sib_no=0
        self.err=[]
    
    def info(self, fid, hid, wid, dom, doe, cid):
        self.fid=fid
        self.hid=hid
        self.wid=wid
        self.dom=dom
        self.doe=doe
        self.cid=cid
        #Checking correctness of dates
        # self.sib_no=sibling_nos(cid)
        if sibling_nos(self.cid)>=16:
            # checks that there are no more than 15 siblings 
            self.err.append("US15")
        if not valid_date(dom):
            # checks if date format is correct and that date is not in future for date of marriage 
            self.err.append("US42-DOM")
            self.dom="ERR"
        if not valid_date(doe):
            # checks if date format is correct and that date is not in future for date of divorce
            self.err.append("US42-DOE")
            self.doe="ERR"
        ## Check if couple is married before getting a divorce
        if not date_check(self.doe, self.dom):
            #checks for divorce before marriage dates 
            self.err.append('US04')
        h=self.hid
        w=self.wid

        #Checking gender roles
        print("BEFORE CHECKING GENDER ROLES for husb")
        print(individuals[indi.index(h)].sex)
        if gender_roles(individuals[indi.index(h)].sex,1):
            self.err.append('US21-Husband')
        print("BEFORE CHECKING GENDER ROLES for wife")
        print(individuals[indi.index(w)].sex)
        if gender_roles(individuals[indi.index(w)].sex,0):
            self.err.append('US21-Wife')
        print("AFTER CHECKING GENDER ROLES")
        
        ## Check if husband is born before getting married
        if not date_check(self.dom, individuals[indi.index(h)].dob):
            # checks for marriage before birth dates for husband 
            self.err.append('US02-Husb')
        ## Check if wife is born before getting married
        if not date_check(self.dom, individuals[indi.index(w)].dob):
            # checks for marriage before birth dates for wife
            self.err.append('US02-Wife')
        if not date_check(individuals[indi.index(h)].dod, self.dom):
            # checks for marriage before death dates for husband
            self.err.append('US05-Husb')
        if not date_check(individuals[indi.index(w)].dod, self.dom):
            # checks for marriage before death dates for wife
            self.err.append('US05-Wife')
        if not date_check(individuals[indi.index(h)].dod, self.doe):
            # checks for divorce before death dates for husband
            self.err.append('US06-Husb')
        if not date_check(individuals[indi.index(w)].dod, self.doe):
            # checks for divorce before death dates for wife
            self.err.append('US06-Wife')
        #For each child in that family
        for i in self.cid: 
            if not date_check(individuals[indi.index(i)].dob, self.dom):
                # checks for marriage of parents before birth dates  
                self.err.append('US08')
            if not date_check(individuals[indi.index(i)].dob, individuals[indi.index(h)].dod):
                # checks for death of parents before birth dates for father 
                self.err.append('US09-Deceased Father')
            if not date_check(individuals[indi.index(i)].dob, individuals[indi.index(w)].dod):
                # checks for death of parents before birth dates for mother 
                self.err.append('US09-Deceased Mother')
            # check father/mother are not too old compared to the child
            if not check_age(individuals[indi.index(i)].age,individuals[indi.index(h)].age,0):
                self.err.append("US12-Father")
            if not check_age(individuals[indi.index(i)].age,individuals[indi.index(w)].age,1):
                self.err.append("US12-Mother")
        
    def cout(self):
        print('{} : {}'.format("ID",self.fid))
        print('{} : {}'.format("HUSB",self.hid))
        print('{} : {}'.format("WIFE",self.wid))
        print('{} : {}'.format("D.O.M",self.dom))
        print('{} : {}'.format("D.O.E",self.doe))
        print('{} : {}'.format("CID",self.cid))
        print('{} : {}'.format("No. of Siblings",self.sib_no))

    def update_table(self):
        y.add_row([self.fid,self.hid,self.wid,self.dom,self.doe,self.cid,self.err])


### VALID TAGS IN gedcom FILES ###
tags = [ "INDI" , "FAM" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , 
"DATE" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "DIV" ]

#filename = open ( "smith_tree1.ged" )
#filename="/Users/sudhansh/Desktop/CS-555/test1.ged" #For testing purposes
#filename="/Users/sudhansh/git/SSW_555/smith_tree1.ged" #For testing purposes
#filename="/Users/sudhansh/Desktop/CS-555/Proj01_SudhanshAggarwal_CS555.ged"
filename="/Users/sudhansh/Desktop/CS-555/Proj01_SudhanshAggarwal_CS555_2.ged"

### CHECKING IF GEDCOM IS ENTERED, HELP TAKEN FORM AKSHAY SUNDERWANI ###
path = os.getcwd ( )  # method to fetch working directory path.
basefilename = os.path.basename ( filename )
basefilename2 = os.path.splitext ( basefilename )
if basefilename2[ -1 ] != '.ged':
    print ( "Gedcom file not entered" )
    exit ( )

indi=[] #List of all individual IDs
famillia=[] #List of all family IDs

c_ind = c_fam = 0 # for counting the total no.s of individuals and families resp
c_ind1 = c_fam1 = 0 # for keeping track of indi/fams
try:
    #Counting the number of people/families
    with open (filename) as file:
        for line in file:
            words=line.split()
            if words[0]=='0':
                if words[-1] == "INDI":
                    # to get total number of individuals in the GEDCOM
                    c_ind+=1
                elif words[-1] == "FAM":
                    # go get the total number of families in the GEDCOM
                    c_fam+=1

    # Creating an array for each; containing the exact number of objects needed
    individuals=[individual() for i in range(c_ind) ]
    families=[family() for i in range(c_fam) ]

    refresh()
    # Set all global variables to the "NA" state

    with open ( filename ) as file:
        # READ FILE LINE BY LINE
        for line in file:
            # SPLIT LINE INTO LIST OF WORDS
            words = line.split()
            level = words[ 0 ]

            if level=='0':
                if flag == 1:
                    individuals[c_ind1].info(iden, name, sex, dob, dod, famc, fams)
                    # Checking unique IDs
                    if no_reps(indi,iden,flag):
                        individuals[c_ind1].err.append("US22")

                    # Appending indivial's ID to indi[], making easier to find this id later
                    # We can get the loaction of the individual in individuals[] be finding it's position in the list.
                    indi.append(iden)
                    #individuals[c_ind1].showinfo()
                    c_ind1+=1
                elif flag == 2:
                    families[c_fam1].info(iden, hid, wid, dom, doe, cid)
                    # Checking unique IDs
                    if no_reps(famillia,iden,flag):
                        families[c_fam1].err.append("US22")

                    #Appending family's ID to famillia[], making easier to find this ID later.
                    # We can get the location of the family in families[] from it's location in the list
                    famillia.append(iden)
                    # families[c_fam1].cout()
                    c_fam1+=1                    
                refresh()
                tag=words[-1]
                if tag=="INDI":
                    flag=1
                elif tag=="FAM":
                    flag=2
                iden = words[1]
            if level != '0':
                tag=words[1]
                if tag in tags:
                    if tag == "NAME":
                        name=words[2:]
                    elif tag == "SEX":
                        sex=words[-1]
                    elif tag == "BIRT":
                        # Date is given in the next line, so we are going to it.
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dob=getdate(words[2],words[3],words[4])                                
                    elif tag == "DEAT":
                        # Date is given in the next line, so we are going to it.
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dod=getdate(words[2],words[3],words[4])
                    elif tag == "FAMC":
                        famc=words[-1]
                    elif tag == "FAMS":
                        fams=words[-1]
                    elif tag == "HUSB":
                        hid = words[-1]
                    elif tag == "WIFE":
                        wid = words[-1]
                    elif tag == "CHIL":
                        cid.append(words[-1])
                    elif tag == "MARR":
                        # Date is given in the next line, so we are going to it.
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dom=getdate(words[2],words[3],words[4])
                    elif tag == "DIV":
                        # Date is given in the next line, so we are going to it.
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            doe=getdate(words[2],words[3],words[4])
                    

    #Checking that siblings shouldn't marry
    for i in range(c_fam):
        for j in range(c_fam):
            if not sibs_no_marry(families[i].hid,families[i].wid,families[j].cid) and i!=j:
                families[i].err.append("US18")
                families[j].err.append("US18")

    #Checking cousins don't marry

    #Checking aunts/uncles don't marry nephews/nieces.

    #Checking unique name and DOB
    # for i in range(c_ind):
    #     for j in range(c_ind):
    #         if i!=j:
    #             unique_name_dob(individuals[i],individuals[j])

    #UPDATE PRETTY TABLE
    x = prettytable.PrettyTable() # For people
    x.field_names = ["I.D.","NAME","SEX","BIRTH","DEATH","AGE","FAM_C","FAM_S","ERRORS"]
    y = prettytable.PrettyTable() # For Families
    y.field_names = ["I.D.","HUSBAND","WIFE","MARRIAGE","MARR_END","CHILDREN","ERRORS"]
    for i in range(c_ind1):
        individuals[i].update_table()
    for i in range(c_fam1):
        families[i].update_table()

    #PRINT DATA
    print ("INDIVIDUALS")
    print(x)
    print ("\nFAMILIES")
    print(y)

    #Print to output file
    with open("output.txt", 'w') as write_to:
        print ("INDIVIDUALS", file=write_to)
        print(x, file=write_to)
        print ("\nFAMILIES", file=write_to)
        print(y, file=write_to)

except FileNotFoundError:
    # File not found
    print ( "\nSorry the file : " + filename + " does not exist.\n" )
