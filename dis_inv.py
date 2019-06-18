
reader = open("curated.csv","r")
dict_gene={}
for line in reader.readlines():
   curr=line.split(',')
   if curr[1] not in dict_gene.keys():
      dict_gene[curr[1]] = []
   dict_gene[curr[1]].append(curr[0]) 

print len(dict_gene.keys())
max_value=0
min_value=8947
count=0
ctr=0
for key in dict_gene.keys():
   val = len(dict_gene[key])
   if val>max_value:
      max_value=val
   if val<min_value:
      min_value=val
   if val ==1:
      count+=1
   if val==8947:
      ctr+=1
print "maximum number of values for a key: ", max_value,ctr
print "minimum number of values for a key: ", min_value,count
