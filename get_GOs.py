#! /usr/bin/env python

# a script to grab GOterms for SPUIDs

import sys
import pandas as pd

#read in file
#infile = open(sys.argv[1],'r')
infile = open('master_annotations.txt','r')
idfile = open('spuID2go.txt','r')

#set_up_output
outfile = open('GO_mappings.txt', 'w')

#this is where the SPU IDs are in master_annotations.txt
spu_id_field = 61

#set up the working loop
linecount = 0
for line in infile:
	linecount+=1
	#make the header
	if linecount==1:
		outfile.write('SPU_ID\tUniprotID\tGO_terms\tGO_descriptions')
	else:
		line=line.rstrip()
		cols=line.split('\t')
		spu_id = cols[spu_id_field]

####
#### TO DO
####

#1. Read in SPUID to GO file

# method 1
id_match_list = []
for i in infile:
    i = i.rstrip()
    cols_i = i.split('\t')
    spu_id_i = cols_i[61]
    for j in idfile:
        j = j.rstrip()
        cols_j = j.split('\t')
        spu_id_j = cols_j[0]
        if spu_id_i == spu_id_j:
            id_match_list.append(spu_id_i)
        else:
            continue
go_mappings = pd.DataFrame({'SPU ID':id_match_list})

# method 2
spu2go = pd.read_csv('spuID2GO.txt', sep="\t", header=None)
master_annotations = pd.read_csv('master_annotations.txt', sep="\t", header=None)

spu_id_list = master_annotations['SPU.ID'].tolist()
# Key Error: SPU.ID - if I get rid of this error I think this will work

id_match_list = []
for i in spu_id_list:
    if spu2go.loc[spu2go[0] == spu_id]:
        id_match_list.append(i)
    else:
        continue



                               
#2. Compare the SPUIDs to that file to get GO terms
#3. Parse the GO terms
#4. Write it all out



outfile.close()