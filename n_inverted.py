
reader = open("C:/xampp/htdocs/script/files for github/Source code/miR.csv","r")
dict_mirna={}
for line in reader.readlines():
   curr=line.split(',')
   if curr[1] not in dict_mirna.keys():
      dict_mirna[curr[1]] = []
   dict_mirna[curr[1]].append(curr[0]) 

print "Length of keys is:" + str( len(dict_mirna.keys()))
max_value=0
min_value=2685
count=0
ctr=0
for key in dict_mirna.keys():
   val = len(dict_mirna[key])
   if val>max_value:
      max_value=val
   if val<min_value:
      min_value=val
   if val ==1:
      count+=1
   if val==2685:
      ctr+=1
print "maximum number of values for a key: ", max_value,ctr
print "minimum number of values for a key: ", min_value,count
