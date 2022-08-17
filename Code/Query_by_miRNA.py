import pickle
from miRBase_Query import retrieve_mirs

dictfile = input("Enter /path/file of pickle dict of miRNA-Disease mappings\t:")
infile = open(dictfile, 'rb')
dict_3 = pickle.load(infile)
infile.close()

miRNA = input("Enter an miRNA to search in miR2Trait:\t").upper()
word=''
for letter in miRNA:
    if letter.isalnum():
        word+=letter

mir = word
newDict={}

for item in list(dict_3.items()):
    word=''
    for lett in item[0]:
        if lett.isalnum():
            word+=lett
    newDict[word.upper()]=item[1]
        
if mir in newDict:
    disease =list(newDict[mir])
    totdis = len(disease)
    print("Total number of associated Diseases:\t"+str(totdis)+'\n')
    num = int(input("How many diseases would you like to be shown -- enter a number"))
    while True:
        if totdis < num:
            num = int(input("Please enter a number less than the total number of associated diseases:\t"))
            continue
        else:
            print('\n')
            for i in range(len(num)):
                print(disease[i]+'\n')
            ans = input("Would you like to retrieve miRBase information for the given miRNA: Y/N?")
            if ans == 'Y':
                retrieve_mirs([miRNA])
            break
else:
    print('\nmiRNA'+ miRNA + 'not found in the miR2Trait:\n')
