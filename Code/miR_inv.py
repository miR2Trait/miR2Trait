
reader = open("miR.csv","r")
dict_gene_2={}
for line in reader.readlines():
   curr=line.split(',')
   if curr[1] not in list(dict_gene_2.keys()):
      dict_gene_2[curr[1]] = []
   dict_gene_2[curr[1]].append(curr[0]) 

print("Length of keys is:" + str( len(list(dict_gene_2.keys()))))
max_value=0
min_value=2685
count=0
ctr=0
for key in list(dict_gene_2.keys()):
   val = len(dict_gene_2[key])
   if val>max_value:
      max_value=val
   if val<min_value:
      min_value=val
   if val ==1:
      count+=1
   if val==2685:
      ctr+=1
print("maximum number of values for a key: ", max_value,ctr)
print("minimum number of values for a key: ", min_value,count)
