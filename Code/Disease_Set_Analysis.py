import pickle
from collections import Counter

def MyFn(tup):
        return tup[1]

dictfile = input("Enter /path/file of pickle dict of disease-miRNA mappings\t:")
infile = open(dictfile, 'rb')
dict_3 = pickle.load(infile)
infile.close()

print("Simple Over-representation calculation of miRNA in diseases")
dis_list=[]
while True:
	disease = input("Enter a disease or press Enter to stop:\t").upper()
	if disease =='' or disease == ' ' or disease == 'No':
		break
        word=''
        for letter in disease:
                if letter.isalnum():
                        word+=letter
	dis_list.append(word)

if len(dis_list):
        dis_not_found = []
        dis_found=[]
        mirna =[]
        newDict={}
        
        min_n = int(input('Enter the minimum number of miRNA occurrences to search for:\t'))
        for item in list(dict_3.items()):
                word=''
                for lett in item[0]:
                        if lett.isalnum():
                                word+=lett
                newDict[word.upper()]=item[1]
                
        for dis in dis_list:
                if dis in newDict:
                        dis_found.append(dis)
                        mirna+=list(newDict[dis])
                else:
                        dis_not_found.append(dis)
        
        print("\nDiseases not found in the database:\t" + str(len(dis_not_found))+'\n')
        for dis in dis_not_found:
                print(dis, end=' ')
        print("\nDiseases found in the database:\t" + str(len(dis_list)-len(dis_not_found))+'\n')
        for dis in dis_found:
                print(dis, end=' ')

        G=Counter(mirna)

        result=[]
        for item in list(G.items()):
                if item[1] >= min_n:
                        result.append(item)

        print("\nNumber of over-represented miRNAs:\t" + str(len(result)))
        print("miRNA \t\tFrequency of occurrence in disease set\n")

        if len(result):
                result_sorted = sorted(result, key=MyFn,reverse=True)
                for item in result_sorted:
                        print(item[0] +'\t' + str(item[1]) + '\n')
        else:
                print("QUERY RETURNED NO RESULTS\n")

        print('------------------------------------------')


