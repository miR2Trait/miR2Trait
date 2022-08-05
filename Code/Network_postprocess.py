### the adjacency matrix p-values are corrected, -log10 transformed, and Sorted. The top 10,000 instances are read into Cytoscape and analyzed using the Cytoscape plugin Cytohubba. Results from Cytoscape centrality results are stored in a file (for e.g, miR2Trait_miRNA_Centrality_Result.csv )
#Step 1. Formatting the centrality results into a cleaner csv file
fh = input("Filename with Cytoscape centrality results:\t")
lines = open(fh, 'r').readlines()
csvEdit = open("miR2Trait.edit.csv",'w')
for line in lines:
    j = line.split(',')
    writestr = j[0]+','
    for item in j[1:]:
        itemsplit = item.split(': ')
        writestr+=(itemsplit[1])+','
    csvEdit.write(writestr[:-1])

#Step 2. sorting miRNAs by the ith centrality in separate files
for i in range(1,9):
    lines = open("miR2Trait.edit.csv",'r').readlines()
    output = open("centrality_"+str(i)+"_miRNA.csv", 'w')
    lines_sorted = sorted(lines, key=lambda line: float(line.split(',')[i]),reverse=True)
    for line in lines_sorted:
        output.write(line.split(',')[0]+'\n')
    output.close()
    #lines.close        

#Step 3. merging the ith ranks (denoted by miRNAs) in each centrality into a common file
out = open("miR2Trait_Centralities.csv",'w')
masterList=[]
lines={}
for i in range(1,9):
    lines = open("centrality_"+str(i)+"_miRNA.csv", 'r').readlines()
    lst=[]
    for line in lines:
        lst.append(line.split(',')[0][:-1])
    masterList.append(lst)
tupList=list(zip(masterList[0],masterList[1],masterList[2],masterList[3],masterList[4],masterList[5],masterList[6],masterList[7]))
print(tupList[0])
for i in range(len(tupList)):
    out.write(','.join(list(tupList[i]))+'\n')
out.close()

#setting a threshold Rank for consideration (the topNum variable) and obtaining the identities passing a minimum consensus agreement (given by the numTool variable)
import operator
import csv
import sys
import itertools
from collections import Counter
topNum = int(sys.argv[1])
numTool = int(sys.argv[2])

#Step 4. creating a temp file with data passing the threshold ranks
i=0
lines = open("miR2Trait_Centralities.csv",'r').readlines()
newfile = open("centralities_temp.csv",'w')
for line in lines:
    if i<topNum:
        newfile.write(line)
    i+=1

#Step 5. finding the tool_quotient of each miRNA and identifying those passing a minimum consensus agreement 
with open("centralities_temp.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=',')
    my_list = list(reader)
print(len(my_list))
merged = list(itertools.chain.from_iterable(my_list))
print(len(merged))
G=Counter(merged)
print(len(G))
print(len(list(G.keys())))
print(list(G.keys())[0])
newdict={}
for key in list(G.keys()):
    if G[key]>=numTool:
        newdict[key]=G[key]
def myFn(item):
    return item[1]

#Step 6. ranking the consensus miRNAs
newdict2=sorted(list(newdict.items()), key =myFn, reverse=True)
F=open("Consensus.txt","w")
F.write(str(newdict2))

