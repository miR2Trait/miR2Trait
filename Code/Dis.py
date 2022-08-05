
reader = open("Dis.csv","r")
dict_dis={}
for line in reader.readlines():
   curr=line.split(',')
   if curr[0] not in list(dict_dis.keys()):
      dict_dis[curr[0]] = []
   dict_dis[curr[0]].append(curr[1]) 
   
reader.close()
   
print("Length of keys is:" + str( len(list(dict_dis.keys()))))
max_value=0
min_value=8947
count=0
ctr=0
for key in list(dict_dis.keys()):
   val = len(dict_dis[key])
   if val>max_value:
      max_value=val
   if val<min_value:
      min_value=val
   if val ==1:
      count+=1
   if val==481:
      ctr+=1
print("maximum number of values for a key: %d\t%d", max_value,ctr)
print("minimum number of values for a key: %d\t%d", min_value,count)

