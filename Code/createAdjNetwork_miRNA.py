import pickle
import itertools
import scipy.stats as stats
import pandas	
pickle_in = open("miRNA-Disease.pkl","rb")
dict_map = pickle.load(pickle_in)
lst=[] #list of sets
for mirna in list(dict_map.keys()):
   merged = list(itertools.chain.from_iterable(dict_map[mirna]))
   a1=set(merged)
   lst.append(a1)
p=[]
o=[]
len0=len(lst)
print(len0)
a=list(dict_map.keys())
newdict={}
fh=open('miRnetworkData.txt','w')
fh.write('miR1'+'\t'+'miR2'+'\t'+'P-value'+'\t'+'Odds-ratio'+'\n')

for i in range(len0-1):
   odds=[]
   pval=[]
   for j in range(i+1,len0):
      overlap=lst[i].intersection(lst[j])
      len1=len(overlap)
      len2=len(lst[i])
      len3=len(lst[j])
      len4=11689 - len2-len3+len1
      oddsratio,pvalue = stats.fisher_exact([[len1,len2],[len3,len4]])
      newdict[(a[i],a[j])] = (pvalue,oddsratio)
      fh.write(a[i]+'\t'+a[j]+'\t'+str(pvalue)+'\t'+str(oddsratio)+'\n') 
      pval.append(pvalue)
      odds.append(oddsratio)
        
   p.append(pval)
   o.append(odds)


f=list(zip(a,p,o))
pd=pandas.DataFrame(f)
pd.to_csv("mylist.csv")
