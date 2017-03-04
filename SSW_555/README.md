The main script is RobPratSud_Proj03.py

It imports functions from sudhansh.py, prateek.py and Rob_funcs.py

When you run RobPratSud_Proj03, you will be asked to enter the location of your GEDCOM file

This program will read the file and generate a table from the data in the GEDCOM file.


*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
individuals is list of class individual
all people are stored as individuals[i] and can be accessed in the same way

families is the list of class family
all families are stored as families[i] and everythng in them can be accessed in the same way

*** IMPORTANT ***
FOR ALL DATA THAT IS NOT IN LINE WITH THE STORIES, APPEND THAT TO families[i].err or imdividuals[i].err respectively.
For example, if some data goes against User Story 01, append "US01" to the required individuals[i] or families[i]
