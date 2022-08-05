import pickle
from miR_inv import dict_gene_2
from Dis_inv import dict_gene
for key in dict_dis:
    x=key
    y=dict_dis[x]
    break
print(x, y)

for key in dict_gene_2:
    x=key
    y=dict_gene_2[x]
    break
print(x, y)

Dis_miR={}
gene_missing=[]
count_zero=0
for key1 in list(dict_dis.keys()):
    Dis_miR[key1]=[]
    tmp=set()
    for value in dict_dis[key1]:
      if value in dict_gene_2:
          tmp= tmp.union(set(dict_gene_2[value])) 
      else:
            gene_missing.append(value)
    if len(tmp)==0:
        count_zero+=1
    Dis_miR[key1].append(list(tmp))
print(key1, value)

#for key in Dis_miR.keys():
    #Dis_miR[key]=list(set(Dis_miR[key]))

for item in Dis_miR:
    if len(Dis_miR[item])>0:
        Dis_miR[item] = Dis_miR[item][0]
          
gene_missing =list(set(gene_missing))

for key in Dis_miR:
    x=key
    y=Dis_miR[x]
    break
print(x, y)
print(len(Dis_miR))
print(len(list(Dis_miR.keys())))
print(len(list(Dis_miR.values())))
#Dis_miR.len('hsa-let-7a-3p')
print(len(gene_missing))
print(count_zero)
Dis_miR = {x.replace('\n', ''): v
   for x, v in list(Dis_miR.items())}
pickle_out = open("Disease-miRNA.pkl","wb")
pickle.dump(Dis_miR, pickle_out)
pickle_out.close()

