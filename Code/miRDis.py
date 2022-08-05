import pickle
from miR import dict_mirna
from Dis import dict_dis
for key in dict_mirna:
    x=key
    y=dict_mirna[x]
    break
print(x, y)

for key in dict_gene:
    x=key
    y=dict_gene[x]
    break
print(x, y)

miRDis={}
gene_missing=[]
count_zero=0
for key1 in list(dict_mirna.keys()):
    miRDis[key1]=[]
    tmp=set()
    for value in dict_mirna[key1]:
      if value in dict_gene:
          tmp= tmp.union(set(dict_gene[value])) 
      else:
            gene_missing.append(value)
    if len(tmp)==0:
        count_zero+=1
    miRDis[key1].append(list(tmp))
print(key1, value)

#for key in miRDis.keys():
    #miRDis[key]=list(set(miRDis[key]))

for item in miRDis:
    if len(miRDis[item])>0:
        miRDis[item] = miRDis[item][0]
          
gene_missing =list(set(gene_missing))
for key in miRDis:
    x=key
    y=miRDis[x]
    break
print(x, y)
print("Length of dict is:" + str(len(miRDis)))
print("Length of keys is:" + str(len(list(miRDis.keys()))))
print("Length of values is:" + str(len(list(miRDis.values()))))
#miRDis.len('hsa-let-7a-3p')
print("Length of Zero_Count is:" + str(count_zero))
pickle_out = open("miRNA-Disease.pkl","wb")
pickle.dump(miRDis, pickle_out)
pickle_out.close()



