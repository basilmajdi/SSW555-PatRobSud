#!/usr/bin/python

'''
Parser for Robert Basil Majdi, Prateek Tyagi and Sudhansh Aggarwal
CS-555/SSW-555 
'''

import os
import sys
import codecs
import datetime
import Rob_funcs
from sudhansh import no_reps
from sudhansh import sibs_no_marry
from sudhansh import valid_date
from prateek import sibling_nos
import prettytable

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
            self.err.append("US42-DOD")
        if not valid_date(dob):
            self.err.append("US42-DOB")
        if not Rob_funcs.birth_b4_dth(dob, dod):
            self.err.append('check birth and death dates')
        if not Rob_funcs.dates_b4_today(dob) and Rob_funcs.dates_b4_today(dod):
            self.err.append('date is after current date')
        
        
        
            
    def showinfo(self):
        print('{} : {}'.format("ID",self.pid))
        print('{} : {}'.format("NAME",self.name))
        print('{} : {}'.format("SEX",self.sex))
        print('{} : {}'.format("D.O.B",self.dob))
        print('{} : {}'.format("D.O.D",self.dod))
        print('{} : {}'.format("FAMC",self.famc))
        print('{} : {}'.format("FAMS",self.fams))

    def update_table(self):
        x.add_row([self.pid,self.name,self.sex,self.dob,self.dod,self.famc,self.fams,self.err])

class family:
    def __init__(self):
        self.fid="NA"
        self.hid="NA"
        self.wid="NA"
        self.dom="NA"
        self.doe="NA"
        self.cid=[]
        self.sib_no=0
        self.err=[]
    
    def info(self, fid, hid, wid, dom, doe, cid):
        self.fid=fid
        self.hid=hid
        self.wid=wid
        self.dom=dom
        self.doe=doe
        self.cid=cid
        #Checking correctness of dates
        self.sib_no=sibling_nos(cid)
        if not valid_date(dom):
            self.err.append("US42-DOM")
        if not valid_date(doe):
            self.err.append("US42-DOE")
        if not Rob_funcs.marg_b4_dvors(doe, dom):
            self.err.append('check marriage and devorce dates')
        if not Rob_funcs.birth_b4_marg(individual.dob, dom):
            self.err.append('check birth and marriage dates')
        if not Rob_funcs.dates_b4_today(doe) and Rob_funcs.dates_b4_today(dom):
            self.err.append('date is after current date')
        
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

#filename = input ( "Enter the location of the file: " )
#filename="/Users/sudhansh/Desktop/CS-555/test1.ged" #For testing purposes
filename="C:\Users\basilmajdi\Documents\stevens_SSW\agile methods 555\555_proj\SSW555-PatRobSud\SSW_555" #For testing purposes

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
                    c_ind+=1
                elif words[-1] == "FAM":
                    c_fam+=1

    # Creating an array for each; containing the exact number of objects needed
    individuals=[individual() for i in range(c_ind) ]
    families=[family() for i in range(c_fam) ]

    refresh()
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
                    indi.append(iden)
                    #individuals[c_ind1].showinfo()
                    c_ind1+=1
                elif flag == 2:
                    families[c_fam1].info(iden, hid, wid, dom, doe, cid)
                    # Checking unique IDs
                    if no_reps(famillia,iden,flag):
                        families[c_fam1].err.append("US22")
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
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dob=getdate(words[2],words[3],words[4])
                                
                    elif tag == "DEAT":
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
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dom=getdate(words[2],words[3],words[4])
                    elif tag == "DIV":
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            doe=getdate(words[2],words[3],words[4])
                    

    #Checking that siblings shouldn't marry
    for i in range(c_fam):
        for j in range(c_fam):
            if i != j:
                if not sibs_no_marry(families[i].hid,families[i].wid,families[j].cid):
                    families[i].err.append("US18")
                    families[j].err.append("US18")


    #UPDATE PRETTY TABLE
    x = prettytable.PrettyTable() # For people
    x.field_names = ["I.D.","NAME","SEX","BIRTH","DEATH","FAM_C","FAM_S","ERRORS"]
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
    

