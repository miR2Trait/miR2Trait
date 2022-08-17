import pickle
from miRBase_Query import retrieve_mirs
#import re

dictfile = input("Enter /path/file of pickle dict of disease-miRNA mappings\t:")
infile = open(dictfile, 'rb')
dict_3 = pickle.load(infile)
infile.close()

##search_type = input("Would you like to perform an exact match (1) or a regular expression search (2) : 1/2?")
##if search_type == '1':
disease = input("Please enter the disease to search in miR2Trait:\t").upper()
word=''
for letter in disease:
    if letter.isalnum():
        word+=letter

dis = word
newDict={}

for item in list(dict_3.items()):
    word=''
    for lett in item[0]:
        if lett.isalnum():
            word+=lett
    newDict[word.upper()]=item[1]
        
if dis in newDict:
    mirna=list(newDict[dis])
    totmir = len(mirna)
    print("Total number of associated miRNAs:\t"+str(totmir)+'\n')
    num = int(input("How many miRNAs would you like to be listed -- enter a number"))
    while True:
        if totmir < num:
            num = int(input("Please enter a number less than the total number of associated miRNAs:\t"))
            continue
        else:
            print('\n')
            for i in range(len(num)):
                print(mirna[i]+'\n')
            ans = input("Would you like to retrieve miRBase information for the above miRNAs: Y/N?")
            if ans == 'Y':
                retrieve_mirs(mirna[:num])
            break
else:
    print('\nDisease'+ disease + 'not found in the miR2Trait:\n')
