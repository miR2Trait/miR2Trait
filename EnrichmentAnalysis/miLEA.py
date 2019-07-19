##!/usr/bin/env python 
from __future__ import division
import pickle
import scipy.stats as stats
import sys
#import pandas as pd
#import string
import csv
import numpy as np

a=sys.argv[1:-1]
new_a=[]
for i in range(len(a)-1):
    new_a.append(a[i].replace('mir', 'miR').replace('Hsa', 'hsa'))

b=sys.argv[-1]
default = 0.05
#a=['hsa-miR-21-3p','hsa-miR-454-3p']
dictfile = raw_input("Enter /path/file of pickle dict of disease-miRNA mappings")

infile = open(dictfile, 'rb')
outflag = raw_input("Would you like to save the results in a csv file (miLEA_out.csv in the same path as input file) -- Yes?")
dict_3 = pickle.load(infile)
infile.close()

def MyFn(lst):
    return lst[2]

def correct_pvalues_for_multiple_testing(pvalues, correction_type = "Benjamini-Hochberg"):
    """                                                                                                   
    consistent with R - print correct_pvalues_for_multiple_testing([0.0, 0.01, 0.029, 0.03, 0.031, 0.05, 0.069, 0.07, 0.071, 0.09, 0.1]) 
    """
    pvalues = np.array(pvalues) 
    n = float(pvalues.shape[0])                                                                   
    qvalues = np.empty(pvalues.shape[0])
    if correction_type == "Bonferroni":                                                                   
        qvalues = n * pvalues
    elif correction_type == "Bonferroni-Holm":                                                            
        values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]                                      
        values.sort()
        for rank, vals in enumerate(values):                                                              
            pvalue, i = vals
            qvalues[i] = (n-rank) * pvalue                                                            
    elif correction_type == "Benjamini-Hochberg":                                                         
        values = [ (pvalue, i) for i, pvalue in enumerate(pvalues) ]                                      
        values.sort()
        values.reverse()                                                                                  
        new_values = []
        for i, vals in enumerate(values):                                                                 
            rank = n - i
            pvalue, index = vals                                                                          
            new_values.append((n/rank) * pvalue)                                                          
        for i in xrange(0, int(n)-1):  
            if new_values[i] < new_values[i+1]:                                                           
                new_values[i+1] = new_values[i]                                                           
        for i, vals in enumerate(values):
            pvalue, index = vals
            qvalues[index] = new_values[i]                                                                                                                  
    return qvalues.tolist()

x1=set(new_a)
dis=[]
pval=[]
odds=[]
totmir = len(dict_3.keys())
##check totmir 

if b[0].upper() == "Y":
    b = default
else:
    b=float(b)
for disease in dict_3.keys():
    d = dict_3[disease]
    y1=set(d)
    param1 = len(y1.intersection(x1))
    param2 = len(y1)-param1
    param3= len(x1)-param1
    param4 = totmir -param2-param3+param1
    oddsratio,pvalue=stats.fisher_exact([[param1, param2],[param3,param4]])
    if pvalue<b:
        odds.append(oddsratio)
        pval.append(pvalue)
        dis.append(disease)
qvalues = correct_pvalues_for_multiple_testing(pval)

dis=list(map(str.strip,dis))
zipped = zip(dis,odds,pval,qvalues)
j= len(zipped)
print '\nSignificantly enriched diseases for the given set of miRNAs: ' + str(j) + '\n'
print "Disease\t\tEffect-size\t\tP-value\tAdj.p-value\n"
result = sorted(zipped, key=MyFn)
for item in result:
#   print item[0], np.format_float_scientific(round(item[1],8,),precision=2),np.format_float_scientific(round(item[2],8,),precision=2), np.format_float_scientific(round(item[3],8,),precision=2))

    print "{0: <50}\t{1:.2f}\t".format(item[0],round(item[1],2)), (np.format_float_scientific(round(item[2],8),precision=2)), (np.format_float_scientific(round(item[3],8),precision=2))

#   print "{0}\t{1:.2f}\t{2:.8f}\t{3:.8f}".format(item[0], item[1], item[2],item[3])

if outflag[0].upper() == "Y":
    path = dictfile.split('/')
    path = path[:-1]
    outfile = '/'.join(path) + '/miLEA_out.csv'
    with open(outfile, 'w') as csvFile:
        csvFile.write('Input miRNA list:' + str(new_a) + '\n\n')
        csvFile.write('Significantly enriched diseases for the given set of miRNAs: ' + str(j) + '\n\n')
        csvFile.write("Disease,\t\tEffect-size,\t\tP-value,\t\tAdj.p-value\n")
        writer = csv.writer(csvFile)
        writer.writerows(result)
    csvFile.close()

#   print '\n'

##for item in result:
##   print '%s %.3e", % (item[0],item[2])

#for i in range(len(result)):
#   print "{0}\t {1:.8f}\t {2:.8f}".format(result[i][2],result[i][0],result[i][1])


