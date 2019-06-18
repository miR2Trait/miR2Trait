import pickle
from n_inv import dict_mirna
from dis_inv import dict_gene
for key in dict_gene:
    x=key
    y=dict_gene[x]
    break
print x, y

for key in dict_mirna:
    x=key
    y=dict_mirna[x]
    break
print x, y

dict_3={}
gene_missing=[]
count_zero=0
for key1 in dict_gene.keys():
    dict_3[key1]=[]
    tmp=set()
    for value in dict_gene[key1]:
      if dict_mirna.has_key(value):
          tmp= tmp.union(set(dict_mirna[value])) 
      else:
            gene_missing.append(value)
    if len(tmp)==0:
        count_zero+=1
    dict_3[key1].append(list(tmp))
print key1, value

#for key in dict_3.keys():
    #dict_3[key]=list(set(dict_3[key]))

for item in dict_3:
    if len(dict_3[item])>0:
        dict_3[item] = dict_3[item][0]
          
gene_missing =list(set(gene_missing))

for key in dict_3:
    x=key
    y=dict_3[x]
    break
print x, y
print len(dict_3)
print len(dict_3.keys())
print len(dict_3.values())
#dict_3.len('hsa-let-7a-3p')
print len(gene_missing)
print count_zero
dict_3 = {x.replace('\n', ''): v
   for x, v in dict_3.items()}
pickle_out = open("Disease-miRNA.pkl","wb")
pickle.dump(dict_3, pickle_out)
pickle_out.close()

