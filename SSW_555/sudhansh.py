#!/usr/bin/python

'''
noreps makes sure there are no repeated IDs
Made by Sudhansh Aggarwal
'''
def no_reps(group,id_, flag,op_group):
    if flag !=1 and flag !=2:
        return 0
    else:
        if id_ in group:
            op_group.append(id_)
            id_=id_+"REP"
        return id_

def valid_date(date):

def sibs_dont_marry():
	'''
	for list of fams:
		if husb in fam[i].cid and wife in fam[i].cid:
			dude wtf?!?!?!?
	'''