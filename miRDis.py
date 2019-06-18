import pickle
from n import dict_mirna
from dis import dict_gene
for key in dict_mirna:
    x=key
    y=dict_mirna[x]
    break
print x, y

for key in dict_gene:
    x=key
    y=dict_gene[x]
    break
print x, y

dict_3={}
gene_missing=[]
count_zero=0
for key1 in dict_mirna.keys():
    dict_3[key1]=[]
    tmp=set()
    for value in dict_mirna[key1]:
      if dict_gene.has_key(value):
          tmp= tmp.union(set(dict_gene[value])) 
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
print "Length of dict is:" + str(len(dict_3))
print "Length of keys is:" + str(len(dict_3.keys()))
print "Length of values is:" + str(len(dict_3.values()))
#dict_3.len('hsa-let-7a-3p')
print "Length of Zero_Count is:" + str(count_zero)
pickle_out = open("miRNA-Disease.pkl","wb")
pickle.dump(dict_3, pickle_out)
pickle_out.close()



