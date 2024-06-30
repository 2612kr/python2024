#Importance
# list
list_1 = []
list_2 = list()
con = [5,6,7,8]
list_1 = list_1 + con
print (list_1) # output of list_1
inst = (8,9,1,5,6,7,8,1)
list_2.extend(inst)
print(list_2) # output of list_2
list_1.extend(list_2)
print(list_1) # output of both list_2 and list_1 in single list_1
print(list_1.count(8)) # print the frequency of count 8
# mean = sum of all items / no . of . items
mean = (sum(list_1) / len(list_1))
print(mean) # output of the mean
print(sum(list_1)+ min(list_1)+ max(list_1)) # output of sum(list)+min()+max()
import statistics
print(statistics.median(list_1)) # output of median of the list
list_1 = set(list_1)
print(tuple(list_1))
